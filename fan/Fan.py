class Fan:
    '''
    A class to represent an electric fan

    ...

    Attributes
    ----------
    __speed : str
        the electric fan's speed
    __power : bool
        specifies whether fan is on or off
    __radius : float
        the electric fan's radius
    __color: str
        the electric fan's color
    
    Methods
    -------
    get_speed
        gets the electric fan's speed
    set_speed
        sets the electric fan's speed
    get_power
        gets the electric fan's power state
    set_power
        sets the electric fan's power state
    get_radius
        gets the electric fan's radius
    set_radius
        sets the electric fan's radius
    get_color
        gets the electric fan's color
    set_color
        sets the electric fan's color
    
    '''

    __SLOW = 1
    __MEDIUM = 2
    __FAST = 3

    def __init__(self, power: bool=False, speed: int=__SLOW, radius: float=5.0, color: str='blue') -> None:
        '''
        Parameters
        ----------
        power : bool, optional
            specifies whether fan is on or off (default is False)
        speed : int, optional
            the electric fan's speed (default is __SLOW = 1)
        radius : float, optional
            the electric fan's radius (default is 5.0)
        color : str, optional
            the electric fan's color (default is blue)
         '''
        self.__power = power
        self.__speed = speed
        self.__radius = radius
        self.__color = color

    def get_power(self) -> bool:
        '''
        Gets the electric fan's power state
        '''
        return self.__power
    
    def set_power(self, power: bool) -> None:

        '''
        Sets the electric fan's power state
        '''

        # Check if power is boolean. If not, change nothing.
        if (not(type(power) == bool)):
            raise TypeError("Power input should be a boolean (True/False)")
        
        self.__power = power

    def get_speed(self) -> int:
        '''
        Gets the electric fan's speed
        '''

        return self.__speed
    
    def set_speed(self, speed:int) -> None:
        '''
        Sets the electric fan's power state
        '''

        # Check if speed is an integer. If not, change nothing.
        if(not(type(speed) == int)):
            raise TypeError("Speed input should be an integer")
        
        # Restrict speed integer input (1 - 3 only)
        if(not( 1 <= speed <= 3 )):
            raise ValueError("Speed input must be only from 1 to 3")
        
        self.__speed = speed

    def get_radius(self) -> float:
        '''
        Gets the fan's radius
        '''

        return self.__radius
    
    def set_radius(self, radius:float) -> None:
        '''
        Sets the fan's radius
        '''

        # Try to convert input to float
        try:
            radius = float(radius)

        except ValueError:
            raise TypeError("Radius input must be a floating point number")
        
        self.__radius = radius

    def get_color(self) -> str:
        '''
        Gets the fan's color
        '''

        return self.__color
    
    def set_color(self, color:str) -> None:
        '''
        Sets the fan's color
        '''

        # Try to convert input to string
        try:
            color = str(color)

        except ValueError:
            raise TypeError("Color input must be a string")
        
        self.__color = color