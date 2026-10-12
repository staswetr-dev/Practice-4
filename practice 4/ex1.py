n = int(input("Введіть N: "))

print("Прямий порядок:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

print("Зворотний порядок:")
for i in range(n, 0, -1):
    print(i, end=" ")
print()