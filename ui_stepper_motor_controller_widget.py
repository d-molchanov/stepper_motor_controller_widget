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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

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
        self.groupBoxMotor.setGeometry(QRect(760, 170, 151, 351))
        self.layoutWidget = QWidget(self.groupBoxMotor)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 131, 302))
        self.verticalLayout_6 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget_2 = QWidget(Form)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(0, 10, 331, 321))
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBoxCOMPorts = QComboBox(self.layoutWidget_2)
        self.comboBoxCOMPorts.setObjectName(u"comboBoxCOMPorts")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBoxCOMPorts.sizePolicy().hasHeightForWidth())
        self.comboBoxCOMPorts.setSizePolicy(sizePolicy1)
        self.comboBoxCOMPorts.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.comboBoxCOMPorts)

        self.pushButtonRefresh = QPushButton(self.layoutWidget_2)
        self.pushButtonRefresh.setObjectName(u"pushButtonRefresh")
        self.pushButtonRefresh.setMinimumSize(QSize(0, 32))
        icon = QIcon()
        icon.addFile(u"icons/refresh.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonRefresh.setIcon(icon)
        self.pushButtonRefresh.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButtonRefresh)

        self.comboBoxBaudRate = QComboBox(self.layoutWidget_2)
        self.comboBoxBaudRate.setObjectName(u"comboBoxBaudRate")
        sizePolicy1.setHeightForWidth(self.comboBoxBaudRate.sizePolicy().hasHeightForWidth())
        self.comboBoxBaudRate.setSizePolicy(sizePolicy1)
        self.comboBoxBaudRate.setMinimumSize(QSize(100, 0))
        self.comboBoxBaudRate.setModelColumn(0)

        self.horizontalLayout.addWidget(self.comboBoxBaudRate)

        self.pushButtonConnect = QPushButton(self.layoutWidget_2)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        self.pushButtonConnect.setMinimumSize(QSize(0, 32))
        icon1 = QIcon()
        icon1.addFile(u"icons/connect.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonConnect.setIcon(icon1)
        self.pushButtonConnect.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pushButtonConnect)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.textEdit_2 = QTextEdit(self.layoutWidget_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy2)
        self.textEdit_2.setMaximumSize(QSize(16777215, 32))

        self.horizontalLayout_2.addWidget(self.textEdit_2)

        self.pushButtonSend = QPushButton(self.layoutWidget_2)
        self.pushButtonSend.setObjectName(u"pushButtonSend")
        self.pushButtonSend.setEnabled(False)
        self.pushButtonSend.setMinimumSize(QSize(0, 32))
        icon2 = QIcon()
        icon2.addFile(u"icons/send.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonSend.setIcon(icon2)
        self.pushButtonSend.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButtonSend)

        self.pushButtonClearLogs = QPushButton(self.layoutWidget_2)
        self.pushButtonClearLogs.setObjectName(u"pushButtonClearLogs")
        self.pushButtonClearLogs.setMinimumSize(QSize(0, 32))
        icon3 = QIcon()
        icon3.addFile(u"icons/clear_logs.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonClearLogs.setIcon(icon3)
        self.pushButtonClearLogs.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButtonClearLogs)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.textEditLogs = QTextEdit(self.layoutWidget_2)
        self.textEditLogs.setObjectName(u"textEditLogs")
        sizePolicy2.setHeightForWidth(self.textEditLogs.sizePolicy().hasHeightForWidth())
        self.textEditLogs.setSizePolicy(sizePolicy2)
        self.textEditLogs.setMinimumSize(QSize(200, 0))

        self.verticalLayout_5.addWidget(self.textEditLogs)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(340, 10, 311, 271))
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 196, 134))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelNumberOfSteps = QLabel(self.widget)
        self.labelNumberOfSteps.setObjectName(u"labelNumberOfSteps")

        self.gridLayout.addWidget(self.labelNumberOfSteps, 2, 0, 1, 1)

        self.labelRotationDirection = QLabel(self.widget)
        self.labelRotationDirection.setObjectName(u"labelRotationDirection")

        self.gridLayout.addWidget(self.labelRotationDirection, 0, 0, 1, 1)

        self.labelStepDivider = QLabel(self.widget)
        self.labelStepDivider.setObjectName(u"labelStepDivider")

        self.gridLayout.addWidget(self.labelStepDivider, 1, 0, 1, 1)

        self.spinBoxSteps = QSpinBox(self.widget)
        self.spinBoxSteps.setObjectName(u"spinBoxSteps")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spinBoxSteps.sizePolicy().hasHeightForWidth())
        self.spinBoxSteps.setSizePolicy(sizePolicy3)
        self.spinBoxSteps.setMaximum(999999)
        self.spinBoxSteps.setValue(10)

        self.gridLayout.addWidget(self.spinBoxSteps, 2, 1, 1, 1)

        self.spinBoxVelocity = QSpinBox(self.widget)
        self.spinBoxVelocity.setObjectName(u"spinBoxVelocity")
        self.spinBoxVelocity.setMaximum(65535)
        self.spinBoxVelocity.setValue(200)

        self.gridLayout.addWidget(self.spinBoxVelocity, 3, 1, 1, 1)

        self.comboBoxStep = QComboBox(self.widget)
        self.comboBoxStep.setObjectName(u"comboBoxStep")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.comboBoxStep.sizePolicy().hasHeightForWidth())
        self.comboBoxStep.setSizePolicy(sizePolicy4)
        self.comboBoxStep.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.comboBoxStep, 1, 1, 1, 1)

        self.comboBoxDirection = QComboBox(self.widget)
        self.comboBoxDirection.setObjectName(u"comboBoxDirection")
        sizePolicy4.setHeightForWidth(self.comboBoxDirection.sizePolicy().hasHeightForWidth())
        self.comboBoxDirection.setSizePolicy(sizePolicy4)
        self.comboBoxDirection.setMinimumSize(QSize(100, 0))

        self.gridLayout.addWidget(self.comboBoxDirection, 0, 1, 1, 1)

        self.labelVelocity = QLabel(self.widget)
        self.labelVelocity.setObjectName(u"labelVelocity")

        self.gridLayout.addWidget(self.labelVelocity, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButtonDisconnect = QPushButton(Form)
        self.pushButtonDisconnect.setObjectName(u"pushButtonDisconnect")
        self.pushButtonDisconnect.setEnabled(False)
        self.pushButtonDisconnect.setGeometry(QRect(110, 430, 146, 32))
        self.pushButtonDisconnect.setMinimumSize(QSize(0, 32))
        icon4 = QIcon()
        icon4.addFile(u"icons/disconnect.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonDisconnect.setIcon(icon4)
        self.pushButtonDisconnect.setIconSize(QSize(24, 24))
        self.labelMoveTo = QLabel(Form)
        self.labelMoveTo.setObjectName(u"labelMoveTo")
        self.labelMoveTo.setGeometry(QRect(440, 400, 49, 16))
        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(660, 30, 38, 186))
        self.verticalLayout_7 = QVBoxLayout(self.widget1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButtonStartMotor = QPushButton(self.widget1)
        self.pushButtonStartMotor.setObjectName(u"pushButtonStartMotor")
        self.pushButtonStartMotor.setEnabled(False)
        self.pushButtonStartMotor.setMinimumSize(QSize(0, 32))
        icon5 = QIcon()
        icon5.addFile(u"icons/start_motor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonStartMotor.setIcon(icon5)
        self.pushButtonStartMotor.setIconSize(QSize(24, 24))
        self.pushButtonStartMotor.setCheckable(False)
        self.pushButtonStartMotor.setChecked(False)

        self.verticalLayout_7.addWidget(self.pushButtonStartMotor)

        self.pushButtonStopMotor = QPushButton(self.widget1)
        self.pushButtonStopMotor.setObjectName(u"pushButtonStopMotor")
        self.pushButtonStopMotor.setEnabled(False)
        self.pushButtonStopMotor.setMinimumSize(QSize(0, 32))
        icon6 = QIcon()
        icon6.addFile(u"icons/stop_motor.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonStopMotor.setIcon(icon6)
        self.pushButtonStopMotor.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.pushButtonStopMotor)

        self.pushButtonPoweroffMotor = QPushButton(self.widget1)
        self.pushButtonPoweroffMotor.setObjectName(u"pushButtonPoweroffMotor")
        self.pushButtonPoweroffMotor.setEnabled(False)
        self.pushButtonPoweroffMotor.setMinimumSize(QSize(0, 32))
        icon7 = QIcon()
        icon7.addFile(u"icons/poweroff.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonPoweroffMotor.setIcon(icon7)
        self.pushButtonPoweroffMotor.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.pushButtonPoweroffMotor)

        self.pushButtonSetZero = QPushButton(self.widget1)
        self.pushButtonSetZero.setObjectName(u"pushButtonSetZero")
        self.pushButtonSetZero.setEnabled(False)
        self.pushButtonSetZero.setMinimumSize(QSize(0, 32))
        icon8 = QIcon()
        icon8.addFile(u"icons/set_zero.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonSetZero.setIcon(icon8)
        self.pushButtonSetZero.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.pushButtonSetZero)

        self.pushButtonCheckState = QPushButton(self.widget1)
        self.pushButtonCheckState.setObjectName(u"pushButtonCheckState")
        self.pushButtonCheckState.setEnabled(False)
        self.pushButtonCheckState.setMinimumSize(QSize(0, 32))
        icon9 = QIcon()
        icon9.addFile(u"icons/check_state.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButtonCheckState.setIcon(icon9)
        self.pushButtonCheckState.setIconSize(QSize(24, 24))

        self.verticalLayout_7.addWidget(self.pushButtonCheckState)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBoxMotor.setTitle(QCoreApplication.translate("Form", u"Motor", None))
#if QT_CONFIG(tooltip)
        self.pushButtonRefresh.setToolTip(QCoreApplication.translate("Form", u"Refresh", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonRefresh.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonConnect.setToolTip(QCoreApplication.translate("Form", u"Connect", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonConnect.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonSend.setToolTip(QCoreApplication.translate("Form", u"Send", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSend.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonClearLogs.setToolTip(QCoreApplication.translate("Form", u"Clear logs", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonClearLogs.setText("")
        self.labelNumberOfSteps.setText(QCoreApplication.translate("Form", u"Number of steps", None))
        self.labelRotationDirection.setText(QCoreApplication.translate("Form", u"Direction", None))
        self.labelStepDivider.setText(QCoreApplication.translate("Form", u"Step Divider", None))
#if QT_CONFIG(tooltip)
        self.spinBoxSteps.setToolTip(QCoreApplication.translate("Form", u"Steps", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.spinBoxVelocity.setToolTip(QCoreApplication.translate("Form", u"Velosity", None))
#endif // QT_CONFIG(tooltip)
        self.labelVelocity.setText(QCoreApplication.translate("Form", u"Velocity", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Raw", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Control", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"Sequence", None))
#if QT_CONFIG(tooltip)
        self.pushButtonDisconnect.setToolTip(QCoreApplication.translate("Form", u"Disconnect", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonDisconnect.setText("")
        self.labelMoveTo.setText(QCoreApplication.translate("Form", u"Move to", None))
#if QT_CONFIG(tooltip)
        self.pushButtonStartMotor.setToolTip(QCoreApplication.translate("Form", u"Start Motor", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonStartMotor.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonStopMotor.setToolTip(QCoreApplication.translate("Form", u"Stop Motor", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonStopMotor.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonPoweroffMotor.setToolTip(QCoreApplication.translate("Form", u"Poweroff Motor", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonPoweroffMotor.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonSetZero.setToolTip(QCoreApplication.translate("Form", u"Set Zero", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonSetZero.setText("")
#if QT_CONFIG(tooltip)
        self.pushButtonCheckState.setToolTip(QCoreApplication.translate("Form", u"Check state", None))
#endif // QT_CONFIG(tooltip)
        self.pushButtonCheckState.setText("")
    # retranslateUi

