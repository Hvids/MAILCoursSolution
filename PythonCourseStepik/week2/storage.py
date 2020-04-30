import argparse
import json
import os
import tempfile


def get_storage_path():
    name_file = 'storage.data'
    storage_path = os.path.join(tempfile.gettempdir(), name_file)
    return storage_path


def emty_file(srtoage_path):
    empty = False
    with open(storage_path, 'r') as file_read:
        data = file_read.read()
        if data == '':
            empty = True
    return empty


def create_storage(storage_path):
    with open(storage_path, 'w') as file_write:
        data = {}
        json_data = json.JSONEncoder().encode(data)
        file_write.write(json_data)


def read_storage(storage_path):
    with open(storage_path, 'r') as file_read:
        data_read = file_read.read()
        data_read = json.JSONDecoder().decode(data_read)
    return data_read


def write_storage(storage_path, data):
    with open(storage_path, 'w') as file_write:
        json_data = json.JSONEncoder().encode(data)
        file_write.write(json_data)


def insert_value(key, value, storage_path):
    data = read_storage(storage_path)
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]
    write_storage(storage_path, data)


def get_value_by_key(key, storage_path):
    data = read_storage(storage_path)
    if key in data:
        for i, value in enumerate(data[key]):
            if i == len(data[key]) - 1:
                print(f'{value}')
            else:
                print(f'{value}, ', end='')
    else:
        print('None')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', type=str)
    parser.add_argument('-v', '--val', type=str)
    args = parser.parse_args()
    storage_path = get_storage_path()
    if emty_file(storage_path):
        create_storage(storage_path)
    if args.val and args.key:
        insert_value(args.key, args.val, storage_path)
    elif args.key:
        get_value_by_key(args.key, storage_path)
