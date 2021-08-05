countryA = 80000
growA = 1.03

countryB = 200000
growB = 1.015
count = 0

while True:
    countryA = countryA * growA
    countryB = countryB * growB
    count += 1
    if countryA > countryB:
        print(f"A população de A ultrapassou a de B em {count} anos.")
        print(f"A tem {int(countryA)} e B tem {int(countryB)} habitantes.")
        print(f"A diferença é de {int(countryA - countryB)}")
        break

    continue
