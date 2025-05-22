import tkinter as tk
from tkinter import messagebox
import basicFunc
import complexFunc
import converter

def handle_error(error_message):
    messagebox.showerror("Ошибка", error_message)

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    try:
        expression = expression.replace("√", "complexFunc.root")
        expression = expression.replace("^", "**")
        expression = expression.replace("lg", "complexFunc.logarithm")
        expression = expression.replace("sin", "complexFunc.sine")
        expression = expression.replace("cos", "complexFunc.cosine")
        expression = expression.replace("ctg", "complexFunc.cotangent")
        expression = expression.replace("tg", "complexFunc.tangent")


        result = eval(expression)
        input_text.set(result)
        expression = str(result)
    except ZeroDivisionError:
        handle_error("Деление на ноль")
        expression = ""
        input_text.set("")
    except Exception as e:
        handle_error(str(e))
        expression = ""
        input_text.set("")

def button_delete():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

def button_percentage():
    global expression
    try:
        result = basicFunc.percentage(eval(expression))
        input_text.set(result)
        expression = str(result)
    except Exception as e:
        handle_error(str(e))
        expression = ""
        input_text.set("")

def button_power():
    global expression
    expression = expression + "^"
    input_text.set(expression)

def button_root():
    global expression
    expression = expression + "√("
    input_text.set(expression)

def button_factorial():
    global expression
    try:
        result = complexFunc.factorial(eval(expression))
        input_text.set(result)
        expression = str(result)
    except Exception as e:
        handle_error(str(e))
        expression = ""
        input_text.set("")

def button_log():
    global expression
    expression = expression + "lg("
    input_text.set(expression)

def button_sin():
    global expression
    expression = expression + "sin("
    input_text.set(expression)

def button_cos():
    global expression
    expression = expression + "cos("
    input_text.set(expression)

def button_tan():
    global expression
    expression = expression + "tg("
    input_text.set(expression)

def button_cot():
    global expression
    expression = expression + "ctg("
    input_text.set(expression)

def on_key_press(event):
    if event.char.isdigit() or event.char in "+-*/.()":
        button_click(event.char)
        return "break"
    elif event.keysym == "Return":
        button_equal()
        return "break"
    elif event.keysym == "BackSpace":
        button_delete()
        return "break"
    elif event.char == "%":
        button_percentage()
        return "break"
    elif event.char == "^":
        button_power()
        return "break"
    elif event.char == "!":
        button_factorial()
        return "break"
    return None

