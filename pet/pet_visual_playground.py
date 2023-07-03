from PetApp import PetApp
from Pet import Pet
import tkinter as tk
pet = Pet('Rudolf', 'Cat', 4)

root = tk.Tk()

pet_app = PetApp(root, pet, './pet/assets/cat.png')

root.mainloop()