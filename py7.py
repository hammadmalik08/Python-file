print("hy")
                # definition of function in python
def greet():
    print("my fav course")

#                 #  function call
    greet()


def greet(name):
    print("hello", name)

    greet(name)




def add(a, b):
    return a + b




def greet(name="Guest"):
    print("hello,", name)

greet()
greet("Hammad")    





def person(name, age):
    print(name, "is", age, "years old.")

person(age=20, name="Hammad")


def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30, 40))