from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import PIL.Image
import ctypes


root = tb.Window(themename="solar")
root.geometry("1000x500")
root.iconbitmap("ikonica.ico")
root.title("Image Converter")

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)




def select():
    root.slika = filedialog.askopenfilename(title="Select an image")
    root.img = PIL.Image.open(root.slika)
    text.config(text="Image Selected")

    

    

def convert():
    
    try:
        root.img.save(filedialog.asksaveasfilename())
        Mbox('Successful', 'Uspesno konvertovanje', 0)
        text.config(text="")
        
    
    except:
        Mbox('Error', 'Unesi ekstenziju idiote', 0)






naslov = tb.Label(root, text="Image Converter", font=("Helvetica", 30))
naslov.pack(pady=20)

dugme = tb.Button(root, text="Select Image", command=select)
dugme.pack(pady=10)

dugme = tb.Button(root, text="Convert", command=convert)
dugme.pack(pady=10)

text = tb.Label(root, text="", font=("Helvetica", 10))
text.pack(pady=20)









root.mainloop()