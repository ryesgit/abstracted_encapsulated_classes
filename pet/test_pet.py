from Pet import Pet

pet = Pet("Kitty", "Cat", 4)

def test_can_instantiate_cat():
    assert type(pet) == Pet