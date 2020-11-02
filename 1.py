# # 如：要将一个图片变为32*32大小的
# import cv2
#
# image = cv2.imread('test.jpg')
# res = cv2.resize(image, (800, 600), interpolation=cv2.INTER_CUBIC)
# cv2.imshow('iker', res)
# # cv2.imshow('image', image)
# cv2.waitKey(0)
# cv2.destoryAllWindows()
import cv2
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout


class QPixmapDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
        self.setImage()

    # 设置ui界面
    def setUI(self):
        self.resize(800, 600)
        self.setWindowTitle('picture')
        self.imgLabel = QLabel()
        self.imgLabel.resize(800, 600)  # 设置label的大小,图片会适配label的大小
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.imgLabel)
        self.setLayout(self.hbox)

    def setImage(self):
        img = cv2.imread('1001.jpg')  # opencv读取图片
        res = cv2.resize(img, (800, 600), interpolation=cv2.INTER_CUBIC)  # 用cv2.resize设置图片大小
        img2 = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)  # opencv读取的bgr格式图片转换成rgb格式
        _image = QtGui.QImage(img2[:], img2.shape[1], img2.shape[0], img2.shape[1] * 3,
                              QtGui.QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
        jpg_out = QtGui.QPixmap(_image)  # 转换成QPixmap
        self.imgLabel.setPixmap(jpg_out)  # 设置图片显示


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QPixmapDemo()
    win.show()
    sys.exit(app.exec_())