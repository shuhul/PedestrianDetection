from src.newfiles import DataHandler, GLCM
import matplotlib.pyplot as plt
import cv2
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import seaborn as sns
import numpy as np


name = 'DaimlerMono'
train_data, test_data = DataHandler.getDataFromSaved(name, maxFiles=200, train_test_split=0.8)
X, y = DataHandler.unzip(train_data)
Xt, yt = DataHandler.unzip(test_data)

classifier = KNeighborsClassifier(n_neighbors=5)
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
acc = round(accuracy_score(yt, yp)*100,3)
cf = confusion_matrix(yt, yp)

print(f'Accuracy: {acc}%')
# print(classification_report(yt, yp))

print(cf)

ax = sns.heatmap(cf/np.sum(cf), annot=True, fmt='.2%', cmap='Blues')

ax.set_title(f'Confusion Matrix on {name} (Accuracy = {acc}%)\n\n');
ax.set_xlabel('\nPredicted Values')
ax.set_ylabel('Actual Values ');

ax.xaxis.set_ticklabels(['0 Pedestrians','1 <= Pedestrians'])
ax.yaxis.set_ticklabels(['0 Pedestrians','1 <= Pedestrians'])

plt.show()