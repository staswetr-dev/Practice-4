n = int(input("Введіть число: "))

if n < 1:
    print("Число має бути не менше 1!")
else:
    for i in range(1, 11):
        print(n, "×", i, "=", n * i)