# Scripts

모두의 발레에서 사용하는 스크립트입니다.

## Python

Python 3.13.2 버전을 사용합니다.
편리한 버전 관리를 위해 [pyenv](https://github.com/pyenv/pyenv) 사용을 권장합니다.

### venv

Python 가상환경을 사용하여 패키지 의존성을 관리하는 것을 추천합니다.

```bash
$ python -m venv {원하는 가상환경 이름}
$ source {원하는 가상환경 이름}/bin/activate
```

VSCode를 사용하는 경우 옵션을 통해 생성한 venv를 간편하게 사용할 수 있습니다.

### 패키지 설치

```bash
$ pip install -r requirements.txt
```

## Credentials

### Firebase

Firebase service account 파일은 모두의 발레 구글 드라이브의 개발 폴더에서 다운로드 받을 수 있습니다.

다운로드 후 `credentials/firebase/ballet-for-all-project-9365caabf1ba.json` 에 위치시키면 됩니다.

### Kakao

kakao-key.json 파일은 모두의 발레 구글 드라이브의 개발 폴더에서 다운로드 받을 수 있습니다.

다운로드 후 `credentials/kakao/kakao-key.json` 에 위치시키면 됩니다.

## cities-csv-to-json

법정동명 CSV 파일을 json 파일로 변환합니다.

법정동명 스프레드시트는 [여기](https://docs.google.com/spreadsheets/d/18miy3THIfF8-Rzdu23CtcsOxZXsZXAoG/edit?usp=sharing&ouid=106558524234893023284&rtpof=true&sd=true)에 있습니다.

가장 최근에 사용된 시트는 '법정동\_20231011' 입니다.

CSV에서 법정동명 리스트를 불러와 Kakao API를 이용하여 3단계로 나뉘어진 주소를 불러옵니다.
3단계로 나뉜 주소를 city, district, block 으로 나누어 json 파일로 저장합니다.

Kakao API를 이용하기 위해 kakao-key.json 파일이 필요합니다.

### 사용법

법정동명 시트를 CSV로 다운로드 합니다.
해당 파일을 cities-csv-to-json/cities.csv에 위치시킨 후 아래 명령어를 실행합니다.

```bash
$ python cities-csv-to-json/script.py
```

## cities-json-to-firestore

cities-csv-to-json 으로 생성된 json 파일을 firestore 에 업로드 합니다.

가장 최근에 업로드된 cities 정보는 'location-v2' 컬렉션에 저장되었습니다.

Firestore 접근을 위해 Firebase sevice account 파일이 필요합니다.

### 사용법

```bash
$ python cities-json-to-firestore/script.py
```

## academies-json-to-firestore

학원 정보를 담고 있는 json 파일을 firestore 에 업로드 합니다.

위치 정보를 저장하기 위해 kakao-key.json 파일이 필요합니다.

Firestore 접근을 위해 Firebase sevice account 파일이 필요합니다.

### 사용법

```bash
$ python academies-json-to-firestore/script.py
```

## search-academies

카카오 지도 API를 이용하여 학원 정보를 검색합니다.

서비스가 제공하는 위치 정보를 불러오기 위해 Firebase service account 파일이 필요합니다.

카카오 지도 API를 이용하기 위해 kakao-key.json 파일이 필요합니다.

### 사용법

#### 캐시된 지역 좌표값을 이용하지 않는 경우

첫 실행 및 Firestore의 Location 정보가 변경된 경우 캐시된 값을 사용하지 않도록 실행해야 합니다.

Firestore의 Location 정보를 불러온 후 지역별 좌표값을 `coordinates.json` 파일에 저장합니다.

```bash
$ python search-academies/script.py
```

#### 캐시된 지역 좌표값을 이용하는 경우

저장되어 있는 `coordinates.json` 파일의 값을 이용하여 바로 검색을 시작합니다.

```bash
$ python search-academies/script.py --use_cached_coordinates=true
```
