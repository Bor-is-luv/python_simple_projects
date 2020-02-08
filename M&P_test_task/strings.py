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
