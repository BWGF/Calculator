import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import basicFunc
import complexFunc
import converter

def handle_error(error_message):
    messagebox.showerror("Ошибка", error_message)

def calculate_basic():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        operation = operation_var.get()
        if operation == "+":
            result = basicFunc.add(x, y)
        elif operation == "-":
            result = basicFunc.subtract(x, y)
        elif operation == "*":
            result = basicFunc.multiply(x, y)
        elif operation == "/":
            result = basicFunc.divide(x, y)
        label_result.config(text=f"Результат: {result}")
    except ZeroDivisionError:
        handle_error("Деление на ноль.")
        return
    except ValueError:
        handle_error("Введите числовые значения.")

def calculate_logarithm():
    try:
        x = float(entry_log_x.get())
        base = float(entry_log_base.get())
        result = complexFunc.logarithm(x, base)
        if isinstance(result, str):
            handle_error(result)
        else:
            label_log_result.config(text=f"Результат: {result}")
    except ValueError:
        handle_error("Введите числовые значения.")

def calculate_factorial():
    try:
        x = int(entry_fact_x.get())
        result = complexFunc.factorial(x)
        if isinstance(result, str):
            handle_error(result)
        else:
            label_fact_result.config(text=f"Результат: {result}")
    except ValueError:
        handle_error("Введите целое неотрицательное число.")

def calculate_root():
    try:
        x = float(entry_root_x.get())
        n = int(entry_root_n.get())
        result = complexFunc.root(x, n)
        if isinstance(result, str):
            handle_error(result)
        else:
            label_root_result.config(text=f"Результат: {result}")
    except ValueError:
        handle_error("Введите числовые значения.")

def calculate_trigonometry():
    try:
        x = float(entry_trig_x.get())
        func = trig_func_var.get()
        if func == "sin":
            result = complexFunc.sine(x)
        elif func == "cos":
            result = complexFunc.cosine(x)
        elif func == "tan":
            result = complexFunc.tangent(x)
        elif func == "cot":
            result = complexFunc.cotangent(x)
        if isinstance(result, str):
            handle_error(result)
        else:
            label_trig_result.config(text=f"Результат: {result}")
    except ValueError:
        handle_error("Введите числовое значение.")

def calculate_percentage():
    try:
        x = float(entry_percent_x.get())
        y = entry_percent_y.get()
        if y.strip() == "":
            result = basicFunc.percentage(x)
        else:
            y = float(y)
            result = basicFunc.percentage(x, y)
        label_percent_result.config(text=f"Результат: {result}")
    except ValueError:
        handle_error("Введите числовые значения.")

def convert_time():
    try:
        value = float(entry_time_value.get())
        unit_from = time_unit_from_var.get()
        unit_to = time_unit_to_var.get()
        result = converter.convert_time(value, unit_from, unit_to)
        label_time_result.config(text=f"Результат: {result}")
    except ValueError as e:
        handle_error(str(e))

def convert_currency():
    try:
        value = float(entry_currency_value.get())
        currency_from = currency_from_var.get()
        currency_to = currency_to_var.get()
        result = converter.convert_currency(value, currency_from, currency_to)
        label_currency_result.config(text=f"Результат: {result}")
    except ValueError as e:
        handle_error(str(e))

root = tk.Tk()
root.title("Математический калькулятор")
root.geometry("600x400")

tab_control = ttk.Notebook(root)

tab_basic = tk.Frame(tab_control)
tab_control.add(tab_basic, text="Базовые операции")

label_x = tk.Label(tab_basic, text="Число X:")
label_x.grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(tab_basic)
entry_x.grid(row=0, column=1, padx=10, pady=5)

label_y = tk.Label(tab_basic, text="Число Y:")
label_y.grid(row=1, column=0, padx=10, pady=5)
entry_y = tk.Entry(tab_basic)
entry_y.grid(row=1, column=1, padx=10, pady=5)

operation_var = tk.StringVar(value="+")
operations = ["+", "-", "*", "/"]
operation_menu = tk.OptionMenu(tab_basic, operation_var, *operations)
operation_menu.grid(row=2, column=0, padx=10, pady=5)

