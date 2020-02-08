def armstrong_num():
    count = 0
    for i in range(100, 9999):
        if i > 999:
            pow = 4
            if int(str(i)[0])**pow + int(str(i)[1])**pow + int(str(i)[2])**pow + int(str(i)[3])**pow == i:
                print("{} - число армстронга".format(i))
                count += 1

        else:
            pow = 3
            if int(str(i)[0]) ** pow + int(str(i)[1]) ** pow + int(str(i)[2]) ** pow == i:
                print("{} - число армстронга".format(i))
                count += 1

    print("Количество чисел {}".format(count))

    return count
