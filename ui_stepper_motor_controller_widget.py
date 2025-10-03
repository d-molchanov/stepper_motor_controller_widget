# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stepper_motor_controller_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1012, 690)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 20, 496, 394))
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBoxCOMPorts = QComboBox(self.widget)
        self.comboBoxCOMPorts.setObjectName(u"comboBoxCOMPorts")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCOMPorts.sizePolicy().hasHeightForWidth())
        self.comboBoxCOMPorts.setSizePolicy(sizePolicy)
        self.comboBoxCOMPorts.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.comboBoxCOMPorts)

        self.comboBoxBaudRate = QComboBox(self.widget)
        self.comboBoxBaudRate.setObjectName(u"comboBoxBaudRate")
        sizePolicy.setHeightForWidth(self.comboBoxBaudRate.sizePolicy().hasHeightForWidth())
        self.comboBoxBaudRate.setSizePolicy(sizePolicy)
        self.comboBoxBaudRate.setMinimumSize(QSize(100, 0))
        self.comboBoxBaudRate.setModelColumn(0)

        self.verticalLayout.addWidget(self.comboBoxBaudRate)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonConnect = QPushButton(self.widget)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")

        self.verticalLayout_2.addWidget(self.pushButtonConnect)

        self.pushButtonDisconnect = QPushButton(self.widget)
        self.pushButtonDisconnect.setObjectName(u"pushButtonDisconnect")

        self.verticalLayout_2.addWidget(self.pushButtonDisconnect)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMaximumSize(QSize(16777215, 48))

        self.horizontalLayout.addWidget(self.textEdit_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonSend = QPushButton(self.widget)
        self.pushButtonSend.setObjectName(u"pushButtonSend")

        self.verticalLayout_3.addWidget(self.pushButtonSend)

        self.pushButtonClearLogs = QPushButton(self.widget)
        self.pushButtonClearLogs.setObjectName(u"pushButtonClearLogs")

        self.verticalLayout_3.addWidget(self.pushButtonClearLogs)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.textEditLogs = QTextEdit(self.widget)
        self.textEditLogs.setObjectName(u"textEditLogs")

        self.verticalLayout_4.addWidget(self.textEditLogs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.pushButtonDisconnect.setText(QCoreApplication.translate("Form", u"Disconnect", None))
        self.pushButtonSend.setText(QCoreApplication.translate("Form", u"Send", None))
        self.pushButtonClearLogs.setText(QCoreApplication.translate("Form", u"Clear logs", None))
    # retranslateUi

