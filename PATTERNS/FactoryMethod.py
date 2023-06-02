from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"
    

class Cat(Animal):
    def speak(self):
        return "Meow!"

# ---------------------------------

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass


class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()
    

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()


'''В этом примере классы Dog и Cat представляют различные типы животных, которые могут издавать звуки. Класс Animal является абстрактным базовым классом, определяющим метод speak, который должен быть реализован в конкретных подклассах.'''

'''Классы DogFactory и CatFactory являются конкретными фабриками, которые реализуют абстрактный метод create_animal из абстрактного класса AnimalFactory. Каждая фабрика создает экземпляр соответствующего животного (собаки или кошки) и возвращает его.'''


dog_factory = DogFactory()
dog = dog_factory.create_animal()
print(dog.speak()) # Вывод: "Woof!"

cat_factory = CatFactory()
cat = cat_factory.create_animal()
print(cat.speak()) # Вывод: "Meow!"


'''В этом примере мы создаем экземпляры DogFactory и CatFactory, а затем используем метод create_animal, чтобы создать соответствующие животные (Dog и Cat). Затем мы вызываем метод speak для каждого животного, чтобы услышать соответствующий звук.'''

'''Паттерн "Фабричный метод" позволяет делегировать создание объектов подклассам, обеспечивая гибкость при создании экземпляров различных типов объектов в зависимости от ситуации. Это может быть полезно, например, когда требуется создание различных продуктов или компонентов в программе.'''