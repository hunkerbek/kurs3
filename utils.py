import json

def load_file(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)

