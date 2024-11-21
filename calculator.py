import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)  # Clear the entry widget
    entry.insert(0, current + str(value))  # Append the new value

def clear_entry():
    entry.delete(0, tk.END)  # Clear the entry widget

def calculate():
    try:
        result = eval(entry.get())  # Evaluate the math expression
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main Tkinter window
root = tk.Tk()
root.title("Simple Calculator")

# Create an Entry widget for input and output
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=clear_entry).grid(row=row, column=col, padx=5, pady=5)
    elif text == '=':
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=('Arial', 14), command=lambda t=text: button_click(t)).grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
root.mainloop()
