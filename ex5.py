
while True:

    print("Bem vindo ao comparador de crescimento!")

    countryA = float(input("Insira a população da cidade A: "))
    growA = float(input("Insira taxa de crescimento (em %): ")) / 100 + 1

    countryB = float(input("Insira a população da cidade B: "))
    growB = float(input("Insira taxa de crescimento (em %): ")) / 100 + 1

    anos = 0

    if countryA <= countryB:
        while True:
            countryA = countryA * growA
            countryB = countryB * growB
            anos += 1
            if countryA > countryB:
                print(f"A população de A ultrapassou a de B em {anos} anos.")
                print(
                    f"A tem {int(countryA)} e B tem {int(countryB)} habitantes.")
                print(f"A diferença é de {int(countryA - countryB)}")
                break

            continue

    else:
        while True:
            countryA = countryA * growA
            countryB = countryB * growB
            anos += 1
            if countryB > countryA:
                print(f"A população de B ultrapassou a de A em {anos} anos.")
                print(
                    f"A tem {int(countryA)} e B tem {int(countryB)} habitantes.")
                print(f"A diferença é de {int(countryB - countryA)}")
                break

            continue

    repeat = input("Deseja continuar? (Y/N)").lower()
    if repeat == "y":
        continue
    else:
        break
