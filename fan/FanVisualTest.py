from FanApp import FanApp
from Fan import Fan
import tkinter

from FanTest import first_fan, second_fan

root = tkinter.Toplevel()
root2 = tkinter.Toplevel()

first_fan_app = FanApp(first_fan, root, image_path='./fan/assets/fan.png')
second_fan_app = FanApp(second_fan, root2, image_path='./fan/assets/fan.png')

root2.mainloop()
root.mainloop()