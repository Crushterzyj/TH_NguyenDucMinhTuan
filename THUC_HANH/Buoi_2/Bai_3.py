import tkinter as tk
from tkinter import Label, Entry, Button
import numpy as np
from sympy import symbols, pi

def tinh_toan():
    loai_hinh = entry_loai_hinh.get()
    kich_thuoc = float(entry_kich_thuoc.get())

    if loai_hinh.lower() == 'hinh tron':
        dien_tich = np.pi * (kich_thuoc**2)
        chu_vi = 2 * np.pi * kich_thuoc
        label_ket_qua.config(text=f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")
    elif loai_hinh.lower() == 'hinh vuong':
        dien_tich = kich_thuoc**2
        chu_vi = 4 * kich_thuoc
        label_ket_qua.config(text=f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")
    elif loai_hinh.lower() == 'tam giac':
        dien_tich = 0.5 * kich_thuoc**2
        chu_vi = 3 * kich_thuoc
        label_ket_qua.config(text=f"Diện tích: {dien_tich:.2f}, Chu vi: {chu_vi:.2f}")
    else:
        label_ket_qua.config(text="Loại hình không hợp lệ")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hỗ trợ Học tập Hình học")

    label_loai_hinh = Label(root, text="Chọn loại hình:")
    label_loai_hinh.grid(row=0, column=0)

    entry_loai_hinh = Entry(root)
    entry_loai_hinh.grid(row=0, column=1)

    label_kich_thuoc = Label(root, text="Nhập kích thước:")
    label_kich_thuoc.grid(row=1, column=0)

    entry_kich_thuoc = Entry(root)
    entry_kich_thuoc.grid(row=1, column=1)

    button_tinh_toan = Button(root, text="Tính toán", command=tinh_toan)
    button_tinh_toan.grid(row=2, column=0, columnspan=2)

    label_ket_qua = Label(root, text="Kết quả:")
    label_ket_qua.grid(row=3, column=0, columnspan=2)

    root.mainloop()
