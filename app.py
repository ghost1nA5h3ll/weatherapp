import tkinter
import request

HEIGHT = 600
WIDTH = 700

#Main Window
root = tkinter.Tk()

canvas = tkinter.Canvas(root,bg='white',height=HEIGHT, width=WIDTH)

top_frame = tkinter.Frame(root,bg='blue',bd=3)
bottom_frame = tkinter.Frame(root,bg='blue',bd=5)

button = tkinter.Button(top_frame, text='Get Weather')
textfield = tkinter.Entry(top_frame)

label = tkinter.Label(bottom_frame)



#Adding all of my shit to root 
canvas.pack()
top_frame.place(relx= 0.15,rely=0.1,relheight=0.05,relwidth=0.7)
bottom_frame.place(relx = 0.15,rely=0.25,relheight=0.6,relwidth=0.7)
button.place(relx=0.75,relwidth=0.25,relheight=1)
textfield.place(relx=0,relwidth=0.7,relheight=1)
label.place(relwidth=1,relheight=1)
root.mainloop()