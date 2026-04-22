import tkinter as tk,PIL.Image as pi,PIL.ImageTk as pit
from tkinter import filedialog as fd
def dispPhoto(path):
    newImage=pi.open(path).resize((300,300))
    imageData=pit.PhotoImage(newImage)
    imageLabel.configure(image=imageData)
    imageLabel.image=imageData
def openFile():
    fpath=fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
root=tk.Tk()
root.geometry("400x350")
btn=tk.Button(text="ファイルを開く",command=openFile)
imageLabel=tk.Label(root)
btn.pack()
imageLabel.pack()
tk.mainloop()