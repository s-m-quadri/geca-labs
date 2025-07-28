import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import filters

def select_image():
    global image_path, preview_label, preview_img
    image_path = filedialog.askopenfilename()
    if image_path:
        img = Image.open(image_path)
        img = img.resize((200, 200))
        preview_img = ImageTk.PhotoImage(img)
        preview_label.config(image=preview_img, text='')

root = tk.Tk()
root.title('Computer Vision')
root.geometry('600x400')

tk.Label(root, text='Computer Vision', font=('Arial', 16, 'bold')).pack()
tk.Label(root, text='GECA 2024-25', font=('Arial', 12)).pack()

frame = tk.Frame(root)
frame.pack()

task_frame = tk.Frame(frame)
task_frame.pack(side=tk.RIGHT, padx=20)

image_path = ''
preview_img = None
preview_label = tk.Label(frame, text='Preview', font=('Arial', 10))
preview_label.pack(side=tk.LEFT, padx=20)

tk.Button(task_frame, text='Select Image', command=select_image).pack()

tasks = [
    ('Show Image', filters.show_image),
    ('Histogram Equalization', filters.histogram_equalization),
    ('Non-linear Filtering', filters.non_linear_filtering),
    ('Apply 2D DFT', filters.apply_2d_dft),
    ('Apply 2D DCT', filters.apply_2d_dct),
    ('Edge Detection', filters.edge_detection),
    ('Line and Corner Detection', filters.line_and_corner_detection),
    ('Segmentation', filters.segmentation),
    ('SIFT Feature Extraction', filters.compute_sift_features)
]

for text, command in tasks:
    tk.Button(task_frame, text=text, command=lambda cmd=command: cmd(image_path)).pack()

root.mainloop()
