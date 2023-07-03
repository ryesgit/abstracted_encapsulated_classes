'''
Utilizes the Car class

Instantiates a car object
- Accelerates car 5 times
    - Display speed for each acceleration
- Decelerates (brakes) car 5 times
    - Display speed for each acceleration
'''

from Car import Car
from time import sleep
from utils.CarHelpers import accelerate_many, decelerate_many

car = Car(2003, 'Ford')

# Display initial car speed
print(f"\nInitial speed: {car.get_speed()}")

print('\nCar accelerates 5 times...\n')
accelerate_many(car, 5)

print('\nCar brakes 5 times...\n')
decelerate_many(car, 5)