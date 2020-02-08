num = []
for i in range(100, 999):
    for j in range(100, 999):
        a = i * j
        b = str(a)
        if (b[0] == b[-1]) & (b[1] == b[-2]) & (b[2] == b[-3]):
            num.append(a)

num.sort()
print(num)
