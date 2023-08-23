import json
import datetime


def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(list_operations):
    result_list = []
    for x in list_operations:
        if x and x["state"] == "EXECUTED":
            result_list.append(x)
    return result_list


def date_time(x):
    return datetime.strptime(x["date"], '%Y-%m-%dT%H:%M:%S.%f')


def sorted_result_list(list_operations):
    return sorted(list_operations, key=date_time, reverse=True)


