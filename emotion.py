from keras.models import Sequential,load_model


from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os

model = load_model("model.h5")

def emotion_analysis(emotions):
    objects = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    x_pos = list(range(len(objects)))
    temp=emotions.values()
    plt.bar(x_pos, temp, align='center')
    plt.xticks(x_pos, objects)
    plt.yticks(range(0, max(temp)+1),map(int, range(0, max(temp)+1)))
    plt.ylabel('number of people')
    plt.title('emotion')
    #print(emotions)
    #plt.show()
    plt.savefig("./temp/Emotion.png")

def analyze_image(file_path):
    global model
    img = image.load_img(file_path, color_mode = "grayscale", target_size=(48, 48))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x /= 255
    custom = model.predict(x)
    return custom[0]

def all_img():
    indices = {0:'angry', 1:'disgust',2:'fear',
               3:'happy',4:'sad',5:'surprise',6:'neutral'}
    stats = {'angry':0, 'disgust':0, 'fear':0, 'happy':0, 'sad':0, 'surprise':0, 'neutral':0}
    dirname = "C:\\xampp\\htdocs\\prakalpa\\temp\\"
    for the_file in os.listdir(dirname):
        file_path = os.path.join(dirname, the_file)
        if os.path.isfile(file_path) and ("extracted" in the_file):
            temp = list(analyze_image(file_path))
            stats[indices[temp.index(max(temp))]]+=1
    emotion_analysis(stats)
all_img()
