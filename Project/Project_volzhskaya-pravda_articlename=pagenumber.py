# в комментариях описаны строки, не обязательные для успешного сохранения, но, возможно, полезные для её последующей обработки и отображения

import urllib.request
import re
import os
import shutil
import time

##def create_path(root, folder1, folder2, folder3):        
##    if not os.path.exists(str(root)):
##        os.makedirs(str(root) + '/' + str(folder1))
##        os.makedirs(str(root) + '/' + str(folder2))
##        os.makedirs(str(root) + '/' + str(folder3))
    
def standart_date(a):
    standart_date = a.replace(' Январь ', '.01.')
    standart_date = standart_date.replace(' Февраль ', '.02.')
    standart_date = standart_date.replace(' Март ', '.03.')
    standart_date = standart_date.replace(' Апрель ', '.04.')
    standart_date = standart_date.replace(' Май ', '.05.')
    standart_date = standart_date.replace(' Июнь ', '.06.')
    standart_date = standart_date.replace(' Июль ', '.07.')
    standart_date = standart_date.replace(' Август ', '.08.')
    standart_date = standart_date.replace(' Сентябрь ', '.09.')
    standart_date = standart_date.replace(' Октябрь ', '.10.')
    standart_date = standart_date.replace(' Ноябрь ', '.11.')
    standart_date = standart_date.replace(' Декабрь ', '.12.')
    standart_date = re.sub('[йцукенгшщзхъфывапролджэячсмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,\\n\\t ]', '', standart_date)
    return standart_date

def cleantext(text):
    cleantext = re.sub('\\n<.*?>', '', text) # -- опциональное удаление надписей на картинках, которые в основном пустые
    cleantext = cleantext.lstrip('\n\t ')
    cleantext = re.sub('<.*?>', '', cleantext) 
    cleantext = cleantext.replace('\n&nbsp;', '') # -- опциональное удаление пустых строк, состоящих из неразрывных пробелов
    cleantext = cleantext.replace('&nbsp;', ' ',) # -- опциональная замена неразрывных пробелов на обычные, на всякий случай
    return cleantext

def create_metadata(file, folder=''): # -- параметр folder для фунцкции в текущем виде не нужен, но я его оставлю, чтобы не забыть идею
    with open (folder + file, 'w', encoding='utf-8') as f:
        metadata = ('path,author,sex,birthday,header,created,sphere,genre_fi,type,topic,chronotop,style,audience_age,audience_level,audience_size,source,publication,publisher,publ_year,medium,country,region,language\n')
        f.write(metadata)
    
def add_metadata(file, path, author, header, created, topic, source, publ_year, folder=''): # -- параметр folder для фунцкции в текущем виде не нужен, но я его оставлю, чтобы не забыть идею
    with open (file,'a', encoding='utf-8') as f:
        metadata = (path + ',' + author + ',,,' + header + ',' + created +',публицистика,,,' + topic + ',,нейтральный,н-возраст,н-уровень,городская,' + source + ',Волжская правда,publisher,' + publ_year + ',газета,Россия,республика Марий Эл,ru\n')
        f.write(metadata)
