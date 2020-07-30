import csv
from django.shortcuts import render
from datetime import datetime

from django.http import HttpResponse


def inflation_view(request):
    current_time = datetime.now().time()
    msg = f'Текущее время: {current_time}'

    CONTENT = []
    def csv_dict_reader(file_obj):
        reader = csv.DictReader(file_obj, delimiter=';')
        for line in reader:
            print(line)
            for key, values in line.items():
                if values == '':
                    line[key] = '-'
                elif '.' in values:
                    line[key] = float(values)
                else:
                    line[key] = int(values)

            CONTENT.append(line)

    with open("inflation_russia.csv", encoding='utf-8') as f_obj:
        csv_dict_reader(f_obj)

    print(CONTENT)

    # with open(r"C:\Unit\Django\dynamic-templates\task1\inflation_russia.csv", encoding='utf-8') as csvfile:
    #     CONTENT = list(csv.DictReader(csvfile))

    #return HttpResponse(CONTENT)

    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    #context = {}

    context = list(CONTENT)
    return render(request, template_name, context={'bus_stations': context})