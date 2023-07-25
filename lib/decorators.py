def decorator(func):
    def wrapper():
        print("I am the output thats let you know the function is about to be called ")
        func()
        print("I am the output that lets you know the function has been called.")
    return wrapper

@decorator
def get_called():
    print("I am the function and I am being called")

# get_called = decorator(get_called) this is the same as the above function
get_called()

# without decorators - here there is repetition of the checking time

def sweep_floors(time):
    if 1100 < time < 2100:
        print("Sweeping the floors...")
    else:
        print("I'm off duty!")

def wash_dishes(time):
    if 1100 < time < 2100:
        print("Washing the dishes...")
    else:
        print("I'm off duty!")

def chop_vegetables(time):
    if 1100 < time < 2100:
        print("Chopping the vegetables...")
    else:
        print("I'm off duty!")

# with decorator

def check_time(func):
    def wrapper(time):
        if 1100 < time < 2100:
            func(time)
        else:
            func(time)
    return wrapper

@check_time
def sweep_floors(time):
    print("Sweeping the floors...")

@check_time
def wash_dishes(time):
    print("Washing the dishes...")

@check_time
def chop_vegetables(time):
    print("Chopping the vegetables...")



