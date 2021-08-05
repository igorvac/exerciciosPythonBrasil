lista = []
soma = 0

for i in range(0, 5):
    lista.append(float(input(f"Informe o valor {i + 1} ")))
    soma += lista[i]

print(soma)
print(soma/len(lista))
