import requests  # pip install requests
import random
import json


def get_random_numbers():
    numbers = random.sample(range(1, 46), 6)
    return sorted(numbers)


def get_lotto_numbers(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    res = requests.get(url).text  # type == String
    data = json.loads(res)  # type == dict
    bonus_number = data['bnusNo']

    real_numbers = []

    if data['returnValue'] == 'success':
        for key, value in data.items():
            if 'drwtNo' in key:
                real_numbers.append(value)

        real_numbers.sort()
    return {'real': real_numbers, 'bonus': bonus_number}


def get_result(real_list, random_list, bonus):
    lucky = set(real_list)
    real = set(random_list)

    match_count = len(real.intersection(lucky))

    result = '꽝'
    if match_count == 6:
        result = 1
    elif match_count == 5 and bonus in random_list:
        result = 2
    elif match_count == 5:
        result = 3
    elif match_count == 4:
        result = 4
    elif match_count == 3:
        result = 5

    return result


print(__name__)
