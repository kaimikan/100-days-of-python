# unlimited arguments method
# args is the usual name developers use, but it can be changed however you want
def add(*args):
    summary = 0
    for n in args:
        summary += n
    return summary


# in this case args will be a tuple
print(add(1, 2, 3, 4, 5, 65, 4, 7, 7))


# unlimited keyword arguments method
# kwargs is also just the usual name developers use
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n


print(calculate(5, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"]
        # self.model = kw["model"]

        # using .get() lets us avoid the program from crashing if the optional argument hasn't been defined
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
# my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)


def all_aboard(a, *args, **kw):
    print(a, args, kw)


# notice how *args is a tuple and **kw is a dictionary
all_aboard(4, 7, 3, 0, x=10, y=64)
