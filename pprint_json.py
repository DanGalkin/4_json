import json


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as json_data_file:
        json_data = json.loads(json_data_file.read())
    return json_data


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    json_filepath = input('Где лежит JSON-файл, который приводим в порядок?')
    pretty_print_json(load_data(json_filepath)[0])
