import tkinter as tk
from tkinter import messagebox


def add_operations(operations):
    Value = calc.get()
    if Value[-1] in "-+/*":
        Value = Value[-1]
    elif "+" in Value or "-" in Value or "*" in Value or "/" in Value:
        calculate()
        Value = calc.get()
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, Value + operations)
    calc["state"] = tk.DISABLED


def add_digit(digit):
    Value = calc.get()
    if Value[0] == "0" and len(Value) == 1:
        Value = Value[1:]
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, Value + digit)
    calc["state"] = tk.DISABLED


def calculate():
    Value = calc.get()
    if Value[-1] in "+-*/":
        Value = Value + Value[:-1]
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(Value))
        calc["state"] = tk.DISABLED
    except (NameError, SyntaxError):
        messagebox.showinfo("INFO", "INPUT ONLY DIGITS")
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo("ZERO DIVISION", "DONT DIVISION ON ZERO")


def clear():
    calc["state"] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, 0)
    calc["state"] = tk.DISABLED


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=("Arial", 13), fg="black",
                     command=lambda: add_digit(digit))


def make_operations_button(operations):
    return tk.Button(text=operations, bd=5, font=("Arial", 13), fg="green",
                     command=lambda: add_operations(operations))


def make_calk_button(operations):
    return tk.Button(text=operations, bd=5, font=("Arial", 13), fg="green",
                     command=calculate)


def make_clear_button(operations):
    return tk.Button(text=operations, bd=5, font=("Arial", 13), fg="green",
                     command=clear)


def press_key(event):
    print(event.char)
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-*/":
        add_operations(event.char)
    elif event.char == "\r":
        calculate()


root = tk.Tk()
root.geometry(f"240x270+100+200")
root["bg"] = "#33ffe6"
root.title("Kalkulated")

root.bind("<Key>", press_key)

calc = tk.Entry(root, justify=tk.RIGHT, font=("Arial", 13), width=15, )
calc.insert(0, "0")
calc["state"] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, stick="we", padx=5)

make_operations_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operations_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operations_button("*").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operations_button("/").grid(row=4, column=3, stick="wens", padx=5, pady=5)

make_calk_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_clear_button("c").grid(row=4, column=1, stick="wens", padx=5, pady=5)

make_digit_button("1").grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button("2").grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button("3").grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button("4").grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button("5").grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button("6").grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button("7").grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button("8").grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button("9").grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button("0").grid(row=4, column=0, stick="wens", padx=5, pady=5)

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()
