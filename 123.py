import random, codecs
name = input("Как тебя зовут?\n")
age = input("Сколько тебе лет?\n")
color = input("Какой твой любимый цвет?\n")
music = input("Какой твой любимый музыкальный исполнитель?\n")
dream = input("Какая у тебя мечта?\n")
with open("information.txt", "w", encoding="utf-8") as information:
    information.write(name + '\n')
    information.write(age + '\n')
    information.write(color + '\n')
    information.write(music + '\n')
    information.write(dream + '\n')
    
    
    
    
    

