from config import DATA_DIR
import json


def get_data():
    """
    Функция извлекает данные из json файла и преобразует в читаемый формат (словарь)
    """
    with open(DATA_DIR, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)
    return data


def encode_count_num(count_num):
    """
    Функция, которая возвращает скрытый счет/номер
    """
    if len(count_num) == 20:
        return f'**{count_num[-4:]}'
    elif len(count_num) == 16:
        return f'{count_num[:4]} {count_num[4:6]}** **** {count_num[-4:]}'


def splitting_text_numbers(count):
    """
    Функция которая возвращает в списке название карты/счета и номер
    """
    text = ""
    numbers = ""
    output = []
    for i in count:
        if i.isdigit():
            numbers += i
        else:
            text += i
    output.append(text.strip())
    output.append(numbers)
    return output
