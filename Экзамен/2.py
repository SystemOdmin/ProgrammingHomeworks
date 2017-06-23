import re
def newfile(a):
    with open (a,'w', encoding='utf-8') as f:
        f.write('')
def table(a,b):
    with open (a, 'r', encoding='cp1251') as f:
        x = ''.join(re.findall('content="(.+)" name="author">', f.read()))
        f.seek(0,0)
        y = ''.join(re.findall('content="(.+)" name="created"', f.read()))
    with open (b, 'a', encoding='utf-8') as f:
        f.write('\n' + a + ',' + x + ',' + y)

newfile('2.csv')
table('_itartass1.xhtml', '2.csv')
table('_itartass2.xhtml', '2.csv')
table('_itartass3.xhtml', '2.csv')
table('_itartass4.xhtml', '2.csv')
table('_itartass5.xhtml', '2.csv')
table('_rbk2.xhtml', '2.csv')
table('_rbk3.xhtml', '2.csv')
table('_rbk4.xhtml', '2.csv')
table('_rbk6.xhtml', '2.csv')
table('_rbk7.xhtml', '2.csv')
table('_rian1.xhtml', '2.csv')
table('_rian2.xhtml', '2.csv')
table('_rian3.xhtml', '2.csv')
table('_rian5.xhtml', '2.csv')
 
