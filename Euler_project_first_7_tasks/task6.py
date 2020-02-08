a = 0
sum = 0
for i in range(1, 100):
    a = a + i * i

for j in range(1, 100):
    sum = sum + j

print(sum * sum - a)
