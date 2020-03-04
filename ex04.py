my_name = 'Random Name'
my_age = 25  # age
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

height_cm = my_height * 2.54 / 1
print(f"The height in cm is {height_cm}.")  # weight in kg

weight_kg = round(my_weight / 2.2046)  # rounded
print(f"The weight in kg is {weight_kg}.")

print(f"Hey let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} i get {total}.")
