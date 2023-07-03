from PIL import Image, ImageTk
import tkinter as tk
from Car import Car

class CarApp:
    '''
    Attributes
    ----------
    car : Car
        the car instance
    master : tk.Tk
        the widget instance for tkinter
    image_path : str
        the car image
    
    Methods
    -------
    draw_car()
        draws the car onto the canvas
    move_car()
        moves car along plane
        according to speed
    '''
    def __init__(self, car: Car, master: tk.Tk, image_path: str) -> None:
        '''
        Parameters
        ----------
        car : Car
            the car instance
        master : tk.Tk
            the Tkinter widget instance
        image_path : str
            the path of the car image
        '''

        self.__car = car
        self.__master = master
        image = Image.open(image_path)
        self.__image = image
        self.__canvas = tk.Canvas(master, width=(self.__image.size[0] * 5), height=(self.__image.size[1] + 20))
        self.__canvas.pack()