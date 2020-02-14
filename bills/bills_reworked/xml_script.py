from datetime import datetime
from xml.etree import ElementTree as et


ru_en_dict = {
    'Омский Газмяс': 'Omskiy Gazmyas',
    'Медсервис': 'Medservice',
    'Стройдвор': 'Stroidvor'
}


class BankAccount:
    def __init__(self, client, date, number, sum):
        self.client_name = ru_en_dict[client]
        self.date = datetime.strptime(date, "%d.%m.%Y")
        self.number = number
        self.sum = float(sum)

    def __str__(self):
        return f'{self.client_name} {self.date} {self.number} {self.sum}'


def xml_reader(file):
    accounts = []
    tree = et.parse(file)
    bank_accounts = tree.getroot()
    for i in range(len(bank_accounts)):
        account = bank_accounts[i].attrib
        one_acc = BankAccount(account.get('Client'),
                              account.get('Date'),
                              account.get('Number'),
                              account.get('Sum'))

        accounts.append(one_acc)
    return accounts


def sort_by_name(accs):
    for i in range(len(accs)-1):
        for j in range(len(accs)-1-i):
            if accs[j].client_name < accs[j+1].client_name:
                accs[j], accs[j+1]=accs[j+1], accs[j]
    return accs


def sort_by_date_after_sort_by_name(amounts):
    for i in range(len(amounts) - 1):
        for j in range(len(amounts) - i - 1):
            if amounts[j].date > amounts[j + 1].date and amounts[j].client_name == amounts[j + 1].client_name:
                amounts[j], amounts[j + 1] = amounts[j + 1], amounts[j]

    return amounts


accs = xml_reader('Lab_4_Scheta.xml')
for acc in accs:
    print(acc)


class XMLResult:
    def __init__(self, account, payment, change=0):
        self.client_name = account.client_name
        self.date_of_pay = payment.date
        self.number_of_pay = payment.number
        self.date_of_account = account.date
        self.number_of_account = account.number
        self.sum_of_payment = payment.sum
        self.change = change

    def __repr__(self):
        return f'Клиент {self.client_name} ' \
               f'{self.date_of_pay} положил деньги ' \
               f'платежом номер {self.number_of_pay} ' \
               f'на счет датируемый {self.date_of_account} ' \
               f'с номером {self.number_of_account} ' \
               f'в размере {self.sum_of_payment}, ' \
               f'сдача составила {self.change}'


def write_xml(results):
    root = et.Element("Payments")

    for result in results:
        et.SubElement(
            root, "payment", name=str(result.client_name),
            Date_of_pay=str(result.date_of_pay),
            Number_of_pay=str(result.number_of_pay),
            Date_of_account=str(result.date_of_account),
            Number_of_account=str(result.number_of_account),
            sum_of_payment=str(result.sum_of_payment)
        )

    tree = et.ElementTree(root)
    tree.write("result.xml")
