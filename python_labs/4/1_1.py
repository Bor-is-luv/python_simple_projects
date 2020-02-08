numbers = [1, 5, 2, 6, 3, 7]
def uniq(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
        else:
            return False
    return True
print(uniq(numbers))
