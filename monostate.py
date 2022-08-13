class Monostate:
    _shared_state = {}
    def __init__(cls, *args, **kwargs):
        breakpoint()
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        breakpoint()
        self.name = ''
        self.money_managed = 0


    def __str__(self):
        return f'{self.name} manages ${self.money_managed}'



class CEO:
    __shared_stat = {
        'name':'Steve',
        'age':55
    }

    def __init__(self):
        self.__dict__ = self.__shared_stat


    def  __str__(self):
        return f'{self.name} is {self.age} years old'

if  __name__ == '__main__':
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    ceo2.age = 77
    print(ceo2)
    print(ceo1)

    cfo1 = CFO()
    cfo1.name = 'jack'
    cfo1.money_managed = 100
    cfo2 = CFO()
    cfo3 = CFO()

    print(cfo1)
    print(cfo2)

