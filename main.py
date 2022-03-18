sssssss#Import Libraries
from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2 as cv
import os

#Read or Load data
img=cv.imread('1.png')
plt.imshow(img[:,:,::-1])

result=DeepFace.analyze(img)

plt.imshow(img[:,:,::-1])
plt.title("2k19-BSCS-347" + "\n" "Hello" +result["gender"])

#image Analyzer
print("Emotions:" ,result)
print("Angry:",+result['emotion']['angry'])
print("Disgust:",+result['emotion']['disgust'])
print("Fear:",+result['emotion']['fear'])
print("Happy:",+result['emotion']['happy'])
print("Sad:",+result['emotion']['sad'])
print("Surprise:",+result['emotion']['surprise'])
print("Neutral:",+result['emotion']['neutral'])
print("Age:",+result['age'])

plt.show()