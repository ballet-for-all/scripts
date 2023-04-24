import csv
import json

csv_file_path = 'cities.csv'
json_file_path = 'cities.json'

# Open the CSV file and read its contents
with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = [row for row in reader]

# Group the rows by city and district
groups = {}
for row in rows:
    city = row['Cities']
    district = row['Districts']
    block = row['Blocks']
    if city not in groups:
        groups[city] = {}
    if district not in groups[city]:
        groups[city][district] = []
    groups[city][district].append(block)

# Convert the groups into the desired JSON format
json_data = []
for city, districts in groups.items():
    city_data = {'name': city, 'districts': []}
    for district, blocks in districts.items():
        district_data = {
            'name': district,
            'blocks': [{
                'name': block
            } for block in blocks]
        }
        city_data['districts'].append(district_data)
    json_data.append(city_data)

# Write the JSON data to a file
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(json_data, jsonfile, ensure_ascii=False, indent=2)
