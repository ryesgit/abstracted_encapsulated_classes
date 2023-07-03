# Abstracted & Encapsulated Classes

## Terminologies

**Abstraction** is a concept in Object-Oriented Programming. Imagine a toaster; you put in slices of bread in it, you wait a while for the bread to toast, and you pick it up to consume afterwards. This is analogous to the concept of abstraction. Users should be able to input in the method of a class without worrying much about the process taking place. All they need to know is what the method does, and what the method outputs.

**Encapsulation** is another OOP concept. Say you want the users to access the class' private properties, but you don't want them to access them ***directly***. Encapsulation saves the day! Encapsulation takes advantage of the nature of scoping in programming, amd allows for private properties inside the class to be indirectly accessed by outside parties.

## Three Abstracted & Encapsulated Programs

This repository consists of three programs showcasing abstraction and encapsulation:

- Car Program
- Fan Program
- Pet Program

To test them out, here are the instructions:

### Clone This Repository
```
git clone https://github.com/ryesgit/abstracted_encapsulated_classes
```

> :bulb: ***Tip:*** All commands should take place while in `abstracted_encapsulated_classes/` directory

### Install Dependencies
```
pip install -r requirements.txt
```


### Car Program

For CLI Testing:
```
python car/CarTestDrive.py
```

For visual testing:
```
python car/CarVisualTest.py
```

### Fan Program

For CLI Testing:
```
python fan/FanTest.py
```

For visual testing:
```
python fan/FanVisualTest.py
```

### Pet Program

For CLI Testing:
```
python pet/PetPlayground.py
```

For visual testing:
```
python car/pet_visual_playground.py
```