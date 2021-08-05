result = 0

for i in range(1, 6):
    num_temp = int(input(f"Insira o {i} numero: "))
    if i == 1:
        result = num_temp

    if num_temp > result:
        result = num_temp

    print(result)

print(f"\nO maio número é {result}")
