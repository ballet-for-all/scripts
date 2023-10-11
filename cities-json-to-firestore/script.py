import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

CITIES_JSON_FILE_PATH = 'cities-csv-to-json/cities.json'
FIREBASE_SERVICE_ACCOUNT_PATH = 'credentials/firebase/ballet-for-all-project-9365caabf1ba.json'


def initialize_firebase():
    try:
        app = firebase_admin.get_app()
    except ValueError as e:
        cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)


def read_cities_from_json():
    with open(CITIES_JSON_FILE_PATH, 'r', encoding='utf-8') as jsonfile:
        json_data = json.load(jsonfile)
        return json_data


def save_to_firestore(data):
    db = firestore.client()
    db.collection(u'location-v2').document(u'cities').set({'cities': data})


def main():
    initialize_firebase()
    cities = read_cities_from_json()
    save_to_firestore(cities)


if __name__ == '__main__':
    main()
