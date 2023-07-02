import pytest
from Fan import Fan

first_fan = Fan(False, 2, 5, 'Red')

def test_throws_error():
    with pytest.raises(TypeError):
        first_fan.set_power('Cthulu')