import random
#todo программа выберайт случайное слов из списка создаёт из выбранного слово новое слово с перемешеными буквами!
attempts= 3 #попытки
is_game = True #Игра верна
words = ["Яблоня","Деревня","Осминог"] #Список слов
# 1 блок
word = random.choice(words) #переменная выберающая слово
t_word = list(word)# преобразовывания в список
random_word = [] # пустой список
#цикл for
for i in word:
 random_word.append(random.choice(word))#Добавление в список из переменной word
