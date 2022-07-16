from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(414, 481)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(40, 10, 341, 451))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_felicidad = QtWidgets.QPushButton(self.frame)
        self.btn_felicidad.setGeometry(QtCore.QRect(90, 70, 161, 61))
        self.btn_felicidad.setObjectName("btn_felicidad")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 10, 291, 51))
        self.label.setObjectName("label")
        self.btn_sorpresa = QtWidgets.QPushButton(self.frame)
        self.btn_sorpresa.setGeometry(QtCore.QRect(90, 150, 161, 61))
        self.btn_sorpresa.setObjectName("btn_sorpresa")
        self.btn_enojo = QtWidgets.QPushButton(self.frame)
        self.btn_enojo.setGeometry(QtCore.QRect(90, 230, 161, 61))
        self.btn_enojo.setObjectName("btn_enojo")
        self.btn_tisteza = QtWidgets.QPushButton(self.frame)
        self.btn_tisteza.setGeometry(QtCore.QRect(90, 310, 161, 61))
        self.btn_tisteza.setObjectName("btn_tisteza")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_felicidad.setText(_translate("Dialog", "Felicidad"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">¿Cual de los DataSet de emociónes desea Poblar?</span></p></body></html>"))
        self.label.setText(_translate("Dialog", "¿Cual de los DataSet de emociónes desea Poblar?"))
        self.btn_sorpresa.setText(_translate("Dialog", "Sorpresa"))
        self.btn_enojo.setText(_translate("Dialog", "Enojo"))
        self.btn_tisteza.setText(_translate("Dialog", "Tristeza"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
