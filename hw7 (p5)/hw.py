a = 0
b = 0
with open ('text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line.replace('\ufeff', '')
        line.replace('\n', '')
        c = line.split()
        for i in c:
            if len(i) == 1:
                a+=1
            elif len(i) == 3:
                b+=1
if a == 0:
    print('Слов длины 1 нет')
if b == 0:
    print('Слов длины 3 нет')
else:
    print(b/a) 
        
    
    
