num = int(input("Insira um numero para ser realizada a tabuada: "))

print(f"A tabuada do {num} é: ")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
