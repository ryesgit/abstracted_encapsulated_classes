import pytest
from Car import Car

car_one = Car(2003, 'Honda')
DELTA = 5

def test_can_instantiate_car():
    assert type(car_one) == Car

def test_can_get_speed():
    assert car_one.get_speed() == 0

def test_can_accelerate():
    init_speed = car_one.get_speed()
    car_one.accelerate()
    assert car_one.get_speed() == init_speed + DELTA

def test_can_brake():
    init_speed = car_one.get_speed()
    car_one.brake()
    assert car_one.get_speed() == init_speed - DELTA