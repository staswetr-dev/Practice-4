balance = 1000

while True:
    print()
    print("=== БАНКОМАТ ===")
    print("1 — Переглянути баланс")
    print("2 — Поповнити рахунок")
    print("3 — Зняти кошти")
    print("4 — Вийти")

    vibir = input("Ваш вибір: ")

    if vibir == "1":
        print("Ваш баланс:", balance, "грн")

    elif vibir == "2":
        suma = int(input("Сума поповнення: "))
        if suma <= 0:
            print("Сума має бути більшою за нуль!")
        else:
            balance = balance + suma
            print("Рахунок поповнено.")
            print("Баланс:", balance, "грн")

    elif vibir == "3":
        suma = int(input("Сума для зняття: "))
        if suma <= 0:
            print("Сума має бути більшою за нуль!")
        elif suma > balance:
            print("Недостатньо коштів.")
        else:
            balance = balance - suma
            print("Операція успішна.")
            print("Баланс:", balance, "грн")

    elif vibir == "4":
        print("Дякуємо за використання банкомата!")
        break

    else:
        print("Неправильний пункт меню.")