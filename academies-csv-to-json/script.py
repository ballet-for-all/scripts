import csv
import json
from collections import OrderedDict

ACADEMIES_CSV_PATH = 'academies-csv-to-json/academies.csv'
ACADEMIES_JSON_PATH = 'academies-csv-to-json/academies.json'

SNS_LIST = [
    'kakaoTalk', 'naverTalkTalk', 'homepage', 'naverModoo', 'naverBlog',
    'naverCafe', 'instagram', 'facebook'
]


def read_academies_from_csv():
    with open(ACADEMIES_CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = [row for row in reader]
        return rows


def extract_list(raw_dict, key):
    result = []
    index = 0
    while True:
        if (f'{key}/{index}') not in raw_dict:
            break
        data = raw_dict[f'{key}/{index}']
        if data:
            result.append(data)
        index += 1
    return result


def extract_sns(raw_dict):
    sns = {}
    for sns_name in SNS_LIST:
        id = raw_dict[f'sns/{sns_name}']
        sns[sns_name] = id if id else None
    return sns


def extract_teachers(raw_dict):
    teachers = []
    index = 0
    while True:
        if (f'teachers/{index}/name') not in raw_dict:
            break

        teacher = {}
        name = raw_dict[f'teachers/{index}/name']
        teacher['name'] = name if name else None
        description = raw_dict[f'teachers/{index}/description']
        teacher['description'] = description if description else None
        imageUrl = raw_dict[f'teachers/{index}/imageUrl']
        teacher['imageUrl'] = imageUrl if imageUrl else None
        if name or description or imageUrl:
            teachers.append(teacher)
        index += 1
    return teachers


def extract_schedules(schedules_dict):
    schedules = []
    index = 0
    while True:
        if (f'schedules/{index}/startTime') not in schedules_dict:
            break

        schedule = {}
        startTime = schedules_dict[f'schedules/{index}/startTime']
        schedule['startTime'] = startTime if startTime else None
        durationInMinutes = schedules_dict[
            f'schedules/{index}/durationInMinutes']
        schedule['durationInMinutes'] = int(
            durationInMinutes) if durationInMinutes else None
        day = schedules_dict[f'schedules/{index}/day']
        schedule['day'] = day if day else None
        teacherName = schedules_dict[f'schedules/{index}/teacherName']
        schedule['teacherName'] = teacherName if teacherName else None
        if startTime or durationInMinutes or day or teacherName:
            schedules.append(schedule)
        index += 1
    return schedules


def extract_classes(classes_dict):
    classes = []
    index = 0
    while True:
        if (f'classes/{index}/className') not in classes_dict:
            break

        class_ = {}
        className = classes_dict[f'classes/{index}/className']
        class_['className'] = className if className else None
        classTag = classes_dict[f'classes/{index}/classTag']
        class_['classTag'] = classTag if classTag else None
        schadules_keys = [
            key for key in classes_dict.keys()
            if key.startswith(f'classes/{index}/schedules/')
        ]
        schedules_dict = {
            key.replace(f'classes/{index}/', ''): classes_dict[key]
            for key in schadules_keys
        }
        class_['schedules'] = extract_schedules(schedules_dict)
        if className or classTag or class_['schedules']:
            classes.append(class_)
        index += 1
    return classes


def extract_timetables(raw_dict):
    timetables = []
    index = 0
    while True:
        if (f'timetables/{index}/timetableName') not in raw_dict:
            break

        timetable = {}
        timetableName = raw_dict[f'timetables/{index}/timetableName']
        timetable['timetableName'] = timetableName if timetableName else None
        classes_keys = [
            key for key in raw_dict.keys()
            if key.startswith(f'timetables/{index}/classes/')
        ]
        classes_dict = {
            key.replace(f'timetables/{index}/', ''): raw_dict[key]
            for key in classes_keys
        }
        timetable['classes'] = extract_classes(classes_dict)
        if timetableName or timetable['classes']:
            timetables.append(timetable)
        index += 1
    return timetables


def extract_pricing(raw_dict):
    pricing_list = []
    index = 0
    while True:
        if (f'pricing/{index}/numberPerWeek') not in raw_dict:
            break

        pricing = {}
        numberPerWeek = raw_dict[f'pricing/{index}/numberPerWeek']
        pricing['numberPerWeek'] = int(
            numberPerWeek) if numberPerWeek else None
        totalCount = raw_dict[f'pricing/{index}/totalCount']
        pricing['totalCount'] = int(totalCount) if totalCount else None
        durationInMonth = raw_dict[f'pricing/{index}/durationInMonth']
        pricing['durationInMonth'] = int(
            durationInMonth) if durationInMonth else None
        classTimeInMinutes = raw_dict[f'pricing/{index}/classTimeInMinutes']
        pricing['classTimeInMinutes'] = int(
            classTimeInMinutes) if classTimeInMinutes else None
        plan = raw_dict[f'pricing/{index}/plan']
        pricing['plan'] = plan if plan else None
        originalPrice = raw_dict[f'pricing/{index}/originalPrice']
        pricing['originalPrice'] = originalPrice if originalPrice else None
        salePrice = raw_dict[f'pricing/{index}/salePrice']
        pricing['salePrice'] = salePrice if salePrice else None
        discountPercent = raw_dict[f'pricing/{index}/discountPercent']
        pricing['discountPercent'] = float(
            discountPercent.strip('%')) / 100.0 if discountPercent else None
        if numberPerWeek or totalCount or durationInMonth or classTimeInMinutes or plan or originalPrice or salePrice or discountPercent:
            pricing_list.append(pricing)
        index += 1
    return pricing_list


def academy_raw_to_dict(raw):
    raw_dict = dict(OrderedDict(raw))
    academy = {}
    name = raw_dict['name']
    academy['name'] = name if name else None
    address = raw_dict['address']
    academy['address'] = address if address else None
    academy['phone'] = extract_list(raw_dict, 'phone')
    academy['sns'] = extract_sns(raw_dict)
    academy['coupon'] = raw_dict['coupon'] != ''
    academy['images'] = extract_list(raw_dict, 'images')
    academy['teachers'] = extract_teachers(raw_dict)
    academy['timetables'] = extract_timetables(raw_dict)
    academy['pricing'] = extract_pricing(raw_dict)
    pricingDescription = raw_dict['pricingDescription']
    academy[
        'pricingDescription'] = pricingDescription if pricingDescription else None
    return academy


def write_dict_to_json_file(dict_data):
    with open(ACADEMIES_JSON_PATH, 'w', encoding='utf-8') as jsonfile:
        json.dump(dict_data, jsonfile, ensure_ascii=False, indent=2)


def main():
    academies = read_academies_from_csv()
    academies = [
        academy_raw_to_dict(academy) for academy in academies
        if academy['name']
    ]
    write_dict_to_json_file(academies)


if __name__ == '__main__':
    main()
