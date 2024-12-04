import random


random_integer = random.randint(1,6)
print("random int", random_integer)


random_float = random.random()
print("random float", random_float)

# create random floating between 0 and 5 (not inclusive)

new_random = random.random() * 5
print(new_random)