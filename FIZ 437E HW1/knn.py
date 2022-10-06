import numpy as np
import os 
import cv2 as cv
import math
#import matplotlib.pyplot as plt

source1 = "C:\FIZ 437E HW1\car"
destination1 = "C:\FIZ 437E HW1\car_labelled"

source2 = "C:/FIZ 437E HW1/aircraft"
destination2 = "C:/FIZ 437E HW1/aircraft_labelled"

airplane_vectors=[]
for f in os.listdir(destination2):
    filename=os.path.join(destination2,f)
    image = cv.imread(filename)
    numpydata = np.asarray(image)
    data = np.ravel(numpydata)
    airplane_vectors.append(data)
    image = cv.imwrite(filename,image)


car_vectors=[]
for f in os.listdir(destination1):
    filename=os.path.join(destination1,f)
    image = cv.imread(filename)
    numpydata = np.asarray(image)
    data = np.ravel(numpydata)
    car_vectors.append(data)
    image = cv.imwrite(filename,image)    


airplane_vectors_train=airplane_vectors[:450]
airplane_vectors_test=airplane_vectors[-50:]

car_vectors_train=car_vectors[:450]
car_vectors_test=car_vectors[-50:]

test=car_vectors_test+airplane_vectors_test
train=car_vectors+airplane_vectors

lenn=len(train[0])

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)


def find_distance(vector1,vector2):
    distances=np.zeros(len(vector2))
    for i in range(len(vector1)):
        for j  in range(len(vector2)):
            distance=euclidean_distance(vector1[i],vector2[j])
            distances[j]=distance
    return (distances)
    

def find_label(dists, k):
    num_test = dists.shape[0]
    pred = np.zeros(num_test)
    for i in range(num_test):
        closest = []
        closest = [np.argsort(dists[i])][0:k]
        pred[i] = np.bincount(closest).argmax()
    return pred


def accuracy(pred , test):
    count = 0
    for i in range(len(pred)):
        if pred[i] == test[i]:
            count +=1
            
    return print("Accuracy =", (count/len(pred))*100, "%")    

    


    
    
     
        