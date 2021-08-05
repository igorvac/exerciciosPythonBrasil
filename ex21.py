num = int(input("Digite um número para saber se ele é primo: "))

if num % 2 == 0 or num == 2 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
    print("Não é primo")

else:
    print("É primo!")
