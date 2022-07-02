import keras
from keras.preprocessing import image
import numpy as np
from PIL import Image
import tensorflow as tf
import cv2

model = keras.models.load_model('RecycleModel.h5')

labels_dict={0:'glass', 1:'paper', 2:'plastic'}
image_path = "Data/test/glass/glass614.jpg"
test_image = image.load_img(image_path, target_size = (224,224)) 



#test_image.show()
img = cv2.imread(image_path)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image,axis = 0)
result = model.predict(test_image)
label = np.argmax(result, axis=1)[0]

cv2.putText(img, labels_dict[label], (0, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,255), 3)
while (1):
    cv2.imshow("RECYCLE", img)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
        