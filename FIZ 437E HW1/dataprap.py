import cv2 as cv
import os
import random
import shutil
import numpy as np


source1 = "C:\FIZ 437E HW1\car"
destination1 = "C:\FIZ 437E HW1\car_labelled"

source2 = "C:/FIZ 437E HW1/aircraft"
destination2 = "C:/FIZ 437E HW1/aircraft_labelled"


image_number = 0
while image_number<500:   
    random_image=random.choice(os.listdir(source1))
    source_file = os.path.join(source1,random_image)
    #"shutil.move" function moves file from one directory to another
    shutil.move(source_file,destination1)
    image_number+=1
    
for f in os.listdir(destination1):
    filename=os.path.join(destination1,f)
    image = cv.imread(filename) 
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)      
    image = cv.resize(image, (100,100), interpolation = cv.INTER_AREA)
    image = cv.imwrite(filename,image)

image_number = 0
while image_number<500:   
    random_image=random.choice(os.listdir(source2))
    source_file = os.path.join(source2,random_image)
    #"shutil.move" function moves file from one directory to another
    shutil.move(source_file,destination2)
    image_number+=1
    
for f in os.listdir(destination2):
    filename=os.path.join(destination2,f)
    image = cv.imread(filename) 
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)      
    image = cv.resize(image, (100,100), interpolation = cv.INTER_AREA)
    image = cv.imwrite(filename,image)
    print (type(image))