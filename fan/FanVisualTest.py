from FanApp import FanApp
from Fan import Fan
import tkinter

root = tkinter.Tk()

fan = Fan(True)
fan_app = FanApp(fan, root, image_path='./fan/assets/fan.png')
fan_app.draw_image()
root.mainloop()