import csv
import json
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from absl import app
from absl import flags

FIREBASE_SERVICE_ACCOUNT_PATH = 'credentials/firebase/ballet-for-all-project-9365caabf1ba.json'
KEYWORD_SEARCH_API = "https://dapi.kakao.com/v2/local/search/keyword.json"
ADDRESS_SEARCH_API = "https://dapi.kakao.com/v2/local/search/address.json"
KAKAO_CREDENTIAL_PATH = "credentials/kakao/kakao-key.json"
KAKAO_REST_API_KEY = "rest_api_key"
ACADEMY_GROUP_CODE = "AC5"
CACHED_COORDINATES_PATH = 'search-academies/coordinates.csv'
ACADEMIES_PATH = 'search-academies/academies.csv'

FLAGS = flags.FLAGS
flags.DEFINE_bool('use_cached_coordinates', False,
                  'Whether to use cached coordinates')


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


def load_flatten_locations():
    db = firestore.client()
    location_ref = db.collection('location')
    cities_doc = location_ref.document('cities').get().to_dict()
    cities = cities_doc['cities']

    flatten = []
    for city in cities:
        city_name = city['name']
        for district in city['districts']:
            district_name = district['name']
            for block in district['blocks']:
                block_name = block['name']
                flatten.append(f'{city_name} {district_name} {block_name}')

    return flatten


def find_coordinates(location, kakao_rest_api_key):
    headers = {'Authorization': f'KakaoAK {kakao_rest_api_key}'}
    params = {
        'query': location,
    }
    response = requests.get(ADDRESS_SEARCH_API, headers=headers,
                            params=params).json()
    documents = response['documents']

    if len(documents) == 0:
        print(f'No coordinate found for {location}')
        return None

    return [{
        'location': document['address_name'],
        'x': document['x'],
        'y': document['y']
    } for document in documents]


def cache_coordinates(coordinates_list):
    print('Caching coordinates')
    with open(CACHED_COORDINATES_PATH, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['location', 'x', 'y'])
        for coordinates in coordinates_list:
            writer.writerow(
                [coordinates['location'], coordinates['x'], coordinates['y']])


def load_cached_coordinates():
    print('Loading cached coordinates')
    with open(CACHED_COORDINATES_PATH, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        return [{
            'location': row[0],
            'x': row[1],
            'y': row[2]
        } for row in reader]


def search_academies(coordinates, kakao_rest_api_key):
    academies = []
    page = 1
    headers = {'Authorization': f'KakaoAK {kakao_rest_api_key}'}
    while True:
        params = {
            'query': '발레',
            'category_group_code': ACADEMY_GROUP_CODE,
            'x': coordinates['x'],
            'y': coordinates['y'],
            'radius': 2500,
            'sort': 'distance',
            'page': page
        }
        response = requests.get(KEYWORD_SEARCH_API,
                                headers=headers,
                                params=params).json()
        documents = response['documents']
        academies.extend(documents)

        meta = response['meta']
        if meta['total_count'] > 45:
            print(
                f'{meta["total_count"]} academies found for {coordinates["location"]}'
            )
        if meta['is_end']:
            break
        page += 1
    return academies


def main(argv):
    del argv  # Unused.

    api_key = get_kakao_rest_api_key()

    coordinates_list = []
    if FLAGS.use_cached_coordinates:
        coordinates_list = load_cached_coordinates()
    else:
        initialize_firebase()

        print('-' * 80)
        print('Loading locations')
        locations = load_flatten_locations()

        print('-' * 80)
        print('Finding coordinates for locations')
        for i, location in enumerate(locations):
            print(f'\r {i/len(locations)*100:.2f}%', end='')
            found = find_coordinates(location, api_key)
            if found:
                coordinates_list.extend(found)
        print()

        cache_coordinates(coordinates_list)
    print(f'Total coordinates to find academies: {len(coordinates_list)}')

    print('-' * 80)
    print('Searching academies')
    academies_dict = {}
    for i, coordinates in enumerate(coordinates_list):
        print(f'\r {i/len(coordinates_list)*100:.2f}%', end='')
        academies = search_academies(coordinates, api_key)
        for academy in academies:
            academies_dict[academy['id']] = academy
    print()

    print('-' * 80)
    print('Saving academies')
    with open(ACADEMIES_PATH, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'address', 'phone', 'place_url'])
        for academy in academies_dict.values():
            writer.writerow([
                academy['place_name'], academy['road_address_name'],
                academy['phone'], academy['place_url']
            ])


if __name__ == '__main__':
    app.run(main)
