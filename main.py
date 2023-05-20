# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
#
# *Пример:*
#
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам

from numpy import unique

def allTheSame(elem):
    return len(unique(elem)) <= 1

def izPoemRheme (list):
    tempInt = 0
    tempList = []
    letterList = ('А','Е','И','О','У','Ы','Э','Ю','Я')
    for word in list:
        for char in word:
            if char.upper() in letterList:
                tempInt += 1
        tempList.append(tempInt)
        tempInt = 0
    if allTheSame(tempList):
        print("Парам пам-пам")
    else:
        print("Пам парам")


poem = input("Напишите фразу(Фраза может состоять из одного слова,если во фразе несколько слов,"
             " то они разделяются дефисами. Фразы отделяются друг от друга пробелами.:")

lst = poem.split()
izPoemRheme(lst)