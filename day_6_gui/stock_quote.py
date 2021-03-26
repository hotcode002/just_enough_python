from tkinter import *
import requests
import json


window = Tk()
window.title("Stock Quote App")
stock_code = StringVar()
stock_price = StringVar()

main_label = Label(window, text="Stock Quotes", font=(
    "courier", 36), relief=SUNKEN, fg="#003333", bg="#00b3b3").grid(row=0, column=0, columnspan=3, padx=20, pady=20)

stock_ticker_label = Label(window, text="Stock code").grid(
    row=1, column=0, padx=10, pady=10)
stock_ticker = Entry(window, textvariable=stock_code).grid(
    row=1, column=1, padx=10, pady=10, sticky=W)


def submitClicked():

    stock_code_l = stock_code.get()
    if stock_code_l != "":

        print("submit clicked", stock_code.get())
        url = 'https://api.worldtradingdata.com/api/v1/stock'

        params = {
            'api_token': '2KBRjSLj5bOvtuLxfGBuUBESucoZLTGPSYxbqFgbMAoE7hfKq60xXGpAsCIj'
        }

        params["symbol"] = stock_code_l
        try:
            response = requests.request('GET', url, params=params, timeout=10)
            if response.status_code == 200:
                json = response.json()
                stock_price.set(json["data"][0]["price_open"])
                print(json["data"][0]["price_open"])
            else:
                print("error")
        except:
            print("Exception occured")


submit_button = Button(window, text="Get quote", command=submitClicked).grid(
    row=1, column=2, padx=10, pady=10)

price_label = Label(window, text="Stock Price").grid(
    row=2, column=0, padx=10, pady=10)

price = Label(window, text="", textvariable=stock_price, font=(
    "courier", 16), relief=SUNKEN, fg="#003333", bg="#00cccc", width=5).grid(row=2, column=1, padx=10, pady=10, sticky=W)


window.mainloop()
