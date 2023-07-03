from CarApp import CarApp
from Car import Car
import tkinter as tk
from utils.CarHelpers import accelerate_many, decelerate_many
car = Car(2003, 'Honda')
root = tk.Tk()


# Credits to Vector Stall for the race car icon!
# https://www.flaticon.com/authors/vector-stall

car_app = CarApp(car, root, './car/assets/race-car.png')

for time in range(5):
    car.accelerate()

root.mainloop()