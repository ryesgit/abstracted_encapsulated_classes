class Car:
    '''
    A class to instantiate car objects

    ...

    Attributes
    ----------
    __year_model : str
        the year when the car was made
    __maker : str
        the car's manufacturer information
    __speed : str
        the car's speed
    
    Methods
    -------
    get_speed
        gets the car's speed
    accelerate
        adds 5 to the car's speed
    brake
        deducts 5 from the car's speed
    
    '''

    def __init__(self, year_model:int, maker:str, speed:int=0) -> None:

        '''
        Parameters
        ----------

        year_model : int
            the year the car was made
        maker : str
            the car's manufacturer
        speed : int, optional
            the car's speed (default is 0)

        '''

        # Validate input first
        if ( not( type(year_model) == int or type(speed) == int ) ):
            raise TypeError("Invalid arguments type")
        
        # Coerce maker to be a string
        try:
            maker = str(maker)
        except ValueError:
            raise TypeError("Maker input must be a string")

        self.__year_model = year_model
        self.__maker = maker
        self.__speed = speed

    def get_speed(self) -> int:
        '''
        returns the car speed
        '''
        return self.__speed