class Dog:
    # Attribute
    atribut1 = "mamalia"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))


Rodger = Dog("Dodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Rodger.__class__.atribut1))
print("Rodger is a {}".format(Tommy.__class__.atribut1))

Rodger.speak()
Tommy.speak()
