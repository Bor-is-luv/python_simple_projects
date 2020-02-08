numbers = [1, 5, 2, 6, 3, 7]

def uniq(numbers):
    if numbers[1] > numbers[0]:
        for i in range(len(numbers) - 1):
            if numbers[i+1] < numbers[i]:
                return False
    elif numbers[1] < numbers[0]:
        for i in range(len(numbers) - 1):
            if numbers[i+1] > numbers[i]:
                return False

    return True
print(uniq(numbers))