class Bird:

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the bird can fly but some cannot.")


class sparrow(Bird):

    def flight(self):
        print("Sparrow can fly.")


class ostritch(Bird):

    def flight(self):
        print("Ostrichs cannot fly.")


obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostritch()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
