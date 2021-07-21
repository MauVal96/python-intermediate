# Nested Lists and Dictionaries
def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {
        "firstname": "Mauricio",
        "lastname": "Valadez"
    }

    super_list = [
        {"firstname": "Mauricio", "lastname": "Valadez"},
        {"firstname": "Carlos", "lastname": "García"},
        {"firstname": "Francisco", "lastname": "Hernández"},
        {"firstname": "Laura", "lastname": "Pérez"},
        {"firstname": "Gabriela", "lastname": "Rojas"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "float_nums": [1.2, 3.7, 9.86]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for item in super_list:
        print(item["firstname"], "-", item["lastname"])

if __name__ == '__main__':
    run()