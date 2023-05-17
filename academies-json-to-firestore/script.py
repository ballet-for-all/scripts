import json
import requests

from model.academy import Academy
from model.location import Location

ACADEMIES_JSON_FILE_PATH = 'academies-json-to-firestore/academies.json'
ADDRESS_SEARCH_API = "https://dapi.kakao.com/v2/local/search/address.json"
KAKAO_CREDENTIAL_PATH = "credentials/kakao/kakao-key.json"
KAKAO_REST_API_KEY = "rest_api_key"


def get_kakao_rest_api_key():
    with open(KAKAO_CREDENTIAL_PATH, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        return json_data[KAKAO_REST_API_KEY]


def read_academies_from_json():
    with open(ACADEMIES_JSON_FILE_PATH, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        return [Academy(**academy) for academy in json_data]


def add_location_to_academy(academy, kakao_rest_api_key):
    address = academy.address
    location = search_location(address, kakao_rest_api_key)
    academy.location = location


def search_location(address_str, kakao_rest_api_key):
    headers = {'Authorization': f'KakaoAK {kakao_rest_api_key}'}
    params = {'query': address_str}
    response = requests.get(ADDRESS_SEARCH_API, headers=headers, params=params)
    documents = response.json()['documents']

    if (len(documents) != 1):
        print(f'address_str: {address_str} is not unique')
        return

    address = documents[0]
    lng = float(address['x'])
    lat = float(address['y'])
    block = address['address']['region_3depth_name']

    return Location(lng, lat, block)


def main():
    kakao_rest_api_key = get_kakao_rest_api_key()

    academies = read_academies_from_json()
    for academy in academies:
        add_location_to_academy(academy, kakao_rest_api_key)


if __name__ == '__main__':
    main()
