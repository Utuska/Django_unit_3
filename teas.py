import csv


def csv_dict_reader(file_obj):
    reader = csv.DictReader(file_obj, delimiter=';')
    for line in reader:
         print(line)


if __name__ == "__main__":
    with open("inflation_russia.csv", encoding='utf-8') as f_obj:
        csv_dict_reader(f_obj)