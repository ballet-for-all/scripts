import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

OUTPUT_JSON_FILE_PATH = 'cities-firestore-to-json/cities.json'
FIREBASE_SERVICE_ACCOUNT_PATH = 'credentials/firebase/ballet-for-all-project-9365caabf1ba.json'


def initialize_firebase():
    try:
        app = firebase_admin.get_app()
    except ValueError as e:
        cred = credentials.Certificate(FIREBASE_SERVICE_ACCOUNT_PATH)
        firebase_admin.initialize_app(cred)


def fetch_cities_from_firestore():
    db = firestore.client()
    doc_ref = db.collection(u'location-v2').document(u'cities')
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get('cities', [])
    else:
        return []


def save_to_json(data):
    with open(OUTPUT_JSON_FILE_PATH, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)


def main():
    initialize_firebase()
    cities = fetch_cities_from_firestore()
    save_to_json(cities)


if __name__ == '__main__':
    main()
