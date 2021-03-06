from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1108, 686)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.picture_box = QtWidgets.QLabel(self.centralwidget)
        self.picture_box.setGeometry(QtCore.QRect(0, 0, 640, 491))
        self.picture_box.setText("")
        self.picture_box.setObjectName("picture_box")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-10, 490, 1121, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.append("لطفا مختصصات خود را وارد کنید.")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1070, 120, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1060, 90, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(1060, 100, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1060, 80, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1060, 120, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(1060, 130, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1060, 110, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1030, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1060, 140, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1060, 150, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1060, 130, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1060, 170, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1060, 160, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.p1_x = QtWidgets.QLineEdit(self.centralwidget)
        self.p1_x.setGeometry(QtCore.QRect(900, 90, 113, 32))
        self.p1_x.setObjectName("p1_x")
        self.p1_y = QtWidgets.QLineEdit(self.centralwidget)
        self.p1_y.setGeometry(QtCore.QRect(900, 140, 113, 32))
        self.p1_y.setObjectName("p1_y")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1030, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(830, 130, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(830, 170, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(800, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.p2_x = QtWidgets.QLineEdit(self.centralwidget)
        self.p2_x.setGeometry(QtCore.QRect(670, 90, 113, 32))
        self.p2_x.setObjectName("p2_x")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(840, 120, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(830, 90, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(830, 100, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(830, 140, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(830, 150, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(830, 80, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(800, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(830, 130, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(830, 160, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.p2_y = QtWidgets.QLineEdit(self.centralwidget)
        self.p2_y.setGeometry(QtCore.QRect(670, 140, 113, 32))
        self.p2_y.setObjectName("p2_y")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(830, 120, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(830, 110, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.tx = QtWidgets.QLineEdit(self.centralwidget)
        self.tx.setGeometry(QtCore.QRect(670, 210, 113, 32))
        self.tx.setObjectName("tx")
        self.ty = QtWidgets.QLineEdit(self.centralwidget)
        self.ty.setGeometry(QtCore.QRect(670, 260, 113, 32))
        self.ty.setObjectName("ty")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1060, 220, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(830, 240, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(1060, 200, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1060, 270, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(1030, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(830, 290, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(830, 220, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(840, 240, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(830, 230, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(830, 250, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(1070, 240, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(830, 270, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(830, 200, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(800, 210, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(1030, 260, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.centralwidget)
        self.label_45.setGeometry(QtCore.QRect(830, 250, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.label_46 = QtWidgets.QLabel(self.centralwidget)
        self.label_46.setGeometry(QtCore.QRect(800, 260, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.p3_x = QtWidgets.QLineEdit(self.centralwidget)
        self.p3_x.setGeometry(QtCore.QRect(900, 210, 113, 32))
        self.p3_x.setObjectName("p3_x")
        self.p3_y = QtWidgets.QLineEdit(self.centralwidget)
        self.p3_y.setGeometry(QtCore.QRect(900, 260, 113, 32))
        self.p3_y.setObjectName("p3_y")
        self.label_47 = QtWidgets.QLabel(self.centralwidget)
        self.label_47.setGeometry(QtCore.QRect(1060, 280, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.centralwidget)
        self.label_48.setGeometry(QtCore.QRect(1060, 250, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.centralwidget)
        self.label_49.setGeometry(QtCore.QRect(830, 280, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.label_50 = QtWidgets.QLabel(self.centralwidget)
        self.label_50.setGeometry(QtCore.QRect(1060, 260, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.centralwidget)
        self.label_51.setGeometry(QtCore.QRect(830, 210, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.centralwidget)
        self.label_52.setGeometry(QtCore.QRect(830, 260, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(1060, 250, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(1060, 210, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.centralwidget)
        self.label_55.setGeometry(QtCore.QRect(1060, 230, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(self.centralwidget)
        self.label_56.setGeometry(QtCore.QRect(1060, 290, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.centralwidget)
        self.label_57.setGeometry(QtCore.QRect(1060, 240, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(900, 320, 191, 34))
        self.run.setObjectName("run")
        self.clean = QtWidgets.QPushButton(self.centralwidget)
        self.clean.setGeometry(QtCore.QRect(670, 320, 191, 34))
        self.clean.setObjectName("clean")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(670, 370, 421, 34))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.run.clicked.connect(self.Transport)
        self.clean.clicked.connect(self.clear)
        self.exit.clicked.connect(self.exit_app)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def Transport(self):
        self.textBrowser.clear()
        P1x = int(self.p1_x.text())
        P1y = int(self.p1_y.text())
        P2x = int(self.p2_x.text())
        P2y = int(self.p2_y.text())
        P3x = int(self.p3_x.text())
        P3y = int(self.p3_y.text())
        Tx = int(self.tx.text())
        Ty = int(self.ty.text())
        from Transport import transport
        transport(P1x,P1y,P2x,P2y,P3x,P3y,Tx,Ty)
        self.picture_box.setPixmap(QtGui.QPixmap("2D Transport.png"))
        self.textBrowser.append("مختصصات شما رسم گردید.\n")
        self.textBrowser.append("مثلث سبز رنگ شکل اولیه است و مثلث آبی رنگ شکل انتقال داده شده.")

    def clear(self):
        self.picture_box.clear()
        self.p1_x.clear()
        self.p1_y.clear()
        self.p2_x.clear()
        self.p2_y.clear()
        self.p3_x.clear()
        self.p3_y.clear()
        self.tx.clear()
        self.ty.clear()
        self.textBrowser.clear()
        self.textBrowser.append("لطفا مختصصات خود را وارد کنید.")

    def exit_app(self):
        MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "انتقال دو بعدی"))
        self.label_2.setText(_translate("MainWindow", "P1"))
        self.label_3.setText(_translate("MainWindow", "|"))
        self.label_4.setText(_translate("MainWindow", "|"))
        self.label_5.setText(_translate("MainWindow", "|"))
        self.label_6.setText(_translate("MainWindow", "|"))
        self.label_7.setText(_translate("MainWindow", "|"))
        self.label_8.setText(_translate("MainWindow", "|"))
        self.label_9.setText(_translate("MainWindow", ":x"))
        self.label_11.setText(_translate("MainWindow", "|"))
        self.label_12.setText(_translate("MainWindow", "|"))
        self.label_13.setText(_translate("MainWindow", "|"))
        self.label_14.setText(_translate("MainWindow", "|"))
        self.label_15.setText(_translate("MainWindow", "|"))
        self.label_16.setText(_translate("MainWindow", ":y"))
        self.label_10.setText(_translate("MainWindow", "|"))
        self.label_17.setText(_translate("MainWindow", "|"))
        self.label_18.setText(_translate("MainWindow", ":y"))
        self.label_19.setText(_translate("MainWindow", "P2"))
        self.label_20.setText(_translate("MainWindow", "|"))
        self.label_21.setText(_translate("MainWindow", "|"))
        self.label_22.setText(_translate("MainWindow", "|"))
        self.label_23.setText(_translate("MainWindow", "|"))
        self.label_24.setText(_translate("MainWindow", "|"))
        self.label_25.setText(_translate("MainWindow", ":x"))
        self.label_26.setText(_translate("MainWindow", "|"))
        self.label_27.setText(_translate("MainWindow", "|"))
        self.label_28.setText(_translate("MainWindow", "|"))
        self.label_29.setText(_translate("MainWindow", "|"))
        self.label_30.setText(_translate("MainWindow", "|"))
        self.label_31.setText(_translate("MainWindow", "|"))
        self.label_32.setText(_translate("MainWindow", "|"))
        self.label_33.setText(_translate("MainWindow", "|"))
        self.label_34.setText(_translate("MainWindow", ":x"))
        self.label_35.setText(_translate("MainWindow", "|"))
        self.label_36.setText(_translate("MainWindow", "|"))
        self.label_37.setText(_translate("MainWindow", "T"))
        self.label_38.setText(_translate("MainWindow", "|"))
        self.label_39.setText(_translate("MainWindow", "|"))
        self.label_40.setText(_translate("MainWindow", "P3"))
        self.label_41.setText(_translate("MainWindow", "|"))
        self.label_42.setText(_translate("MainWindow", "|"))
        self.label_43.setText(_translate("MainWindow", ":x"))
        self.label_44.setText(_translate("MainWindow", ":y"))
        self.label_45.setText(_translate("MainWindow", "|"))
        self.label_46.setText(_translate("MainWindow", ":y"))
        self.label_47.setText(_translate("MainWindow", "|"))
        self.label_48.setText(_translate("MainWindow", "|"))
        self.label_49.setText(_translate("MainWindow", "|"))
        self.label_50.setText(_translate("MainWindow", "|"))
        self.label_51.setText(_translate("MainWindow", "|"))
        self.label_52.setText(_translate("MainWindow", "|"))
        self.label_53.setText(_translate("MainWindow", "|"))
        self.label_54.setText(_translate("MainWindow", "|"))
        self.label_55.setText(_translate("MainWindow", "|"))
        self.label_56.setText(_translate("MainWindow", "|"))
        self.label_57.setText(_translate("MainWindow", "|"))
        self.run.setText(_translate("MainWindow", "محاسبه"))
        self.clean.setText(_translate("MainWindow", "پاک کن"))
        self.exit.setText(_translate("MainWindow", "خروج"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
