import tensorflow as tf
import keras
import numpy as np
from keras.preprocessing.image import load_img,img_to_array



model = tf.keras.models.load_model("vgg16_nasu_fine.h5")
label=['kusanasu','nasu']
test="eggplant\\51be4adf00aa136a270e1ba2f9f97335.jpg"

def judge(images):
    temp_img=load_img(images,target_size=(224,224))
    #Images normalization
    temp_img_array=img_to_array(temp_img)
    temp_img_array=temp_img_array.astype('float32')/255.0
    temp_img_array=temp_img_array.reshape((1,224,224,3))
    #predict image
    img_pred=model.predict(temp_img_array)
    print(label[np.argmax(img_pred)])
judge(test)