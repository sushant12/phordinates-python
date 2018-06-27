#! /usr/bin/python3

import tkinter as tk
from tkinter import filedialog
import exifread as ef

window = tk.Tk()
window.title("GEO Extractor")
window.geometry("400x200")

def open_callback():
    print(open_folder())

def open_folder():
    folder = tk.filedialog.askdirectory(initialdir = "/", title = "Select a folder")
    return folder

def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)


btn = tk.Button(window, text="Open Folder", command=open_callback)
btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


window.mainloop()
