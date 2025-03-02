import json
import hashlib
from supabase import create_client, Client

SUPABASE_CREDENTIALS_PATH = 'credentials/supabase/supabase-credential.json'
CITIES_JSON_FILE_PATH = 'cities-firestore-to-json/cities.json'

def supabase_init():
    with open(SUPABASE_CREDENTIALS_PATH) as f:
        credentials = json.load(f)
    url = credentials['SUPABASE_URL']
    key = credentials['SUPABASE_KEY']
    return create_client(url, key)


def hash_string(s):
    return hashlib.md5(s.encode()).hexdigest()


def save_to_supabase(supabase: Client, cities_data):
    # 데이터를 저장할 배열 초기화
    cities_to_insert = []
    districts_to_insert = []
    blocks_to_insert = []
    
    # 모든 데이터를 순회하며 배열에 추가
    for city in cities_data:
        city_id = hash_string(city['name'])
        print(f"도시 추가 준비: {city['name']}")
        cities_to_insert.append({'id': city_id, 'name': city['name']})
        
        for district in city['districts']:
            district_id = hash_string(city['name'] + district['name'])
            print(f"  구/군 추가 준비: {district['name']} (도시: {city['name']})")
            districts_to_insert.append({'id': district_id, 'name': district['name'], 'city_id': city_id})
            
            for block in district['blocks']:
                block_id = hash_string(city['name'] + district['name'] + block['name'])
                print(f"    동/읍/면 추가 준비: {block['name']} (도시: {city['name']}, 구/군: {district['name']})")
                blocks_to_insert.append({'id': block_id, 'name': block['name'], 'district_id': district_id})
    
    # 데이터가 있는 경우에만 한 번에 insert
    if cities_to_insert:
        print(f"도시 {len(cities_to_insert)}개 저장 중...")
        supabase.table('cities').insert(cities_to_insert).execute()
        print("도시 저장 완료!")
    
    if districts_to_insert:
        print(f"구/군 {len(districts_to_insert)}개 저장 중...")
        supabase.table('districts').insert(districts_to_insert).execute()
        print("구/군 저장 완료!")
    
    if blocks_to_insert:
        print(f"동/읍/면 {len(blocks_to_insert)}개 저장 중...")
        supabase.table('blocks').insert(blocks_to_insert).execute()
        print("동/읍/면 저장 완료!")


def load_cities_json():
    try:
        with open(CITIES_JSON_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {CITIES_JSON_FILE_PATH}")
        return []
    except json.JSONDecodeError:
        print(f"JSON 파일 형식이 올바르지 않습니다: {CITIES_JSON_FILE_PATH}")
        return []


def print_sample_cities(cities_data):
    print("=== 도시 데이터 샘플 출력 ===")
    
    if not cities_data:
        print("도시 데이터가 비어 있습니다.")
        return
        
    print(f"총 도시 수: {len(cities_data)}")
    
    # 처음 3개 도시만 출력
    for i, city in enumerate(cities_data[:3]):
        print(f"\n도시 {i+1}: {city['name']}")
        print(f"- 구/군 수: {len(city['districts'])}")
        
        # 각 도시의 처음 2개 구/군만 출력
        for j, district in enumerate(city['districts'][:2]):
            print(f"  구/군 {j+1}: {district['name']}")
            print(f"  - 동/읍/면 수: {len(district['blocks'])}")
            
            # 각 구/군의 처음 3개 동/읍/면만 출력
            for k, block in enumerate(district['blocks'][:3]):
                print(f"    동/읍/면 {k+1}: {block['name']}")


def test_supabase_connection():
    print("\n=== Supabase 연결 테스트 ===")
    try:
        supabase = supabase_init()
        print("Supabase 연결 성공!")
        
        # 간단한 쿼리 테스트
        response = supabase.table('cities').select('id').limit(1).execute()
        print(f"테이블 쿼리 응답: {response}")
        
        return True
    except Exception as e:
        print(f"Supabase 연결 실패: {str(e)}")
        return False


def main():
    # Supabase 연결
    supabase = supabase_init()
    if not supabase:
        print("Supabase 연결에 실패했습니다. 프로그램을 종료합니다.")
        return
        
    print("Supabase에 연결되었습니다.")
    
    # 도시 데이터 로드
    cities_data = load_cities_json()
    print_sample_cities(cities_data)  # 테스트를 위해 도시 데이터 출력 부분 주석 처리
    
    # 사용자 확인 후 데이터 저장
    if cities_data:
        print("데이터 저장 중...")
        save_to_supabase(supabase, cities_data)
        print("데이터 저장 완료!")
    else:
        print("저장할 도시 데이터가 없습니다.")


if __name__ == '__main__':
    main()
