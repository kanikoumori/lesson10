import sklearn.datasets,sklearn.svm,PIL.Image,numpy
import tkinter as tk,PIL.ImageTk
from tkinter import filedialog as fd

def imagetodata(filename):
    grayImage=PIL.Image.open(filename).convert("L")
    grayImage=grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
    numImage=numpy.asarray(grayImage,dtype=float)
    numImage=16-numpy.floor(17*numImage/256)
    numImage=numImage.flatten()
    predictdigits(numImage)

def predictdigits(data):
    digits=sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data,digits.target)
    n=clf.predict([data])
    txlbl.configure(text=f"上の画像は数字の{n[0]}です")

def openfile():
    numfile=fd.askopenfilename()
    if numfile:
        numimg=PIL.Image.open(numfile)
        numimg=numimg.resize((200,120))
        tkimg=PIL.ImageTk.PhotoImage(numimg)
        imglbl.configure(image=tkimg)
        imglbl.image=tkimg
        imagetodata(numfile)

root=tk.Tk()
root.geometry("400x350")
btn=tk.Button(text="画像を開く",command=(openfile))
imglbl=tk.Label(root)
txlbl=tk.Label(text="予測")
btn.pack()
imglbl.pack()
txlbl.pack()
tk.mainloop()
