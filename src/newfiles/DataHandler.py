import os
import cv2
import matplotlib.pyplot as plt

def getData():
    imgs = []
    anots = []
    os.chdir('../../data/PennFudan/')
    for file in os.listdir('Annotation'):
        with open('Annotation/' + file, 'r') as f:
            lines = f.readlines()
            name = lines[4][28:29]
            anots.append(name)
            # print(name)
            # image = cv2.imread(name)
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # image = cv2.resize(image, (256, 256), interpolation = cv2.INTER_AREA)
            # imgs.append(image)
    os.chdir('../../data/Training/Annotation')
    for i in range(len(anots)):
        with open(f'img{i}.txt', 'w') as f:
            f.write(f'Number of people: {anots[i]}')
    # plt.imshow(imgs[0])
    # plt.show()
    pass

def getTrainingDataGS():
    pass



getData()