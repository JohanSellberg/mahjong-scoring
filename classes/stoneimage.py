import numpy as np
import cv2

class stoneImage:
    img = np.zeros((5,5,3), dtype=np.uint8)
    reverseImg = np.zeros((5,5,3), dtype=np.uint8)
    name = ""
    path = ""
    type = ""
    detail = ""
    xpos = 0
    ypos = 0
    number = -1
    id = -1

    def setValue(self):
        if(self.id >= 0):
            filename = self.path.split("\\")[-1]
            self.name = filename.split(".")[0]
            if(self.name[-1].isdigit()):
                self.number = int(self.name[-1])
                self.type = self.name.rstrip("123456789")
                self.detail = str(self.number)
                print(self.type + " " + self.detail)
            else:
                self.type, self.detail = self.name.split("_")
                print(self.detail + " " + self.type)

    def __init__(self,img,reverseImg,path,id): 
          self.path = path
          self.reverseImg = cv2.resize(reverseImg, (159,99))
          self.img = cv2.resize(img, (159,99))
          self.id = id
          self.setValue()

    
        
        


