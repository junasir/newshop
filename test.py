import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets,QtGui

from first import Ui_MainWindow # 导入我们刚转换的ui
import cv2
import time

class MyWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    returnSignal = pyqtSignal()
    def __init__(self):
        super(MyWindows, self).__init__()
        self.a=0
        self.timer_camera = QTimer()  # 初始化定时器
        self.timer_button = QTimer()  # 初始化定时器
        self.cap = cv2.VideoCapture()  # 初始化摄像头
        self.CAM_NUM = 0
        self.setupUi(self)
        # self.initUI()
        self.slot_init()
        self.queren.clicked.connect(self.shuaxin)
        self.init_table()


        # self.queren.clicked.connect(self.putimage)

    def putimage2(self):
        self.label_i.clear()
        # pix = QPixmap('1002.jpg')
        # self.label_i.setPixmap(pix)

    def putimage(self):

        # 打开摄像头并显示图像信息
        pix = QPixmap('QRcod.jpg')
        self.label_i.setPixmap(pix)
        # self.queren.setText('确认订单')


    def image_init(self):


        # 信号和槽连接
        # self.queren.clicked.connect(self.returnSignal)
        self.queren.clicked.connect(self.putimage)
        # self.timer_camera1.start(30)

    def shuaxin(self):
            # self.timer_camera1.timeout.connect(self.putimage2)
    # 打开摄像头并显示图像信息
            if self.a is 1:
                self.putimage2()
                self.a=0
                self.queren.setText('确认订单')

                # t=0
                # while t<1:
                #     # time.sleep(5)
                #     self.queren.setEnabled(False)
                #
                #     time.sleep(1)
                #     self.queren.setEnabled(True)
                #     t +=1

            else :
                self.putimage()
                self.a=1
                self.queren.setText('刷新订单')
                self.queren.setEnabled(False)
                self.timer_button.start(2000)
            # t = 0
            # while t < 1:
            #
            #     self.queren.setEnabled(False)
            #
            #     t += 1
            # self.queren.setEnabled(True)
    def delaytime(self):
        self.queren.setEnabled(True)
        self.timer_button.stop()

    def init_table(self):
        print('-----初始化-----')
        font = QFont('微软雅黑', 12)
        font.setBold(False)  # 设置字体是否加粗
        self.tableWidget.horizontalHeader().setFont(font)  # 设置表头字体
        self.tableWidget.horizontalHeader().setFixedHeight(30)  # 设置表头高度
        # self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)  # 设置最后一列拉伸至最大,充满屏幕
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可更改

        # font_bill = QFont('微软雅黑', 10)
        # self.tableWidget_bill.horizontalHeader().setFont(font_bill)  # 设置表头字体
        # self.tableWidget_bill.horizontalHeader().setFixedHeight(30)  # 设置表头高度
        # self.tableWidget_bill.horizontalHeader().setStretchLastSection(True)  # 设置最后一列拉伸至最大,充满屏幕
        # self.tableWidget_bill.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 设置表格不可更改

        # 初始时按钮不可点击结算
        # self.button_ok.setEnabled(False)
        # self.button_pay.setEnabled(False)
        # self.button_update.setEnabled(False)
        # self.button_print.setEnabled(False)

        # 识别到的商品显示窗口
        self.tableWidget.clear()
        # 设置列数
        self.tableWidget.setColumnCount(4)
        get_list = ['商品id', '商品名称', '单价(元)', '个数']
        self.tableWidget.setHorizontalHeaderLabels(get_list)
        print(get_list)

        # 账单显示窗口
        # self.tableWidget_bill.clear()
        # self.tableWidget_bill.setColumnCount(2)
        # bill_list = ['名称', '单价(元)*个数']
        # self.tableWidget_bill.setHorizontalHeaderLabels(bill_list)
        #
        # print(bill_list)


    def slot_init(self):
        self.timer_camera.timeout.connect(self.show_camera)
        self.pushButton_2.clicked.connect(self.slotCameraButton)
        self.timer_button.timeout.connect(self.delaytime)



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