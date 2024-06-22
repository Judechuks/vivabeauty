# for making api requests
import requests
import os

CSC_API_KEY = os.environ.get('COUNTRY_STATE_CITY_API_KEY')

# for all countries
def get_countries():
  api_url = "https://api.countrystatecity.in/v1/countries"
  headers = {"X-CSCAPI-KEY": CSC_API_KEY}  # Replace CSC_API_KEY with your own API key
  # Making the API request and parsing the response
  try:
    response = requests.get(api_url, headers=headers)
    countries_data = response.json()
    countries = [(country['name'], country['name']) for country in countries_data] # country list with 'name' as key and 'name' as value
    # print(countries_data[0]['name'])
    return countries # Return list of countries
  except requests.RequestException as e:
    print(f"Error fetching countries: {e}")
    return []  # Return an empty list if there's an error
