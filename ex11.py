num1 = int(input("Escreva o primeiro número: "))
num2 = int(input("Escreva o segundo número: "))
soma = 0

for i in range(num1, num2 + 1):
    print(i)
    soma += i

print(soma)
