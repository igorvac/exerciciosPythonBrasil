

while True:
    num = input("Digite o número que deseja o fatorial: ")

    try:
        num = int(num)
    except:
        print("Opa, esse número precisa ser inteiro! ")
        continue

    if num < 0:
        print("Opa, esse número precisa positivo! ")
        continue

    if num > 16:
        print("Opa, esse número precisa ser menor que 16! ")
        continue

    result = num

    for i in range(1, num):
        result = result * i

    print(f"O resultado é {result}")

    again = input("\nDeseja fazer outra operação? (Y/N)").lower()

    if again == "y":
        continue
    else:
        break
