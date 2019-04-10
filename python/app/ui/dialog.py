# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(809, 460)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.show_folder = QtGui.QPushButton(Dialog)
        self.show_folder.setObjectName("show_folder")
        self.verticalLayout.addWidget(self.show_folder)
        self.create_folder = QtGui.QPushButton(Dialog)
        self.create_folder.setObjectName("create_folder")
        self.verticalLayout.addWidget(self.create_folder)
        self.launch_maya = QtGui.QPushButton(Dialog)
        self.launch_maya.setObjectName("launch_maya")
        self.verticalLayout.addWidget(self.launch_maya)
        self.launch_ps = QtGui.QPushButton(Dialog)
        self.launch_ps.setObjectName("launch_ps")
        self.verticalLayout.addWidget(self.launch_ps)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "The Current Sgtk Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.show_folder.setText(QtGui.QApplication.translate("Dialog", "Show Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.create_folder.setText(QtGui.QApplication.translate("Dialog", "Create Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.launch_maya.setText(QtGui.QApplication.translate("Dialog", "Launch Maya", None, QtGui.QApplication.UnicodeUTF8))
        self.launch_ps.setText(QtGui.QApplication.translate("Dialog", "Launch Photoshop", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
