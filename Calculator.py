import tkinter as tk

# --- Initializing window ---
window = tk.Tk()  # Create a window
window.title('Calculator')  # Set title for your window
window.geometry('300x400')  # Set size of your window
window.iconbitmap(r'C:\Users\jatin\Desktop\Programing\Logo.ico')  # Set icon
window.minsize(width=300, height=400)  # Set minimum size of your window
window.maxsize(width=1980, height=1080)  # Set maximum size of your window
window.resizable(width=False, height=False)  # Lock window size

# --- Function ---
def press(key):
    current = Entry.get()
    Entry.delete(0, tk.END)
    Entry.insert(0, current + str(key))

def clear():
    Entry.delete(0, tk.END)

def backspace():
    current = Entry.get()
    Entry.delete(0, tk.END)
    Entry.insert(0, current[:-1])

def calculate():
    try:
        result = eval(Entry.get().replace('x', '*').replace('÷', '/'))
        Entry.delete(0, tk.END)
        Entry.insert(0, str(result))
    except Exception as e:
        Entry.delete(0, tk.END)
        Entry.insert(0, "Error")

def calculate_percentage():
    try:
        current = float(Entry.get()) 
        Entry.delete(0, tk.END)      
        Entry.insert(0, str(current / 100))  
    except ValueError:              
        Entry.delete(0, tk.END)
        Entry.insert(0, "Error")      

# --- Button style settings ---
button_style = {
    'bg': 'salmon',
    'fg': 'white',
    'font': ('Arial', 14, 'bold'),
    'padx': 20,
    'pady': 15
}

button_style2 = {
    'bg': 'coral',
    'fg': 'white',
    'font': ('Arial', 14, 'bold'),
    'padx': 20,
    'pady': 15
}

# --- Create buttons --- (For design buttons)
Button00 = tk.Button(text="00", **button_style, command=lambda: press("00"))
Button0 = tk.Button(text="0", **button_style, command=lambda: press("0"))
Button1 = tk.Button(text="1", **button_style, command=lambda: press("1"))
Button2 = tk.Button(text="2", **button_style, command=lambda: press("2"))
Button3 = tk.Button(text="3", **button_style, command=lambda: press("3"))
Button4 = tk.Button(text="4", **button_style, command=lambda: press("4"))
Button5 = tk.Button(text="5", **button_style, command=lambda: press("5"))
Button6 = tk.Button(text="6", **button_style, command=lambda: press("6"))
Button7 = tk.Button(text="7", **button_style, command=lambda: press("7"))
Button8 = tk.Button(text="8", **button_style, command=lambda: press("8"))
Button9 = tk.Button(text="9", **button_style, command=lambda: press("9"))
ButtonPl = tk.Button(text="+", **button_style2, command=lambda: press("+"))
Buttonsub = tk.Button(text="-", **button_style2, command=lambda: press("-"))
Buttonmul = tk.Button(text="x", **button_style2, command=lambda: press("x"))
Buttondiv = tk.Button(text="÷", **button_style2, command=lambda: press("÷"))
Buttoneq = tk.Button(text="=", **button_style2, command=calculate)
Buttonper = tk.Button(text="%", **button_style, command=calculate_percentage)  # Updated button for percentage
Buttondec = tk.Button(text=".", **button_style, command=lambda: press("."))
ButtonAC = tk.Button(text="AC", bg='darkgray', fg='white', font=('Arial', 13, 'bold'), command=clear)
ButtonBS = tk.Button(text='⌫', bg='orange', fg='white', font=('Arial', 14, 'bold'), command=backspace)

# --- Pack --- (Set position of buttons)
Button00.place(x=5, y=349, width=70, height=45)
Button0.place(x=80, y=349, width=70, height=45)
Button1.place(x=5, y=300, width=70, height=45)
Button2.place(x=80, y=300, width=70, height=45)
Button3.place(x=155, y=300, width=70, height=45)
Button4.place(x=5, y=249, width=70, height=45)
Button5.place(x=80, y=249, width=70, height=45)
Button6.place(x=155, y=249, width=70, height=45)
Button7.place(x=5, y=200, width=70, height=45)
Button8.place(x=80, y=200, width=70, height=45)
Button9.place(x=155, y=200, width=70, height=45)
ButtonPl.place(x=230, y=300, width=65, height=45)
Buttonsub.place(x=230, y=249, width=65, height=45)
Buttonmul.place(x=230, y=200, width=65, height=45)
Buttondiv.place(x=230, y=150, width=65, height=45)
Buttoneq.place(x=230, y=349, width=65, height=45)
Buttonper.place(x=118, y=150, width=107, height=45) 
Buttondec.place(x=155, y=349, width=70, height=45)
ButtonAC.place(x=5, y=150, width=107, height=45)
ButtonBS.place(x=230, y=100, width=65, height=45)

# --- Entry --- (For result window)
Entry = tk.Entry(window, border=2, relief='solid', font=('Arial', 14, 'bold'))
Entry.place(x=5, y=5, width=290, height=45)

# --- Mainloop ---
window.mainloop()
