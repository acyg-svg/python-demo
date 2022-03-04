import os;
from time import sleep
import tkinter as tk
from tkinter import ttk
from PIL import Image,ImageTk
import PyQt5.QtWidgets
class VisualG(object):
    def __init__(self,master = None):
        self.root = master;
        self.create_widgets();
    def create_widgets(self):
        frame = tk.Toplevel()
        img='556454988.jpg'
        img_open = Image.open(img)
        img_png = ImageTk.PhotoImage(img_open)
        self.Image2 = tk.Label(frame,bg = 'white',bd =20,height=500,width=500,image =img_png)
        self.Image2.pack()
        frame.mainloop()
root = tk.Tk()
VisualG(root)
root.mainloop()
