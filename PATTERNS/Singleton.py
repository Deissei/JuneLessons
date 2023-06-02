class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

'''В этом примере класс Singleton имеет приватное статическое поле _instance, которое хранит единственный экземпляр класса. При создании нового объекта класса Singleton, проверяется, существует ли уже экземпляр класса. Если экземпляр уже существует, возвращается ссылка на него. Если экземпляр еще не создан, создается новый экземпляр и сохраняется в поле _instance, а затем возвращается ссылка на него.'''

s1 = Singleton()
s2 = Singleton()

print(s1 is s2) # True

'''В этом примере s1 и s2 являются двумя переменными, которые ссылаются на один и тот же объект Singleton. В результате сравнения s1 is s2 получается значение True, что означает, что оба объекта ссылаются на один и тот же экземпляр класса Singleton.'''

'''Таким образом, паттерн "Одиночка" позволяет гарантировать, что класс имеет только один экземпляр, и предоставляет глобальную точку доступа к этому экземпляру. Это может быть полезно, например, когда требуется использовать общие ресурсы или настройки во всем приложении.'''