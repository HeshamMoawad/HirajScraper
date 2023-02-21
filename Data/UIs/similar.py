# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Similar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(715, 574)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Similar = QtWidgets.QFrame(self.frame)
        self.Similar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Similar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Similar.setObjectName("Similar")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Similar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SimilarLabel = QtWidgets.QLabel(self.Similar)
        self.SimilarLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SimilarLabel.setObjectName("SimilarLabel")
        self.horizontalLayout_2.addWidget(self.SimilarLabel)
        self.verticalLayout_2.addWidget(self.Similar)
        self.NumbersFrame = QtWidgets.QFrame(self.frame)
        self.NumbersFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NumbersFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NumbersFrame.setObjectName("NumbersFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.NumbersFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.NumbersLabel = QtWidgets.QLabel(self.NumbersFrame)
        self.NumbersLabel.setObjectName("NumbersLabel")
        self.horizontalLayout.addWidget(self.NumbersLabel, 0, QtCore.Qt.AlignHCenter)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.NumbersFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.NumbersFrame)
        self.ExportNameFrame = QtWidgets.QFrame(self.frame)
        self.ExportNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ExportNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ExportNameFrame.setObjectName("ExportNameFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ExportNameFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ExportNameLabel = QtWidgets.QLabel(self.ExportNameFrame)
        self.ExportNameLabel.setObjectName("ExportNameLabel")
        self.horizontalLayout_3.addWidget(self.ExportNameLabel, 0, QtCore.Qt.AlignHCenter)
        self.ExportNameLineEdit = QtWidgets.QLineEdit(self.ExportNameFrame)
        self.ExportNameLineEdit.setObjectName("ExportNameLineEdit")
        self.horizontalLayout_3.addWidget(self.ExportNameLineEdit)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.ExportNameFrame)
        self.ButtonsFrame = QtWidgets.QFrame(self.frame)
        self.ButtonsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonsFrame.setObjectName("ButtonsFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.ButtonsFrame)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StartButton = QtWidgets.QToolButton(self.ButtonsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(sizePolicy)
        self.StartButton.setObjectName("StartButton")
        self.horizontalLayout_4.addWidget(self.StartButton)
        self.StopButton = QtWidgets.QToolButton(self.ButtonsFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout_4.addWidget(self.StopButton)
        self.verticalLayout_2.addWidget(self.ButtonsFrame)
        self.TreeWidgetFrame = QtWidgets.QFrame(self.frame)
        self.TreeWidgetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TreeWidgetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TreeWidgetFrame.setObjectName("TreeWidgetFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.TreeWidgetFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.TreeWidgetFrame)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.treeWidget)
        self.CounterLabel = QtWidgets.QLabel(self.TreeWidgetFrame)
        self.CounterLabel.setObjectName("CounterLabel")
        self.verticalLayout.addWidget(self.CounterLabel, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addWidget(self.TreeWidgetFrame)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(3, 5)
        self.verticalLayout_2.setStretch(4, 20)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SimilarLabel.setText(_translate("Form", "TextLabel"))
        self.NumbersLabel.setText(_translate("Form", "TextLabel"))
        self.ExportNameLabel.setText(_translate("Form", "TextLabel"))
        self.StartButton.setText(_translate("Form", "..."))
        self.StopButton.setText(_translate("Form", "..."))
        self.CounterLabel.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())