def button_converter(root, button_click, button_clear, button_delete):
    converter_window = tk.Toplevel(root)
    converter_window.title("Конвертер величин")
    converter_window.geometry('400x600')
    converter_window.configure(background='black')

    converter_window.grid_rowconfigure(0, weight=1)
    converter_window.grid_rowconfigure(1, weight=1)
    converter_window.grid_rowconfigure(2, weight=1)
    converter_window.grid_rowconfigure(3, weight=1)
    converter_window.grid_rowconfigure(4, weight=1)
    converter_window.grid_columnconfigure(0, weight=1)
    converter_window.grid_columnconfigure(1, weight=1)
    converter_window.grid_columnconfigure(2, weight=1)
    converter_window.grid_columnconfigure(3, weight=1)
    converter_window.grid_columnconfigure(4, weight=1)

    conversion_type_var = tk.StringVar(converter_window)
    conversion_type_var.set("Длина")
    conversion_type_dropdown = tk.OptionMenu(converter_window, conversion_type_var, "Длина", "Время", "Валюта")
    conversion_type_dropdown.config(font=('arial', 16), bg='cyan', fg='black')
    conversion_type_dropdown.grid(row=0, column=0, columnspan=5, padx=5, pady=5, sticky='ew')

    from_var = tk.StringVar(converter_window)
    from_var.set("см")
    from_dropdown = tk.OptionMenu(converter_window, from_var, "см", "мм", "м", "км")
    from_dropdown.config(font=('arial', 16), bg='cyan', fg='black')
    from_dropdown.grid(row=1, column=0, columnspan=3, padx=0, pady=0, sticky='ew')

    to_var = tk.StringVar(converter_window)
    to_var.set("мм")
    to_dropdown = tk.OptionMenu(converter_window, to_var, "см", "мм", "м", "км")
    to_dropdown.config(font=('arial', 16), bg='cyan', fg='black')
    to_dropdown.grid(row=2, column=0, columnspan=3, padx=0, pady=0, sticky='ew')

    value_from_entry = tk.Entry(converter_window, bg="black", fg="cyan", font=('arial', 20, 'bold'), justify='right')
    value_from_entry.grid(row=1, column=3, columnspan=2, padx=5, pady=5, sticky='ew')

    result_display = tk.Label(converter_window, text="", bg="black", fg="cyan", font=('arial', 20, 'bold'), justify='right')
    result_display.grid(row=2, column=3, columnspan=2, padx=5, pady=5, sticky='ew')

    def perform_conversion():
        try:
            value = float(value_from_entry.get())
            from_unit = from_var.get()
            to_unit = to_var.get()
            conversion_type = conversion_type_var.get()

            if from_unit == to_unit:
                result = value
            elif conversion_type == "Длина":
                result = converter.convert_length(value, from_unit, to_unit)
            elif conversion_type == "Время":
                result = converter.convert_time(value, from_unit, to_unit)
            elif conversion_type == "Валюта":
                result = converter.convert_currency(value, from_unit, to_unit)
            else:
                result = "Не поддерживается"

            result_display.config(text=str(result))
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    convert_button = tk.Button(converter_window, text="Конвертировать", font=('Arial', 16), bg='cyan', fg='black', bd='2', command=perform_conversion, padx=20, pady=10)
    convert_button.grid(row=4, column=2, columnspan=3, sticky='nsew')

    def insert_value(value):
        current_value = value_from_entry.get()
        value_from_entry.delete(0, tk.END)
        value_from_entry.insert(0, current_value + str(value))

    but_del = tk.Button(converter_window, text='del', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: value_from_entry.delete(len(value_from_entry.get()) - 1, tk.END), padx=20, pady=10)
    but_del.grid(row=4, column=0, columnspan=2, sticky='nsew')

    but_7 = tk.Button(converter_window, text='7', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(7), padx=20, pady=10)
    but_7.grid(row=5, column=0, columnspan=2, sticky='nsew')
    but_8 = tk.Button(converter_window, text='8', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(8), padx=20, pady=10)
    but_8.grid(row=5, column=2, columnspan=2, sticky='nsew')
    but_9 = tk.Button(converter_window, text='9', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(9), padx=20, pady=10)
    but_9.grid(row=5, column=4, columnspan=2, sticky='nsew')

    but_4 = tk.Button(converter_window, text='4', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(4), padx=20, pady=10)
    but_4.grid(row=6, column=0, columnspan=2, sticky='nsew')
    but_5 = tk.Button(converter_window, text='5', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(5), padx=20, pady=10)
    but_5.grid(row=6, column=2, columnspan=2, sticky='nsew')
    but_6 = tk.Button(converter_window, text='6', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(6), padx=20, pady=10)
    but_6.grid(row=6, column=4, columnspan=2, sticky='nsew')

    but_1 = tk.Button(converter_window, text='1', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(1), padx=20, pady=10)
    but_1.grid(row=7, column=0, columnspan=2, sticky='nsew')
    but_2 = tk.Button(converter_window, text='2', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(2), padx=20, pady=10)
    but_2.grid(row=7, column=2, columnspan=2, sticky='nsew')
    but_3 = tk.Button(converter_window, text='3', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(3), padx=20, pady=10)
    but_3.grid(row=7, column=4, columnspan=2, sticky='nsew')

    but_0 = tk.Button(converter_window, text='0', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value(0), padx=20, pady=10)
    but_0.grid(row=8, column=2, columnspan=2, sticky='nsew')
    but_fl = tk.Button(converter_window, text=',', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: insert_value('.'), padx=20, pady=10)
    but_fl.grid(row=8, column=4, columnspan=2, sticky='nsew')
    but_clear_all = tk.Button(converter_window, text='AC', font=('Arial', 16), bg='cyan', fg='black', bd='2', command=lambda: value_from_entry.delete(0, tk.END), padx=20, pady=10)
    but_clear_all.grid(row=8, column=0, columnspan=2, sticky='nsew')


    def update_units(*args):
        conversion_type = conversion_type_var.get()
        if conversion_type == "Длина":
            units = ["см", "мм", "м", "км"]
        elif conversion_type == "Время":
            units = ["секунды", "минуты", "часы", "дни", "месяцы", "годы"]
        elif conversion_type == "Валюта":
            units = ["рубль", "доллар", "евро"]
        else:
            units = []

        from_dropdown['menu'].delete(0, 'end')
        to_dropdown['menu'].delete(0, 'end')
        for unit in units:
            from_dropdown['menu'].add_command(label=unit, command=tk._setit(from_var, unit))
            to_dropdown['menu'].add_command(label=unit, command=tk._setit(to_var, unit))

    conversion_type_var.trace('w', update_units)