btn_calculate_basic = tk.Button(tab_basic, text="Вычислить", command=calculate_basic)
btn_calculate_basic.grid(row=2, column=1, padx=10, pady=5)

label_result = tk.Label(tab_basic, text="Результат:")
label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

tab_complex = tk.Frame(tab_control)
tab_control.add(tab_complex, text="Сложные операции")

complex_operation_var = tk.StringVar(value="Логарифм")
complex_operations = ["Логарифм", "Факториал", "Корень", "Тригонометрия", "Проценты"]
complex_operation_menu = tk.OptionMenu(tab_complex, complex_operation_var, *complex_operations)
complex_operation_menu.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

def on_complex_operation_change(*args):
    operation = complex_operation_var.get()
    for widget in tab_complex.winfo_children():
        if widget not in [complex_operation_menu]:
            widget.grid_forget()

    if operation == "Логарифм":
        label_log_x = tk.Label(tab_complex, text="Число:")
        label_log_x.grid(row=1, column=0, padx=10, pady=5)
        global entry_log_x
        entry_log_x = tk.Entry(tab_complex)
        entry_log_x.grid(row=1, column=1, padx=10, pady=5)

        label_log_base = tk.Label(tab_complex, text="Основание:")
        label_log_base.grid(row=2, column=0, padx=10, pady=5)
        global entry_log_base
        entry_log_base = tk.Entry(tab_complex)
        entry_log_base.grid(row=2, column=1, padx=10, pady=5)

        btn_calculate_log = tk.Button(tab_complex, text="Вычислить логарифм", command=calculate_logarithm)
        btn_calculate_log.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        global label_log_result
        label_log_result = tk.Label(tab_complex, text="Результат:")
        label_log_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    elif operation == "Факториал":
        label_fact_x = tk.Label(tab_complex, text="Число:")
        label_fact_x.grid(row=1, column=0, padx=10, pady=5)
        global entry_fact_x
        entry_fact_x = tk.Entry(tab_complex)
        entry_fact_x.grid(row=1, column=1, padx=10, pady=5)

        btn_calculate_fact = tk.Button(tab_complex, text="Вычислить факториал", command=calculate_factorial)
        btn_calculate_fact.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

        global label_fact_result
        label_fact_result = tk.Label(tab_complex, text="Результат:")
        label_fact_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    elif operation == "Корень":
        label_root_x = tk.Label(tab_complex, text="Число:")
        label_root_x.grid(row=1, column=0, padx=10, pady=5)
        global entry_root_x
        entry_root_x = tk.Entry(tab_complex)
        entry_root_x.grid(row=1, column=1, padx=10, pady=5)

        label_root_n = tk.Label(tab_complex, text="Степень:")
        label_root_n.grid(row=2, column=0, padx=10, pady=5)
        global entry_root_n
        entry_root_n = tk.Entry(tab_complex)
        entry_root_n.grid(row=2, column=1, padx=10, pady=5)

        btn_calculate_root = tk.Button(tab_complex, text="Вычислить корень", command=calculate_root)
        btn_calculate_root.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        global label_root_result
        label_root_result = tk.Label(tab_complex, text="Результат:")
        label_root_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

    elif operation == "Тригонометрия":
        label_trig_x = tk.Label(tab_complex, text="Угол (в радианах):")
        label_trig_x.grid(row=1, column=0, padx=10, pady=5)
        global entry_trig_x
        entry_trig_x = tk.Entry(tab_complex)
        entry_trig_x.grid(row=1, column=1, padx=10, pady=5)

        global trig_func_var
        trig_func_var = tk.StringVar(value="sin")
        trig_functions = ["sin", "cos", "tan", "cot"]
        trig_menu = tk.OptionMenu(tab_complex, trig_func_var, *trig_functions)
        trig_menu.grid(row=2, column=0, padx=10, pady=5)

        btn_calculate_trig = tk.Button(tab_complex, text="Вычислить", command=calculate_trigonometry)
        btn_calculate_trig.grid(row=2, column=1, padx=10, pady=5)

        global label_trig_result
        label_trig_result = tk.Label(tab_complex, text="Результат:")
        label_trig_result.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

    elif operation == "Проценты":
        label_percent_x = tk.Label(tab_complex, text="Число:")
        label_percent_x.grid(row=1, column=0, padx=10, pady=5)
        global entry_percent_x
        entry_percent_x = tk.Entry(tab_complex)
        entry_percent_x.grid(row=1, column=1, padx=10, pady=5)

        label_percent_y = tk.Label(tab_complex, text="Процент (пусто для 1%):")
        label_percent_y.grid(row=2, column=0, padx=10, pady=5)
        global entry_percent_y
        entry_percent_y = tk.Entry(tab_complex)
        entry_percent_y.grid(row=2, column=1, padx=10, pady=5)

        btn_calculate_percent = tk.Button(tab_complex, text="Вычислить процент", command=calculate_percentage)
        btn_calculate_percent.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        global label_percent_result
        label_percent_result = tk.Label(tab_complex, text="Результат:")
        label_percent_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

