# -*- coding: utf-8 -*-

#
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SendRecvDialog(object):
    def setupUi(self, SendRecvDialog):
        SendRecvDialog.setObjectName("SendRecvDialog")
        SendRecvDialog.setWindowModality(QtCore.Qt.NonModal)
        SendRecvDialog.resize(868, 628)
        self.gridLayout_3 = QtWidgets.QGridLayout(SendRecvDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditIP = QtWidgets.QLineEdit(SendRecvDialog)
        self.lineEditIP.setObjectName("lineEditIP")
        self.gridLayout.addWidget(self.lineEditIP, 1, 1, 1, 1)
        self.spinBoxGain = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinBoxGain.setMinimum(1)
        self.spinBoxGain.setProperty("value", 40)
        self.spinBoxGain.setObjectName("spinBoxGain")
        self.gridLayout.addWidget(self.spinBoxGain, 5, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(SendRecvDialog)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(SendRecvDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.cbDevice = QtWidgets.QComboBox(SendRecvDialog)
        self.cbDevice.setObjectName("cbDevice")
        self.cbDevice.addItem("")
        self.cbDevice.addItem("")
        self.gridLayout.addWidget(self.cbDevice, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(SendRecvDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(SendRecvDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.labelIP = QtWidgets.QLabel(SendRecvDialog)
        self.labelIP.setObjectName("labelIP")
        self.gridLayout.addWidget(self.labelIP, 1, 0, 1, 1)
        self.spinBoxNRepeat = QtWidgets.QSpinBox(SendRecvDialog)
        self.spinBoxNRepeat.setMaximum(999999999)
        self.spinBoxNRepeat.setObjectName("spinBoxNRepeat")
        self.gridLayout.addWidget(self.spinBoxNRepeat, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(SendRecvDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.labelNRepeat = QtWidgets.QLabel(SendRecvDialog)
        self.labelNRepeat.setObjectName("labelNRepeat")
        self.gridLayout.addWidget(self.labelNRepeat, 6, 0, 1, 1)
        self.spinBoxFreq = KillerDoubleSpinBox(SendRecvDialog)
        self.spinBoxFreq.setDecimals(3)
        self.spinBoxFreq.setMinimum(0.001)
        self.spinBoxFreq.setMaximum(1000000000000.0)
        self.spinBoxFreq.setObjectName("spinBoxFreq")
        self.gridLayout.addWidget(self.spinBoxFreq, 2, 1, 1, 1)
        self.spinBoxSampleRate = KillerDoubleSpinBox(SendRecvDialog)
        self.spinBoxSampleRate.setDecimals(3)
        self.spinBoxSampleRate.setMinimum(0.001)
        self.spinBoxSampleRate.setMaximum(1000000000000.0)
        self.spinBoxSampleRate.setObjectName("spinBoxSampleRate")
        self.gridLayout.addWidget(self.spinBoxSampleRate, 3, 1, 1, 1)
        self.spinBoxBandwidth = KillerDoubleSpinBox(SendRecvDialog)
        self.spinBoxBandwidth.setDecimals(3)
        self.spinBoxBandwidth.setMinimum(0.001)
        self.spinBoxBandwidth.setMaximum(1000000000000.0)
        self.spinBoxBandwidth.setObjectName("spinBoxBandwidth")
        self.gridLayout.addWidget(self.spinBoxBandwidth, 4, 1, 1, 1)
        self.btnLockBWSR = QtWidgets.QToolButton(SendRecvDialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/data/icons/lock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLockBWSR.setIcon(icon)
        self.btnLockBWSR.setCheckable(True)
        self.btnLockBWSR.setChecked(True)
        self.btnLockBWSR.setObjectName("btnLockBWSR")
        self.gridLayout.addWidget(self.btnLockBWSR, 3, 2, 2, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtWidgets.QGroupBox(SendRecvDialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 14, 0, 1, 1)
        self.lSamplesSentText = QtWidgets.QLabel(self.groupBox)
        self.lSamplesSentText.setObjectName("lSamplesSentText")
        self.gridLayout_2.addWidget(self.lSamplesSentText, 13, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.lTimeText = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lTimeText.setFont(font)
        self.lTimeText.setObjectName("lTimeText")
        self.gridLayout_2.addWidget(self.lTimeText, 7, 0, 1, 1)
        self.lSamplesCapturedText = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSamplesCapturedText.sizePolicy().hasHeightForWidth())
        self.lSamplesCapturedText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lSamplesCapturedText.setFont(font)
        self.lSamplesCapturedText.setObjectName("lSamplesCapturedText")
        self.gridLayout_2.addWidget(self.lSamplesCapturedText, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnStart = QtWidgets.QToolButton(self.groupBox)
        self.btnStart.setMinimumSize(QtCore.QSize(42, 42))
        self.btnStart.setMaximumSize(QtCore.QSize(42, 42))
        self.btnStart.setText("")
        icon = QtGui.QIcon.fromTheme("media-record")
        self.btnStart.setIcon(icon)
        self.btnStart.setIconSize(QtCore.QSize(32, 32))
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnStop = QtWidgets.QToolButton(self.groupBox)
        self.btnStop.setMinimumSize(QtCore.QSize(42, 42))
        self.btnStop.setMaximumSize(QtCore.QSize(42, 42))
        self.btnStop.setText("")
        icon = QtGui.QIcon.fromTheme("media-playback-stop")
        self.btnStop.setIcon(icon)
        self.btnStop.setIconSize(QtCore.QSize(32, 32))
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.btnSave = QtWidgets.QToolButton(self.groupBox)
        self.btnSave.setMinimumSize(QtCore.QSize(42, 42))
        self.btnSave.setMaximumSize(QtCore.QSize(42, 42))
        icon = QtGui.QIcon.fromTheme("document-save")
        self.btnSave.setIcon(icon)
        self.btnSave.setIconSize(QtCore.QSize(32, 32))
        self.btnSave.setObjectName("btnSave")
        self.horizontalLayout.addWidget(self.btnSave)
        self.btnClear = QtWidgets.QToolButton(self.groupBox)
        self.btnClear.setMinimumSize(QtCore.QSize(42, 42))
        self.btnClear.setMaximumSize(QtCore.QSize(42, 42))
        self.btnClear.setText("")
        icon = QtGui.QIcon.fromTheme("view-refresh")
        self.btnClear.setIcon(icon)
        self.btnClear.setIconSize(QtCore.QSize(32, 32))
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.lSignalSizeText = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalSizeText.sizePolicy().hasHeightForWidth())
        self.lSignalSizeText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lSignalSizeText.setFont(font)
        self.lSignalSizeText.setObjectName("lSignalSizeText")
        self.gridLayout_2.addWidget(self.lSignalSizeText, 5, 0, 1, 1)
        self.lSamplesCaptured = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSamplesCaptured.sizePolicy().hasHeightForWidth())
        self.lSamplesCaptured.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lSamplesCaptured.setFont(font)
        self.lSamplesCaptured.setAlignment(QtCore.Qt.AlignCenter)
        self.lSamplesCaptured.setObjectName("lSamplesCaptured")
        self.gridLayout_2.addWidget(self.lSamplesCaptured, 4, 0, 1, 2)
        self.lTime = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lTime.setFont(font)
        self.lTime.setAlignment(QtCore.Qt.AlignCenter)
        self.lTime.setObjectName("lTime")
        self.gridLayout_2.addWidget(self.lTime, 10, 0, 1, 2)
        self.lSignalSize = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lSignalSize.sizePolicy().hasHeightForWidth())
        self.lSignalSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lSignalSize.setFont(font)
        self.lSignalSize.setAlignment(QtCore.Qt.AlignCenter)
        self.lSignalSize.setObjectName("lSignalSize")
        self.gridLayout_2.addWidget(self.lSignalSize, 6, 0, 1, 2)
        self.lblRepeatText = QtWidgets.QLabel(self.groupBox)
        self.lblRepeatText.setObjectName("lblRepeatText")
        self.gridLayout_2.addWidget(self.lblRepeatText, 11, 0, 1, 1)
        self.lblCurrentRepeatValue = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCurrentRepeatValue.setFont(font)
        self.lblCurrentRepeatValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lblCurrentRepeatValue.setObjectName("lblCurrentRepeatValue")
        self.gridLayout_2.addWidget(self.lblCurrentRepeatValue, 12, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.txtEditErrors = QtWidgets.QTextEdit(SendRecvDialog)
        self.txtEditErrors.setReadOnly(True)
        self.txtEditErrors.setObjectName("txtEditErrors")
        self.verticalLayout.addWidget(self.txtEditErrors)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 2, 1)
        self.graphicsView = LiveGraphicView(SendRecvDialog)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 2, 1)
        self.label_6 = QtWidgets.QLabel(SendRecvDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.sliderYscale = QtWidgets.QSlider(SendRecvDialog)
        self.sliderYscale.setMinimum(1)
        self.sliderYscale.setMaximum(10)
        self.sliderYscale.setProperty("value", 5)
        self.sliderYscale.setOrientation(QtCore.Qt.Vertical)
        self.sliderYscale.setObjectName("sliderYscale")
        self.gridLayout_3.addWidget(self.sliderYscale, 1, 2, 1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 5)
        self.gridLayout_3.setColumnStretch(2, 1)

        self.retranslateUi(SendRecvDialog)
        QtCore.QMetaObject.connectSlotsByName(SendRecvDialog)
        SendRecvDialog.setTabOrder(self.cbDevice, self.lineEditIP)
        SendRecvDialog.setTabOrder(self.lineEditIP, self.spinBoxFreq)
        SendRecvDialog.setTabOrder(self.spinBoxFreq, self.spinBoxSampleRate)
        SendRecvDialog.setTabOrder(self.spinBoxSampleRate, self.spinBoxBandwidth)
        SendRecvDialog.setTabOrder(self.spinBoxBandwidth, self.spinBoxGain)
        SendRecvDialog.setTabOrder(self.spinBoxGain, self.spinBoxNRepeat)
        SendRecvDialog.setTabOrder(self.spinBoxNRepeat, self.btnStart)
        SendRecvDialog.setTabOrder(self.btnStart, self.btnStop)
        SendRecvDialog.setTabOrder(self.btnStop, self.btnSave)
        SendRecvDialog.setTabOrder(self.btnSave, self.btnClear)
        SendRecvDialog.setTabOrder(self.btnClear, self.graphicsView)
        SendRecvDialog.setTabOrder(self.graphicsView, self.sliderYscale)
        SendRecvDialog.setTabOrder(self.sliderYscale, self.txtEditErrors)

    def retranslateUi(self, SendRecvDialog):
        _translate = QtCore.QCoreApplication.translate
        SendRecvDialog.setWindowTitle(_translate("SendRecvDialog", "Record Signal"))
        self.lineEditIP.setText(_translate("SendRecvDialog", "192.168.10.2"))
        self.label_4.setText(_translate("SendRecvDialog", "Gain:"))
        self.label_5.setText(_translate("SendRecvDialog", "Bandwidth (Hz):"))
        self.cbDevice.setItemText(0, _translate("SendRecvDialog", "USRP"))
        self.cbDevice.setItemText(1, _translate("SendRecvDialog", "HackRF"))
        self.label_3.setText(_translate("SendRecvDialog", "Device:"))
        self.label_2.setText(_translate("SendRecvDialog", "Sample rate (Sps):"))
        self.labelIP.setText(_translate("SendRecvDialog", "IP address:"))
        self.spinBoxNRepeat.setSpecialValueText(_translate("SendRecvDialog", "Infinite"))
        self.label.setText(_translate("SendRecvDialog", "Frequency (Hz):"))
        self.labelNRepeat.setText(_translate("SendRecvDialog", "Repeat:"))
        self.btnLockBWSR.setText(_translate("SendRecvDialog", "..."))
        self.progressBar.setFormat(_translate("SendRecvDialog", "%v/%m"))
        self.lSamplesSentText.setText(_translate("SendRecvDialog", "Samples sent:"))
        self.lTimeText.setText(_translate("SendRecvDialog", "Time (in seconds):"))
        self.lSamplesCapturedText.setText(_translate("SendRecvDialog", "Samples captured:"))
        self.btnStart.setToolTip(_translate("SendRecvDialog", "Record signal"))
        self.btnStop.setToolTip(_translate("SendRecvDialog", "Stop recording"))
        self.btnSave.setText(_translate("SendRecvDialog", "Save..."))
        self.btnClear.setToolTip(_translate("SendRecvDialog", "Clear"))
        self.lSignalSizeText.setText(_translate("SendRecvDialog", "Signal size (in MiB):"))
        self.lSamplesCaptured.setText(_translate("SendRecvDialog", "0"))
        self.lTime.setText(_translate("SendRecvDialog", "0"))
        self.lSignalSize.setText(_translate("SendRecvDialog", "0"))
        self.lblRepeatText.setText(_translate("SendRecvDialog", "Current iteration:"))
        self.lblCurrentRepeatValue.setText(_translate("SendRecvDialog", "0"))
        self.label_6.setText(_translate("SendRecvDialog", "Y-Scale"))

from urh.ui.KillerDoubleSpinBox import KillerDoubleSpinBox
from urh.ui.views.LiveGraphicView import LiveGraphicView
from . import urh_rc
