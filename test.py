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
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = 0
        # self.setupUi(self)



        self.setupUi(self)
        # self.initUI()
        self.slot_init()
        # self.pushButton.clicked.connect(self.slotCameraButton)
        self.queren.clicked.connect(self.putimage)
    def putimage(self):
        pix = QPixmap('1001.jpg')
        self.label_i.setPixmap(pix)


    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        # 信号和槽连接
        self.pushButton.clicked.connect(self.returnSignal)
        self.pushButton_2.clicked.connect(self.slotCameraButton)

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