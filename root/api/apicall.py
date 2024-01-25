# pip install requests
import requests

from root.helper.json_to_text import json_text


def get_data():
    # define URL
    url = "https://restcountries.com/v3.1/all"
    # send request to URL
    response = requests.get(url)
    # extract the data from the JSON
    countries = response.json()
    # loop through the countries

    return countries


def get_data_region(region):
    # define URL
    url = "https://restcountries.com/v3.1/region/" + region
    # send request to URL
    response = requests.get(url)
    # extract the data from the JSON
    countries = response.json()
    return countries
