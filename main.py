import tkinter as tk
from tkinter import ttk
import requests

API_URL = "https://v6.exchangerate-api.com/v6/682277ba9cfc0cd42d2e384f/latest/USD"

def fetch_conversion_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data["conversion_rates"]

def convert_currency():
    from_currency = fromCurrency.get()
    to_currency = toCurrency.get()
    amount = float(amount_entry.get())
    
    rates = fetch_conversion_rates()
    conversion_rate = rates[to_currency] / rates[from_currency]
    converted_amount = amount * conversion_rate
    
    result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_currency}")

root = tk.Tk()
root.geometry("600x600")
root.title("Currency Converter")

fromCurrency = tk.StringVar(root)
toCurrency = tk.StringVar(root)

rates = fetch_conversion_rates()
currencies = list(rates.keys())
print(currencies)

from_currency_label = ttk.Label(root, text="From Currency:")
from_currency_label.grid(column=0, row=0, padx=10, pady=10)
from_currency_menu = ttk.Combobox(root, textvariable=fromCurrency, values=currencies)
from_currency_menu.grid(column=1, row=0, padx=10, pady=10)

to_currency_label = ttk.Label(root, text="To Currency:")
to_currency_label.grid(column=0, row=1, padx=10, pady=10)
to_currency_menu = ttk.Combobox(root, textvariable=toCurrency, values=currencies)
to_currency_menu.grid(column=1, row=1, padx=10, pady=10)

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(column=0, row=2, padx=10, pady=10)
amount_entry = ttk.Entry(root)
amount_entry.grid(column=1, row=2, padx=10, pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(column=0, row=3, columnspan=2, pady=10)

result_label = ttk.Label(root, text="Converted Amount:")
result_label.grid(column=0, row=4, columnspan=2, pady=10)

from_currency_menu.set(currencies[0])
to_currency_menu.set(currencies[1])

root.mainloop()
