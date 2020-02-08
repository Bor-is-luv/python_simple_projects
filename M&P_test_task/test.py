import sys
from time import sleep


matrix_len = int(input("Введите длину стороны квадратной матрицы.\nТолько не слишком большое, Вам потом вручную"
                       " заполнять матрицу "))
matrix = [[int(input("Введите число ")) for y in range(matrix_len)] for x in range(matrix_len)]  # инициализация матрицы

min_element = sys.maxsize  # максимальное интовое число для Вашей системы
print(matrix, " матрица до умножения минимального элемента на 10")
min_column = 1
min_row = 1
row_number = 0

for row in matrix:  # проходимся по каждой строке матрицы
    row_number += 1
    column_num = 0
    for number in row:  # по каджому элементу строки
        column_num += 1
        if number < min_element:  # если число в матрице меньше текущего минимального значения, то записываем число в
            # min_element, min_row - строка минимального элемента, min_column - колонка мин.элемента
            min_element = number
            min_row = row_number
            min_column = column_num

print(min_element, "минимальный элемент")
matrix[min_row - 1][min_column - 1] *= 10
print(matrix, "матрица после умножения минимального элемента на 10")

max_on_the_diagonal = -sys.maxsize
for i in range(matrix_len):
    if matrix[i][i] > max_on_the_diagonal:  # смотрим числа только на главной диагонали
        max_on_the_diagonal = matrix[i][i]

print(max_on_the_diagonal, 'максимальный элемент на диагонали')
sum_of_digits = 0
while max_on_the_diagonal > 0:
    sum_of_digits = sum_of_digits + max_on_the_diagonal % 10
    max_on_the_diagonal = max_on_the_diagonal // 10

print(sum_of_digits, 'сумма цифр максимального числа на диагонали')


def str_split(str):  # функция, делящая строку на слова
    words = []
    word = ''
    for letter in str:
        if letter != ' ':
            word += letter
        else:
            words.append(word)
            word = ''

    if word != '': words.append(word)

    return words


def word_len(word):  # вычисляет длину слова
    count = 0
    for letter in word:
        count += 1

    return count


str = input("Введите строку с пробелами ")
words = str_split(str)
longest_word_len = 0
j = 0
long_word_index = 0
for word in words:  # цикл для нахождения длинейшего слова
    if word_len(word) > longest_word_len:
        longest_word_len = word_len(word)
        long_word_index = j
    j += 1

print(words[long_word_index], 'самое длинное слово, его длина', longest_word_len)

print(words)
frequency = {}
for word in words:
    if word[0] in frequency.keys():  # если в словаре существует значение по такому ключу, то прибавляем к нему 1
        frequency[word[0]] += 1
    else:  # а если нет, то создаём
        frequency[word[0]] = 1

max_value = 0
key_max = 'Default'
for key, value in frequency.items():
    if value > max_value:
        max_value = value
        key_max = key

print(key_max, 'на эту букву начинается большинство слов в строке, их число ', frequency[key_max])

print('Использую time.sleep(20), чтобы программа не закрывалась по завершении при запуске из командной строки')

sleep(20)