##
##def fixate_metadata(file, folder):
##    if os.path.exists(folder + '/' + file):
##        os.remove(folder + '/' + file)
##    shutil.move(file, folder)
    
        
def download_page(url, pagenumber_first, pagenumber_last):
    if os.path.exists('volzhskaya_pravda/metadata.csv'):
        shutil.move('volzhskaya_pravda/metadata.csv', './')
    if os.path.exists('metadata.csv'):
        with open ('metadata.csv', 'r', encoding='utf-8') as f:
            lastline = f.readlines()[-1]
            pagenumber_exist = int(''.join(re.findall('volzhskaya_pravda/plain/(.*?).txt', lastline)))
            if pagenumber_exist > pagenumber_first:
                pagenumber_first = pagenumber_exist + 1
    else:
        create_metadata('metadata.csv', 'volzhskaya_pravda')
    for i in range(pagenumber_first, pagenumber_last):
        try:
            req = urllib.request.Request(url + str(i), headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'})
            with urllib.request.urlopen(req) as response:
                html = response.read().decode('utf-8')
                author = ''.join(re.findall('<meta name="author" content="(.*?)" />', html))
                header = ''.join(re.findall('<meta name="title" content="(.*?)" />', html))
                created = standart_date(''.join(re.findall('<span class="itemDateCreated">(.*?) [0-9]+?:', html, flags=re.DOTALL)))
                publ_year = re.sub('[0-9][0-9].[0-9][0-9].', '', created)
                publ_month = re.sub('.[0-9][0-9][0-9][0-9]', '', created)
                publ_month = re.sub('[0-9][0-9].', '', publ_month)
                topic = ''.join(re.findall('<span>Опубликовано в.*?<a href=".*?">(.*?)</a>', html, flags=re.DOTALL))
                intro = ''.join(re.findall('<div class="itemIntroText">?(.*?)</div>', html, flags=re.DOTALL))
                introtext = ''.join(re.findall('<p>(.+?)</p>', intro))
                full = ''.join(re.findall('<div class="itemFullText">+?(.*?)</div>', html, flags=re.DOTALL))
                fulltext = ''.join(re.findall('<p>(.+?)</p>', full))
                text = cleantext(intro + full)
                with open (str(i) + '.txt', 'w', encoding='utf-8') as f:
                    f.write('@au ' + author + '\n')
                    f.write('@ti ' + header + '\n')
                    f.write('@da ' + created + '\n')
                    f.write('@topic ' + topic + '\n')
                    f.write('@url ' + url + str(i) + '\n')
                    f.write(text)
                if not os.path.exists('volzhskaya_pravda/mystem-plain/' + publ_year + '/' + publ_month):
                    os.makedirs('volzhskaya_pravda/mystem-plain/' + publ_year + '/' + publ_month)
                if not os.path.exists('volzhskaya_pravda/mystem-xml/' + publ_year + '/' + publ_month):
                    os.makedirs('volzhskaya_pravda/mystem-xml/' + publ_year + '/' + publ_month)
                os.system('mystem.exe ' + str(i)+'.txt ' + 'volzhskaya_pravda/mystem-plain/'+publ_year+'/'+publ_month+'/'+str(i)+'.txt ' + '-n -d -i --generate-all')
                os.system('mystem.exe ' + str(i)+'.txt ' + 'volzhskaya_pravda/mystem-xml/'+publ_year+'/'+publ_month+'/'+str(i)+'.xml ' + '-n -d -i --format="xml" --generate-all')
                if not os.path.exists('volzhskaya_pravda/plain/' + publ_year + '/' + publ_month + '/' + str(i) +  '.txt'):
                    if not os.path.exists('volzhskaya_pravda/plain/' + publ_year + '/' + publ_month):
                        os.makedirs('volzhskaya_pravda/plain/' + publ_year + '/' + publ_month)
                    shutil.move(str(i) + '.txt', 'volzhskaya_pravda/plain/' + publ_year + '/' + publ_month)
                else:
                    os.remove('volzhskaya_pravda/plain/' + publ_year + '/' + publ_month + '/' + str(i) +  '.txt')
                    shutil.move(str(i) + '.txt', 'volzhskaya_pravda/plain/' + publ_year + '/' + publ_month)
                add_metadata('metadata.csv', 'volzhskaya_pravda/plain/' + str(i) + '.txt', author, header, created, topic, url + str(i), publ_year)
                print('Succesfully downloaded page ' + url + str(i))
        except:
            print('Error occured on page ' + url + str(i) + ': HTTP 404 - Not Found')
    shutil.move('metadata.csv', 'volzhskaya_pravda/metadata.csv')
    
download_page('http://gazeta-vp.ru/news/item/', 1, 5078)
download_page('http://gazeta-vp.ru/news/item/', 5080, 6055)
download_page('http://gazeta-vp.ru/news/item/', 6056, 6073)
download_page('http://gazeta-vp.ru/news/item/', 6223, 13850)
## После первого тестового запуска оказалось, что некоторые страницы дают перенаправление на другую страницу, требуя логин и пароль. 
## Программа, обрабатывая их, выдает пустые файлы (не считая @au, @ti, @da, @topic, @url)
## Поскольку уже было известно, какие именно это страницы, как они себя ведут, и как выглядят, удалить их вручную мне показалось проще, чеи писать отдельный код для их обработки
## Зато это помогло придумать алгоритм, по которому программа продолжает работу при запуске после сбоя, а не обрабатывает страницы заново с самой первой
## И в принципе проработать систему с многократным запуском функции
