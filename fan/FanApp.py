from PIL import Image, ImageTk
import tkinter as tk
from Fan import Fan

class FanApp:
    '''
    Attributes
    ----------
    fan : Fan
        The fan instance from the Fan Class
    master : Tk
        The tk widget; main window of the app
    canvas : Tk.Canvas
        The application's canvas (dimensions are 500 x 500)

    Methods
    -------
    draw_image
        draw image onto canvas
    rotate_image
        rotate image inside canvas
    '''
    def __init__(self, fan:Fan, master: tk.Tk) -> None:
        '''
        Parameters
        ----------
        fan: Fan
            A fan instance
        master: tk.Tk
            an instance of Tkinter widget
        '''

        self.__fan = fan
        self.__master = master
        self.__canvas = tk.Canvas(master, width=500, height=500)