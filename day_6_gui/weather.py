from tkinter import *
import requests
import json
# pip install pillow
from PIL import Image, ImageTk
from io import BytesIO

window = Tk()
window.title("Weather App")
pincode = StringVar()
location = StringVar()
temperature = StringVar()
description = StringVar()
img = None

load = Image.open("./pics/weather.png")
render = ImageTk.PhotoImage(load)

img = Label(window, image=render)
img.grid(row=0, column=0, columnspan=3)

pincode_label = Label(window, text="Pin code").grid(
    row=1, column=0, padx=10, pady=10)
pincode_text = Entry(window, textvariable=pincode).grid(
    row=1, column=1, padx=10, pady=10, sticky=W)


def submitClicked():

    pincode_l = pincode.get()
    if pincode_l != "":
        url = 'https://api.openweathermap.org/data/2.5/weather'

        params = {
            'appid': '37a81ae1e682ac417883b0a3727080a6'
        }

        params["zip"] = pincode_l+",in"
        try:
            response = requests.get(url, params=params, timeout=10)
            print(response.url)
            if response.status_code == 200:
                global img
                json = response.json()
                description.set(json["weather"][0]["description"])
                location.set(json["name"])
                temperature.set(json["main"]["temp"])
                # Now get the image
                image_url = "https://openweathermap.org/img/wn/" + \
                    json["weather"][0]["icon"]+".png"
                response_img = requests.get(image_url)
                print(response_img.status_code)
                print(response_img.url)
                image_data = response_img.content
                img = ImageTk.PhotoImage(Image.open(BytesIO(image_data)))
                icon = Label(window, image=img, bg="#C0C0C0",
                             width=35, height=35)
                icon.grid(row=4, column=2)

            else:
                print("error")
        except Exception as e:
            print("Exception occured ,", e)


submit_button = Button(window, text="Get weather", command=submitClicked).grid(
    row=1, column=2, padx=10, pady=10)

temp_label = Label(window, text="Temperature").grid(
    row=2, column=0, padx=10, pady=10)

temp = Label(window, text="", textvariable=temperature, font=(
    "courier", 16), relief=SUNKEN, fg="#003333", bg="#00cccc", width=15).grid(row=2, column=1, padx=10, pady=10, sticky=W)

loc_label = Label(window, text="Location").grid(
    row=3, column=0, padx=10, pady=10)

loc = Label(window, text="", textvariable=location, font=(
    "courier", 16), relief=SUNKEN, fg="#003333", bg="#00cccc", width=15).grid(row=3, column=1, padx=10, pady=10, sticky=W)

desc_label = Label(window, text="Description").grid(
    row=4, column=0, padx=10, pady=10)

desc = Label(window, text="", textvariable=description, font=(
    "courier", 16), relief=SUNKEN, fg="#003333", bg="#00cccc", width=15).grid(row=4, column=1, padx=10, pady=10, sticky=W)

window.mainloop()
