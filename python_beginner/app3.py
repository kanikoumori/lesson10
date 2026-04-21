word="こんにちは"+"元気ですか？"
print(word[1:3])
a="100"
b="こんにちは"
print(a+str(23))
print(int(a)+23)
print(a.isdigit())
print(b.isdigit())
if b.isdigit():
    print(int(b)+23)
else:
    print("数字じゃありません！！")
lunch=["カレー","寿司","天ぷら","ラーメン","焼肉","ビーフストロガノフ"]
print(lunch[5])
#tkinterをインポート
import tkinter as tk
#tkinterの中のmessageboxとsimpledialogをインポート
from tkinter import messagebox,simpledialog
#ウィンドウを作成する
root=tk.Tk()
#ウィンドウを表示しないようにする
root.withdraw()
if int(a)>= 80:
    print("合格")
else:
    print("やり直し")
#scoreにsimpledialog.askfloatで数値を入力する
score=simpledialog.askfloat("点数","あなたの点数は？")
if score >= 100:
    messagebox.showinfo("判定","満点です")
elif score >= 80:
    messagebox.showinfo("判定","合格です")
else:    messagebox.showinfo("判定","不合格です")
