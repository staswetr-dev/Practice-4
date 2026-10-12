n = int(input("Введіть N: "))

suma = 0
suma_parni = 0
suma_neparni = 0

# вивід виразу 1 + 2 + 3...
for i in range(1, n + 1):
    suma = suma + i

    if i % 2 == 0:
        suma_parni = suma_parni + i
    else:
        suma_neparni = suma_neparni + i

    if i < n:
        print(i, end=" + ")
    else:
        print(i, end=" = ")

print(suma)
print()

print("Сума:", suma)
print("Сума парних:", suma_parni)
print("Сума непарних:", suma_neparni)