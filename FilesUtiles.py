import json

from Plant import Plant


def obj_list_dict(list_obj:list):
    return [obj.__dict__ for obj in list_obj]

def obj_dict(obj):
    if obj.__class__ == Plant:
        return obj.__dict__
    else:
        return [obj.__dict__ for obj in obj]

def get_plant_from_file(file_name)->list[dict]:
    with open(file_name) as f:
        d = json.load(f)
        f.close()
        return d

def write_to_file(obj:dict):
    with open('save.json','w') as f:
        f.write(json.dumps(obj))
        f.close()

def read_from_file() -> dict:
    with open('save.json') as f:
        d = json.load(f)
        f.close()
        return d