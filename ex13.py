base = int(input("Insira a base: "))
ex = int(input("Insira o expoente: "))
result = base

print(base ** ex)

for i in range(1, ex):
    result = result * base

print(result)
