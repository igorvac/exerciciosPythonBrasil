limit = 500

fib = 0
pFib = 1

print(fib)
print(pFib)

while pFib < limit:
    temp = pFib
    pFib = fib + pFib
    print(pFib)
    fib = temp
