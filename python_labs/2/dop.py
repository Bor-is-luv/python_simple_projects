K = input('Введите целое число, не превышающее 10000 ')
count = 0
number = 0
while count < int(K):
    number += 1
    sum_of_numbers = sum(map(int, list(str(number))))
    if sum_of_numbers == 10:
        count += 1


print(number)