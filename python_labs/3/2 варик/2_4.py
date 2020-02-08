with open("input_2.txt") as file:
    words_1 = file.read().split(' ')

print(words_1)
with open("input_1.txt") as file:
    words_2 = file.read().split(' ')

print(words_2)
result = [word for word in words_1 if word not in words_2]
print(result)