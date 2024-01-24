import tkinter as tk

def convert_decimal_to_binary():
    try:
        decimal_number = int(entry_decimal.get())
        binary_number = bin(decimal_number)[2:]
        label_binary.config(text=binary_number)
    except:
        label_binary.config(text="Error: Please enter a valid decimal number")

def convert_decimal_to_octal():
    try:
        decimal_number = int(entry_decimal.get())
        octal_number = oct(decimal_number)[2:]
        label_octal.config(text=octal_number)
    except:
        label_octal.config(text="Error: Please enter a valid decimal number")

def convert_decimal_to_hexadecimal():
    try:
        decimal_number = int(entry_decimal.get())
        hexadecimal_number = hex(decimal_number)[2:]
        label_hexadecimal.config(text=hexadecimal_number)
    except:
        label_hexadecimal.config(text="Error: Please enter a valid decimal number")

def convert_binary_to_decimal():
    try:
        binary_number = str(entry_binary.get())
        decimal_number = int(binary_number, 2)
        label_decimal.config(text=decimal_number)
    except:
        label_decimal.config(text="Error: Please enter a valid binary number")

def convert_binary_to_octal():
    try:
        binary_number = str(entry_binary.get())
        decimal_number = int(binary_number, 2)
        octal_number = oct(decimal_number)[2:]
        label_octal.config(text=octal_number)
    except:
        label_octal.config(text="Error: Please enter a valid binary number")

def convert_binary_to_hexadecimal():
    try:
        binary_number = str(entry_binary.get())
        decimal_number = int(binary_number, 2)
        hexadecimal_number = hex(decimal_number)[2:]
        label_hexadecimal.config(text=hexadecimal_number)
    except:
        label_hexadecimal.config(text="Error: Please enter a valid binary number")

def convert_octal_to_decimal():
    try:
        octal_number = str(entry_octal.get())
        decimal_number = int(octal_number, 8)
        label_decimal.config(text=decimal_number)
    except:
        label_decimal.config(text="Error: Please enter a valid octal number")

def convert_octal_to_binary():
    try:
        octal_number = str(entry_octal.get())
        decimal_number = int(octal_number, 8)
        binary_number = bin(decimal_number)[2:]
        label_binary.config(text=binary_number)
    except:
        label_binary.config(text="Error: Please enter a valid octal number")

def convert_octal_to_hexadecimal():
    try:
        octal_number = str(entry_octal.get())
        decimal_number = int(octal_number, 8)
        hexadecimal_number = hex(decimal_number)[2:]
        label_hexadecimal.config(text=hexadecimal_number)
    except:
        label_hexadecimal.config(text="Error: Please enter a valid octal number")

def convert_hexadecimal_to_decimal():
    try:
        hexadecimal_number = str(entry_hexadecimal.get())
        decimal_number = int(hexadecimal_number, 16)
        label_decimal.config(text=decimal_number)
    except:
        label_decimal.config(text="Error: Please enter a valid hexadecimal number")

def convert_hexadecimal_to_binary():
    try:
        hexadecimal_number = str(entry_hexadecimal.get())
        decimal_number = int(hexadecimal_number, 16)
        binary_number = bin(decimal_number)[2:]
        label_binary.config(text=binary_number)
    except:
        label_binary.config(text="Error: Please enter a valid hexadecimal number")

def convert_hexadecimal_to_octal():
    try:
        hexadecimal_number = str(entry_hexadecimal.get())
        decimal_number = int(hexadecimal_number, 16)
        octal_number = oct(decimal_number)[2:]
        label_octal.config(text=octal_number)
    except:
        label_octal.config(text="Error: Please enter a valid hexadecimal number")

root = tk.Tk()
root.title("Number System Converter")

#Labels
label_decimal = tk.Label(root, text="Decimal", width=10, bg="yellow")
label_binary = tk.Label(root, text="Binary", width=10, bg="yellow")
label_octal = tk.Label(root, text="Octal", width=10, bg="yellow")
label_hexadecimal = tk.Label(root, text="Hexadecimal", width=10, bg="yellow")

#Entry fields
entry_decimal = tk.Entry(root, width=15)
entry_binary = tk.Entry(root, width=15)
entry_octal = tk.Entry(root, width=15)
entry_hexadecimal = tk.Entry(root, width=15)

#Buttons
button_decimal_to_binary = tk.Button(root, text="Convert to Binary", command=convert_decimal_to_binary)
button_decimal_to_octal = tk.Button(root, text="Convert to Octal", command=convert_decimal_to_octal)
button_decimal_to_hexadecimal = tk.Button(root, text="Convert to Hexadecimal", command=convert_decimal_to_hexadecimal)

button_binary_to_decimal = tk.Button(root, text="Convert to Decimal", command=convert_binary_to_decimal)
button_binary_to_octal = tk.Button(root, text="Convert to Octal", command=convert_binary_to_octal)
button_binary_to_hexadecimal = tk.Button(root, text="Convert to Hexadecimal", command=convert_binary_to_hexadecimal)

button_octal_to_decimal = tk.Button(root, text="Convert to Decimal", command=convert_octal_to_decimal)
button_octal_to_binary = tk.Button(root, text="Convert to Binary", command=convert_octal_to_binary)
button_octal_to_hexadecimal = tk.Button(root, text="Convert to Hexadecimal", command=convert_octal_to_hexadecimal)

button_hexadecimal_to_decimal = tk.Button(root, text="Convert to Decimal", command=convert_hexadecimal_to_decimal)
button_hexadecimal_to_binary = tk.Button(root, text="Convert to Binary", command=convert_hexadecimal_to_binary)
button_hexadecimal_to_octal = tk.Button(root, text="Convert to Octal", command=convert_hexadecimal_to_octal)

#Label Grid
label_decimal.grid(row=0, column=0)
label_binary.grid(row=0, column=1)
label_octal.grid(row=0, column=2)
label_hexadecimal.grid(row=0, column=3)

#Entry Grid
entry_decimal.grid(row=1, column=0)
entry_binary.grid(row=1, column=1)
entry_octal.grid(row=1, column=2)
entry_hexadecimal.grid(row=1, column=3)

#Button Grid
button_decimal_to_binary.grid(row=2, column=1)
button_decimal_to_octal.grid(row=3, column=1)
button_decimal_to_hexadecimal.grid(row=4, column=1)

button_binary_to_decimal.grid(row=2, column=2)
button_binary_to_octal.grid(row=3, column=2)
button_binary_to_hexadecimal.grid(row=4, column=2)

button_octal_to_decimal.grid(row=2, column=3)
button_octal_to_binary.grid(row=3, column=3)
button_octal_to_hexadecimal.grid(row=4, column=3)

button_hexadecimal_to_decimal.grid(row=2, column=4)
button_hexadecimal_to_binary.grid(row=3, column=4)
button_hexadecimal_to_octal.grid(row=4, column=4)

root.mainloop()