import pytest
from Fan import Fan

first_fan = Fan(False, 2, 5, 'Red')

def test_power__throws_error():
    with pytest.raises(TypeError):
        first_fan.set_power('Cthulu')

def test_speed_throws_value_error():
    with pytest.raises(ValueError):
        first_fan.set_speed(1000)

def test_speed_throws_type_error():
    with pytest.raises(TypeError):
        first_fan.set_speed('Cthulu')

def test_can_set_speed():
    first_fan.set_speed(3)
    assert first_fan.get_speed() == 3

def test_can_set_radius():
    first_fan.set_radius(50)
    assert first_fan.get_radius() == 50

def test_radius_throws_error():
    with pytest.raises(TypeError):
        first_fan.set_radius('Cthulu')

def test_can_set_color():
    first_fan.set_color('Green')
    assert first_fan.get_color() == 'Green'