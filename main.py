import tkinter as tk
from tkinter import ttk
import requests
import customtkinter as ctk

API_URL = "https://v6.exchangerate-api.com/v6/682277ba9cfc0cd42d2e384f/latest/USD"

def getConversionRate():
    response = requests.get(API_URL)
    data = response.json()
    return data["conversion_rates"]

def ConvertCurrency():
    from_currency = fromCurrencyDropdown.get()
    to_currency = toCurrencyDropdown.get()
    amount = float(amountEntry.get())
    
    rates = getConversionRate()
    conversionRate = rates[to_currency] / rates[from_currency]
    convertedAmount = amount * conversionRate
    
    resultLabel.configure(text=f"Converted From {from_currency}: {convertedAmount:.2f} {to_currency}")

root = tk.Tk()
root.geometry("350x370")
root.title("Currency Converter")
root.configure(
    bg="#1c1c1c"
)

rates = getConversionRate()
currencies = list(rates.keys())

titleLabel = ctk.CTkLabel(root, text="Currency Converter", font=("Arial", 20, "bold"), text_color="black", bg_color="#ff9500", width=350, height=50)
titleLabel.grid(column=0, row=0, columnspan=2, sticky='ew')

fromCurrencyLabel = ctk.CTkLabel(root, text="From Currency", font=("Arial", 16, "bold"), text_color="white", bg_color="#1c1c1c")
fromCurrencyLabel.grid(column=0, row=1, padx=10, pady=5, sticky='w')
fromCurrencyDropdown = ctk.CTkComboBox(root, values=currencies, width=150, font=("Arial", 14, "bold"), height=30, dropdown_hover_color="black",)
fromCurrencyDropdown.grid(column=0, row=2, padx=10, pady=5, sticky='w')

toCurrencyLabel = ctk.CTkLabel(root, text="To Currency", font=("Arial", 16, "bold"), text_color="white", bg_color="#1c1c1c")
toCurrencyLabel.grid(column=1, row=1, padx=10, pady=5, sticky='w')
toCurrencyDropdown = ctk.CTkComboBox(root, values=currencies, font=("Arial", 14, "bold"), width=150, height=30, dropdown_hover_color="black")
toCurrencyDropdown.grid(column=1, row=2, padx=10, pady=5, sticky='w')

amountLabel = ctk.CTkLabel(root, text="Amount", font=("Arial", 16, "bold"), text_color="white", bg_color="#1c1c1c")
amountLabel.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
amountEntry = ctk.CTkEntry(root, width=200, font=("Arial", 14, "bold"), corner_radius=10, border_width=1, border_color="white", height=30)
amountEntry.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

convertButton = ctk.CTkButton(root, text="Convert", command=ConvertCurrency, corner_radius=15, text_color="white", width=200, font=("Arial", 12, "bold"), fg_color="#505050")
convertButton.grid(column=0, row=5, columnspan=2, pady=10)

resultLabel = ctk.CTkLabel(root, text="", text_color="white", font=("Arial", 16, "bold"), bg_color="#1c1c1c")
resultLabel.grid(column=0, row=6, columnspan=2, pady=10, padx=10)

fromCurrencyDropdown.set(currencies[0])
toCurrencyDropdown.set(currencies[1])

root.mainloop()
