import requests
from win10toast import ToastNotifier
import time


def fetch_covid_data():
    try:
        url = 'https://disease.sh/v3/covid-19/countries/South%20Africa'
        headers = {'Accept': 'application/json'}

        r = requests.get(url, headers=headers)
        r.raise_for_status()  # Raise an HTTPError for bad responses

        data = r.json()

        if 'cases' in data:
            cases = data['cases']
            deaths = data['deaths']
            recovered = data['recovered']

            text = f'COVID-19 Stats for South Africa:\nConfirmed Cases: {cases}\nDeaths: {deaths}\nRecovered: {recovered} '

            toast = ToastNotifier()
            toast.show_toast("COVID-19 Updates - South Africa", text, duration=20)
        else:
            print("Error: Data format from API is not as expected.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Error parsing JSON: {val_err}")
    except Exception as err:
        print(f"An unexpected error occurred: {err}")

    time.sleep(60)
    fetch_covid_data()


if __name__ == "__main__":
    fetch_covid_data()
