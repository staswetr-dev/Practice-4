n = int(input("Введіть N: "))

parni = 0
neparni = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "— парне")
        parni = parni + 1
    else:
        print(i, "— непарне")
        neparni = neparni + 1

print("Парних чисел:", parni)
print("Непарних чисел:", neparni)