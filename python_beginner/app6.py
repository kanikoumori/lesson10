import tkinter as tk,PIL.Image as pi,PIL.ImageTk as pit
from tkinter import filedialog as fd
def dispPhoto(path):
    #PIL.Image.openで変数pathに代入されている画像を開きconvert("L")で画像を白黒にしてresizeで縦横32ピクセルに変更しさらにもう一度resizeで縦横300ピクセルに変更する事でモザイク風の加工を再現し変数newImageに代入
    newImage=pi.open(path).convert("L").resize((32,32)).resize((300,300),resample=0)
    #newImageに代入した画像をtkinter上で開けるようにPIL.ImageTkで変換しimageDataに代入
    imageData=pit.PhotoImage(newImage)
    #imageLabel.configureでimageLabelの設定を変更し、画像設定（image）でimageDataに設定する
    imageLabel.configure(image=imageData)
    #ガベージコレクションにより関数が終了しても画像が消えないようにimageLabel上の変数imageに画像を代入
    imageLabel.image=imageData
def openFile():
    #filedialog.askopenfilenameで選択したファイルのパスをfpathに代入する
    fpath=fd.askopenfilename()
    #もし変数fpathにデータがあれば以下のコードを実行
    if fpath:
        #関数dispPhtoにfpathを与えて実行
        dispPhoto(fpath)
#ウィンドウを作成
root=tk.Tk()
#ウィンドウのサイズを400x350ピクセルに変更
root.geometry("400x350")
#ボタンを作成し名前をファイルを開くにして、ボタンを押したら関数openFileを実行
btn=tk.Button(text="ファイルを開く",command=openFile)
#root(作成したウィンドウ)の中にラベルを作り変数に代入
imageLabel=tk.Label(root)
#ボタンの配置
btn.pack()
#ラベルの配置
imageLabel.pack()
#ウィンドウを表示し続け、ユーザーの操作を待つ
tk.mainloop()