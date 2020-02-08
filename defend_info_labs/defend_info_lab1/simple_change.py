import random

with open('input.txt', 'rb') as file:
    text = file.read()

print(text)
keys = {}
with open('keys.txt') as file:
    for line in file:
        keys[line.split()[0]] = line.split()[1]

symbols = set(text)
new_symbols = symbols.copy()


for symbol in symbols:
    if chr(symbol) not in keys:
        sym = random.choice(list(new_symbols))
        keys[chr(symbol)] = chr(sym + 1)
        new_symbols.remove(sym)

print(keys)

with open('keys.txt', 'w') as file:
    for key, val in keys.items():
        file.write('{} {}\n'.format(key, val))
del new_symbols

with open('output.txt', 'w') as file:
    for symbol in text:
        file.write(keys[chr(symbol)])

with open('output.txt', 'rb') as output:
    with open('input1.txt', 'w') as input1:
        text = output.read()
        for letter in text:
            for sym1, sym2 in keys.items():
                if chr(letter) == sym2:
                    input1.write(sym1)