import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageShow

def browse_image():
    file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        entry_path.config(state="normal")
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)
        entry_path.config(state="disabled")

        show_image(file_path)

def show_image(file_path):
    # Hiển thị ảnh gốc
    original_image = Image.open(file_path)
    original_image.thumbnail((200, 200))
    photo_original = ImageTk.PhotoImage(original_image)
    label_original.config(image=photo_original)
    label_original.image = photo_original

    # Hiển thị ảnh đã làm mịn
    smoothed_image = smooth_image_opencv(file_path)
    smoothed_image.thumbnail((200, 200))
    photo_smoothed = ImageTk.PhotoImage(smoothed_image)
    label_smoothed.config(image=photo_smoothed)
    label_smoothed.image = photo_smoothed

def smooth_image_opencv(file_path):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(file_path)

    # Áp dụng bộ lọc làm mịn
    smoothed_img = cv2.GaussianBlur(img, (15, 15), 0)

    # Chuyển đổi từ mảng NumPy sang đối tượng Image
    smoothed_image = Image.fromarray(cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2RGB))

    return smoothed_image

def open_original_image():
    original_image_path = entry_path.get()
    if original_image_path:
        original_image = Image.open(original_image_path)
        ImageShow.show(original_image)

def open_smoothed_image():
    smoothed_image_path = entry_path.get()
    if smoothed_image_path:
        smoothed_image = smooth_image_opencv(smoothed_image_path)
        ImageShow.show(smoothed_image)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ứng dụng Lọc Ảnh")

    label_path = tk.Label(root, text="Chọn ảnh:")
    label_path.grid(row=0, column=0, pady=10)

    entry_path = tk.Entry(root, state="disabled", width=40)
    entry_path.grid(row=0, column=1, padx=10)

    button_browse = tk.Button(root, text="Chọn ảnh", command=browse_image)
    button_browse.grid(row=0, column=2)

    button_smooth = tk.Button(root, text="Làm mịn ảnh", command=lambda: show_image(entry_path.get()))
    button_smooth.grid(row=1, column=0, columnspan=3, pady=10)

    label_original = tk.Label(root, text="Ảnh Gốc")
    label_original.grid(row=2, column=0, padx=10)

    label_smoothed = tk.Label(root, text="Ảnh Làm Mịn")
    label_smoothed.grid(row=2, column=2, padx=10)

    button_open_original = tk.Button(root, text="Xem ảnh gốc", command=open_original_image)
    button_open_original.grid(row=3, column=0, pady=5)

    button_open_smoothed = tk.Button(root, text="Xem ảnh làm mịn", command=open_smoothed_image)
    button_open_smoothed.grid(row=3, column=2, pady=5)

    root.mainloop()
