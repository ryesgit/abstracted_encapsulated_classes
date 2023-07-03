from FanApp import FanApp
from Fan import Fan
import tkinter

root = tkinter.Toplevel()
root2 = tkinter.Toplevel()

fan = Fan(True, 3)
fan_app = FanApp(fan, root, image_path='./fan/assets/fan.png')

closed_fan = Fan(False, 1)
closed_fan_app = FanApp(closed_fan, root2, image_path='./fan/assets/fan.png')

root2.mainloop()
root.mainloop()