import math
i = 6
k = 13
while i < 10001:
    for j in range(2,int(math.sqrt(k))):
        if k % j == 0:
            continue
        k = k+1
    i = i+1


print(k)
