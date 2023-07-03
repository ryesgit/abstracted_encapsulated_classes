import tkinter as tk
from Pet import Pet
from PIL import Image, ImageTk

class PetApp:
    '''
    GUI for Pet instances

    Attributes
    ----------
    master : tk.Tk
        the widget instance from Tkinter
    pet : Pet
        the pet instance
    image_path : str
        the image path for the pet's image

    Methods
    -------
    draw_pet()
        draws the pet's image
    display_dialogue()
        display's the pet's speech

    '''

    def __init__(self, master: tk.Tk, pet: Pet) -> None:
        self.__pet = pet
        self.__master = master
        self.__canvas = tk.Canvas(master, width=500, height=500)
        self.__canvas.pack()