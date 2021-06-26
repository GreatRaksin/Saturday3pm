'''
ООП - объектно-ориентированное программирование

Когда вы создаете объект, вы создаете СВОЙ тип данных.

У классов есть методы. Метод - это функция, которая задает
определенное поведение и действия.

У классов есть экземпляры.
'''


class Dog:  # класс
    def __init__(self, name, age, color):
        """__init__ - устанавливает начальное
        состояние объекта, присваивая значения
        свойствам объекта в момент создания экземпляра"""
        self.dog_name = name  # описываю свойства класса, задаваемые при его создании
        self.dog_age = age
        self.dog_color = color
        '''self.__name__ - это атрибуты экземпляра, которые применимы
        только к определенному экземпляру класса'''

    # атрибут КЛАССА
    tail = True  # это атрибут, который одинаков ДЛЯ ВСЕХ экземпляров

    # метод
    def __str__(self):  # теперь экземпляр класса знает о себе следующее:
        return f'Dog {self.dog_name} is {self.dog_age} years old.'

    '''__init__, __str__ - называются dunder-методами'''

    # метод 2
    def wof(self, sound):
        return f'{self.dog_name} says: {sound}.'


miguel = Dog('Miguel', 2, 'pink')  # экземпляр класса
sally = Dog('Sally', 3, 'black')
print(miguel == sally)
print(miguel.dog_name, miguel.dog_name, miguel.tail, sally.tail)

''' Методы экземпляра - ЭТО ФУНКЦИИ. 
Они определяются внутри класса и могут быть вызваны 
только для определенного экземпляра.'''

print(sally.wof('Wof wof'))

# у списков можно вывести содержимое
names = ['Sally', 'John', 'Sam']  # здесь выведется список имен всех
print(names)
print(sally)
