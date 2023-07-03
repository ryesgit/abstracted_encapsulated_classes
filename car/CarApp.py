from PIL import Image, ImageTk
import tkinter as tk
from Car import Car
from utils.CarHelpers import accelerate_many, decelerate_many
from threading import Thread

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
        self.__delta = 0
        self.__car_x = self.__image.size[0] / 2
        self.__car_y = self.__image.size[1] / 2
        self.__canvas = tk.Canvas(master, width=(self.__image.size[0] * 5), height=(self.__image.size[1] + 20))
        self.__canvas.pack()
        self.__master.after(100, self.draw_car)
        self.__master.after(1000, self.accelerate_five)
        self.__master.after(6000, self.decelerate_five)

    def draw_car(self):
        '''
        Draws car image onto canvas
        '''
        self.__tkimage = ImageTk.PhotoImage(self.__image)

        # Increase car x coordinate by delta speed
        self.__car_x += self.__delta
        self.__canvas_image = self.__canvas.create_image( self.__car_x, self.__car_y,  image=self.__tkimage)
        self.__master.after_idle(self.move_car)
        
    def move_car(self):
        '''
        moves the car along the plane in the canvas
        '''
        self.__delta = self.__car.get_speed() * 0.1
        self.__canvas.delete(self.__canvas_image)
        self.draw_car()

    def accelerate_five(self):
        '''
        accelerates car five times
        '''

        accelerate_thread = Thread(target=accelerate_many, args=(self.__car, 5))
        accelerate_thread.start()

    def decelerate_five(self):
        '''
        decelerates car five times
        '''

        decelerate_thread = Thread(target=decelerate_many, args=(self.__car, 5))
        decelerate_thread.start()
