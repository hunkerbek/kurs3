import json

def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(list_operations):
    result_list = []
    for x in list_operations:
        if x and x["state"] == "EXECUTED":
            result_list.append(x)
    return result_list


