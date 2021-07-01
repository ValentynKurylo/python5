'''
1)
создать два класса Prince и Cinderella:
у золушки должно быть имя возраст и размер ноги
у принца имя, возраст и размер найденой туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую

2) максимально в этих двух классах проанотировать типы

3) у класса золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
'''

class Prince:
    def __init__(self, name:str, age:int, size:int):
        self.name = name
        self.age = age
        self.size = size

    def found(self, list:list):
        for i in list:
            if self.size == i.size:
                print(i.name, i.age, i.size)



class Cinderella:
    count: int = 0
    def __init__(self, name:str, age:int, size:int):
        self.name = name
        self.age = age
        self.size = size
        Cinderella.count += 1




Ivan = Prince('Ivan', 20, 38)
Vika = Cinderella('Vika', 18, 38)
Olga = Cinderella('Olga', 24, 40)
Olena = Cinderella('Olena', 20, 37)

Ivan.found([Vika, Olga])
print(Olena.count)

