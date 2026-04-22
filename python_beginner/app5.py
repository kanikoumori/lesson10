import tkinter as tk,random as rd
#関数dispLabelの作成
def dispLabel():
    #リストkuziを作成
    kuzi=["大吉","中吉","小吉","凶","大凶"]
    #ラベルの文字をリストkuziの中からランダムに選んで変更
    lbl.configure(text=rd.choice(kuzi))
#ウィンドウの作成
root=tk.Tk()
#ウィンドウのサイズ
root.geometry("200x100")
#ラベルを作りラベルのテキストをLABELとする
lbl=tk.Label(text="LABEL")
#ボタンを作りボタンの名称をPUSHとしボタンを押すと関数dispLabelを呼び出し
btn=tk.Button(text="PUSH",command=dispLabel)
#ラベルを配置する
lbl.pack()
#ボタンを配置する
btn.pack()
#ウィンドウを表示したままにする
tk.mainloop()

