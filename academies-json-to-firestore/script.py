import json
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from model.academy import Academy
from model.location import Location

ACADEMIES_JSON_FILE_PATH = 'academies-json-to-firestore/academies.json'
ADDRESS_SEARCH_API = "https://dapi.kakao.com/v2/local/search/address.json"
KAKAO_CREDENTIAL_PATH = "credentials/kakao/kakao-key.json"
KAKAO_REST_API_KEY = "rest_api_key"
FIREBASE_SERVICE_ACCOUNT_PATH = 'credentials/firebase/ballet-for-all-project-9365caabf1ba.json'


def initialize_firebase():
    try:
        app = firebase_admin.get_app()
    except ValueError as e:
        cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)


def get_kakao_rest_api_key():
    with open(KAKAO_CREDENTIAL_PATH, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        return json_data[KAKAO_REST_API_KEY]


def read_academies_from_json():
    with open(ACADEMIES_JSON_FILE_PATH, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        return [Academy.from_dict(academy) for academy in json_data]


def add_location_to_academy(academy, kakao_rest_api_key):
    address = academy.address
    location = search_location(address, kakao_rest_api_key)
    academy.setLocation(location)


def search_address(address_str, kakao_rest_api_key):
    headers = {'Authorization': f'KakaoAK {kakao_rest_api_key}'}
    params = {'query': address_str}
    response = requests.get(ADDRESS_SEARCH_API, headers=headers, params=params)
    documents = response.json()['documents']
    return documents


def search_location(original_address_str, kakao_rest_api_key):
    address_str = original_address_str
    while True:
        documents = search_address(address_str, kakao_rest_api_key)
        if len(documents) > 0:
            break
        if len(address_str.split(' ')) == 1:
            print(f'no address found for {original_address_str}')
            break
        address_str = address_str.rsplit(' ', 1)[0]

    if (len(documents) != 1):
        print(f'original_address_str: {original_address_str} is not unique')
        print(f'documents: {documents}')
        return

    address = documents[0]
    lng = float(address['x'])
    lat = float(address['y'])
    city = address['address']['region_1depth_name']
    district = address['address']['region_2depth_name']
    block = address['address']['region_3depth_name']

    location_dict = {
        'lng': lng,
        'lat': lat,
        'city': city,
        'district': district,
        'block': block
    }

    return Location.from_dict(location_dict)


def clear_collection(collection):
    docs = collection.stream()
    deleted = 0

    for doc in docs:
        doc.reference.delete()
        deleted = deleted + 1

    print(f'{deleted} documents deleted.')


def save_to_firestore(collection, academy):
    collection.add(academy.to_dict())
    print(f'{academy.name} is saved')


def main():
    initialize_firebase()
    kakao_rest_api_key = get_kakao_rest_api_key()

    print('Reading academies from json...')
    academies = read_academies_from_json()
    print(f'Total academies: {len(academies)}')
    print('Adding location to academy...')
    for academy in academies:
        print(f'Adding location to {academy.name}...')
        add_location_to_academy(academy, kakao_rest_api_key)
    db = firestore.client()
    collection = db.collection(u'academies')
    print('Clearing academies collection...')
    clear_collection(collection)
    print('Saving academies to firestore...')
    for academy in academies:
        save_to_firestore(collection, academy)
    print('Done.')


if __name__ == '__main__':
    main()
