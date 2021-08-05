maior = 0
menor = 0
soma = 0

for i in range(0, 6):
    num = int(input("Digite um número: "))

    if i == 0:
        maior = num
        menor = num

    elif num >= maior:
        maior = num

    elif num <= menor:
        menor = num

    soma += num

print(f"O maior é {maior}, o menor é {menor} e a soma é {soma}")
