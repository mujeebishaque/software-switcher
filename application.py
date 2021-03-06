
from PyQt5 import QtCore, QtGui, QtWidgets
from messenger import show_message
from switcher import Switcher
import sys
import os

class Ui_MainWindow(object):
    
    switcher = Switcher()

    def __init__(self):
        self.switcher.retrieve_settings()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(590, 0, 161, 51))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("sesil_logo.jpg"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 220, 31))

        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 340, 230, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 340, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(80, 110, 561, 191))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 30, 230, 130))
        self.groupBox_2.setObjectName("groupBox_2")
        self.start_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.start_btn.setGeometry(QtCore.QRect(50, 30, 130, 30))
        self.start_btn.setObjectName("start_btn")
        self.exit_btn = QtWidgets.QPushButton(self.groupBox_2)
        self.exit_btn.setGeometry(QtCore.QRect(50, 80, 130, 30))
        self.exit_btn.setObjectName("exit_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 30, 190, 130))
        self.groupBox_3.setObjectName("groupBox_3")
        self.check_settings_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.check_settings_btn.setGeometry(QtCore.QRect(40, 30, 110, 30))
        self.check_settings_btn.setObjectName("check_settings_btn")
        self.reports_folder_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.reports_folder_btn.setGeometry(QtCore.QRect(40, 80, 110, 30))
        self.reports_folder_btn.setObjectName("reports_folder_btn")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(300, 30, 3, 140))
        self.line.setStyleSheet("background-color: rgb(64, 81, 112);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)

        # linking buttons to connnects
        self.start_btn.clicked.connect(self.start_application)
        self.exit_btn.clicked.connect(self.exit_application)
        
        self.check_settings_btn.clicked.connect(self.check_settings)
        self.reports_folder_btn.clicked.connect(self.open_reports_folder)
        # linking ends here

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Application Switcher SESIL"))
        self.label.setText(_translate("MainWindow", "Window Switcher"))
        self.label_2.setText(_translate("MainWindow", "All Rights Reserved To SESIL PVT. LTD."))
        self.label_3.setText(_translate("MainWindow", "@mujeebishaque"))
        self.groupBox.setTitle(_translate("MainWindow", "Switcher"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Functional"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Misc."))
        self.check_settings_btn.setText(_translate("MainWindow", "Check Settings"))
        self.reports_folder_btn.setText(_translate("MainWindow", "Reports Folder"))

    def start_application(self):
        self.switcher.starter()

    def open_reports_folder(self):
        self.switcher.check_reports()

    def exit_application(self):
        sys.exit()

    def check_settings(self):
        self.switcher.check_settings()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
