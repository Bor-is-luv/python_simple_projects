import math

a = 600851475143
just = 1
for i in range(3, 300425737571):
    for j in range(2, math.ceil(i / 2) + 1):
        if i % j == 0:
            continue
        elif j == math.ceil(i / 2) + 1:
            just = i
    if a % just == 0:
        big = just
