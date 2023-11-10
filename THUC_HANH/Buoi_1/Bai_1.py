from tkinter import *
from sympy import symbols

def create():
    gui_cacul=Toplevel(gui)
    num=int(equations.get())
    entries = [ ]
    variables = symbols(' '.join([ f'x{i + 1}' for i in range(num) ]))
    for i in range(num):
        for j,var in enumerate(variables):
            label=Label(gui_cacul,text=f"{var}")
            label.grid(row=i+2, column=j*2, padx=10, pady=5)

            entry=Entry(gui_cacul)
            entry.grid(row = i + 2, column = j * 2 + 1, padx = 10, pady = 5)
            entries.append(entry)


    result=Label(gui_cacul)





gui=Tk()
gui.geometry("200x200")
gui.title("Giai He Phuong Trinh")


Label(gui,text="Nhap so he phuong trinh").pack()
equations=Entry(gui)
equations.pack()

but_create=Button(gui,text="CREATE",command=create).pack()

gui.mainloop()