import math
from turtle import color
from math import pi,sqrt
class Figure: #фигура
    sides_count = 0 # кол-во сторон

    def __init__(self,color,*sides):
         self._sides = sides # список сторон инициализируем
         self._color = color # список цветов
         self.filled = False # флаг, указывает закрашена или нет фигура

        # Проверка на кол-во сторон
         if len(sides) == self.sides_count:
             self.set_sides(*sides)
         else:
             self._sides = [1] * self.sides_count #заполнение еденицами если кол-во сторон не совпадвает

    def get_color(self):
        return self._color # вернет список цветов

    def __len__(self):
        return sum(self._sides)# возвращает периметр фигуры

    def get_sides(self):
        return self._sides# возвращает список сторон

    def __is_valid_color(self,r,g,b):
        # принимает параметры r,g,b проверяет корректность пкркданных значений
        # перед установкой нового цвета - корректность - это целые числа от 0 до 255 включительно
         if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
              return r,g,b
            else:
                return self._color # цвет не корректный

    def set_color(self,r,g,b):
        # принимает параметры r,g,b проверяет на коректность и меняет атрибут color
        # на другой если введены коректные данные, если нет цвет остаётся прежний
        new_color = self.__is_valid_color(r,g,b)
        self._color = list(new_color)
        return self._color

    def __is_valid_sides(self,*new_sides):
        # принимает неграниченое кол-во сторон возвращает True если все стороны целые
        # положительные числа ,и совподает с текущим кол-вом сторон иначе False
       for i in new_sides:
            if i > 0 and len(new_sides) == self.sides_count:
                    return True
            else:
               return False

    def set_sides(self,*new_sides):# принимает новые  стороны  и если их кол-во не равно==0
        # то не изменять, иначе менять
        if self.__is_valid_sides(*new_sides):
           self._sides = list(new_sides)

class Circle (Figure):
    sides_count = 1

    def __init__(self,color,circumferense):
        super().__init__(color,circumferense)
        self._radius = circumferense/(2 * pi)

    def get_square(self):
        x = (self._radius ** 2)* pi
        return x

class Cube(Figure):
    sides_count = 12
    
    def __init__(self,color,*sides):
        super().__init__(color,*sides)
        self._sides = [sides[0]] * self.sides_count
        print(self._sides)

    def get_volume(self):
        v = self._sides[0] ** 3
        return v


class Triangle(Figure):
    sides_count = 3

    def __init__(self,color,*sides):
        super().__init__(color,*sides)

    def get_square(self):
        a,b,c = self._sides
        p = (a+b+c)/2
        return math.sqrt(p *(p-a)*(p-b)*(p-c))


circle1 = Circle((200,200,100),10)# цвет стороны
cube1 = Cube((222,35,130),6)

# Проверка на изменение цвета
circle1.set_color(55,66,77)# Измениться
print(cube1.get_color())
cube1.set_color(77,500,15)# Не измениться
print(cube1.get_color())

  #Проверка на изменение сторон
cube1.set_sides(5,3,12,4,5)# Не измениться
print(cube1.get_sides())
circle1.set_sides(15) # Измениться
print(circle1.get_sides())

 # Проверка периметра (круга), это и есть длинна
print(len(circle1))

 # проверка обьёма (куба)
print(cube1.get_volume())

 # площадь
print(circle1.get_square())





