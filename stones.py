import cv2
import math
import numpy as np
import classes.stoneimage as si
#import classes.handofstones as hos
import helpers
import glob


def getStoneImages(format):
    path = 'images\stones\*.jpg'
    files = glob.glob(path)
    images = []
    index = 0
    for f in files:
        image = cv2.imread(f,format)
        revImg = cv2.flip(image, -1)
        stoneImg = si.stoneImage(image,revImg,f,index)
        images.append(stoneImg)
        index = (index+1)
    print("StoneInitDone")
    return images

def addStoneToHand(stone):
    pass

def matchStone(img,stones):
    matchResult = si.stoneImage(np.zeros((5,5,3), dtype=np.uint8),np.zeros((5,5,3), dtype=np.uint8),"NoImage",-1)
    threshhold = .85
    matches = []
    for stone in stones:
        result = cv2.matchTemplate(img, stone.img, cv2.TM_CCOEFF_NORMED)
        min_val, max_val,min_loc, max_loc = cv2.minMaxLoc(result)
        matches.append(max_val)
        
    largest = max(matches)
    if (largest > 0.5):
        largestIndex = matches.index(largest)
        matchResult = stones[largestIndex]
    else:
        matches = []
        for stone2 in stones:
            result = cv2.matchTemplate(img, stone2.reverseImg, cv2.TM_CCOEFF_NORMED)
            min_val, max_val,min_loc, max_loc = cv2.minMaxLoc(result)
            matches.append(max_val)
        largest = max(matches)
        if (largest > 0.5):
            largestIndex = matches.index(largest)
            print(str(largest))
            matchResult = stones[largestIndex]
        else:
            print(str(largest))
    return matchResult


def getStone(img,approx):
    width = 160
    height = 100 
    approx = helpers.reorder(approx)
    pts1 = np.float32(approx)
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOut = cv2.warpPerspective(img, matrix, (width,height))
    return imgOut

def findStonesInImage(canny,image,stones):
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    rowIndex = -1
    columnIndex = -1
    lastX = -30
    hand = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        #cv2.drawContours(image,cnt,-1,(255,0,0),2)
        if(area>3000):
            # Large controur found

            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            objCor = len(approx)
            print(objCor) 
            x,y,w,h = cv2.boundingRect(approx)     
            if(objCor == 4):
                # Contour have 4 corners so most likely a stone

                imgStone = getStone(image,approx)
                correct = matchStone(imgStone,stones)
                #print(correct.name)
                if(correct.id != -1):
                    # Found a matching stone
                    print(correct.type + " " + correct.detail + " x:" + str(x) + " y:" + str(y))
                    if(x > lastX+30):
                        rowIndex = rowIndex+1
                        hand.append([])
                    
                    hand[rowIndex].append(correct) # Only a reference to a stone Image.. todo: Needs a new object to represent the stone with coordinates and such!
                    lastX = x

                    cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),1)                    
                else:
                    cv2.rectangle(image, (x,y),(x+w,y+h),(0,255,0),3)
                
                cv2.putText(image,str(correct.id) + " x:" + str(x) + " y:" + str(y),(x+3,y+30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0))
    return hand
