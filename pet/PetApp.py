import tkinter as tk
from Pet import Pet
from PIL import Image, ImageTk
from tkinter import messagebox
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
        '''
        Parameters
        ----------
        master : tk.Tk
            widget instance from tkinter
        pet : Pet
            the pet instance
        image_path : str
            the path for the pet's image
        '''
        self.__master = master
        self.__pet = pet
        image = Image.open(image_path)
        self.__image = image
        self.__canvas = tk.Canvas(master, width=image.size[0] + 100, height=image.size[1] + 100 )
        self.__canvas.pack()
        self.__master.after(100, self.draw_pet)
        self.__master.after(1000, self.display_dialogue)


    def draw_pet(self) -> None:
        '''
        draws the pet onto the canvas
        '''
        self.__tkimage = ImageTk.PhotoImage(self.__image)
        self.__canvas_image = self.__canvas.create_image(self.__canvas.winfo_width() / 2, self.__canvas.winfo_height() / 2, image=self.__tkimage)

    def display_dialogue(self):
        '''
        pops up a dialogue of pet's info
        '''
        pet = self.__pet
        dialogue = f"Hello! My name is {pet.get_name()}, I am a {pet.get_animal_type()}, and I am {pet.get_age()} years old!"
        messagebox.showinfo("Pet Info!", dialogue)
        