a = int(input ("Введите a "))
b = int(input ("Введите b "))
c = int(input ("Введите c "))
if a + b == c:
    print ("a + b = c")
else:
    print ("a + b ≠ c")
if b == 0:
    print ("a + b ≠ с, и вообще, на ноль делить нельзя!")
else:
    if a / b == c:
        print ("a / b = c")
    else:
        print ("a / b ≠ c")
