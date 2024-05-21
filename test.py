print('Setting UP')
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from sklearn.model_selection import train_test_split
from utlis import *
import pandas as pd
print(pd.__version__)

#### STEP 1 - INITIALIZE DATA
path = 'Lane\\DataCollected'
data = importDataInfo(path)
print(data.head())


#### STEP 2 - VISUALIZE AND BALANCE DATA
#data = balanceData(data,display=True)

imagesPath, steerings = loadData(path,data)
print('No of Path Created for Images ',len(imagesPath),len(steerings))
cv2.imshow('Test Image',cv2.imread(imagesPath[2]))
cv2.waitKey(0)

#augmentation
#
# imgRe,st = augmentImage('Lane/DataCollected/IMG0/Image_1713686520057643.jpg',0.5)
# #mpimg.imsave('Result.jpg',imgRe)
# plt.imshow(imgRe)
# plt.show()


#preprocessing images
