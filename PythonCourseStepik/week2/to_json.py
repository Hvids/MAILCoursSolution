import json
from functools import wraps
def to_json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        json_data = json.JSONEncoder().encode(data)
        return  json_data
    return  wrapper
# @to_json
# def get_data():
#   return {
#     'data': 42
#   }
# if __name__ == '__main__':
#     print(get_data())
