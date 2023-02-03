class Animal:
    def __init__(self):
        self.eyes_count = 2

    def breathe(self):
        print("Inhale, exhale")


# Fish inherits Animal -> Fish(Animal)
class Fish(Animal):
    def __init__(self):
        # inheriting constructor initialization
        super().__init__()

    def breathe(self):
        # super().method does everything that the method from the super does
        super().breathe()

        print("doing it underwater though")

    def swim(self):
        print("moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.eyes_count)
