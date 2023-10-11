import csv
import json
from datetime import datetime

import requests

ADDRESS_SEARCH_API = "https://dapi.kakao.com/v2/local/search/address.json"
KAKAO_CREDENTIAL_PATH = "credentials/kakao/kakao-key.json"
KAKAO_REST_API_KEY = "rest_api_key"
CITIES_CSV_FILE_PATH = 'cities-csv-to-json/cities.csv'
json_file_path = 'cities-csv-to-json/cities.json'


# Open the CSV file and read its contents
def read_locations_from_csv():
    with open(CITIES_CSV_FILE_PATH, newline='',
              encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row['법정동명'] for row in reader]
        return rows


def get_kakao_rest_api_key():
    with open(KAKAO_CREDENTIAL_PATH, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        return json_data[KAKAO_REST_API_KEY]


# Find the city, district and block for the given keyword
def find_location_from_address(address_str, kakao_rest_api_key):
    headers = {'Authorization': f'KakaoAK {kakao_rest_api_key}'}
    params = {
        'query': address_str,
    }
    response = requests.get(ADDRESS_SEARCH_API, headers=headers,
                            params=params).json()

    meta = response['meta']
    if meta['total_count'] == 0:
        print(f'주소 없음: {address_str}')
        return []

    result = []
    document = response['documents']
    for document in response['documents']:
        if document['address_type'] != 'REGION':
            print(f'도로명 주소: {address_str}')
            continue
        address = document['address']
        if not address['region_3depth_name']:
            if address['region_3depth_h_name']:
                print(
                    f'행정동 주소: {address_str} - {address["region_3depth_h_name"]}'
                )
                continue
            else:
                print(f'상위 주소: {address_str}')
                continue
        result.append({
            'city': address['region_1depth_name'],
            'district': address['region_2depth_name'],
            'block': address['region_3depth_name']
        })
    return result


# Group the rows by city and district
def group_addresses_by_city_and_district(addresses):
    groups = {}
    for address in addresses:
        city = address['city']
        district = address['district']
        block = address['block']
        if city not in groups:
            groups[city] = {}
        if district not in groups[city]:
            groups[city][district] = []
        groups[city][district].append(block)
    return groups


# Convert the groups into the desired JSON format
def convert_groups_to_json(groups):
    json_data = []
    for city, districts in groups.items():
        city_data = {'name': city, 'districts': []}
        for district, blocks in districts.items():
            # Remove duplicated blocks
            blocks = list(set(blocks))
            district_data = {
                'name': district,
                'blocks': [{
                    'name': block
                } for block in blocks]
            }
            city_data['districts'].append(district_data)
        json_data.append(city_data)
    return json_data


# Write the JSON data to a file
def write_json_to_file(json_data):
    with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(json_data, jsonfile, ensure_ascii=False, indent=2)


def main():
    locations = read_locations_from_csv()
    print(f'Find address for {len(locations)} locations')
    start_time = datetime.now()
    print(f'Start time: {start_time}')
    api_key = get_kakao_rest_api_key()
    addresses = []
    for i, location in enumerate(locations):
        if i % 100 == 0:
            print(f'{i} / {(i / len(locations) * 100):.2f}%')
        addresses += find_location_from_address(location, api_key)
    addresses = [address for address in addresses if address is not None]
    groups = group_addresses_by_city_and_district(addresses)
    json_data = convert_groups_to_json(groups)
    write_json_to_file(json_data)
    end_time = datetime.now()
    print(f'End time: {end_time}')
    print(f'Time elapsed: {end_time - start_time}')


if __name__ == '__main__':
    main()
