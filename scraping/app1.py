import requests
URL="https://www.ymori.com/books/python2nen/test1.html"
#URLにあるページのデータを取得する
response=requests.get(URL)
#response.apparent_encodingで表示する文字コードを自動変換
response.encoding=response.apparent_encoding
#上記で取得した文字データを表示
print(response.text)
#変数FileNameにDownLoad.txtと名前を付ける
FileName="DownLoad.txt"
#FileNameを書き込みモードで開き変数flにする"w"は書き込み"r"は読み込み"a"は追記
with open(FileName, "w", encoding="utf-8") as fl:
    #変数flに取得したデータを書き込む
    fl.write(response.text)