root = tk.Tk()
root.title("Калькулятор")
root.geometry('400x600')
root.configure(background='black')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)

root.rowconfigure(0, weight=5)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
root.rowconfigure(7, weight=1)

input_text = tk.StringVar()
expression = ""

input_frame = tk.Frame(root, bg="black")
input_frame.grid(row=0, column=0, columnspan=4, sticky='nsew')

input_field = tk.Entry(input_frame, font=('arial', 32, 'bold'), textvariable=input_text, bg="black", fg='cyan',
                       justify='right')
input_field.pack(fill='both', expand=True)
input_field.focus_set()
input_field.bind("<Key>", on_key_press)

but_clear_all = tk.Button(root, text='AC', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_clear)
but_clear_all.grid(row=1, column=0, sticky='nsew')
but_del = tk.Button(root, text='del', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_delete)
but_del.grid(row=1, column=1, sticky='nsew')
but_perc = tk.Button(root, text='%', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_percentage)
but_perc.grid(row=1, column=2, sticky='nsew')
but_rov = tk.Button(root, text='=', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_equal)
but_rov.grid(row=1, column=3, sticky='nsew')

but_sin = tk.Button(root, text='sin', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_sin)
but_sin.grid(row=2, column=0, sticky='nsew')
but_cos = tk.Button(root, text='cos', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_cos)
but_cos.grid(row=2, column=1, sticky='nsew')
but_tg = tk.Button(root, text='tg', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_tan)
but_tg.grid(row=2, column=2, sticky='nsew')
but_ctg = tk.Button(root, text='ctg', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_cot)
but_ctg.grid(row=2, column=3, sticky='nsew')

but_log = tk.Button(root, text='lg', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_log)
but_log.grid(row=3, column=0, sticky='nsew')
but_root = tk.Button(root, text='√', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_root)
but_root.grid(row=3, column=1, sticky='nsew')
but_pow = tk.Button(root, text='^', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_power)
but_pow.grid(row=3, column=2, sticky='nsew')
but_fact = tk.Button(root, text='!', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=button_factorial)
but_fact.grid(row=3, column=3, sticky='nsew')

but_7 = tk.Button(root, text='7', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(7))
but_7.grid(row=4, column=0, sticky='nsew')
but_8 = tk.Button(root, text='8', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(8))
but_8.grid(row=4, column=1, sticky='nsew')
but_9 = tk.Button(root, text='9', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(9))
but_9.grid(row=4, column=2, sticky='nsew')
but_div = tk.Button(root, text='/', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click('/'))
but_div.grid(row=4, column=3, sticky='nsew')

but_4 = tk.Button(root, text='4', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(4))
but_4.grid(row=5, column=0, sticky='nsew')
but_5 = tk.Button(root, text='5', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(5))
but_5.grid(row=5, column=1, sticky='nsew')
but_6 = tk.Button(root, text='6', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(6))
but_6.grid(row=5, column=2, sticky='nsew')
but_mult = tk.Button(root, text='*', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click('*'))
but_mult.grid(row=5, column=3, sticky='nsew')

but_1 = tk.Button(root, text='1', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(1))
but_1.grid(row=6, column=0, sticky='nsew')
but_2 = tk.Button(root, text='2', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(2))
but_2.grid(row=6, column=1, sticky='nsew')
but_3 = tk.Button(root, text='3', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(3))
but_3.grid(row=6, column=2, sticky='nsew')
but_sub = tk.Button(root, text='-', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click('-'))
but_sub.grid(row=6, column=3, sticky='nsew')

but_convert = tk.Button(root, text='conv', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_converter(root, button_click, button_clear, button_delete))
but_convert.grid(row=7, column=0, sticky='nsew')
but_0 = tk.Button(root, text='0', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click(0))
but_0.grid(row=7, column=1, sticky='nsew')
but_fl = tk.Button(root, text=',', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click('.'))
but_fl.grid(row=7, column=2, sticky='nsew')
but_add = tk.Button(root, text='+', font=('Arial', '16'), bg='cyan', fg='black', bd='2', command=lambda: button_click('+'))
but_add.grid(row=7, column=3, sticky='nsew')

root.mainloop()
