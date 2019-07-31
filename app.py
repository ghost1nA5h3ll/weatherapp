import tkinter
import configparser
import requests
import os
from PIL import Image,ImageTk


def get_api_config():
    config= configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def show_weather_image(weather):
    if 'rain' in weather:
        img = Image.open('rain.png')
        print("Regen erkannt")
    
    pic = ImageTk.PhotoImage(img)
    weather_img_label.configure(image=pic)
    weather_img_label.image = pic



def get_weather(city):
    api_key = get_api_config()
    url = "http://api.openweathermap.org/data/2.5/weather?q={},de&units=metric&APPID={}".format(city,api_key)
    req = requests.get(url)
    data = req.json()
    name = data['name']
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(name + ": " + str(temp) + " Celsius "+ desc)
    label['text'] = '{}\n{}°C\n{}'.format(name,temp,desc)
    show_weather_image(desc)

    #print(data)
    return data

HEIGHT = 600
WIDTH = 700

#Main Window
root = tkinter.Tk()
root.title("Weather App")
root.geometry(str(WIDTH) + "x" + str(HEIGHT))

image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)

bg_label = tkinter.Label(root,image=photo)

top_frame = tkinter.Frame(root,bg='#05d5ec',bd=3)
bottom_frame = tkinter.Frame(root,bg='#05d5ec',bd=5)

textfield = tkinter.Entry(top_frame)
button = tkinter.Button(top_frame, text='Get Weather',command= lambda: get_weather(textfield.get()))


label = tkinter.Label(bottom_frame,bg='white')
clear_img = ImageTk.PhotoImage(Image.open('clear.png'))
weather_img_label  = tkinter.Label(label, image=clear_img, bg = 'white')


#Adding all of my shit to root 

bg_label.place(relwidth=1,relheight=1)
top_frame.place(relx= 0.15,rely=0.1,relheight=0.05,relwidth=0.7)
bottom_frame.place(relx = 0.15,rely=0.25,relheight=0.6,relwidth=0.7)
button.place(relx=0.75,relwidth=0.25,relheight=1)
textfield.place(relx=0,relwidth=0.7,relheight=1)
label.place(relwidth=1,relheight=1)
weather_img_label.place(relx=0.3,rely=0.6,relwidth=0.4,relheight=0.4)
root.mainloop()