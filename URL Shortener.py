from tkinter import *
import pyshorteners
from tkinter import ttk

# Set up the window
root = Tk()
root.title("URL Shortener")
root.geometry("480x150")
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

# Set up the labels and entry boxes
label_long_url = Label(root, text="Long URL:")
label_long_url.grid(column=0, row=0, padx=10, pady=10, sticky="w")
entry_long_url = Entry(root, width=50)
entry_long_url.grid(column=1, row=0, padx=10, pady=10)
label_short_url = Label(root, text="Short URL:")
label_short_url.grid(column=0, row=1, padx=10, pady=10, sticky="w")
entry_short_url = Entry(root, width=50)
entry_short_url.grid(column=1, row=1, padx=10, pady=10)

# Set up the function to shorten the URL
def shorten_url():
    long_url = entry_long_url.get()
    if long_url:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        entry_short_url.delete(0, END)
        entry_short_url.insert(0, short_url)

# Set up the button
button_shorten = Button(root, text="Shorten", command=shorten_url)
button_shorten.grid(column=1, row=2, padx=10, pady=10, sticky="e")

# Start the GUI
root.mainloop()
