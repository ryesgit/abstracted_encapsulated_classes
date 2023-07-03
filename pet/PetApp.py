import tkinter as tk
from Pet import Pet
from PIL import Image, ImageTk

class PetApp:
    '''
    GUI for Pet instances

    Attributes
    ----------
    pet : Pet
        the pet instance
    image_path : str
        the image path for the pet's image
    master : tk.Tk
        the widget instance from Tkinter

    Methods
    -------
    draw_pet()
        draws the pet's image
    display_dialogue()
        display's the pet's speech

    '''

    def __init__(self, master: tk.Tk, pet: Pet, image_path: str) -> None:
        self.__master = master
        self.__pet = pet
        image = Image.open(image_path)
        self.__image = image
        self.__canvas = tk.Canvas(master, width=image.size[0] + 100, height=image.size[1] + 100 )
        self.__canvas.pack()