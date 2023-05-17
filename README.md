# Firebase scripts

모두의 발레에서 사용될 Firebase 에 접근하는 스크립트입니다.

## Credentials

### Firebase

Firebase service account 파일은 모두의 발레 구글 드라이브의 개발 폴더에서 다운로드 받을 수 있습니다.

다운로드 후 `credentials/firebase/ballet-for-all-project-9365caabf1ba.json` 에 위치시키면 됩니다.

### Kakao

kakao-key.json 파일은 모두의 발레 구글 드라이브의 개발 폴더에서 다운로드 받을 수 있습니다.

다운로드 후 `credentials/kakao/kakao-key.json` 에 위치시키면 됩니다.

## cities-csv-to-json

전국행정동리스트 CSV 파일을 json 파일로 변환합니다.

전국행정동리스트 스프레드시트는 [여기](https://docs.google.com/spreadsheets/d/18miy3THIfF8-Rzdu23CtcsOxZXsZXAoG/edit?usp=sharing&ouid=106558524234893023284&rtpof=true&sd=true)에 있습니다.

### 사용법

전국행정도리스트 스프레드시트에서 Cities, Districts, Blocks 로 정렬한 시트를 CSV로 다운로드 합니다.
해당 파일을 cities-csv-to-json/cities.csv에 위치시킨 후 아래 명령어를 실행합니다.

```bash
$ python cities-csv-to-json/script.py
```

## cities-json-to-firestore

cities-csv-to-json 으로 생성된 json 파일을 firestore 에 업로드 합니다.

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
