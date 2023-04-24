# CSV to JSON

모두의 발레에서 사용될 CSV 데이터를 JSON으로 변환하는 스크립트입니다.

## 전국행정동리스트 CSV

전국행정동리스트 스프레드시트는 [여기](https://docs.google.com/spreadsheets/d/18miy3THIfF8-Rzdu23CtcsOxZXsZXAoG/edit?usp=sharing&ouid=106558524234893023284&rtpof=true&sd=true)에 있습니다.

### 사용법

전국행정도리스트 스프레드시트에서 Cities, Districts, Blocks 로 정렬한 시트를 CSV로 다운로드 합니다.
해당 파일을 cities.csv로 이름을 바꾼 후 아래 명령어를 실행합니다.

```bash
$ python cities_csv_to_json.py
```
