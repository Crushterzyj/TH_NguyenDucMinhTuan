from tkinter import *


gui=Tk()
gui.geometry("400x350")
gui.title("May Tinh")


def on_button_click( value ):
    current_value = result_entry.get()

    if value == 'C':
        result_entry.delete(0, END)
    elif value == '⌫':  # Backspace button
        result_entry.delete(len(current_value) - 1, END)
    elif value == 'DH':
        pass
    elif value == 'TP':
        pass
    elif value == 'LIM':
        pass
    elif value == '=':

        result = eval(current_value)
        result_entry.delete(0, END)
        result_entry.insert(END, str(result))
    else:
        result_entry.insert(END, value)
result_entry =Entry(gui, width=20, font=('Arial', 14), bd=5, insertwidth=4, justify='right')
result_entry.grid(row=0, column=0, columnspan=4)

# Tạo các nút số và các nút toán tử
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),('x',1,4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),('y',2,4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),('**',3,4),
    ('0', 4, 1), ('C', 4, 0), ('⌫', 4, 2), ('+', 4, 3),('sprt(',4,4),
    ('DH',5,0),('TP',5,1),('LIM',5,2),('(',5,3),(')',5,4),('=', 7, 2)

]

for (text, row, column) in buttons:
    button = Button(gui, text=text, width=5, height=2,command=lambda t=text:on_button_click(t))
    button.grid(row=row+1, column=column+1, padx=5, pady=5)



gui.mainloop()