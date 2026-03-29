#1
import math


class Facade:
    pass

#2
facade_1 = Facade()

#3
facade_1_type = type(facade_1)
print(facade_1_type)

#4
class Grade:
    title = '65'
minimum_passing = Grade()
print(minimum_passing.title)

#5
class Rulse:
    def washing_brush(self):
        return 'Point bristles towards the basin while washing your brushes'

#6
class Circle:
    pi = 3.14

    def area(self, radius):
        return self.pi * radius ** 2

circle = Circle()
print(circle.area(10))

#7
class Circle:

    def __init__(self, diametre):
        print(f'New circle with diametre: {diametre}')

teaching_table = Circle(36)

#8
class Circle:
    pi = 3.14

    def __init__(self, diametre):
        self.radius = diametre

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print('medium_pizza circumference =', medium_pizza.circumference())
print('teaching_table circumference =', teaching_table.circumference())
print('round_room circumference =', round_room.circumference())

#9
number = 5
print(dir(number))

def this_function_is_an_object():
    print(dir(this_function_is_an_object))

#10
class Circle:
    pi = 3.14

    def __init__(self, diametre):
        self.radius = diametre

    def area(self, radius):
        return self.pi * radius ** 2

    def circumference(self):
        return 2 * self.pi * self.radius

    def __repr__(self):
        return f'Circle with diametre: {self.radius}'

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())