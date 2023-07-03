from CarApp import CarApp
from Car import Car
import tkinter as tk

car = Car(2003, 'Honda', 10)
root = tk.Tk()


# Credits to Vector Stall for the race car icon!
# https://www.flaticon.com/authors/vector-stall

car_app = CarApp(car, root, './car/assets/race-car.png')

root.mainloop()