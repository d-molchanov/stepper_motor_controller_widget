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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1012, 690)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.groupBoxMotor = QGroupBox(Form)
        self.groupBoxMotor.setObjectName(u"groupBoxMotor")
        self.groupBoxMotor.setGeometry(QRect(630, 10, 151, 281))
        self.widget = QWidget(self.groupBoxMotor)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 20, 131, 251))
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.comboBoxDirection = QComboBox(self.widget)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxDirection.sizePolicy().hasHeightForWidth())
        self.comboBoxDirection.setSizePolicy(sizePolicy1)
        self.comboBoxDirection.setMinimumSize(QSize(100, 0))

        self.verticalLayout_6.addWidget(self.comboBoxDirection)

        self.comboBoxStep = QComboBox(self.widget)
        self.comboBoxStep.setObjectName(u"comboBoxStep")
        sizePolicy1.setHeightForWidth(self.comboBoxStep.sizePolicy().hasHeightForWidth())
        self.comboBoxStep.setSizePolicy(sizePolicy1)
        self.comboBoxStep.setMinimumSize(QSize(100, 0))

        self.verticalLayout_6.addWidget(self.comboBoxStep)

        self.spinBoxSteps = QSpinBox(self.widget)
        self.spinBoxSteps.setObjectName(u"spinBoxSteps")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.spinBoxSteps.sizePolicy().hasHeightForWidth())
        self.spinBoxSteps.setSizePolicy(sizePolicy2)
        self.spinBoxSteps.setMaximum(999999)
        self.spinBoxSteps.setValue(10)

        self.verticalLayout_6.addWidget(self.spinBoxSteps)

        self.pushButtonStartMotor = QPushButton(self.widget)
        self.pushButtonStartMotor.setObjectName(u"pushButtonStartMotor")
        self.pushButtonStartMotor.setEnabled(False)
        self.pushButtonStartMotor.setMinimumSize(QSize(0, 32))
        self.pushButtonStartMotor.setCheckable(False)
        self.pushButtonStartMotor.setChecked(False)

        self.verticalLayout_6.addWidget(self.pushButtonStartMotor)

        self.pushButtonStopMotor = QPushButton(self.widget)
        self.pushButtonStopMotor.setObjectName(u"pushButtonStopMotor")
        self.pushButtonStopMotor.setEnabled(False)
        self.pushButtonStopMotor.setMinimumSize(QSize(0, 32))

        self.verticalLayout_6.addWidget(self.pushButtonStopMotor)

        self.pushButtonSetZero = QPushButton(self.widget)
        self.pushButtonSetZero.setObjectName(u"pushButtonSetZero")
        self.pushButtonSetZero.setEnabled(False)
        self.pushButtonSetZero.setMinimumSize(QSize(0, 32))

        self.verticalLayout_6.addWidget(self.pushButtonSetZero)

        self.pushButtonCheckState = QPushButton(self.widget)
        self.pushButtonCheckState.setObjectName(u"pushButtonCheckState")
        self.pushButtonCheckState.setEnabled(False)
        self.pushButtonCheckState.setMinimumSize(QSize(0, 32))

        self.verticalLayout_6.addWidget(self.pushButtonCheckState)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(1, 6, 617, 284))
        self.verticalLayout_5 = QVBoxLayout(self.widget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(16)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.comboBoxCOMPorts = QComboBox(self.widget1)
        self.comboBoxCOMPorts.setObjectName(u"comboBoxCOMPorts")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxCOMPorts.sizePolicy().hasHeightForWidth())
        self.comboBoxCOMPorts.setSizePolicy(sizePolicy3)
        self.comboBoxCOMPorts.setMinimumSize(QSize(100, 0))

        self.verticalLayout.addWidget(self.comboBoxCOMPorts)

        self.comboBoxBaudRate = QComboBox(self.widget1)
        self.comboBoxBaudRate.setObjectName(u"comboBoxBaudRate")
        sizePolicy3.setHeightForWidth(self.comboBoxBaudRate.sizePolicy().hasHeightForWidth())
        self.comboBoxBaudRate.setSizePolicy(sizePolicy3)
        self.comboBoxBaudRate.setMinimumSize(QSize(100, 0))
        self.comboBoxBaudRate.setModelColumn(0)

        self.verticalLayout.addWidget(self.comboBoxBaudRate)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButtonRefresh = QPushButton(self.widget1)
        self.pushButtonRefresh.setObjectName(u"pushButtonRefresh")
        self.pushButtonRefresh.setMinimumSize(QSize(0, 32))

        self.verticalLayout_4.addWidget(self.pushButtonRefresh)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButtonConnect = QPushButton(self.widget1)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        self.pushButtonConnect.setMinimumSize(QSize(0, 32))

        self.verticalLayout_2.addWidget(self.pushButtonConnect)

        self.pushButtonDisconnect = QPushButton(self.widget1)
        self.pushButtonDisconnect.setObjectName(u"pushButtonDisconnect")
        self.pushButtonDisconnect.setEnabled(False)
        self.pushButtonDisconnect.setMinimumSize(QSize(0, 32))

        self.verticalLayout_2.addWidget(self.pushButtonDisconnect)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.textEdit_2 = QTextEdit(self.widget1)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.textEdit_2.setMaximumSize(QSize(16777215, 1000))

        self.horizontalLayout.addWidget(self.textEdit_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButtonSend = QPushButton(self.widget1)
        self.pushButtonSend.setObjectName(u"pushButtonSend")
        self.pushButtonSend.setEnabled(False)
        self.pushButtonSend.setMinimumSize(QSize(0, 32))

        self.verticalLayout_3.addWidget(self.pushButtonSend)

        self.pushButtonClearLogs = QPushButton(self.widget1)
        self.pushButtonClearLogs.setObjectName(u"pushButtonClearLogs")
        self.pushButtonClearLogs.setMinimumSize(QSize(0, 32))

        self.verticalLayout_3.addWidget(self.pushButtonClearLogs)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.textEditLogs = QTextEdit(self.widget1)
        self.textEditLogs.setObjectName(u"textEditLogs")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.textEditLogs.sizePolicy().hasHeightForWidth())
        self.textEditLogs.setSizePolicy(sizePolicy4)
        self.textEditLogs.setMinimumSize(QSize(300, 0))

        self.verticalLayout_5.addWidget(self.textEditLogs)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBoxMotor.setTitle(QCoreApplication.translate("Form", u"Motor", None))
        self.pushButtonStartMotor.setText(QCoreApplication.translate("Form", u"Start Motor", None))
        self.pushButtonStopMotor.setText(QCoreApplication.translate("Form", u"Stop Motor", None))
        self.pushButtonSetZero.setText(QCoreApplication.translate("Form", u"Set Zero", None))
        self.pushButtonCheckState.setText(QCoreApplication.translate("Form", u"Check state", None))
        self.pushButtonRefresh.setText(QCoreApplication.translate("Form", u"Refresh", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("Form", u"Connect", None))
        self.pushButtonDisconnect.setText(QCoreApplication.translate("Form", u"Disconnect", None))
        self.pushButtonSend.setText(QCoreApplication.translate("Form", u"Send", None))
        self.pushButtonClearLogs.setText(QCoreApplication.translate("Form", u"Clear logs", None))
    # retranslateUi

