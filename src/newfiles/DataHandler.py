import os
import cv2
import ast

ROOT_DIR = os.path.abspath(os.curdir)

def fixData():
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
    # os.chdir('../../data/Training/DaimlerMono/Annotation')
    # for i in range(201):
    #     with open(f'img{i}', 'w') as f:
    #         n = 1
    #         if(i > 100):
    #             n = 0
    #         f.write(f'Number of people: {n}')

    # print(len(imgs))
    # print(imgs[0].shape)
    # plt.imshow(imgs[0])
    # plt.show()
    pass

def getTrainingData(name, grayscale=False, maxFiles=1000):
    os.chdir(f'../../data/Training/{name}')

    imgs = []
    vals = []
    count = 0
    os.chdir('Annotation')
    for file in os.listdir():
        line1 = readText(file)[0]
        val = int(line1[-1:])
        vals.append(val)
        count+=1
        if(count >= maxFiles):
            break
    if(grayscale):
        os.chdir('../Images/Grayscale')
    else:
        os.chdir('../Images/Normal')
    count = 0
    for file in os.listdir():
        if(grayscale):
            img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        else:
            img = cv2.imread(file)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgs.append(img)
        count += 1
        if (count >= maxFiles):
            break

    out = list(zip(imgs, vals))

    return out

def readText(filename):
    with open(filename, 'r') as f:
        return f.readlines()
def saveText(filename, lines):
    with open(filename, 'w') as f:
        f.writelines(lines)

def saveData(data):
    os.chdir('../../Data')
    for i in range(len(data)):
        lines = []
        lines.append('Features: '+ str(data[i][0]) + '\n')
        lines.append('Output: ' + str(data[i][1]))
        saveText(f'data{i}', lines)


def getDataFromSaved(name, maxFiles=1000, train_test_split = 0.6):
    os.chdir(f'../../data/Training/{name}/Data')
    features = []
    outputs = []
    count = 0
    for file in os.listdir():
        lines = readText(file)
        features.append(ast.literal_eval(lines[0][10:]))
        outputs.append(int(lines[1][7:]))
        count+=1
        if(count >= maxFiles):
            break

    os.chdir(f'../../')
    num_train = int(count*train_test_split)
    train_data = list(zip(features[:num_train], outputs[:num_train]))
    test_data = list(zip(features[num_train:], outputs[num_train:]))
    return (train_data, test_data)

def unzip(data):
    X = [d for d,o in data]
    y = [o for d,o in data]
    return (X,y)

# data = getDataFromSaved('PennFudan')
# data = getTrainingData('PennFudan',grayscale=True,maxFiles=1000)
# data = GLCM.getFeaturesFromData(data)
# saveData(data)