from Pet import Pet

pet = Pet("Kitty", "Cat", 4)

def test_can_instantiate_cat():
    assert type(pet) == Pet

def test_can_get_and_set_name():
    pet.set_name("Galore")
    assert pet.get_name() == "Galore"