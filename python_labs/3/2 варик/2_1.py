with open('input.txt') as file:
    numbers = file.read()

numbers = numbers.split(' ')
max = int(numbers[0])
for number in numbers:
    if int(number) > max:
        max = int(number)

with open('output.txt', 'w') as file:
    file.write(str(max))