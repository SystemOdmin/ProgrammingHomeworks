a = [] 
s = input("Введите слово ")
while s != (""):
    a.append(s)
    s = input("Введите слово ")
for i in range(len(a)):
    print(a[i][i+1:])
