import pytest
from Car import Car

def test_can_instantiate_car():
    car_one = Car(2003, 'Honda')
    assert type(car_one) == Car