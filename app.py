import tkinter
import request
import os
from PIL import Image,ImageTk


HEIGHT = 600
WIDTH = 700

#Main Window
root = tkinter.Tk()
root.geometry(str(WIDTH) + "x" + str(HEIGHT))

image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)

bg_label = tkinter.Label(root,image=photo)

top_frame = tkinter.Frame(root,bg='#05d5ec',bd=3)
bottom_frame = tkinter.Frame(root,bg='#05d5ec',bd=5)

button = tkinter.Button(top_frame, text='Get Weather')
textfield = tkinter.Entry(top_frame)

label = tkinter.Label(bottom_frame)



#Adding all of my shit to root 

bg_label.place(relwidth=1,relheight=1)
top_frame.place(relx= 0.15,rely=0.1,relheight=0.05,relwidth=0.7)
bottom_frame.place(relx = 0.15,rely=0.25,relheight=0.6,relwidth=0.7)
button.place(relx=0.75,relwidth=0.25,relheight=1)
textfield.place(relx=0,relwidth=0.7,relheight=1)
label.place(relwidth=1,relheight=1)
root.mainloop()