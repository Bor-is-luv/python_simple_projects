from functools import reduce

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

def lists(*args):
    ln = len(args)
    result = []
    for i in range (0, ln):
        for j in range(0, ln):
            if i == j:
                continue
            else:
                if set(args[i]) & set(args[j]):
                    result.append(set(args[i]) & set(args[j]))

    return result

print(lists(list_1, list_2, list_3))