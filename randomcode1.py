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

    def gcn(self):
        self.browsebt1.clicked.connect(self.browsclickex1)
        self.browsebt2.clicked.connect(self.browsclickex2)
        self.browsebt3.clicked.connect(self.browsclickex3)
        self.browsebt4.clicked.connect(self.browsclickex4)
        self.changebt1.clicked.connect(self.change1)
        self.changebt2.clicked.connect(self.change2)
        self.changebt3.clicked.connect(self.change3)


    def change1(self):
        if len(self.listpic1)>0:
            self.ranpic1=random.choice(self.listpic1)
            self.pixmap1=QPixmap(self.file_pathex1+'\\'+self.ranpic1)
            self.img1.setScaledContents(True)
            self.img1.setPixmap(self.pixmap1)
            self.imbg =  Image.open(self.file_pathex1+'\\'+self.ranpic1)

    def change2(self):
        if len(self.listpic2)>0:
            self.ranpic2=random.choice(self.listpic2)
            self.pixmap2=QPixmap(self.file_pathex2+'\\'+self.ranpic2)
            self.img2.setScaledContents(True)
            self.img2.setPixmap(self.pixmap2)
            self.imcrop1 =  Image.open(self.file_pathex2+'\\'+self.ranpic2)

            self.ranpic3=random.choice(self.listpic2)
            self.pixmap3=QPixmap(self.file_pathex2+'\\'+self.ranpic3)
            self.img3.setScaledContents(True)
            self.img3.setPixmap(self.pixmap3)
            self.imcrop2 =  Image.open(self.file_pathex2+'\\'+self.ranpic3)
    def change3(self):
        if len(self.listpic3)>0:
            self.ranpic4=random.choice(self.listpic3)
            self.pixmap4=QPixmap(self.file_pathex3+'\\'+self.ranpic4)
            self.img4.setScaledContents(True)
            self.img4.setPixmap(self.pixmap4)
            self.imweed1 =  Image.open(self.file_pathex3+'\\'+self.ranpic4)

            self.ranpic5=random.choice(self.listpic3)
            self.pixmap5=QPixmap(self.file_pathex3+'\\'+self.ranpic5)
            self.img5.setScaledContents(True)
            self.img5.setPixmap(self.pixmap5)
            self.imweed2 =  Image.open(self.file_pathex3+'\\'+self.ranpic5)

            self.ranpic6=random.choice(self.listpic3)
            self.pixmap6=QPixmap(self.file_pathex3+'\\'+self.ranpic6)
            self.img6.setScaledContents(True)
            self.img6.setPixmap(self.pixmap6)
            self.imweed3 =  Image.open(self.file_pathex3+'\\'+self.ranpic6)

            self.ranpic7=random.choice(self.listpic3)
            self.pixmap7=QPixmap(self.file_pathex3+'\\'+self.ranpic7)
            self.img7.setScaledContents(True)
            self.img7.setPixmap(self.pixmap7)
            self.imweed4 =  Image.open(self.file_pathex3+'\\'+self.ranpic7)
        
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

            self.ranpic3=random.choice(self.listpic2)
            self.pixmap3=QPixmap(self.file_pathex2+'\\'+self.ranpic3)
            self.img3.setScaledContents(True)
            self.img3.setPixmap(self.pixmap3)
            self.imcrop2 =  Image.open(self.file_pathex2+'\\'+self.ranpic3)

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

            self.ranpic5=random.choice(self.listpic3)
            self.pixmap5=QPixmap(self.file_pathex3+'\\'+self.ranpic5)
            self.img5.setScaledContents(True)
            self.img5.setPixmap(self.pixmap5)
            self.imweed2 =  Image.open(self.file_pathex3+'\\'+self.ranpic5)

            self.ranpic6=random.choice(self.listpic3)
            self.pixmap6=QPixmap(self.file_pathex3+'\\'+self.ranpic6)
            self.img6.setScaledContents(True)
            self.img6.setPixmap(self.pixmap6)
            self.imweed3 =  Image.open(self.file_pathex3+'\\'+self.ranpic6)

            self.ranpic7=random.choice(self.listpic3)
            self.pixmap7=QPixmap(self.file_pathex3+'\\'+self.ranpic7)
            self.img7.setScaledContents(True)
            self.img7.setPixmap(self.pixmap7)
            self.imweed4 =  Image.open(self.file_pathex3+'\\'+self.ranpic7)

    def browsclickex4(self):
        dialog4=QFileDialog()
        self.file_pathex4=dialog4.getExistingDirectory(None,"Select Folder")
        print(self.file_pathex4)
        self.browse4.setText(self.file_pathex4)

if __name__ == "__main__":
    mycode = ranptaste()
    MainWindow.show()
    sys.exit(app.exec_())