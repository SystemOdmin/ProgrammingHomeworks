def newfile(a):
    with open (a,'w', encoding='utf-8') as f:
        f.write('')

def count_lex(a,b):
    with open (a, 'r', encoding='cp1251') as f:
        y = str(f.read().count('lex'))
    with open (b, 'a', encoding='utf-8') as f:
        f.write('\n' + a + '    ' + y)

newfile('1.txt')
count_lex('_itartass1.xhtml', '1.txt')
count_lex('_itartass2.xhtml', '1.txt')
count_lex('_itartass3.xhtml', '1.txt')
count_lex('_itartass4.xhtml', '1.txt')
count_lex('_itartass5.xhtml', '1.txt')
count_lex('_rbk2.xhtml', '1.txt')
count_lex('_rbk3.xhtml', '1.txt')
count_lex('_rbk4.xhtml', '1.txt')
count_lex('_rbk6.xhtml', '1.txt')
count_lex('_rbk7.xhtml', '1.txt')
count_lex('_rian1.xhtml', '1.txt')
count_lex('_rian2.xhtml', '1.txt')
count_lex('_rian3.xhtml', '1.txt')
count_lex('_rian5.xhtml', '1.txt')
 
