from PyQt5 import QtCore, QtGui, QtWidgets
import dialog_emociones as dialog_emociones

class Ui_main_frame_2(object):
    def setupUi(self, main_frame_2):
        main_frame_2.setObjectName("main_frame_2")
        main_frame_2.resize(348, 457)
        main_frame_2.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(main_frame_2)
        self.centralwidget.setObjectName("centralwidget")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(11, 11, 330, 441))
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.btn_poblar_DS = QtWidgets.QPushButton(self.main_frame)
        self.btn_poblar_DS.setGeometry(QtCore.QRect(80, 50, 171, 71))
        self.btn_poblar_DS.setObjectName("btn_poblar_DS")
        self.btn_entrenar_modelo = QtWidgets.QPushButton(self.main_frame)
        self.btn_entrenar_modelo.setGeometry(QtCore.QRect(80, 140, 171, 71))
        self.btn_entrenar_modelo.setObjectName("btn_entrenar_modelo")
        self.btn_main_RE = QtWidgets.QPushButton(self.main_frame)
        self.btn_main_RE.setGeometry(QtCore.QRect(80, 230, 171, 71))
        self.btn_main_RE.setObjectName("btn_main_RE")
        self.btn_info = QtWidgets.QPushButton(self.main_frame)
        self.btn_info.setGeometry(QtCore.QRect(80, 320, 171, 71))
        self.btn_info.setObjectName("btn_info")
        main_frame_2.setCentralWidget(self.centralwidget)

        self.btn_poblar_DS.clicked.connect(self.abrirEmocionesDialog)

        self.retranslateUi(main_frame_2)
        QtCore.QMetaObject.connectSlotsByName(main_frame_2)

    def retranslateUi(self, main_frame_2):
        _translate = QtCore.QCoreApplication.translate
        main_frame_2.setWindowTitle(_translate(
            "main_frame_2", "Proyecto Final AA"))
        self.btn_poblar_DS.setText(_translate(
            "main_frame_2", "Poblar DataSet"))
        self.btn_entrenar_modelo.setText(
            _translate("main_frame_2", "Entrenar Modelo"))
        self.btn_main_RE.setText(_translate(
            "main_frame_2", "Detectar mi emociones"))
        self.btn_info.setText(_translate("main_frame_2", "Caso de Uso"))

    def abrirEmocionesDialog(self):
        self.emociones_dialog = QtWidgets.QDialog()
        self.ui = dialog_emociones.Ui_Dialog()
        self.ui.setupUi(self.emociones_dialog)
        self.emociones_dialog.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_frame_2 = QtWidgets.QMainWindow()
    ui = Ui_main_frame_2()
    ui.setupUi(main_frame_2)
    main_frame_2.show()
    sys.exit(app.exec_())
