dict = {}

with open("input.txt") as file:
    letters = file.read()

for letter in letters:
    if letter != ' ':
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1

with open("output.txt", 'w') as file:
    for letter in sorted(dict, key=dict.get, reverse=True):
        file.write(letter + ' ' + str(dict[letter]) + '\n')
