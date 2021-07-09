import numpy as np
import classes.stoneimage as si

class stone:
    stoneImage = si.stoneImage(np.zeros((5,5,3), dtype=np.uint8),np.zeros((5,5,3), dtype=np.uint8),"NoImage",-1)
    xloc = -1
    yloc = -1

    def __init__(self,stoneImg, x, y):
        self.stoneImage = stoneImg
        self.xloc = x
        self.yloc = y

class handOfStones(object):
    stones = []

    def __init__(self):
        self.stones = []
        

    def addStone(self,stoneImage,x,y):
        self.stones.append(stone(stoneImage,x,y))
        self.sortByXlocation()
   
    def sortByXlocation(self):
        self.stones.sort(key=lambda x: x.xloc, reverse=False)

    def print(self):
        #rowindex = -1        
        #for row in self.stones:
        #    rowindex = rowindex + 1
        #    stoneindex = -1
        #    for stone in row:
        #        stoneindex = stoneindex+1
        for stone in self.stones:
            print("X: " + str(stone.xloc) + ", Y: " + str(stone.yloc) + ", name: " + stone.stoneImage.name)


