fib1 = 1
fib2 = 1
fib_sum2 = 0
fib_sum = 0
while fib_sum < 4000000:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    if fib_sum % 2 == 0:
        fib_sum2 = fib_sum2 + fib_sum
        print(fib_sum2)
print(fib_sum2)
