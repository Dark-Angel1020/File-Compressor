import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import zipfile
import urllib.request

def compress_files():
    file_list = filedialog.askopenfilenames()
    if file_list:
        output_filename = filedialog.asksaveasfilename(defaultextension='.zip')
        if output_filename:
            label.config(image=animation[0])
            root.after(100, update_animation, 1)
            
            with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as z:
                for file in file_list:
                    z.write(file)
            response = messagebox.askyesno('Compression Done', 'Your files have been compressed. Do you want to compress more files?')
            if response:
                compress_files()
            else:
                root.destroy()
            
            # Stop the animation
            label.config(image=None)

def update_animation(i):
    label.config(image=animation[i])
    i = (i + 1) % len(animation)
    root.after(100, update_animation, i)

root = tk.Tk()
root.title('File Compression')
root.configure(bg='#ADD8E6')

heading = tk.Label(root, text='File Compressing', font=('Helvetica', 24), bg='#ADD8E6')
heading.pack(pady=20)



image_url = 'https://www.techadvisor.com/wp-content/uploads/2022/06/best_compression_zip_software.jpg?quality=50&strip=all'
with urllib.request.urlopen(image_url) as url:
    image = Image.open(url)
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

animation = []
for i in range(8):
    with urllib.request.urlopen(f'https://www.techadvisor.com/wp-content/uploads/2022/06/best_compression_zip_software.jpg?quality=50&strip=all') as url:
        image = Image.open(url)
    animation.append(ImageTk.PhotoImage(image))

button = tk.Button(root, text='Select files and compress', command=compress_files, font=('Helvetica', 16), bg='#90EE90')
button.pack(pady=20)

def on_enter(event):
    button['bg'] = '#00FF00'

def on_leave(event):
    button['bg'] = '#90EE90'

button.bind('<Enter>', on_enter)
button.bind('<Leave>', on_leave)

root.mainloop()
