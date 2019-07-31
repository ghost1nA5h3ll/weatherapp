#Importing our needed modules
import tkinter #for GUI
import configparser #for reading the config.ini file
import requests #for api http request
from PIL import Image,ImageTk #for image conversion

#read the config.ini file and return the api key which is stored in there
#ToDo: Decode Base64 String in here
def get_api_config():
    config= configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

#change image of weather_img_label to current weather condition (visual weather status)
def show_weather_image(weather):
    if 'rain' in weather:
        img = Image.open('rain.png')
    elif 'sun' in weather:
        img = Image.open('sun.png')
    elif 'few clouds' in weather:
        img = Image.open('covered.png')
    elif 'clear sky' in weather:
        img = Image.open('sun.png')
    elif 'thunder' in weather:
        img = Image.open('thunder.png')
    else:
        img = Image.open('clear.png')
        
    pic = ImageTk.PhotoImage(img)
    weather_img_label.configure(image=pic)
    weather_img_label.image = pic


#sends the http api request and extract the needed data. 
#call the show_weather_image function
#return the data as python dictonary (converted from json)
def get_weather(city):
    api_key = get_api_config()
    url = "http://api.openweathermap.org/data/2.5/weather?q={},de&units=metric&APPID={}".format(city,api_key)
    req = requests.get(url)
    data = req.json()
    try:
        name = data['name']
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        label['text'] = '{}\n{}°C\n{}'.format(name,temp,desc)
        show_weather_image(desc)
    except:
        label['text'] = "Da ist etwas schiefgelaufen!"

    #print(data)
    return data

#statup size of main window
HEIGHT = 600
WIDTH = 700

#main Window
root = tkinter.Tk()
root.title("Weather App")
root.geometry(str(WIDTH) + "x" + str(HEIGHT))

#background image into label
image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)
bg_label = tkinter.Label(root,image=photo)

#upper frame for user input
top_frame = tkinter.Frame(root,bg='#05d5ec',bd=3)

#lower frame for application output
bottom_frame = tkinter.Frame(root,bg='#05d5ec',bd=5)

#tkinter input widgets
textfield = tkinter.Entry(top_frame)
button = tkinter.Button(top_frame, text='Get Weather',command= lambda: get_weather(textfield.get()))

#tkinter output widgets
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