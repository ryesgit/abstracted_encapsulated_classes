from PetApp import PetApp
from Pet import Pet
import tkinter as tk
pet = Pet('Rudolf', 'Cat', 4)

root = tk.Tk()

# Credits to Flat Icons for the cat icon
# https://www.flaticon.com/authors/flat-icons

pet_app = PetApp(root, pet, './pet/assets/cat.png')

root.mainloop()