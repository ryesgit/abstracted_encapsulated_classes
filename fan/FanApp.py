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
        self.__rotation = 0
        self.__canvas = tk.Canvas(self.__master, width=self.__image.size[0] + 20, height=self.__image.size[1] + 20, bg=self.__fan.get_color())
        self.__canvas.pack()
        self.__master.after(100, self.draw_image)

    def draw_image(self):
        '''
        draws the image onto the canvas
        '''
        self.__tkimage = ImageTk.PhotoImage(self.__image.rotate(self.__rotation))
        canvas_image = self.__canvas.create_image(250, 250, image=self.__tkimage)
        self.__canvas_image = canvas_image
        self.__master.after_idle(self.rotate_image)

    def rotate_image(self):
        '''
        rotates image to "turn on" the fan
        '''
        # Do not rotate image if fan is off
        if not self.__fan.get_power():
            print("Fan is in off state")
            return

        self.__canvas.delete(self.__canvas_image)
        self.__rotation += 10
        self.__rotation %= 360
        self.draw_image()