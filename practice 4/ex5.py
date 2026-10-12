secret_number = 7
sproby = 0

while True:
    chislo = int(input("Введіть число: "))
    sproby = sproby + 1

    if chislo < secret_number:
        print("Загадане число більше.")
        print()
    elif chislo > secret_number:
        print("Загадане число менше.")
        print()
    else:
        print("Ви вгадали!")
        print("Кількість спроб:", sproby)
        break