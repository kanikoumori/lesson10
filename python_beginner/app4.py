for i in range(3):
    print(i)
list=[20,30,40,55,67,77]
for i in list:
    print(i)
total=0
for i in list:
    total=total+i
    print(total)
for i in range(10):
    for j in range(10):
        print(i,"×",j,"=",i*j)
def sayhello():
    print("hello")
sayhello()
def sayhello2(name):
    print("こんにちは"+name+"さん")
sayhello2("宮田")
import tax,tkinter as tk ,tax1,tax2
from tkinter import messagebox,simpledialog
root=tk.Tk()
root.withdraw()
print(f"税込み{tax.postTaxPrice(simpledialog.askfloat("価格","税抜き価格は？"))}円")
print(tax.postTaxPrice(100))
#上記二つのprint文だと100×1.1に対して答えが110.00000000000001になるのでintを使い修正
print(tax1.postTaxPrice(100))
#CatGptの回答ではお金の計算をする際にはDecimalを使う方がより実践的のようなのでテスト
print(f"税込み{tax2.postTaxPrice(simpledialog.askfloat("価格","税抜き価格は？"))}円")
