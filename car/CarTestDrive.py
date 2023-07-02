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

car = Car(2003, 'Ford')

def accelerate_many(car:Car, times:int):
    '''
    Accelerates a car instance n times

    Parameters
    ----------
    car : Car
        the car instance to be accelerated
    times : int
        the number of times the car instance must be
        accelerated

    '''

    for time in range(times):
        car.accelerate()
        print(f"Acceleration #{time + 1} speed: {car.get_speed()}")
        sleep(1)

def decelerate_many(car:Car, times:int):
    '''
    Decelerates a car instance n times

    Parameters
    ----------
    car : Car
        the car instance to be accelerated
    times : int
        the number of times the car instance must be
        decelerated

    '''

    for time in range(times):
        car.brake()
        print(f"Brake #{time + 1} speed: {car.get_speed()}")
        sleep(1)

# Display initial car speed
print(f"\nInitial speed: {car.get_speed()}")

print('\nCar accelerates 5 times...\n')
accelerate_many(car, 5)

print('\nCar brakes 5 times...\n')
decelerate_many(car, 5)