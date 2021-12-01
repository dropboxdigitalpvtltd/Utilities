from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import requests

"""
url = r'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'

payload = {'some': 'data'}

headers = {'APIKEY': '4ff4d45d0887ac054fe00195145086ac9410a3721ef6263372759977f1d7fb9d'}

response1 = requests.get(url, data=json.dumps(payload), headers=headers)

"""



root = Tk()
root.title("Koaloafolio")
# root.iconbitmap('url')
root.geometry("400x200")


def graph():
    data = np.array([300, 700, 1900])
    plt.plot(data)
    plt.show()


first_button = Button(root, text="Plot It!", command=graph)
first_button.pack()
root.mainloop()