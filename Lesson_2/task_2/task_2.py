import json


def write_order_to_json(filepath, **kwargs):
    with open(filepath, encoding='UTF-8') as json_file:
        data = json.load(json_file)

    data['orders'].append(kwargs)

    with open(filepath, 'w', encoding='UTF-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    for_write = [
        {'item': 'Lenovo Yoga 7i',
         'quantity': 1,
         'price': 186890.00,
         'buyer': 'Петин Петр',
         'date': '19-05-2022'},
    ]

    for order in for_write:
        write_order_to_json('orders.json', **order)
