numbers = []
positive_sum = 0
negative_sum = 0
number = int(input("Введите целое число "))
while number != 0:
    numbers.append(number)
    number = int(input())

for item in numbers:
    if item > 0:
        positive_sum += item
    else:
        negative_sum += item

print("Сумма положительных равна {}".format(positive_sum))
print("Сумма положительных равна {}".format(negative_sum))



