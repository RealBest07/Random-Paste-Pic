from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from randomui import Ui_MainWindow
from PIL import Image, ImageDraw, ImageFilter
import sys
from datetime import *
import pyqtgraph as pg
import numpy as np
import os
import sys
import random
import shutil
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

class ranptaste(Ui_MainWindow):
    def __init__(self) -> None:
        super().setupUi(MainWindow)
        self.gcn()
        self.minim1x = 0
        self.minim1y = 0
        self.minim2x = 0
        self.minim2y = 0
        self.i=0

    def gcn(self):
        self.browsebt1.clicked.connect(self.browsclickex1)
        self.browsebt2.clicked.connect(self.browsclickex2)
        self.browsebt3.clicked.connect(self.browsclickex3)
        self.browsebt4.clicked.connect(self.browsclickex4)
        self.changebt1.clicked.connect(self.change1)
        self.changebt2.clicked.connect(self.change2)
        self.changebt3.clicked.connect(self.change3)
        self.randombt1.clicked.connect(self.generatefnc)
        self.savebt1.clicked.connect(self.saveim)

    def saveim(self):
        if self.i >= 0:   
            self.imbg.save(self.file_pathex4+'\\'+'image'+str(self.i)+'.jpg')
        self.i = self.i + 1   
        
        
    def generatefnc(self):
        self.imbgori = Image.open(self.file_pathex1+'\\'+self.ranpic1)
        self.imbg =  self.imbgori.copy()
        self.ranpo1x = random.randrange(self.minim1x,self.maxim1x)
        self.ranpo1y = random.randrange(self.minim1y,self.maxim1y)
        self.ranpo2x = random.randrange(self.minim1x,self.maxim1x)
        self.ranpo2y = random.randrange(self.minim1y,self.maxim1y)
        self.ranpo3x = random.randrange(self.minim1x,self.maxim1x)
        self.ranpo3y = random.randrange(self.minim1y,self.maxim1y)
        self.ranpo4x = random.randrange(self.minim1x,self.maxim1x)
        self.ranpo4y = random.randrange(self.minim1y,self.maxim1y)
        self.ranpo5x = random.randrange(self.minim1x,self.maxim1x)
        self.ranpo5y = random.randrange(self.minim1y,self.maxim1y)
        self.ranpo6x = random.randrange(self.minim1x,self.maxim1x)
        self.ranpo6y = random.randrange(self.minim1y,self.maxim1y)
        self.imbg.paste(self.imcrop1,(self.ranpo1x, self.ranpo1y), self.mask_crop1)
        self.imbg.paste(self.imcrop2,(self.ranpo2x, self.ranpo2y), self.mask_crop2)   
        self.imbg.paste(self.imweed1,(self.ranpo3x, self.ranpo3y), self.mask_weed1)
        self.imbg.paste(self.imweed2,(self.ranpo4x, self.ranpo4y), self.mask_weed2)   
        self.imbg.paste(self.imweed3,(self.ranpo5x, self.ranpo5y), self.mask_weed3)
        self.imbg.paste(self.imweed4,(self.ranpo6x, self.ranpo6y), self.mask_weed4) 
        self.imbg.save(self.file_pathex4+'\\'+'image'+'.jpg')
        self.pixmap8=QPixmap(self.file_pathex4+'\\'+'image'+'.jpg')
        self.img8.setScaledContents(True)
        self.img8.setPixmap(self.pixmap8)
        os.remove(self.file_pathex4+'\\'+'image'+'.jpg')
        


    def change1(self):
        if len(self.listpic1)>0:
            self.ranpic1=random.choice(self.listpic1)
            self.pixmap1=QPixmap(self.file_pathex1+'\\'+self.ranpic1)
            self.img1.setScaledContents(True)
            self.img1.setPixmap(self.pixmap1)
            self.imbgori = Image.open(self.file_pathex1+'\\'+self.ranpic1)
            self.imbg =  self.imbgori.copy()
            self.maxim1x = self.imbg.size[0]
            self.maxim1y = self.imbg.size[1]
            self.ranpo1x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo1y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo2x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo2y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo3x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo3y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo4x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo4y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo5x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo5y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo6x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo6y = random.randrange(self.minim1y,self.maxim1y)

    def change2(self):
        if len(self.listpic2)>0:
            self.ranpic2=random.choice(self.listpic2)
            self.pixmap2=QPixmap(self.file_pathex2+'\\'+self.ranpic2)
            self.img2.setScaledContents(True)
            self.img2.setPixmap(self.pixmap2)
            self.imcrop1 =  Image.open(self.file_pathex2+'\\'+self.ranpic2)
            self.mask_crop1 = Image.open(self.file_pathex2+'\\'+self.ranpic2).convert('L')
            


            self.ranpic3=random.choice(self.listpic2)
            self.pixmap3=QPixmap(self.file_pathex2+'\\'+self.ranpic3)
            self.img3.setScaledContents(True)
            self.img3.setPixmap(self.pixmap3)
            self.imcrop2 =  Image.open(self.file_pathex2+'\\'+self.ranpic3)
            self.mask_crop2 = Image.open(self.file_pathex2+'\\'+self.ranpic3).convert('L')
            

    def change3(self):
        if len(self.listpic3)>0:
            self.ranpic4=random.choice(self.listpic3)
            self.pixmap4=QPixmap(self.file_pathex3+'\\'+self.ranpic4)
            self.img4.setScaledContents(True)
            self.img4.setPixmap(self.pixmap4)
            self.imweed1 =  Image.open(self.file_pathex3+'\\'+self.ranpic4)
            self.mask_weed1 = Image.open(self.file_pathex3+'\\'+self.ranpic4).convert('L')

            self.ranpic5=random.choice(self.listpic3)
            self.pixmap5=QPixmap(self.file_pathex3+'\\'+self.ranpic5)
            self.img5.setScaledContents(True)
            self.img5.setPixmap(self.pixmap5)
            self.imweed2 =  Image.open(self.file_pathex3+'\\'+self.ranpic5)
            self.mask_weed2 = Image.open(self.file_pathex3+'\\'+self.ranpic5).convert('L')

            self.ranpic6=random.choice(self.listpic3)
            self.pixmap6=QPixmap(self.file_pathex3+'\\'+self.ranpic6)
            self.img6.setScaledContents(True)
            self.img6.setPixmap(self.pixmap6)
            self.imweed3 =  Image.open(self.file_pathex3+'\\'+self.ranpic6)
            self.mask_weed3 = Image.open(self.file_pathex3+'\\'+self.ranpic6).convert('L')

            self.ranpic7=random.choice(self.listpic3)
            self.pixmap7=QPixmap(self.file_pathex3+'\\'+self.ranpic7)
            self.img7.setScaledContents(True)
            self.img7.setPixmap(self.pixmap7)
            self.imweed4 =  Image.open(self.file_pathex3+'\\'+self.ranpic7)
            self.mask_weed4 = Image.open(self.file_pathex3+'\\'+self.ranpic7).convert('L')
        
    def browsclickex1(self):
        dialog=QFileDialog()
        self.file_pathex1=dialog.getExistingDirectory(None,"Select Folder")
        print(self.file_pathex1)
        self.browse1.setText(self.file_pathex1)
        self.listpic1=os.listdir(self.file_pathex1)
        if len(self.listpic1)>0:
            self.ranpic1=random.choice(self.listpic1)
            self.pixmap1=QPixmap(self.file_pathex1+'\\'+self.ranpic1)
            self.img1.setScaledContents(True)
            self.img1.setPixmap(self.pixmap1)
            # print(self.ranpic1)
            self.imbg =  Image.open(self.file_pathex1+'\\'+self.ranpic1)
            self.maxim1x = self.imbg.size[0]
            self.maxim1y = self.imbg.size[1]
            self.ranpo1x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo1y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo2x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo2y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo3x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo3y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo4x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo4y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo5x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo5y = random.randrange(self.minim1y,self.maxim1y)
            self.ranpo6x = random.randrange(self.minim1x,self.maxim1x)
            self.ranpo6y = random.randrange(self.minim1y,self.maxim1y)
            
    
    def browsclickex2(self):
        dialog2=QFileDialog()
        self.file_pathex2=dialog2.getExistingDirectory(None,"Select Folder")
        print(self.file_pathex2)
        self.browse2.setText(self.file_pathex2)
        self.listpic2=os.listdir(self.file_pathex2)
        if len(self.listpic2)>0:
            self.ranpic2=random.choice(self.listpic2)
            self.pixmap2=QPixmap(self.file_pathex2+'\\'+self.ranpic2)
            self.img2.setScaledContents(True)
            self.img2.setPixmap(self.pixmap2)
            self.imcrop1 =  Image.open(self.file_pathex2+'\\'+self.ranpic2)
            self.mask_crop1 = Image.open(self.file_pathex2+'\\'+self.ranpic2).convert('L')

            self.ranpic3=random.choice(self.listpic2)
            self.pixmap3=QPixmap(self.file_pathex2+'\\'+self.ranpic3)
            self.img3.setScaledContents(True)
            self.img3.setPixmap(self.pixmap3)
            self.imcrop2 =  Image.open(self.file_pathex2+'\\'+self.ranpic3)
            self.mask_crop2 = Image.open(self.file_pathex2+'\\'+self.ranpic3).convert('L')


    def browsclickex3(self):
        dialog3=QFileDialog()
        self.file_pathex3=dialog3.getExistingDirectory(None,"Select Folder")
        print(self.file_pathex3)
        self.browse3.setText(self.file_pathex3)
        self.listpic3=os.listdir(self.file_pathex3)
        if len(self.listpic3)>0:
            self.ranpic4=random.choice(self.listpic3)
            self.pixmap4=QPixmap(self.file_pathex3+'\\'+self.ranpic4)
            self.img4.setScaledContents(True)
            self.img4.setPixmap(self.pixmap4)
            self.imweed1 =  Image.open(self.file_pathex3+'\\'+self.ranpic4)
            self.mask_weed1 = Image.open(self.file_pathex3+'\\'+self.ranpic4).convert('L')

            self.ranpic5=random.choice(self.listpic3)
            self.pixmap5=QPixmap(self.file_pathex3+'\\'+self.ranpic5)
            self.img5.setScaledContents(True)
            self.img5.setPixmap(self.pixmap5)
            self.imweed2 =  Image.open(self.file_pathex3+'\\'+self.ranpic5)
            self.mask_weed2 = Image.open(self.file_pathex3+'\\'+self.ranpic5).convert('L')

            self.ranpic6=random.choice(self.listpic3)
            self.pixmap6=QPixmap(self.file_pathex3+'\\'+self.ranpic6)
            self.img6.setScaledContents(True)
            self.img6.setPixmap(self.pixmap6)
            self.imweed3 =  Image.open(self.file_pathex3+'\\'+self.ranpic6)
            self.mask_weed3 = Image.open(self.file_pathex3+'\\'+self.ranpic6).convert('L')

            self.ranpic7=random.choice(self.listpic3)
            self.pixmap7=QPixmap(self.file_pathex3+'\\'+self.ranpic7)
            self.img7.setScaledContents(True)
            self.img7.setPixmap(self.pixmap7)
            self.imweed4 =  Image.open(self.file_pathex3+'\\'+self.ranpic7)
            self.mask_weed4 = Image.open(self.file_pathex3+'\\'+self.ranpic7).convert('L')

    def browsclickex4(self):
        dialog4=QFileDialog()
        self.file_pathex4=dialog4.getExistingDirectory(None,"Select Folder")
        print(self.file_pathex4)
        self.browse4.setText(self.file_pathex4)

if __name__ == "__main__":
    mycode = ranptaste()
    MainWindow.show()
    sys.exit(app.exec_())