#print(1+1)
#print(5*10)
#print(20/5)
#print("あああ"+"いいい"+"aaa")
#print("あああ"*3)
#print('私は"おはよう"と言いました')
#name="あああああ"
#print("私の名前は"+name+"です")
#ランダムモジュールをインポート
import random as rrr
#おみくじに使うリストを作成
omikuzi=["大吉","中吉","小吉","末吉","凶","大凶"]
#ランダムモジュールを使いリストから一つ選んで表示
print("今日のあなたの運勢は"+rrr.choice(omikuzi)+"です")
#inputで数値を入力し、floatで文字型の数値を実数に変換して計算
h=float(input("あなたの身長を入力してください"))/100
w=float(input("あなたの体重を入力してください"))
#BMIを計算して変数bmiに代入
bmi=w/(h*h)
print("あなたのBMIは",bmi,"です")
#ライブラリを省略して使用できるようにインポート、名前がかぶったり何の機能を呼び出しているか混乱するので非推奨
from turtle import *
#上記のインポートの仕方により本来はturtle.shape()と書くところを省略
shape("turtle")
#色の名前のリストを作成
col=["orange","limegreen","gold","plum","tomato"]
#for文でインデントを開けたブロックを4回繰り返す
for i in range(5):
    #colorでリストの文字をペンや図形の色にしてiで順番に変更
    color(col[i])
    #前方に200ピクセル進む
    forward(200)
    #左に144度回る
    left(144)
for i in range(5):
    #ランダムに色を変更
    color(rrr.choice(col))
    #半径100の円を描く
    circle(100)
    left(72)
#終了後ウィンドウを閉じずに維持する
done()