from src.newfiles import DataHandler
from src.oldfiles import GLCM
import matplotlib.pyplot as plt
import os
import cv2
from sklearn.neighbors import KNeighborsClassifier


data = DataHandler.getDataFromSaved('PennFudan', maxFiles=100)
X, y = DataHandler.unzip(data)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)


# dataset = 'DaimlerMono'
# number = 101

dataset = 'PennFudan'
number = 104

testImgPath = f'{dataset}/Images/Grayscale/img{number}.png'
testOutputPath = f'{dataset}/Annotation/img{number}.txt'


testImg = cv2.imread(testImgPath)
testImgGS = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)

actual = int(DataHandler.readText(testOutputPath)[0][-1:])

testFeatures = GLCM.getFeatures(testImgGS)
prediction = classifier.predict([testFeatures])[0]

print('Prediction:', prediction)
print('Actual', actual)

plt.imshow(testImg)
plt.show()