complex_operation_var.trace("w", on_complex_operation_change)
on_complex_operation_change()

tab_converter = tk.Frame(tab_control)
tab_control.add(tab_converter, text="Конвертер")

label_time_value = tk.Label(tab_converter, text="Значение:")
label_time_value.grid(row=0, column=0, padx=10, pady=5)
entry_time_value = tk.Entry(tab_converter)
entry_time_value.grid(row=0, column=1, padx=10, pady=5)

time_units = ["секунды", "минуты", "часы", "дни", "месяцы", "годы"]
time_unit_from_var = tk.StringVar(value=time_units[0])
time_unit_to_var = tk.StringVar(value=time_units[1])

label_time_from = tk.Label(tab_converter, text="Из:")
label_time_from.grid(row=1, column=0, padx=10, pady=5)
time_from_menu = tk.OptionMenu(tab_converter, time_unit_from_var, *time_units)
time_from_menu.grid(row=1, column=1, padx=10, pady=5)

label_time_to = tk.Label(tab_converter, text="В:")
label_time_to.grid(row=2, column=0, padx=10, pady=5)
time_to_menu = tk.OptionMenu(tab_converter, time_unit_to_var, *time_units)
time_to_menu.grid(row=2, column=1, padx=10, pady=5)

btn_convert_time = tk.Button(tab_converter, text="Конвертировать время", command=convert_time)
btn_convert_time.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

label_time_result = tk.Label(tab_converter, text="Результат:")
label_time_result.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

label_currency_value = tk.Label(tab_converter, text="Сумма:")
label_currency_value.grid(row=5, column=0, padx=10, pady=5)
entry_currency_value = tk.Entry(tab_converter)
entry_currency_value.grid(row=5, column=1, padx=10, pady=5)

currencies = ["рубль", "доллар", "евро"]
currency_from_var = tk.StringVar(value=currencies[0])
currency_to_var = tk.StringVar(value=currencies[1])

label_currency_from = tk.Label(tab_converter, text="Из:")
label_currency_from.grid(row=6, column=0, padx=10, pady=5)
currency_from_menu = tk.OptionMenu(tab_converter, currency_from_var, *currencies)
currency_from_menu.grid(row=6, column=1, padx=10, pady=5)

label_currency_to = tk.Label(tab_converter, text="В:")
label_currency_to.grid(row=7, column=0, padx=10, pady=5)
currency_to_menu = tk.OptionMenu(tab_converter, currency_to_var, *currencies)
currency_to_menu.grid(row=7, column=1, padx=10, pady=5)

btn_convert_currency = tk.Button(tab_converter, text="Конвертировать валюту", command=convert_currency)
btn_convert_currency.grid(row=8, column=0, columnspan=2, padx=10, pady=5)

label_currency_result = tk.Label(tab_converter, text="Результат:")
label_currency_result.grid(row=9, column=0, columnspan=2, padx=10, pady=5)

tab_control.pack(expand=1, fill="both")

root.mainloop()