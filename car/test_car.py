import pytest
from Car import Car

car_one = Car(2003, 'Honda')

def test_can_instantiate_car():
    assert type(car_one) == Car

def test_can_get_speed():
    assert car_one.get_speed() == 0