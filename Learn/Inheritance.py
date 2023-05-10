# https://www.geeksforgeeks.org/python-oops-concepts/

class Person(object):

    # konstruktor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("Id Number: {}".format(self.idnumber))


class Employee(Person):

    # Konstruktor
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        Person.__init__(self, name, idnumber)

    def details(self):
        print("My name is {}".format(self.name))
        print("IdNumber: {}".format(self.idnumber))
        print("Post: {}".format(self.post))


a = Employee('Angga', 11017130, 8000000, "Intern")

a.display()
a.details()
