import tkinter as tk
from tkinter import ttk
import qrcode
from PIL import Image
def qr_code_generator():
    val = value.get()
    color_type = optiontype.get()
    if color_type == "Black on white":
        fill="black"
        back="white"
        code(val,fill,back)
    elif color_type == "Red on white":
        fill="red"
        back="white"
        code(val,fill,back)
    elif color_type == "Pink on white":
        fill="pink"
        back="white"
        code(val,fill,back)
    elif color_type == "Grey on white":
        fill="grey"
        back="white"
        code(val,fill,back)
    elif color_type == "Blue on white":
        fill="blue"
        back="white"
        code(val,fill,back)
    elif color_type == "Purple on white":
        fill="purple"
        back="white"
        code(val,fill,back)
def code(url,fill,back):
    filename="qr_code.png"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill, back_color=back)
    img.save(filename)
    result_label.config(text=f"QR Code generated and saved as {file_name}")
root = tk.Tk()
root.title("QR CODE GENERATOR")
label_type = ttk.Label(root, text="Choose color:")
label_type.grid(row=0,column=0)
types = ["Black on white", "Red on white","Pink on white","Grey on white","Blue on white","Purple on white"]
optiontype = ttk.Combobox(root, values=types)
optiontype.grid(row=0,column=1)
# For entering the value
label_value = ttk.Label(root, text="Enter URL:")
label_value.grid(row=2,column=0,padx=10,pady=10)
value = ttk.Entry(root)
value.grid(row=2,column=1,padx=10,pady=10)
generate_button = ttk.Button(root, text="Generate", command=qr_code_generator)
generate_button.grid(row=3,padx=10,pady=10)
result_label = ttk.Label(root, text="")
result_label.grid(row=4,padx=10,pady=10)
root.mainloop()
