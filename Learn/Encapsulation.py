class Base:
    def __init__(self):
        self.a = "Angga"
        self.__c = "Prakasa"


class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Private base class: ")
        print(self.__c)


obj1 = Base()
print(obj1.a)