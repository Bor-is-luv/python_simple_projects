from ReadWrite1 import CSVReader, XMLReader, XMLResult


def sort(platezhi, scheta):
    scheta = XMLReader.sort_by_name(scheta)
    platezhi = CSVReader.sort_by_name(platezhi)
    scheta = XMLReader.sort_by_date_after_sort_by_name(scheta)
    platezhi = CSVReader.sort_by_date_after_sort_by_name(platezhi)


def busines(platezhi, scheta):
    result = []
    ended = []
    for schet in scheta:
        for platezh in platezhi:
            if schet.ClientName == platezh.ClientName and schet.Sum > 0 and platezh.Sum > 0:
                if schet.Sum > platezh.Sum:
                    schet.Sum -= platezh.Sum
                    result.append(XMLResult(schet, platezh))
                    platezh.Sum = 0
                    print('platezh sum')
                    # ended.append('')

                elif schet.Sum < platezh.Sum:
                    sdacha = platezh.Sum - schet.Sum
                    result.append(XMLResult(schet, platezh, sdacha))
                    platezh.Sum -= schet.Sum
                    schet.Sum = 0
                    print('счёт сум')
                else:
                    result.append(XMLResult(schet, platezh))
                    schet.Sum = 0
                    platezh.Sum = 0
                    print('nothing')
            elif schet.Sum == 0:
                print('брякнулось')
                break
            elif platezh.Sum == 0:
                print('continue')
                continue

    return result


if __name__ == '__main__':
    platezhi = CSVReader.csv_bd('Lab_4_Platezhi.csv')
    scheta = XMLReader.xml_bd('Lab_4_Scheta.xml')
    sum_of_payment = CSVReader.sum_of_payment(platezhi)
    sort(platezhi, scheta)
    results = busines(platezhi, scheta)
    XMLResult.WriteXML(results)
