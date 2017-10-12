my_name = input('Name: ')
my_age = int(input('Age: '))
my_height = int(input('Height (inches): '))
my_weight = int(input('Weight (pounds): '))
my_eyes = input('Eye Colour: ')
my_hair = input('Hair Colour: ')
is_heavy = my_weight > 3000

print(f"Let's talk about {my_name}.")
print(f"He is {my_height} inches tall.")
print(f"He is {my_weight} pounds heavy.")
print(f"Is is {is_heavy} that he is overweight.")
print(f"He has {my_eyes} eyes and {my_hair} hair.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}")
