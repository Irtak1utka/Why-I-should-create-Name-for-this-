from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.Draw = QtWidgets.QPushButton(parent=Form)
        self.Draw.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.Draw.setObjectName("Draw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Draw.setText(_translate("Form", "Draw"))
