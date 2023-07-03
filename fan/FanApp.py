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
    def __init__(self, fan:Fan, master: tk.Tk, image_path: str) -> None:
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
        image = Image.open(image_path)
        self.__image = image
        self.__canvas = tk.Canvas(self.__master, width=self.__image.size[0] + 20, height=self.__image.size[1] + 20)
        self.__canvas.pack()

    def draw_image(self):
        self.__tkimage = ImageTk.PhotoImage(self.__image)
        canvas_image = self.__canvas.create_image(250, 250, image=self.__tkimage)
        self.__canvas_image = canvas_image