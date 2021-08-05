num = int(input("Digite um número: "))
lista = []
cont = 0

for i in range(2, num):
    if (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
        lista.append(i)
    elif i == 2 or i == 3 or i == 5 or i == 7:
        lista.append(i)
    cont += 1

print(lista)
print(f"Foram realizadas {cont} operações")
