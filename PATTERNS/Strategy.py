from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Executing strategy A"
    

class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Executing strategy B"



class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy
    
    def execute_strategy(self):
        return self._strategy.execute()

'''В этом примере у нас есть абстрактный класс Strategy, который определяет метод execute. Классы ConcreteStrategyA и ConcreteStrategyB являются конкретными реализациями стратегий и реализуют метод execute соответственно.'''

'''Класс Context представляет контекст, в котором используется стратегия. Он имеет методы set_strategy для изменения текущей стратегии и execute_strategy для выполнения текущей стратегии.'''


strategy_a = ConcreteStrategyA()
context = Context(strategy_a)
result_a = context.execute_strategy()
print(result_a)

strategy_b = ConcreteStrategyB()
context.set_strategy(strategy_b)
result_b = context.execute_strategy()
print(result_b)


'''В этом примере мы создаем экземпляры ConcreteStrategyA и ConcreteStrategyB. Затем мы создаем объект Context с исходной стратегией strategy_a. Затем мы вызываем execute_strategy для контекста, что приводит к выполнению стратегии strategy_a.'''

'''Затем мы изменяем стратегию контекста на strategy_b с помощью метода set_strategy и снова вызываем execute_strategy, что приводит к выполнению стратегии strategy_b.'''

'''Паттерн "Стратегия" позволяет выбирать алгоритм во время выполнения программы, обеспечивая гибкость и легкость замены алгоритма. Это полезно, когда у нас есть несколько вариантов алгоритма, и нам нужно выбрать один из них в зависимости от контекста или требований приложения.'''
