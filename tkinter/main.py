from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests


# my_tree['columns'] = () 

"""
url = r'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
payload = {'some': 'data'}
headers = {'APIKEY': '4ff4d45d0887ac054fe00195145086ac9410a3721ef6263372759977f1d7fb9d'}
response1 = requests.get(url, data=json.dumps(payload), headers=headers)
"""

"""
root.title("Koaloafolio")
# root.iconbitmap('url')
root.geometry("400x200")
tree = ttk.Treeview(win, column=("Currecy", "Value"), show='headings', height=5)
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Country")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Value")
json_object = json.loads(response1.text)
for key in json_object:
    tree.insert('', 'end', text="1", values=(key, json_object[key]))
tree.pack()
"""

# def graph():
#     data = np.array([300, 700, 1900])
#     plt.plot(data)
#     plt.show()

# def chart():
#     sns.barplot()

# first_button = Button(root, text="Plot It!", command=graph)
# first_button.pack()
# root.mainloop()



"""
https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR
https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=BTC,USD,EUR,XMR,REP,ZEC &extraParams=your_app_name
https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=XMR,REP,ZEC &extraParams=your_app_name
https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=XMR,ETH,ZEC &extraParams=your_app_name
https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,XMR,ETH,ZEC     &e=Coinbase&extraParams=your_app_name

"""



from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

url_1 = r'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,JPY,AUD,CAD'
url_2 = r'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,JPY,AUD,CAD'
headers = {'APIKEY': '4ff4d45d0887ac054fe00195145086ac9410a3721ef6263372759977f1d7fb9d'}
response_B = requests.get(url_1, headers=headers)
response_E = requests.get(url_2, headers=headers)
print("Done")

ETH = response_E.json()
BTC = response_B.json()

root = Tk()
root.title('Dropbox Digital Crypto Dashboard')
root.iconbitmap('logo.ico')
root.geometry("500x500")

def graph():
    plt.style.use('seaborn-darkgrid')
    plt.figure(2, figsize=(10,5))

    plt.subplot(1, 2, 1)
    plt.bar(ETH.keys(), ETH.values(), width=0.3)  
    plt.title("Ethereum")
    plt.subplot(1, 2, 2)
    plt.bar(BTC.keys(), BTC.values(), width=0.3)
    plt.title("Bitcoin")

    # plt.title("BTC")
    # plt.xlabel('BTC')
    # plt.ylabel('USD')
    plt.plot()

my_tree = ttk.Treeview(root)
my_tree['columns'] = ("Coin", "Price in USD", "Price in EUR",
                      "Price in JPY", "Price in AUD", "Price in CAD")
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Coin", anchor=W, width=100)
my_tree.column("Price in USD", anchor=W, width=100)
my_tree.column("Price in EUR", anchor=W, width=100)
my_tree.column("Price in JPY", anchor=W, width=100)
my_tree.column("Price in AUD", anchor=W, width=100)
my_tree.column("Price in CAD", anchor=W, width=100)


# Create Headings
my_tree.heading("Coin", text="Coin", anchor=W)
my_tree.heading("Price in USD", text="Price in USD", anchor=W)
my_tree.heading("Price in EUR", text="Price in EUR", anchor=W)
my_tree.heading("Price in JPY", text="Price in JPY", anchor=W)
my_tree.heading("Price in AUD", text="Price in AUD", anchor=W)
my_tree.heading("Price in CAD", text="Price in CAD", anchor=W)

# add data
my_tree.insert(parent="", index="end", values=(
    "Bitcoin", BTC['USD'], BTC['EUR'], BTC['JPY'], BTC['AUD'], BTC['CAD']))
my_tree.insert(parent="", index="end", iid=0, values=(
    "Ethereum", ETH['USD'], ETH['EUR'], ETH['JPY'], ETH['AUD'], ETH['CAD']))


my_tree.pack(pady=20)
root.mainloop()
