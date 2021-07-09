import numpy as np
import classes.stoneimage as si


class handOfStones(object):
    stones = []

    def __init__(self,stones):
        self.stones = stones
   
    def print(self):
        rowindex = -1        
        for row in self.stones:
            rowindex = rowindex + 1
            stoneindex = -1
            for stone in row:
                stoneindex = stoneindex+1
                print("Row: " + str(rowindex) + ", index: " + str(stoneindex) + ", name: " + self.stones[rowindex][stoneindex].name)


