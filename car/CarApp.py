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
        flip_img = image.transpose(Image.FLIP_LEFT_RIGHT)

        self.__image = flip_img
        self.__canvas = tk.Canvas(master, width=(self.__image.size[0] * 5), height=(self.__image.size[1] + 20))
        self.__canvas.pack()
        self.__master.after(100, self.draw_car)

    def draw_car(self):
        '''
        Draws car image onto canvas
        '''
        self.__tkimage = ImageTk.PhotoImage(self.__image)
        self.__canvas_image = self.__canvas.create_image(self.__image.size[0] / 2, self.__image.size[1] / 2,  image=self.__tkimage)
        