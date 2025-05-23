
# In Python, functions are first-class objects. This means:


# You can assign them to variables
def greet():
    print("Hello")

my_greet = greet
# my_greet()


# You can pass them to other functions
def say_hello():
    print("Hello1")

def new_function(function):
    function()
# new_function(say_hello)

# You can return them from functions
def outer_function():
    print("Outer function")
    def inner_function():
        print("Inner function")
    return inner_function

# return_function = outer_function()
# return_function()

# Decorator
def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hi():
    print("Hello2")

# say_hi = my_decorator(say_hi)
say_hi()