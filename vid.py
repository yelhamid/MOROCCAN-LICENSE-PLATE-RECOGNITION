
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAbstractButton, QButtonGroup, QCheckBox, QFileDialog, QMainWindow, QMessageBox, \
    QApplication
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import icons

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import cv2
import re


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 622)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("background-color: #f6f6f6;\n"
"border-radius:20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.MENUPRIN = QtWidgets.QPushButton(self.frame)
        self.MENUPRIN.setMinimumSize(QtCore.QSize(40, 40))
        self.MENUPRIN.setMaximumSize(QtCore.QSize(30, 16777215))
        self.MENUPRIN.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"\n"
"background-color:#1890cf;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 rgba(20,146,208,255),stop:1 rgb(246,246,246));\n"
"\n"
"}")
        self.MENUPRIN.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MENUPRIN.setIcon(icon)
        self.MENUPRIN.setCheckable(False)
        self.MENUPRIN.setAutoRepeat(False)
        self.MENUPRIN.setObjectName("MENUPRIN")
        self.horizontalLayout_3.addWidget(self.MENUPRIN)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(200, 25))
        self.label.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.CHARVID = QtWidgets.QPushButton(self.frame)
        self.CHARVID.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CHARVID.setFont(font)
        self.CHARVID.setStyleSheet("QPushButton{\n"
"border-radius:15px;\n"
"color:#f6f6f6;\n"
"background-color:#1890cf;\n"
"}\n"
"QPushButton:hover{\n"
"background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 rgba(20,146,208,255),stop:1 rgb(246,246,246));\n"
"\n"
"}")
        self.CHARVID.setObjectName("CHARVID")
        self.horizontalLayout_3.addWidget(self.CHARVID)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)

        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setStyleSheet("background-color: #f6f6f6;\n"
"border-radius:20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(150, 0, 160, 29))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.VID = QtWidgets.QLabel(self.frame_4)
        self.VID.setGeometry(QtCore.QRect(40, 70, 401, 330))
        self.VID.setMinimumSize(QtCore.QSize(300, 330))
        self.VID.setMaximumSize(QtCore.QSize(16777215, 300))
        self.VID.setStyleSheet("BORDEr:1px solid black;\n""border-radius:0px;")
        self.VID.setText("")
        self.VID.setObjectName("VID")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setGeometry(QtCore.QRect(30, 30, 381, 25))
        self.frame_6.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        #self.YOLO = QtWidgets.QRadioButton(self.frame_6)
        #self.YOLO.setGeometry(QtCore.QRect(100, 0, 82, 17))
        #font = QtGui.QFont()
        #font.setFamily("MV Boli")
        #font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        #self.YOLO.setFont(font)
        #self.YOLO.setObjectName("YOLO")
        #self.DETECTOR = QtWidgets.QRadioButton(self.frame_6)
        #self.DETECTOR.setEnabled(True)
        #self.DETECTOR.setGeometry(QtCore.QRect(200, 0, 100, 17))
        #self.DETECTOR.setMinimumSize(QtCore.QSize(100, 0))
        #font = QtGui.QFont()
        #font.setFamily("MV Boli")
        #font.setPointSize(10)
        #font.setBold(True)
        #font.setWeight(75)
        #self.DETECTOR.setFont(font)
        #self.DETECTOR.setObjectName("DETECTOR")
        #self.STARVI = QtWidgets.QPushButton(self.frame_4)
        #self.STARVI.setGeometry(QtCore.QRect(120, 410, 60, 60))
        #self.STARVI.setMinimumSize(QtCore.QSize(60, 60))
        #self.STARVI.setMaximumSize(QtCore.QSize(30, 16777215))
        #self.STARVI.setStyleSheet("QPushButton{\n"
##"border-radius:30px;\n"
#"\n"
#"background-color:#1890cf;\n"
#"}\n"
#"\n"
#"QPushButton:hover{\n"
#"background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 rgba(20,146,208,255),stop:1 rgb(246,246,246));\n"
#"\n"
#"}"
        #self.STARVI.setText("")
        #icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.STARVI.setIcon(icon1)
        #self.STARVI.setObjectName("STARVI")
       # self.PAUSE = QtWidgets.QPushButton(self.frame_4)
        #self.PAUSE.setGeometry(QtCore.QRect(290, 410, 60, 60))
        #self.PAUSE.setMinimumSize(QtCore.QSize(60, 60))
        #self.PAUSE.setMaximumSize(QtCore.QSize(30, 16777215))
        #self.PAUSE.setStyleSheet("QPushButton{\n"
#"border-radius:30px;\n"
#"\n"
#"background-color:#1890cf;\n"
#"}\n"
#"\n"
#"QPushButton:hover{\n"
#"background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 rgba(20,146,208,255),stop:1 rgb(246,246,246));\n"
#"\n"
#"}")
 #       self.PAUSE.setText("")
        #self.horizontalLayout_3.addWidget(self.PAUSE,0,QtCore,Qt.AlignHCenter)
        #icon2 = QtGui.QIcon()
        #icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.PAUSE.setIcon(icon2)
        #self.PAUSE.setObjectName("PAUSE")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(510, 0, 501, 474))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setMinimumSize(QtCore.QSize(150, 0))
        self.label_4.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PLAQUE = QtWidgets.QLabel(self.frame_5)
        self.PLAQUE.setMinimumSize(QtCore.QSize(350, 70))
        self.PLAQUE.setMaximumSize(QtCore.QSize(350, 70))
        self.PLAQUE.setStyleSheet("BORDEr:1px solid black;\n"
"border-radius:0px;")
        self.PLAQUE.setText("")
        self.PLAQUE.setObjectName("PLAQUE")
        self.verticalLayout_2.addWidget(self.PLAQUE, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setMinimumSize(QtCore.QSize(230, 0))
        self.label_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.DROLICEN = QtWidgets.QTextBrowser(self.frame_5)
        self.DROLICEN.setMinimumSize(QtCore.QSize(350, 200))
        self.DROLICEN.setMaximumSize(QtCore.QSize(350, 200))
        self.DROLICEN.setStyleSheet("BORDEr:1px solid black;")
        self.DROLICEN.setObjectName("DROLICEN")
        self.DROLICEN.setFont(QFont('Arial',20))
        self.verticalLayout_2.addWidget(self.DROLICEN, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.horizontalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.CHARVID.clicked.connect(self.on_click_load_vd)


        def load_yolo():
            net = cv2.dnn.readNet("yolov3_plates_final.weights", "yolov3-license-plates.cfg")
            classes = []
            with open("classes.names", "r") as f:
                classes = [line.strip() for line in f.readlines()]
            layers_names = net.getLayerNames()
            output_layers = [layers_names[i - 1] for i in net.getUnconnectedOutLayers()]

            return net, classes, output_layers

        self.model_yolo, self.classes_yolo, self.output_layers_yolo = load_yolo()
        self.load_model("yolov3_last_characters.weights", "yolov3_characters.cfg")

    def load_model(self, weight_path: str, cfg_path: str):
            self.net = cv2.dnn.readNet(weight_path, cfg_path)
            with open("classes_ocr.names", "r") as f:
                self.classes = [line.strip() for line in f.readlines()]
            self.layers_names = self.net.getLayerNames()
            self.output_layers = [self.layers_names[i - 1] for i in self.net.getUnconnectedOutLayers()]
            self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Moroccan LPDR"))
        self.CHARVID.setText(_translate("MainWindow", "CHARGER LA VIDEO"))
        self.label_2.setText(_translate("MainWindow", "DETECTION:"))
        self.label_4.setText(_translate("MainWindow", "LA PLAQUE:"))
        self.label_3.setText(_translate("MainWindow", "RECONAISSANCE:"))


    def on_click_load_vd(self):
            vd = QFileDialog.getOpenFileName(None, 'OpenFile', '', "Image file(*.mp4)")
            vidpath = vd[0]
            capVid = cv2.VideoCapture(vidpath)
            plats = []
            self.play = True
            while (capVid.isOpened() and self.play):
                    ret, frame = capVid.read()
                    if ret:
                            cv2.imwrite('frame.jpg', frame)
                            image, height, width, channels = self.load_image('frame.jpg')
                            blob, outputs = self.detect_objects_yolo(image, self.model_yolo, self.output_layers_yolo)
                            boxes, confs, class_ids = self.get_box_dimensions_yolo(outputs, height, width)
                            plat_img, LpImg = self.draw_labels_yolo(boxes, confs, class_ids, self.classes_yolo, image)
                            if len(LpImg):
                                    cv2.imwrite('car_box.jpg', plat_img)
                                    cv2.imwrite('plate_box.jpg', LpImg[0])
                                    self.VID.setPixmap(QtGui.QPixmap('car_box.jpg'))
                                    self.VID.setScaledContents(True)
                                    #----------- reconnaissance
                                    form = re.compile("[0-9]+[ ][|][ ][\W][ ][|][ ][0-9][0-9][0-9]+", re.ASCII)

                                    image, height, width, channels = self.load_image('plate_box.jpg')
                                    blob, outputs = self.read_plate(image)
                                    boxes, confidences, class_ids = self.get_boxes(outputs, width, height,
                                                                                   threshold=0.3)
                                    segmented, plate_text = self.draw_labels(boxes, confidences, class_ids, image)

                                    if (re.search(form, plate_text)):

                                        if plate_text not in plats:
                                            plats.append(plate_text)
                                            self.DROLICEN.append("    " + plate_text)
                                    self.PLAQUE.setPixmap(QtGui.QPixmap('plate_box.jpg'))
                                    self.PLAQUE.setScaledContents(True)

                            else:
                                    self.VID.setPixmap(QtGui.QPixmap('frame.jpg'))
                                    self.VID.setScaledContents(True)


                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                    break
                    else:
                            break
            capVid.release()
            cv2.destroyAllWindows()


    def load_image(self, img_path):
        img = cv2.imread(img_path)
        height, width, channels = img.shape
        return img, height, width, channels

    def detect_objects_yolo(self, img, net, output_layers):
        blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
        net.setInput(blob)
        outputs = net.forward(output_layers)
        return blob, outputs

    def get_box_dimensions_yolo(self, outputs, height, width):
        boxes = []
        confs = []
        class_ids = []
        for output in outputs:
            for detect in output:
                scores = detect[5:]
                class_id = np.argmax(scores)
                conf = scores[class_id]
                if conf > 0.3:
                    center_x = int(detect[0] * width)
                    center_y = int(detect[1] * height)
                    w = int(detect[2] * width)
                    h = int(detect[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confs.append(float(conf))
                    class_ids.append(class_id)
        return boxes, confs, class_ids

    def draw_labels_yolo(self, boxes, confs, class_ids, classes, img):
        indexes = cv2.dnn.NMSBoxes(boxes, confs, 0.1, 0.1)
        font = cv2.FONT_HERSHEY_PLAIN
        plats = []
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[class_ids[i]])
                color_green = (0, 255, 0)
                crop_img = img[y:y + h, x:x + w]
                crop_resized = cv2.resize(crop_img, dsize=(470, 110))
                plats.append(crop_resized)
                cv2.rectangle(img, (x, y), (x + w, y + h), color_green, 2)
                confidence = round(confs[i], 3) * 100

        return img, plats


    def read_plate(self, img):
        blob = cv2.dnn.blobFromImage(img, scalefactor=0.00392, size=(320, 320), mean=(0, 0, 0), swapRB=True, crop=False)
        self.net.setInput(blob)
        outputs = self.net.forward(self.output_layers)
        return blob, outputs

    def get_boxes(self, outputs, width, height, threshold=0.3):
        boxes = []
        confidences = []
        class_ids = []
        for output in outputs:
            for detect in output:
                scores = detect[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > threshold:
                    center_x = int(detect[0] * width)
                    center_y = int(detect[1] * height)
                    w = int(detect[2] * width)
                    h = int(detect[3] * height)
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        return boxes, confidences, class_ids

    def draw_labels(self, boxes, confidences, class_ids, img):
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.1, 0.1)
        font = cv2.FONT_HERSHEY_PLAIN
        c = 0
        characters = []
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                color = self.colors[i % len(self.colors)]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                confidence = round(confidences[i], 3) * 100
                cv2.putText(img, str(confidence) + "%", (x, y - 6), font, 1, color, 2)
                characters.append((label, x))
        characters.sort(key=lambda x: x[1])
        plate = ""
        for l in characters:
            plate += l[0]
        chg = 0
        for i in range(len(plate)):
            if plate[i] in ['b', 'h', 'd', 'a']:
                if plate[i-1] == 'w':
                    ar = i-1
                    chg = 2
                elif plate[i-1] == 'c':
                    ar = i - 1
                    chg = 3
                else:
                    ar = i
                    chg = 1


        if chg == 1:
            plate =  plate[ar+1:] + ' | ' + str(self.arabic_chars(ord(plate[ar])), encoding="utf-8") + ' | ' + plate[:ar]
        if chg == 2:
            index = 0
            for i in range(3):
                index = index + plate[ar+i]
            plate = plate[ar+3:] + ' | ' + str(self.arabic_chars(index), encoding="utf-8") + ' | ' + plate[ar+3:]
        if chg == 3:
            index = 0
            for i in range(2):
                index = index + plate[ar+i]
            plate = + plate[ar+2:] + ' | ' + str(self.arabic_chars(index), encoding="utf-8") + ' | ' + plate[:ar]
        return img, plate

    def arabic_chars(self, index):
        if (index == ord('a')):
            return "أ".encode("utf-8")

        if (index == ord('b')):
            return "ب".encode("utf-8")

        if (index == 2 * ord('w') + ord('a') or index == ord('w')):
            return "و".encode("utf-8")

        if (index == ord('d')):
            return "د".encode("utf-8")

        if (index == ord('h')):
            return "ه".encode("utf-8")

        if (index == ord('c') + ord('h')):
            return "ش".encode("utf-8")
