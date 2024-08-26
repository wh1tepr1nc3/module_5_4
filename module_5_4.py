class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        args = args[0]
        cls.houses_history.append(args)
        return obj

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        if isinstance(number_of_floors, int):
            self.houses_history = number_of_floors

    # def go_to(self, new_floor):
    #     if 0 < new_floor <= self.number_of_floors:
    #         for floor in range(1, new_floor + 1):
    #             print(floor)
    #     else:
    #         print('Такого этажа не существует')

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: "{self.name}", кол-во этажей: {self.number_of_floors}.'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return True

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, other):
        if isinstance(other, int) or isinstance(other, House):
            return self + other


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Домовенок', 20)
print(House.houses_history)
h3 = House('ЖК Мелиса', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)

# print(h1)
# print(h2)
#
# print(h1 == h2)  # __eq__

# h1 = h1 + 10  # __add__
# print(h1)
# print(h1 == h2)
#
# h1 += 10  # __iadd__
# print(h1)
#
# h2 = 10 + h2  # __radd__
# print(h2)
#
# print(h1 > h2)  # __gt__
# print(h1 >= h2)  # __ge__
# print(h1 < h2)  # __lt__
# print(h1 <= h2)  # __le__
# print(h1 != h2)  # __ne__
#
# # h1.go_to(5)
# # h2.go_to(9)
