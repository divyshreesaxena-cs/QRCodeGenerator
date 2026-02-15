import qrcode
from qrcode.constants import ERROR_CORRECT_L
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = data_entry.get()
    file_name = file_entry.get()
    fill_color = fill_entry.get()
    back_color = back_entry.get()

    if not data or not file_name:
        messagebox.showerror("Error", "Data and file name are required!")
        return

    try:
        qr = qrcode.QRCode(
            version=None,
            error_correction=ERROR_CORRECT_L,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # Save image
        img.save(f"{file_name}.png")

        # Convert for Tkinter display
        img = img.resize((200, 200))
        tk_image = ImageTk.PhotoImage(img)

        qr_label.config(image=tk_image)
        qr_label.image = tk_image  # Prevent garbage collection

        messagebox.showinfo("Success", "QR Code generated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")


# Create window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x550")

tk.Label(root, text="Enter Text or URL:").pack(pady=5)
data_entry = tk.Entry(root, width=40)
data_entry.pack()

tk.Label(root, text="Enter File Name:").pack(pady=5)
file_entry = tk.Entry(root, width=40)
file_entry.pack()

tk.Label(root, text="QR Color (e.g., black):").pack(pady=5)
fill_entry = tk.Entry(root, width=40)
fill_entry.pack()
fill_entry.insert(0, "black")

tk.Label(root, text="Background Color (e.g., white):").pack(pady=5)
back_entry = tk.Entry(root, width=40)
back_entry.pack()
back_entry.insert(0, "white")

tk.Button(root, text="Generate QR Code", command=generate_qr).pack(pady=15)

# Label to display QR
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
