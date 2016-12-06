b = 0
with open ('quotes.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        a = line.split()
        for word in a:
            if word == 'Разум' or word == 'разум':
                for i in range(len(a)):
                    if i == '—':
                            print(a[i:])
                    else:
                        continue
                b+=1          
            else:
                continue
print(b)
          
            
