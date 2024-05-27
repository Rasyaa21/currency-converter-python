import tkinter as tk
import requests
import customtkinter as ctk

#membuat variable yang menampung api
API_URL = "https://v6.exchangerate-api.com/v6/682277ba9cfc0cd42d2e384f/latest/USD"

#membuat function untuk mendapatkan nilai tukar mata uang dari api
def getConversionRate():
    #membuat variable yang digunakan untuk mendapatkan data dari api
    response = requests.get(API_URL)
    #merubah data yang didapatkan menjadi format json
    data = response.json()
    #mengambil conversion_rates pada data json tersebut 
    return data["conversion_rates"]

#membuat function yang dapat menghitung nilai uang yang akan di ubah
def ConvertCurrency():
    #mendapatkan nilai mata dari combobox
    from_currency = fromCurrencyDropdown.get()
    to_currency = toCurrencyDropdown.get()
    #mengambil nilai dari amount dan diubah menjadi float
    amount = float(amountEntry.get())

    #memanggil function untuk mendapatkan rate harga dari mata uang 
    rates = getConversionRate()
    #membagi rate mata uang yang akan di convert dengan mata uang yang mau di convert
    conversionRate = rates[to_currency] / rates[from_currency]
    #mengkalikan jumlah dan rate yang sudah dihitung 
    convertedAmount = amount * conversionRate

    #menampilkan hasil dari nilai yang sudah di convert kedalam label
    resultLabel.configure(text=f"Converted From {from_currency}: {convertedAmount:.2f} {to_currency}")


#membuat canvas dari tkinter
root = tk.Tk()
#menentukan ukuran canvas dari tkinter
root.geometry("350x370")
#menentukan judul
root.title("Currency Converter")
#menentukan background dari canvas
root.configure(
    bg="#1c1c1c"
)

#mendapatkan nilai tukar mata uang
rates = getConversionRate()
#mendapatkan mata uang dan mengubahnya menjadi list
currencies = list(rates.keys())

#membuat gui pada canvas
titleLabel = ctk.CTkLabel(root, text="Currency Converter", font=("Arial", 20, "bold"), text_color="black", bg_color="#ff9500", width=350, height=50)
titleLabel.grid(column=0, row=0, columnspan=2, sticky='ew')

fromCurrencyLabel = ctk.CTkLabel(root, text="From Currency", font=("Arial", 16, "bold"), text_color="white", bg_color="#1c1c1c")
fromCurrencyLabel.grid(column=0, row=1, padx=10, pady=5, sticky='w')
#membuat dropdown menggunakan combobox 
fromCurrencyDropdown = ctk.CTkComboBox(root, values=currencies, width=150, font=("Arial", 14, "bold"), height=30, dropdown_hover_color="black",)
fromCurrencyDropdown.grid(column=0, row=2, padx=10, pady=5, sticky='w')

toCurrencyLabel = ctk.CTkLabel(root, text="To Currency", font=("Arial", 16, "bold"), text_color="white", bg_color="#1c1c1c")
toCurrencyLabel.grid(column=1, row=1, padx=10, pady=5, sticky='w')
#membuat dropdown menggunakan combobox 
toCurrencyDropdown = ctk.CTkComboBox(root, values=currencies, font=("Arial", 14, "bold"), width=150, height=30, dropdown_hover_color="black")
toCurrencyDropdown.grid(column=1, row=2, padx=10, pady=5, sticky='w')

amountLabel = ctk.CTkLabel(root, text="Amount", font=("Arial", 16, "bold"), text_color="white", bg_color="#1c1c1c")
amountLabel.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
amountEntry = ctk.CTkEntry(root, width=200, font=("Arial", 14, "bold"), corner_radius=10, border_width=1, border_color="white", height=30)
amountEntry.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

#membuat button pada saat dipencet akan menjalankan funcction convertCurrency
convertButton = ctk.CTkButton(root, text="Convert", command=ConvertCurrency, corner_radius=15, text_color="white", width=200, font=("Arial", 12, "bold"), fg_color="#505050")
convertButton.grid(column=0, row=5, columnspan=2, pady=10)

resultLabel = ctk.CTkLabel(root, text="", text_color="white", font=("Arial", 16, "bold"), bg_color="#1c1c1c")
resultLabel.grid(column=0, row=6, columnspan=2, pady=10, padx=10)

#menetapkan nilai default pada combobox
#contohnya index ke 0 adlaah usd maka di combobox 1 yang akan ditampilkan adalah USD
#sama seperti pada combobox kedua
fromCurrencyDropdown.set(currencies[0])
toCurrencyDropdown.set(currencies[1])

#mainloop digunakan untuk menjalankan program tkinter
root.mainloop()
