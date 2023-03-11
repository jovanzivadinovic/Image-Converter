from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import PIL.Image
import ctypes

class Bool:
    selected = FALSE

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
    Bool.selected = True
    
    dugme2.config(state="enabled")
    

    

    

def convert():
    
    try:
        root.img.save(filedialog.asksaveasfilename())
        Mbox('Successful', 'Uspesno konvertovanje', 0)
        text.config(text="")
        dugme2.config(state="disabled")
        
    
    except:
        Mbox('Error', 'Unesi ekstenziju idiote', 0)
        







naslov = tb.Label(root, text="Image Converter", font=("Helvetica", 30))
naslov.pack(pady=20)

dugme1 = tb.Button(root, text="Select Image", command=select)
dugme1.pack(pady=10)

dugme2 = tb.Button(root, text="Convert", command=convert)
dugme2.pack(pady=10)

text = tb.Label(root, text="", font=("Helvetica", 10))
text.pack(pady=20)

if Bool.selected == False:
    dugme2.config(state="disabled")
else:
    dugme2.config(state="enabled")









root.mainloop()