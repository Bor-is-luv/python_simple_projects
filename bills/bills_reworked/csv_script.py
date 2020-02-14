import csv
from datetime import datetime


class Bill:
    def __init__(self, client_name,
                 date, number, sum):
        self.client_name = client_name
        self.date = datetime.strptime(date, "%d.%m.%Y")
        self.number = number
        self.sum = float(sum)

    def __str__(self):
        return f'{self.client_name} {self.date} {self.number} {self.sum}'


def csv_reader(file):
    bills = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            bills.append(row[0])

    for i in range(len(bills)):
        bills[i] = bills[i].replace('\t', ' ')

    csv_objects = []
    for i in range(len(bills)-1):
        CSV = Bill(bills[i+1].partition(' ')[0],
                   bills[i + 1].partition(' ')[2].partition(' ')[0],
                   bills[i + 1].partition(' ')[2].partition(' ')[2].partition(' ')[0],
                   bills[i + 1].partition(' ')[2].partition(' ')[2].partition(' ')[2])
        csv_objects.append(CSV)

    return csv_objects


def sum_of_payment(payments):
    return sum([float(x.sum) for x in payments])


def sort_by_name(amounts):
    for i in range(len(amounts) - 1):
        for j in range(len(amounts) - i - 1):
            if amounts[j].client_name < amounts[j + 1].client_name:
                amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]

    return amounts


def sort_by_date_after_sort_by_name(amounts):
    for i in range(len(amounts) - 1):
        for j in range(len(amounts) - i - 1):
            if amounts[j].date > \
                    amounts[j + 1].date and \
                    amounts[j].client_name == \
                    amounts[j + 1].client_name:
                amounts[j], amounts[j + 1] = \
                    amounts[j + 1], amounts[j]
    return amounts
