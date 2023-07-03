from FanApp import FanApp
from Fan import Fan
import tkinter

root = tkinter.Tk()

fan = Fan(True, 3)
fan_app = FanApp(fan, root, image_path='./fan/assets/fan.png')

root.mainloop()