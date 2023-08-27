import json
from datetime import datetime


def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(list_operations):
    result_list = []
    for x in list_operations:
        if x and x["state"] == "EXECUTED":
            result_list.append(x)
    return result_list


def date_time(x) -> datetime:
    return datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f')


def sorted_result_list(list_operations):
    return sorted(list_operations, key=date_time, reverse=True)


def operation_details(input_str):
    if input_str is None:
        return "Нет информации"
    words = input_str.split()
    number = words[-1]
    name_card = " ".join(words[:-1])
    if len(number) == 20:
        return f"{name_card} **{number[-4:]}"
    return f"{name_card} {number[:4]} {number[4:6]}** **** {number[-4:]}"


def date_to_str(input_dict):
    return date_time(input_dict).strftime("%d.%m.%Y")



