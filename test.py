import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets,QtGui

from first import Ui_MainWindow # 导入我们刚转换的ui
import cv2

class MyWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    returnSignal = pyqtSignal()
    def __init__(self):
        super(MyWindows, self).__init__()
        self.timer_camera = QTimer()  # 初始化定时器
        self.timer_camera1 = QTimer()
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = 0
        self.setupUi(self)
        # self.initUI()
        self.slot_init()
        self.image_init()


        # self.queren.clicked.connect(self.putimage)

    def putimage2(self):
        pix = QPixmap('1002.jpg')
        self.label_i.setPixmap(pix)

    def putimage(self):

        # 打开摄像头并显示图像信息


        pix = QPixmap('1001.jpg')
        self.label_i.setPixmap(pix)
        self.queren.setText('刷新订单')
    def image_init(self):

        self.timer_camera1.timeout.connect(self.putimage)
        # 信号和槽连接
        # self.queren.clicked.connect(self.returnSignal)
        self.queren.clicked.connect(self.putimage)

    def shuaxin(self):
        # self.timer_camera1.start(30)
        if self.timer_camera1.isActive() == False:

            self.timer_camera1.start(30)

    # 打开摄像头并显示图像信息
            self.show_image()

        else:
            # self.timer_camera1.stop()
            # self.label_i.clear()
            # self.timer_camera1.start(30)
        # 关闭摄像头并清空显示信息
            self.putimage2()
            self.queren.setText('确认订单')
            # self.timer_camera1.stop()
    #
    # def image_init(self):
    #
    #     self.timer_camera1.timeout.connect(self.show_image)
    #     # 信号和槽连接
    #     # self.queren.clicked.connect(self.returnSignal)
    #     self.queren.clicked.connect(self.shuaxin)
    #
    # def show_image(self):
    #     flag,self.inputImage=cv.imread("E:/Alipay_for_QR_code_2/pay/1001.jpg")
    #
    #     cv.imshow("1",self.inputImage)
    #
    #     showimage=cv.cvtColor(self.inputImage,cv.COLOR_BGR2RGB)
    #     showimage=QtGui.QImage(showimage.data,showimage.shape[1],showimage.shape[0],QtGui.QImage.Format_RGB888)
    #     self.label_i.scaledContents(1)
    #     self.label_i.setpixmap(QtGui.QPixmap.fromImage(showimage))



    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        # self.timer_camera.timeout.connect(self.show_image)
        # 信号和槽连接
        # self.pushButton.clicked.connect(self.returnSignal)
        self.pushButton_2.clicked.connect(self.slotCameraButton)
        # self.queren.clicked.connect(self.shuaxin())



    def show_camera(self):
        flag, self.image = self.cap.read()
        show = cv2.resize(self.image, (480, 320))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)

        self.label_v.setPixmap(QPixmap.fromImage(showImage))

    # 打开关闭摄像头控制
    def slotCameraButton(self):
        if self.timer_camera.isActive() == False:

    # 打开摄像头并显示图像信息
            self.openCamera()
        else:
        # 关闭摄像头并清空显示信息
            self.closeCamera()

    # 打开摄像头
    def openCamera(self):
        flag = self.cap.open(self.CAM_NUM)

        if flag == False:
            msg = QMessageBox.Warning(self, u'Warning', u'请检测相机与电脑是否连接正确',
                                      buttons=QMessageBox.Ok,
                                      defaultButton=QMessageBox.Ok)
        else:
            self.timer_camera.start(30)
            self.pushButton_2.setText('关闭摄像头')

    # 关闭摄像头
    def closeCamera(self):
        self.timer_camera.stop()

        self.cap.release()
        self.label_v.clear()
        self.pushButton_2.setText('打开摄像头')





if __name__ =='__main__':
    # cv.waitKey(0)
    app = QApplication(sys.argv)
    my_windows = MyWindows()  # 实例化对象
    my_windows.show()  # 显示窗口
    sys.exit(app.exec_())