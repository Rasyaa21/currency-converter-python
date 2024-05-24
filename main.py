import tkinter as tk
from tkinter import ttk
import requests

API_URL = "https://v6.exchangerate-api.com/v6/682277ba9cfc0cd42d2e384f/latest/USD"

def getConversionRate():
    response = requests.get(API_URL)
    data = response.json()
    return data["conversion_rates"]

def ConvertCurrency():
    from_currency = fromCurrency.get()
    to_currency = toCurrency.get()
    amountLabel = float(amountEntry.get())
    
    rates = getConversionRate()
    conversion_rate = rates[to_currency] / rates[from_currency]
    converted_amountLabel = amountLabel * conversion_rate
    
    resultLabel.config(text=f"Converted amountLabel: {converted_amountLabel:.2f} {to_currency}")

root = tk.Tk()
root.geometry("600x600")
root.title("Currency Converter")

fromCurrency = tk.StringVar(root)
toCurrency = tk.StringVar(root)

rates = getConversionRate()
currencies = list(rates.keys())
print(currencies)

fromCurrecyLabel = ttk.Label(root, text="From Currency:")
fromCurrecyLabel.grid(column=0, row=0, padx=10, pady=10)
fromCurrencyMenu = ttk.Combobox(root, textvariable=fromCurrency, values=currencies)
fromCurrencyMenu.grid(column=1, row=0, padx=10, pady=10)

toCurrencyLabel = ttk.Label(root, text="To Currency:")
toCurrencyLabel.grid(column=0, row=1, padx=10, pady=10)
toCurrencyMenu = ttk.Combobox(root, textvariable=toCurrency, values=currencies)
toCurrencyMenu.grid(column=1, row=1, padx=10, pady=10)

amountLabel = ttk.Label(root, text="amountLabel:")
amountLabel.grid(column=0, row=2, padx=10, pady=10)
amountEntry = ttk.Entry(root)
amountEntry.grid(column=1, row=2, padx=10, pady=10)

convertButton = ttk.Button(root, text="Convert", command=ConvertCurrency)
convertButton.grid(column=0, row=3, columnspan=2, pady=10)

resultLabel = ttk.Label(root, text="Converted amountLabel:")
resultLabel.grid(column=0, row=4, columnspan=2, pady=10)

fromCurrencyMenu.set(currencies[0])
toCurrencyMenu.set(currencies[1])

root.mainloop()
