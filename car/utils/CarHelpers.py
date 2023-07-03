from Car import Car
from time import sleep

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