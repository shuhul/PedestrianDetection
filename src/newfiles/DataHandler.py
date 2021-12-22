import os
import cv2
import matplotlib.pyplot as plt

def getData():
    imgs = []
    # anots = []
    # os.chdir('../../data/DaimlerMono/ped_examples')
    # for file in os.listdir():
    #     image = cv2.imread(file)
    #
    #     image = cv2.resize(image, (256, 256), interpolation = cv2.INTER_CUBIC)
    #     imgs.append(image)
    #     # with open('ped_examples/' + file, 'r') as f:
    #     #     # lines = f.readlines()
    #     #     # name = lines[4][28:29]
    #     #     # anots.append(name)
    #     #     # print(name)
    #     #     image = cv2.imread(name)
    #     #     # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     #     image = cv2.resize(image, (256, 256), interpolation = cv2.INTER_AREA)
    #     #     imgs.append(image)
    # #
    # os.chdir('../../../data/Training/DaimlerMono/Images/Grayscale')
    # for i in range(len(imgs)):
    #     if((i%10) == 0):
    #         cv2.imwrite(f'img{int((i/10))}.png', imgs[i])


        # with open(f'img{i}.txt', 'w') as f:
        #     f.write(f'Number of people: {anots[i]}')
    os.chdir('../../data/Training/DaimlerMono/Annotation')
    for i in range(201):
        with open(f'img{i}', 'w') as f:
            n = 1
            if(i > 100):
                n = 0
            f.write(f'Number of people: {n}')

    # print(len(imgs))
    # print(imgs[0].shape)
    # plt.imshow(imgs[0])
    # plt.show()
    pass

def getTrainingDataGS():
    pass



getData()