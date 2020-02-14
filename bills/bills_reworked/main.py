import csv_script
import xml_script


def sort(payments, accounts):
    accounts = xml_script.sort_by_name(accounts)
    payments = csv_script.sort_by_name(payments)

    accounts = xml_script.sort_by_date_after_sort_by_name(accounts)
    payments = csv_script.sort_by_date_after_sort_by_name(payments)


def business(payments, accounts):
    result = []
    for acc in accounts:
        for pay in payments:
            if acc.client_name == pay.client_name and acc.sum > 0 and pay.sum > 0:
                if acc.sum > pay.sum:
                    acc.sum -= pay.sum
                    result.append(xml_script.XMLResult(acc, pay))
                    pay.sum = 0
                    print('platezh sum')
                    # ended.append('')

                elif acc.sum < pay.sum:
                    change = pay.sum - acc.sum
                    result.append(xml_script.XMLResult(acc, pay, change))
                    pay.sum -= acc.sum
                    acc.sum = 0
                    print('счёт сум')
                else:
                    result.append(xml_script.XMLResult(acc, pay))
                    acc.sum = 0
                    pay.sum = 0
                    print('nothing')
            elif acc.sum == 0:
                print('брякнулось')
                break
            elif pay.sum == 0:
                print('continue')
                continue

    return result


if __name__ == '__main__':
    payments = csv_script.csv_reader('Lab_4_Platezhi.csv')
    accounts = xml_script.xml_reader('Lab_4_Scheta.xml')
    sum_of_payment = csv_script.sum_of_payment(payments)
    sort(payments, accounts)
    results = business(payments, accounts)
    for i in results:
        print(i)
    xml_script.write_xml(results)
