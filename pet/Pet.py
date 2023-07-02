class Pet:
    '''
        A class representing a pet

        Attributes
        ----------

        __name : str
            Name of the pet
        __animal_type : str
            Animal type of pet (could be 'Dog', 'Cat', 'Lion', etc)
        __age : int
            The pet's age

        Methods
        -------

        get_name
            returns a string (name of the pet)
        set_name
            sets the pet's name; receives str
        get_animal_type
            returns the pet's animal type
        set_animal_type
            sets the pet's animal type; receives str
        get_age
            returns the pet's animal type
        set_age
            sets pet's age; returns int
    '''
    def __init__(self, name:str, animal_type:str, age:int) -> None:
        
        # Coerce name and animal type to be string
        try:
            name, animal_type = str(name), str(animal_type)
        except ValueError:
            raise TypeError("Invalid types for name or animal type. Must both be strings")
        

        # Throw exception if age is not int
        if( not ( type(age) == int ) ):
            raise TypeError("Age input must be an integer")
        
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age