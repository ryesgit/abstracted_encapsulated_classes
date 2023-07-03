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