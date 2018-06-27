#! /usr/bin/python3

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import exifread as ef
import os, csv, time

window = tk.Tk()
window.title("GEO Extractor")
window.geometry("400x200")

def open_callback():
    folder = open_folder()
    files = os.listdir(open_folder())
    total_files = len(files)
    progress_bar = ttk.Progressbar(orient="horizontal",
                    length=int(total_files), mode="determinate")
    progress_bar.grid( row=2, column=1, sticky="nsew")
    progress_bar['value'] = 0
    filename = int(round(time.time() * 1000))
    i = 1
    for file in files:
        with open(folder+"/"+file, 'rb') as f:
            tags = ef.process_file(f)
            if "GPS GPSLatitude" in tags and "GPS GPSLongitude" in tags:
                lat = _convert_to_degress(tags.get('GPS GPSLatitude'))
                lon = _convert_to_degress(tags.get('GPS GPSLongitude'))
                coordinates = [lat, lon]
                with open(str(filename)+'.csv', 'a+') as gps_file:
                    wr = csv.writer(gps_file, quoting=csv.QUOTE_ALL)
                    wr.writerow(coordinates)
                    progress_bar['value'] = i
        i += 1

def open_folder():
    folder = tk.filedialog.askdirectory(title = "Select a folder")
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
