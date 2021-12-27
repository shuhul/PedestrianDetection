from src.newfiles import DataHandler, GLCM
import matplotlib.pyplot as plt
import cv2
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix


train_data, test_data = DataHandler.getDataFromSaved('PennFudan', maxFiles=100, train_test_split=0.8)
X, y = DataHandler.unzip(train_data)
Xt, yt = DataHandler.unzip(test_data)

classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(X, y)


# dataset = 'DaimlerMono'
# number = 101
#
# dataset = 'PennFudan'
# number = 104
#
# testImgPath = f'{dataset}/Images/Grayscale/img{number}.png'
# testOutputPath = f'{dataset}/Annotation/img{number}.txt'
#
#
# testImg = cv2.imread(testImgPath)
# testImgGS = cv2.cvtColor(testImg, cv2.COLOR_BGR2GRAY)
#
# actual = int(DataHandler.readText(testOutputPath)[0][-1:])

# testFeatures = GLCM.getFeatures(testImgGS)
# prediction = classifier.predict([testFeatures])[0]
#
# print('Prediction:', prediction)
# print('Actual', actual)
#
# plt.imshow(testImg)
# plt.show()

yp = classifier.predict(Xt)

print(accuracy_score(yt, yp))
# print(classification_report(yt, yp))
# print(confusion_matrix(yt, yp))