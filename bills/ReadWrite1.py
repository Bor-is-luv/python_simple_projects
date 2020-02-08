import csv
from xml.etree import ElementTree as et
from datetime import datetime


class CSVReader:
    def __init__(self, ClientName, Date, Number, Sum):
        try:
            self.ClientName = str(ClientName)
            self.Date = datetime.strptime(Date, "%d.%m.%Y")
            self.Number = str(Number)
            self.Sum = float(Sum)
        except ValueError:
            print('Деффчонка за рулём')

    def __str__(self):
        return (str(str(self.ClientName) + ' ' + str(self.Date) + ' ' + str(self.Number) + ' ' + str(self.Sum)))

    def __repr__(self):
        return (str(str(self.ClientName) + ' ' + str(self.Date) + ' ' + str(self.Number) + ' ' + str(self.Sum)))

    def csv_bd(File):
        platezhi = []
        platezhki = []
        with open('Lab_4_Platezhi.csv') as file:
            reader = csv.reader(file)
            for row in reader:
                row1 = row[0]
                platezhi.append(row1)

        for i in range(len(platezhi)):
            platezhi[i] = platezhi[i].replace('\t', ' ')

        for i in range(len(platezhi) - 1):
            CSV = CSVReader(platezhi[i + 1].partition(' ')[0],
                            platezhi[i + 1].partition(' ')[2].partition(' ')[0],
                            platezhi[i + 1].partition(' ')[2].partition(' ')[2].partition(' ')[0],
                            platezhi[i + 1].partition(' ')[2].partition(' ')[2].partition(' ')[2])
            platezhki.append(CSV)

        return platezhki
        del platezhi, reader, CSV

    def sum_of_payment(payments):
        sum = 0
        for payment in payments:
            sum += payment.Sum

        return sum

    def sort_by_date_after_sort_by_name(amounts):
        for i in range(len(amounts) - 1):
            for j in range(len(amounts) - i - 1):
                if amounts[j].Date > amounts[j + 1].Date and amounts[j].ClientName == amounts[j + 1].ClientName:
                    amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]

        return amounts

    def sort_by_name(amounts):
        for i in range(len(amounts) - 1):
            for j in range(len(amounts) - i - 1):
                if amounts[j].ClientName < amounts[j + 1].ClientName:
                    amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]

        return amounts


class XMLReader:
    def __init__(self, Client, Date, Number, Sum):
        try:
            if Client == 'Медсервис':
                self.ClientName = 'Medservice'
            elif Client == 'Стройдвор':
                self.ClientName = 'Stroidvor'
            else:
                self.ClientName = 'Omskiy Gazmyas'
            self.Date = datetime.strptime(Date, "%d.%m.%Y")
            self.Number = str(Number)
            self.Sum = float(Sum)
        except ValueError:
            print('Не мужик за рулём')

    def xml_bd(File):
        bills = []
        tree = et.parse(File)
        Bills = tree.getroot()
        for i in range(len(Bills)):
            bill = Bills[i].attrib
            one_bill = XMLReader(bill.get('Client'), bill.get('Date'), bill.get('Number'),
                                 bill.get('Sum'))
            bills.append(one_bill)

        return bills

    def __str__(self):
        return (str(str(self.ClientName) + ' ' + str(self.Date) + ' ' + str(self.Number) + ' ' + str(self.Sum)))

    def __repr__(self):
        return (str(str(self.ClientName) + ' ' + str(self.Date) + ' ' + str(self.Number) + ' ' + str(self.Sum)))


    def sort_by_date_after_sort_by_name(amounts):
        for i in range(len(amounts) - 1):
            for j in range(len(amounts) - i - 1):
                if amounts[j].Date > amounts[j + 1].Date and amounts[j].ClientName == amounts[j + 1].ClientName:
                    amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]

        return amounts

    def sort_by_name(amounts):
        for i in range(len(amounts) - 1):
            for j in range(len(amounts) - i - 1):
                if amounts[j].ClientName < amounts[j + 1].ClientName:
                    amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]

        return amounts

    def sum_of_payment(amounts):
        sum = 0
        for amount in amounts:
            sum += amount.Sum

        return sum


class XMLResult:
    def __init__(self, schet, platezh, sdacha=0):
        self.ClientName = schet.ClientName
        self.Date_of_pay = platezh.Date
        self.Number_of_pay = platezh.Number
        self.Date_of_account = schet.Date
        self.Number_of_account = schet.Number
        self.sum_of_payment = platezh.Sum
        self.sdacha = sdacha

    def __repr__(self):
        return (str('Клиент ' + str(self.ClientName) + ' ' + str(self.Date_of_pay) + ' положил деньги платежом номер ' +
                    str(self.Number_of_pay) + ' на счёт датируемый ' + str(self.Date_of_account) + ' с номером ' +
                    str(self.Number_of_account) + ' в размере ' + str(self.sum_of_payment) + ' ,сдача составила ' + str(
            self.sdacha)))

    def WriteXML(results):
        root = et.Element("Payments")

        for result in results:
            et.SubElement(root, "payment", name=str(result.ClientName), Date_of_pay=str(result.Date_of_pay),
                          Number_of_pay=str(result.Number_of_pay),
                          Date_of_account=str(result.Date_of_account), Number_of_account=str(result.Number_of_account),
                          sum_of_payment=str(result.sum_of_payment))

        tree = et.ElementTree(root)
        tree.write("result.xml")


if __name__ == '__main__':
    platezhi = CSVReader.csv_bd('Lab_4_Platezhi.csv')
    scheta = XMLReader.xml_bd('Lab_4_Scheta.xml')

