def is_fibbo(*array_of_numbers):
    for i in range(1, len(array_of_numbers) - 1):
        if int(array_of_numbers[i - 1]) + int(array_of_numbers[i]) != int(array_of_numbers[i + 1]):
            print("Не является последовательностью Фибоначчи")
            return False
    return True
