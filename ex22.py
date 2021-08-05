num = int(input("Digite um número para saber se ele é primo: "))
div = []

for i in range(2, num):
    if num % i == 0 and num != i:
        div.append(i)

if len(div) == 0:
    print("O número é primo")

else:
    print("O número não é primo")
    print(f"Ele é divisível por {div}")
