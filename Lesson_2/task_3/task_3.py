import yaml

data_dict = {
    "data_list": ["Something_1",
                  "Something_2",
                  "Something_3"],
    "number": 110,
    "inner_dict": {'1€': 13,
                   '2€': "something",
                   '3€': ["something_1", "something_2"]}}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_dict, f_n, default_flow_style=True, allow_unicode=True)

with open('file.yaml', encoding='utf-8') as f_n:
    CONTENT_FILE = yaml.load(f_n, Loader=yaml.FullLoader)
    print(CONTENT_FILE)

    if CONTENT_FILE == data_dict:
        print("Данные совпадают")
    else:
        print("Данные не совпадают")