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