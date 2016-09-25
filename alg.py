import random

# Создание пустых списков
n = 1
sex = []
skin = []
eyes = []
hair = []
weight = []
height = []
child = []
print('Первый родитель')

# Цикл вопросов для составления свойств родителей
try:
    for i in range(2):
        sex_parent = int(input('Введите пол (0 или 1): '))
        assert (sex_parent == 0 or sex_parent == 1)
        sex.append(sex_parent)
        skin_parent = int(input('Цвет кожи: '))
        assert (skin_parent == 0 or skin_parent == 1)
        skin.append(skin_parent)
        eyes_parent = int(input('Цвет глаз: '))
        assert (eyes_parent == 0 or eyes_parent == 1 or eyes_parent == 10 or eyes_parent == 11)
        eyes.append(eyes_parent)
        hair_parent = int(input('Цвет волос: '))
        assert (hair_parent == 0 or hair_parent == 1 or hair_parent == 10 or hair_parent == 11)
        hair.append(hair_parent)
        weight_parent = int(input('Вес: '))
        assert (weight_parent == 0 or weight_parent == 1 or weight_parent == 10 or weight_parent == 11)
        weight.append(weight_parent)
        height_parent = int(input('Рост: '))
        assert (height_parent == 0 or height_parent == 1 or height_parent == 10 or height_parent == 11)
        height.append(height_parent)
        if n == 1:
            print('Второй родитель')
            n += 1
        else:
            continue

# Функция генерации возможных характеристик ребенка

    def rand_child():
        sex_random = random.choice(sex)
        skin_random = random.choice(skin)
        eyes_random = random.choice(eyes)
        hair_random = random.choice(hair)
        weight_random = random.choice(weight)
        height_random = random.choice(height)
        print('Характеристики ребенка: ', sex_random, skin_random, eyes_random, hair_random, weight_random, height_random)
    rand_child()


except:
    print('Error')
