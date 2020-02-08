N = input("Введите N ")
count = 0
for i in range(0, int(N)+1):
    sqrt_len = len(str(i**2))
    i_len = len(str(i))
    start = sqrt_len - i_len
    if str(i) == str(i**2)[start:]:
        print(i)
        count += 1

print("Количество чисел {}".format(count))