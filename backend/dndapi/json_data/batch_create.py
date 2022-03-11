
import json
import os

def fetch_from_json(name_of_json: str):
    obj_meta = []
    file = f'{os.path.dirname(os.path.realpath(__file__))}\{name_of_json}.json'
    with open(file, 'r') as d:
        obj_meta.append(json.load(d))
    return obj_meta
    