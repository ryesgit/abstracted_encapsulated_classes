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

    def __init__(self, power: bool, speed: int, radius: float, color: str) -> None:
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