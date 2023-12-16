import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

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

    # Thực hiện tách biên và hiển thị ảnh đã tách biên
    edges_image = detect_edges(file_path)
    edges_image.thumbnail((200, 200))
    photo_edges = ImageTk.PhotoImage(edges_image)
    label_edges.config(image=photo_edges)
    label_edges.image = photo_edges

def detect_edges(file_path):
    # Đọc ảnh từ đường dẫn
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # Thực hiện tách biên bằng phương pháp Canny
    edges = cv2.Canny(img, 100, 200)

    # Chuyển đổi từ mảng NumPy sang đối tượng Image
    edges_image = Image.fromarray(edges)

    return edges_image

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Chương trình Tách Biên Ảnh")

    label_path = tk.Label(root, text="Chọn ảnh:")
    label_path.grid(row=0, column=0, pady=10)

    entry_path = tk.Entry(root, state="disabled", width=40)
    entry_path.grid(row=1, column=0, padx=5)

    button_browse = tk.Button(root, text="Chọn ảnh", command=browse_image)
    button_browse.grid(row=1, column=1)

    label_original = tk.Label(root, text="Ảnh Gốc")
    label_original.grid(row=2, column=0, padx=200)

    label_edges = tk.Label(root, text="Ảnh Tách Biên")
    label_edges.grid(row=3, column=0, padx=200)

    root.mainloop()
