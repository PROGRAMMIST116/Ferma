class Farm(object):

    def __init__(self, name, hunger=0, boredom=0):
        print("Появилась новая зверушка")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def talk(self):
        print('Привет! Я '+self.name+". Я чувствую себя"+self.mood+"!")
        self.__pass_time()

    def eat(self, food):
        print("Вкусно")
        self.hunger-=food
        if self.hunger<0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print("Ура, поиграем?")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    @property
    def mood(self):
        unhappiness = self.hunger +self.boredom
        if unhappiness <5:
            m = "отлично"
        elif 5<=unhappiness<=10:
            m = "нормик"
        elif 10<unhappiness<=15:
            m = "плохо"
        else:
            m = "ужасно"
        return m


class Dog(Farm):
    def __init__(self, name, hunger=0, boredom=0):
        print("Появилась новая собачка")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Гав! Я '+self.name+". Я чувствую себя "+self.mood+"!")
        self._Farm__pass_time()

class Cat(Farm):
    def __init__(self, name, hunger=0, boredom=0):
        print("Появился новый котёнок")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Мяу! Я '+self.name+". Я чувствую себя "+self.mood+"!")
        self._Farm__pass_time()

class Hamster(Farm):
    def __init__(self, name, hunger=0, boredom=0):
        print("Появился новый хомячок")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def talk(self):
        print('Фир! Я '+self.name+". Я чувствую себя "+self.mood+"!")
        self._Farm__pass_time()

def main():
    print('=================================================\nДобро пожаловать на ферму!\nПока что тут есть только собачка, котёнок и хомячок.\nТебе надо придумать им имена!\n=================================================')
    dog = Dog(input('Введи имя собаки: '))
    cat = Cat(input('Введи имя кошки: '))
    hamster = Hamster(input('Введи имя хомяка: '))
    choice = None
    while choice != "0":
        print \
            ("""
==================================================
Выберите зверюшку для взаимодействия
==================================================
0 - Выйти
1 - Собака
2 - Кошка
3 - Хомяк
""")
        choice = input("Ваш выбор: ")
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == '1':
            choice_dog = None
            while choice_dog != '0':
                print \
                    ("""
==================================================
Вы выбрали собаку, выберите дальнейшее действие:
==================================================
0 - Назад
1 - Поговорить с животным
2 - Покормить
3 - Поиграть
""")
                choice_dog = input("Ваш выбор: ")
                if choice_dog == '0':
                    break
                elif choice_dog == '1':
                    dog.talk()
                elif choice_dog == '2':
                    print \
                    ("""
==================================================
Чем хотите покормить?
==================================================
0 - Назад
1 - плюшка(5 единиц)
2 - стейк(8 единиц)
3 - сухой корм(7 единиц)
""")
                    choice_dog_eat = input("Ваш выбор: ")
                    if choice_dog_eat == "0":
                        break
                    elif choice_dog_eat == "1":
                        dog.eat(5)
                    elif choice_dog_eat == "2":
                        dog.eat(8)
                    elif choice_dog_eat == "3":
                        dog.eat(7)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                elif choice_dog == '3':
                    print \
                    ("""
==================================================
С чем хотите поиграть?
==================================================
0 - Назад
1 - Мячик(7 единиц)
2 - Пищалка(8 единиц)
3 - Удочка(4 единицы)
""")
                    choice_dog_play = input("Ваш выбор: ")
                    if choice_dog_play == "0":
                        break
                    elif choice_dog_play == "1":
                        dog.play(7)
                    elif choice_dog_play == "2":
                        dog.play(8)
                    elif choice_dog_play == "3":
                        dog.play(7)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                else:
                    print("Извините, в меню игры нет такого пункта")
        elif choice == '2':
            choice_cat = None
            while choice_cat != '0':
                print \
                    ("""
==================================================
Вы выбрали кошку, выберите дальнейшее действие:
==================================================
0 - Назад
1 - Поговорить с животным
2 - Покормить
3 - Поиграть
""")
                choice_cat = input("Ваш выбор: ")
                if choice_cat == '0':
                    break
                elif choice_cat == '1':
                    cat.talk()
                elif choice_cat == '2':
                    print \
                    ("""
==================================================
Чем хотите покормить?
==================================================
0 - Назад
1 - Молоко(5 единиц)
2 - Рыба(8 единиц)
3 - Корм(7 единиц)
""")
                    choice_cat_eat = input("Ваш выбор: ")
                    if choice_cat_eat == "0":
                        break
                    elif choice_cat_eat == "1":
                        cat.eat(5)
                    elif choice_cat_eat == "2":
                        cat.eat(8)
                    elif choice_cat_eat == "3":
                        cat.eat(7)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                elif choice_cat == '3':
                    print \
                    ("""
==================================================
С чем хотите поиграть?
==================================================
0 - Назад
1 - Игрушечная мышка(7 единиц)
2 - Лазерная указка(8 единиц)
3 - Мячик(5 единицы)
""")
                    choice_cat_play = input("Ваш выбор: ")
                    if choice_cat_play == "0":
                        break
                    elif choice_cat_play == "1":
                        cat.play(7)
                    elif choice_cat_play == "2":
                        cat.play(8)
                    elif choice_cat_play == "3":
                        cat.play(5)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                else:
                    print("Извините, в меню игры нет такого пункта")
        elif choice == '3':
            choice_ham = None
            while choice_ham != '0':
                print \
                    ("""
==================================================
Вы выбрали хомяка, выберите дальнейшее действие:
==================================================
0 - Назад
1 - Поговорить с животным
2 - Накормить
3 - Поиграть
        """)
                choice_ham = input("Ваш выбор: ")
                if choice_ham == '0':
                    break
                elif choice_ham == '1':
                    hamster.talk()
                elif choice_ham == '2':
                    print \
                    ("""
==================================================
Чем хотите накормить?
==================================================
0 - Назад
1 - Морковь(5 единиц)
2 - Капуста(7 единиц)
3 - Корм(6 единиц)
""")
                    choice_ham_eat = input("Ваш выбор: ")
                    if choice_ham_eat == "0":
                        break
                    elif choice_ham_eat == "1":
                        hamster.eat(5)
                    elif choice_ham_eat == "2":
                        hamster.eat(8)
                    elif choice_ham_eat == "3":
                        hamster.eat(7)
                    elif choice_ham_eat == '7':
                        hamster.eat(10)
                        print('Ура, ты нашёл секретное яблоко! Твой '+hamster.name +' очень рад!')
                    else:
                        print("Извините, в меню игры нет такого пункта")
                elif choice_ham == '3':
                    print \
                    ("""
==================================================
С чем хотите поиграть?
==================================================
0 - Назад
1 - Вращающееся колесо(6 единиц)
2 - Лабиринт(8 единиц)
3 - Шар для прогулки(7 единицы)
""")
                    choice_ham_play = input("Ваш выбор: ")
                    if choice_ham_play == "0":
                        break
                    elif choice_ham_play == "1":
                        hamster.play(6)
                    elif choice_ham_play == "2":
                        hamster.play(8)
                    elif choice_ham_play == "3":
                        hamster.play(7)
                    else:
                        print("Извините, в меню игры нет такого пункта")
                else:
                    print("Извините, в меню игры нет такого пункта")
main()
input("\nEnter, чтобы выйти..")