from Pet import Pet

# Ask user for pet details

name = input("Input pet name: ")
animal_type = input("Input pet animal type: ")
age = int(input("Input pet age: "))

def is_vowel(letter:chr):
    return True if letter.lower() in ['a', 'e', 'i', 'o', 'u'] else False

def display_pet_details(pet:Pet):
    print(f"Hello! My name is {pet.get_name()}, I am {'an' if is_vowel(pet.get_animal_type()[0]) else 'a'} {pet.get_animal_type()}.")
    print(f"I am {pet.get_age()} years old!")

pet = Pet(name, animal_type, age)
display_pet_details(pet)
