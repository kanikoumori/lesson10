import sklearn.datasets,matplotlib.pyplot as plt
#変数digitsにsklean.datasetsにある機械学習用の
# データを取り出して代入
digits=sklearn.datasets.load_digits()
#digits.imagesにある画像データの数を数えて表示
print("データの個数=",len(digits.images))

print("画像データ=",digits.images[0])
print("何の数字か=",digits.target[0])
#以下のコードを50回繰り返す
for i in range(50):
    #5x10の盤面に順番に表示する
    plt.subplot(5,10,i+1)
    #数値データの周りにある枠を非表示
    plt.axis("off")
    #数値データのラベルをタイトルとして表示
    plt.title(digits.target[i])
    #digits.imagesにある画像をcmap="Greys"でグレースケール
    # に変えたものをimshowで表示
    plt.imshow(digits.images[i],cmap="Greys")
#作成したグラフ（図）を表示
plt.show()
print(digits.images.shape)
print(digits.target.shape)
from sklearn import svm

clf = svm.SVC()
clf.fit(digits.data, digits.target)

print(clf.predict([digits.data[0]]))