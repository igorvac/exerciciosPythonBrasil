num = int(input("Digite um número: "))
lista = []
cont = 0

for i in range(1, num):
    div = []
    for j in range(2, i):
        if i % j == 0 and i != j:
            div.append(i)
        cont += 1

    if len(div) == 0:
        lista.append(i)

print(lista)
print(f"Foram realizadas {cont} divisões")
