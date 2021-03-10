import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
import requests
from urllib import *
import json
import webbrowser

root = Tk()
root.title('Конвертер валют')
root.geometry('300x250+500+100')
root.resizable(False, False)

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}

base_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'

START_AMOUNT = 1000

def exchange():
    html = urllib.requests.urlopen(base_url)
    data = html.read(s)
    print(data)

header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

h_currency = Label(header_frame, text='Валюта', bg='#ccc', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)

h_buy = Label(header_frame, text='Покупка', bg='#ccc', font='Arial 12 bold')
h_buy.grid(row=0, column=1, sticky=EW)

h_sale = Label(header_frame, text='Продажа', bg='#ccc', font='Arial 12 bold')
h_sale.grid(row=0, column=2, sticky=EW)

#USD course

usd_currency = Label(header_frame, text='USD', font='Arial 10')
usd_currency.grid(row=1, column=0, sticky=EW)

usd_buy = Label(header_frame, text='25.60', font='Arial 10')
usd_buy.grid(row=1, column=1, sticky=EW)

usd_sale = Label(header_frame, text='25.60', font='Arial 10')
usd_sale.grid(row=1, column=2, sticky=EW)

#EUR course

eur_currency = Label(header_frame, text='EUR', bg='#ccc', font='Arial 10')
eur_currency.grid(row=2, column=0, sticky=EW)

eur_buy = Label(header_frame, text='27.50', bg='#ccc', font='Arial 10')
eur_buy.grid(row=2, column=1, sticky=EW)

eur_sale = Label(header_frame, text='27.60', bg='#ccc', font='Arial 10')
eur_sale.grid(row=2, column=2, sticky=EW)

#RUR course

rur_currency = Label(header_frame, text='RUR', font='Arial 10')
rur_currency.grid(row=3, column=0, sticky=EW)

rur_buy = Label(header_frame, text='0.35', font='Arial 10')
rur_buy.grid(row=3, column=1, sticky=EW)

rur_sale = Label(header_frame, text='0.39', font='Arial 10')
rur_sale.grid(row=3, column=2, sticky=EW)

#Calc Frame

calc_frame = Frame(root, bg='#fff')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

#UAH

l_uah = Label(calc_frame, text='Гривна:', bg='#fff', font='Arial 10 bold')
l_uah.grid(row=0, column=0, padx=10)
e_uah = ttk.Entry(calc_frame, justify=CENTER, font='Arial 10')
e_uah.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
e_uah.insert(0, START_AMOUNT)

# Button
btn_calc = ttk.Button(calc_frame, text='Обмен', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

# Result Frame
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

# USD
l_usd = Label(res_frame, text='USD:', font='Arial 10 bold')
l_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, '25000')

# EUR
l_eur = Label(res_frame, text='EUR:', font='Arial 10 bold')
l_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, '25000')

# RUR
l_rur = Label(res_frame, text='RUR:', font='Arial 10 bold')
l_rur.grid(row=4, column=0)
e_rur = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_rur.grid(row=4, column=1, columnspan=2, padx=10, sticky=EW)
e_rur.insert(0, '10000')

root.mainloop()
