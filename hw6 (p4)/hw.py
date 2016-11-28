a = input("Введите слово \n")
for i in range(len(a)):
    print(a)
    a = a[1:] + a[0]
