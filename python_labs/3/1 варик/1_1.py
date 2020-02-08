zresult = 1
with open('input.txt') as file:
    numbers = file.read()

numbers = numbers.split(' ')
for number in numbers:
    result *= int(number)

with open('output.txt', 'w') as file:
    file.write(str(result))