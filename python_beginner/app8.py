import sklearn.datasets,sklearn.svm,PIL.Image,numpy
def imagetodata(filename):
    grayImage=PIL.Image.open(filename).convert("L")
    grayImage=grayImage.resize((8,8),PIL.Image.Resampling.LANCZOS)
    numImage=numpy.asarray(grayImage,dtype=float)
    numImage=16-numpy.floor(17*numImage/256)
    numImage=numImage.flatten()
    return numImage

def predictdigits(data):
    digits=sklearn.datasets.load_digits()
    clf=sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data,digits.target)
    n=clf.predict([data])
    print("予測",n)
data=imagetodata("2.png")
predictdigits(data)
