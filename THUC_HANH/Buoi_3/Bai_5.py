import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, filedialog, Entry, StringVar


def nhap_du_lieu( entry_var ):
    # Hàm nhập dữ liệu từ Entry
    du_lieu = entry_var.get()

    try:
        # Chuyển đổi dữ liệu thành mảng NumPy
        du_lieu_arr = np.fromstring(du_lieu, sep = ' ')
        return du_lieu_arr
    except ValueError:
        # Xử lý lỗi khi chuyển đổi dữ liệu không thành công
        return None


def xu_ly_tin_hieu( data ):
    # Hàm thực hiện xử lý tín hiệu số
    if data is not None:
        # Ví dụ: xử lý tín hiệu bằng cách lấy giá trị tuyệt đối
        processed_data = np.abs(data)
        return processed_data
    return None


def ve_do_thi( data ):
    # Hàm vẽ đồ thị kết quả
    if data is not None:
        plt.plot(data)
        plt.title('Kết quả Xử lý Tín hiệu')
        plt.xlabel('Thời gian')
        plt.ylabel('Biến độ Tín hiệu')
        plt.show()


def nhap_du_lieu_tu_entry( entry_var ):
    # Hàm chạy khi nhấn nút "Nhập dữ liệu"
    du_lieu = nhap_du_lieu(entry_var)
    du_lieu_xu_ly = xu_ly_tin_hieu(du_lieu)
    ve_do_thi(du_lieu_xu_ly)


if __name__ == "__main__":
    # Tạo cửa sổ Tkinter
    root = Tk()
    root.title("Ứng dụng Xử lý Tín hiệu số")

    # Biến lưu trữ dữ liệu từ Entry
    entry_var = StringVar()

    # Widget Entry
    entry_label = Label(root, text = "Nhập dữ liệu (cách nhau bằng khoảng trắng):")
    entry_label.pack()

    entry = Entry(root, textvariable = entry_var)
    entry.pack()

    # Nút Nhập dữ liệu
    submit_button = Button(root, text = "Nhập dữ liệu", command = lambda: nhap_du_lieu_tu_entry(entry_var))
    submit_button.pack()

    root.mainloop()
