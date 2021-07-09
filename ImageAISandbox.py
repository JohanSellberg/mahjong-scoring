import cv2
import math
import numpy as np
import classes.stoneimage as si
import handofstones as hos
import helpers
import stones

from random import *


#format = cv2.IMREAD_GRAYSCALE
format = cv2.IMREAD_COLOR

images = stones.getStoneImages(format)

cannyMin = 150
cannyMax = 200

ThreshMin = 200
ThreshMax = 255

imgWidth = 1000
imgHeight = 750

def loadImage(imagePath):
    image = cv2.imread(imagePath,format)
    image = cv2.resize(image, (imgWidth,imgHeight))    
    #img = cv2.convertScaleAbs(img, 1, 1.2)
    return image

def getGrayImage(colImage):
    retImage = colImage.copy()
    if(format == cv2.IMREAD_COLOR):
        retImage = cv2.cvtColor(colImage,cv2.COLOR_BGR2GRAY)
    return retImage
    

img = loadImage('images/org6.jpg')
img_canny = cv2.Canny(img,cannyMin,cannyMax)
img_gray = getGrayImage(img)
_, img_bin = cv2.threshold(img_gray, ThreshMin, ThreshMax, cv2.THRESH_BINARY)

img2 = loadImage('images/org2.jpg')
img2_canny = cv2.Canny(img2,cannyMin,cannyMax)
img2_gray = getGrayImage(img2)
_, img2_bin = cv2.threshold(img2_gray, ThreshMin, ThreshMax, cv2.THRESH_BINARY)

img3 = loadImage('images/org7.jpg')
img3_canny = cv2.Canny(img3,cannyMin,cannyMax)
img3_gray = getGrayImage(img3)
_, img3_bin = cv2.threshold(img3_gray, ThreshMin, ThreshMax, cv2.THRESH_BINARY)

img4 = loadImage('images/org8.jpg')
img4_canny = cv2.Canny(img4,cannyMin,cannyMax)
img4_gray = getGrayImage(img4)
_, img4_bin = cv2.threshold(img4_gray, ThreshMin, ThreshMax, cv2.THRESH_BINARY)

img5 = loadImage('images/org5.jpg')
img5 = cv2.convertScaleAbs(img5, 1, 1.2)
img5_canny = cv2.Canny(img5,cannyMin,cannyMax)
img5_gray = getGrayImage(img5)
_, img5_bin = cv2.threshold(img5_gray, ThreshMin, ThreshMax, cv2.THRESH_BINARY)

img6 = loadImage('images/org9.jpg')
img6 = cv2.convertScaleAbs(img6, 1, 1.2)
img6_canny = cv2.Canny(img6,cannyMin,cannyMax)
img6_gray = getGrayImage(img6)
_, img6_bin = cv2.threshold(img6_gray, ThreshMin, ThreshMax, cv2.THRESH_BINARY)


print("Image1:")
hand = stones.findStonesInImage(img_bin,img,images)
print("Rows in hand:" + str(len(hand.stones)))
hand.print()

print("Image2:")
hand2 = stones.findStonesInImage(img2_bin,img2,images)
print("Rows in hand:" + str(len(hand2.stones)))
hand2.print()

print("Image3:")
hand3 = stones.findStonesInImage(img3_bin,img3,images)
print("Rows in hand:" + str(len(hand3.stones)))
hand3.print()

print("Image4:")
hand4 = stones.findStonesInImage(img4_bin,img4,images)
print("Rows in hand:" + str(len(hand4.stones)))
hand4.print()

print("Image5:")
hand5 = stones.findStonesInImage(img5_bin,img5,images)
print("Rows in hand:" + str(len(hand5.stones)))
hand5.print()

print("Image6:")
hand6 = stones.findStonesInImage(img6_bin,img6,images)
print("Rows in hand:" + str(len(hand6.stones)))
hand6.print()
#Syntax:
#1. För varje kontur:
#2.   Hitta den Sten som bäst matchar bilden genom att
#3.      Utifrån kontur göra en template match spara ner max resultat 

print("drawing images:")
cv2.imshow('result', img)
cv2.imshow('result2', img2)
cv2.imshow('result3', img3)
cv2.imshow('result4', img4)
cv2.imshow('result5', img5)
cv2.imshow('result6', img6)
#cv2.imshow('result7', img6_bin)

cv2.waitKey()
cv2.destroyAllWindows()