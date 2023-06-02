from abc import ABC, abstractmethod


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Result of operation A from ConcreteProductA1"
    

class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Result of operation A from ConcreteProductA2"
   


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Result of operation B from ConcreteProductB1"
    

class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Result of operation B from ConcreteProductB2"



class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


'''В этом примере у нас есть два семейства продуктов: AbstractProductA и AbstractProductB, каждый из которых имеет несколько конкретных реализаций (ConcreteProductA1, ConcreteProductA2, ConcreteProductB1, ConcreteProductB2).'''

'''Абстрактная фабрика AbstractFactory определяет абстрактные методы create_product_a и create_product_b, которые должны быть реализованы в конкретных фабриках (ConcreteFactory1 и ConcreteFactory2). Каждая конкретная фабрика создает свою собственную версию AbstractProductA и AbstractProductB.'''


factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()

print(product_a1.operation_a())
print(product_b1.operation_b())


factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()

print(product_a2.operation_a())
print(product_b2.operation_b())


'''В этом примере мы создаем экземпляры конкретных фабрик (ConcreteFactory1 и ConcreteFactory2). Затем мы используем методы create_product_a и create_product_b для создания соответствующих продуктов (AbstractProductA и AbstractProductB). Затем мы вызываем операции (operation_a и operation_b) для каждого продукта.'''

'''Паттерн "Абстрактная фабрика" позволяет создавать семейства взаимосвязанных объектов без привязки к конкретным классам. Это позволяет легко заменять семейства продуктов в приложении, поддерживая при этом согласованность между продуктами.'''