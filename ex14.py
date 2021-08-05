par = []
impar = []

for i in range(0, 10):
    num = int(input("escreva um número: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Essa lista tem {len(par)} números pares e {len(impar)} impares")
