# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sysmonTabs.ui'
#
# Created: Wed Sep 17 15:26:48 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(427, 323)
        self.verticalLayout_4 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tabWidget = QtGui.QTabWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 260))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(351, 121))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 502, 91))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelComputerName = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComputerName.sizePolicy().hasHeightForWidth())
        self.labelComputerName.setSizePolicy(sizePolicy)
        self.labelComputerName.setMinimumSize(QtCore.QSize(500, 0))
        self.labelComputerName.setObjectName(_fromUtf8("labelComputerName"))
        self.verticalLayout_2.addWidget(self.labelComputerName)
        self.labelOS = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOS.sizePolicy().hasHeightForWidth())
        self.labelOS.setSizePolicy(sizePolicy)
        self.labelOS.setMinimumSize(QtCore.QSize(500, 0))
        self.labelOS.setObjectName(_fromUtf8("labelOS"))
        self.verticalLayout_2.addWidget(self.labelOS)
        self.labelProcFam = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProcFam.sizePolicy().hasHeightForWidth())
        self.labelProcFam.setSizePolicy(sizePolicy)
        self.labelProcFam.setMinimumSize(QtCore.QSize(500, 0))
        self.labelProcFam.setObjectName(_fromUtf8("labelProcFam"))
        self.verticalLayout_2.addWidget(self.labelProcFam)
        self.labelNUsers = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNUsers.sizePolicy().hasHeightForWidth())
        self.labelNUsers.setSizePolicy(sizePolicy)
        self.labelNUsers.setMinimumSize(QtCore.QSize(340, 0))
        self.labelNUsers.setObjectName(_fromUtf8("labelNUsers"))
        self.verticalLayout_2.addWidget(self.labelNUsers)
        self.labelUptime = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelUptime.sizePolicy().hasHeightForWidth())
        self.labelUptime.setSizePolicy(sizePolicy)
        self.labelUptime.setMinimumSize(QtCore.QSize(340, 0))
        self.labelUptime.setObjectName(_fromUtf8("labelUptime"))
        self.verticalLayout_2.addWidget(self.labelUptime)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.tab)
        self.groupBox_5.setMinimumSize(QtCore.QSize(271, 101))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setUnderline(False)
        font.setBold(False)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.progressBarStatusMemory = QtGui.QProgressBar(self.groupBox_5)
        self.progressBarStatusMemory.setGeometry(QtCore.QRect(200, 20, 171, 23))
        self.progressBarStatusMemory.setProperty(_fromUtf8("value"), 24)
        self.progressBarStatusMemory.setObjectName(_fromUtf8("progressBarStatusMemory"))
        self.progressBarStatusCPU = QtGui.QProgressBar(self.groupBox_5)
        self.progressBarStatusCPU.setGeometry(QtCore.QRect(200, 60, 171, 23))
        self.progressBarStatusCPU.setProperty(_fromUtf8("value"), 24)
        self.progressBarStatusCPU.setObjectName(_fromUtf8("progressBarStatusCPU"))
        self.labelMemUsage = QtGui.QLabel(self.groupBox_5)
        self.labelMemUsage.setGeometry(QtCore.QRect(20, 20, 171, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.labelMemUsage.setFont(font)
        self.labelMemUsage.setObjectName(_fromUtf8("labelMemUsage"))
        self.label_102 = QtGui.QLabel(self.groupBox_5)
        self.label_102.setGeometry(QtCore.QRect(20, 60, 141, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_102.setFont(font)
        self.label_102.setObjectName(_fromUtf8("label_102"))
        self.labelMaxMem = QtGui.QLabel(self.groupBox_5)
        self.labelMaxMem.setGeometry(QtCore.QRect(20, 40, 171, 16))
        self.labelMaxMem.setObjectName(_fromUtf8("labelMaxMem"))
        self.labelCPUCount = QtGui.QLabel(self.groupBox_5)
        self.labelCPUCount.setGeometry(QtCore.QRect(20, 80, 141, 16))
        self.labelCPUCount.setObjectName(_fromUtf8("labelCPUCount"))
        self.gridLayout_5.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.framePlot = QtGui.QFrame(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.framePlot.sizePolicy().hasHeightForWidth())
        self.framePlot.setSizePolicy(sizePolicy)
        self.framePlot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.framePlot.setFrameShadow(QtGui.QFrame.Raised)
        self.framePlot.setObjectName(_fromUtf8("framePlot"))
        self.gridLayout_2.addWidget(self.framePlot, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout = QtGui.QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 35))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 35))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButtonUpdate = QtGui.QPushButton(self.groupBox)
        self.pushButtonUpdate.setGeometry(QtCore.QRect(10, 10, 80, 15))
        self.pushButtonUpdate.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButtonUpdate.setMaximumSize(QtCore.QSize(80, 15))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButtonUpdate.setFont(font)
        self.pushButtonUpdate.setObjectName(_fromUtf8("pushButtonUpdate"))
        self.labelLastUpdate = QtGui.QLabel(self.groupBox)
        self.labelLastUpdate.setGeometry(QtCore.QRect(100, 10, 251, 20))
        self.labelLastUpdate.setMinimumSize(QtCore.QSize(200, 0))
        self.labelLastUpdate.setMaximumSize(QtCore.QSize(300, 16777215))
        self.labelLastUpdate.setObjectName(_fromUtf8("labelLastUpdate"))
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tableWidgetProcess = QtGui.QTableWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(100)
        sizePolicy.setHeightForWidth(self.tableWidgetProcess.sizePolicy().hasHeightForWidth())
        self.tableWidgetProcess.setSizePolicy(sizePolicy)
        self.tableWidgetProcess.setMinimumSize(QtCore.QSize(311, 201))
        self.tableWidgetProcess.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidgetProcess.setRowCount(10)
        self.tableWidgetProcess.setColumnCount(5)
        self.tableWidgetProcess.setObjectName(_fromUtf8("tableWidgetProcess"))
        self.tableWidgetProcess.setColumnCount(5)
        self.tableWidgetProcess.setRowCount(10)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcess.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcess.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcess.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcess.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetProcess.setHorizontalHeaderItem(4, item)
        self.tableWidgetProcess.horizontalHeader().setDefaultSectionSize(57)
        self.tableWidgetProcess.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetProcess.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetProcess.verticalHeader().setVisible(False)
        self.tableWidgetProcess.verticalHeader().setDefaultSectionSize(20)
        self.tableWidgetProcess.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidgetProcess)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(331, 31))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 31))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.radioButtonCPU = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonCPU.setGeometry(QtCore.QRect(10, 0, 100, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonCPU.sizePolicy().hasHeightForWidth())
        self.radioButtonCPU.setSizePolicy(sizePolicy)
        self.radioButtonCPU.setMinimumSize(QtCore.QSize(100, 21))
        self.radioButtonCPU.setObjectName(_fromUtf8("radioButtonCPU"))
        self.radioButtonMem = QtGui.QRadioButton(self.groupBox_2)
        self.radioButtonMem.setGeometry(QtCore.QRect(116, 0, 120, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonMem.sizePolicy().hasHeightForWidth())
        self.radioButtonMem.setSizePolicy(sizePolicy)
        self.radioButtonMem.setMinimumSize(QtCore.QSize(120, 21))
        self.radioButtonMem.setChecked(True)
        self.radioButtonMem.setObjectName(_fromUtf8("radioButtonMem"))
        self.verticalLayout.addWidget(self.groupBox_2)
        self.frameBar = QtGui.QFrame(self.tab_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBar.sizePolicy().hasHeightForWidth())
        self.frameBar.setSizePolicy(sizePolicy)
        self.frameBar.setMinimumSize(QtCore.QSize(331, 201))
        self.frameBar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameBar.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBar.setObjectName(_fromUtf8("frameBar"))
        self.verticalLayout.addWidget(self.frameBar)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.tab_5)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_4.setMinimumSize(QtCore.QSize(160, 180))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.radioButton1Sec = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton1Sec.setGeometry(QtCore.QRect(20, 30, 141, 17))
        self.radioButton1Sec.setObjectName(_fromUtf8("radioButton1Sec"))
        self.radioButton2Secs = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton2Secs.setGeometry(QtCore.QRect(20, 60, 141, 17))
        self.radioButton2Secs.setChecked(True)
        self.radioButton2Secs.setObjectName(_fromUtf8("radioButton2Secs"))
        self.radioButton5Secs = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton5Secs.setGeometry(QtCore.QRect(20, 90, 141, 17))
        self.radioButton5Secs.setObjectName(_fromUtf8("radioButton5Secs"))
        self.radioButton10Secs = QtGui.QRadioButton(self.groupBox_4)
        self.radioButton10Secs.setGeometry(QtCore.QRect(20, 120, 141, 17))
        self.radioButton10Secs.setObjectName(_fromUtf8("radioButton10Secs"))
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_6.setMinimumSize(QtCore.QSize(160, 180))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.radioButton60Secs = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton60Secs.setGeometry(QtCore.QRect(10, 30, 161, 17))
        self.radioButton60Secs.setChecked(True)
        self.radioButton60Secs.setObjectName(_fromUtf8("radioButton60Secs"))
        self.radioButton300Secs = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton300Secs.setGeometry(QtCore.QRect(10, 60, 161, 17))
        self.radioButton300Secs.setObjectName(_fromUtf8("radioButton300Secs"))
        self.radioButton600Secs = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton600Secs.setGeometry(QtCore.QRect(10, 90, 161, 17))
        self.radioButton600Secs.setObjectName(_fromUtf8("radioButton600Secs"))
        self.radioButton3600Secs = QtGui.QRadioButton(self.groupBox_6)
        self.radioButton3600Secs.setGeometry(QtCore.QRect(10, 120, 161, 17))
        self.radioButton3600Secs.setObjectName(_fromUtf8("radioButton3600Secs"))
        self.horizontalLayout.addWidget(self.groupBox_6)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.radioButton1Sec, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.radioButton1Sec.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "System Info", None, QtGui.QApplication.UnicodeUTF8))
        self.labelComputerName.setText(QtGui.QApplication.translate("Form", "Computer Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOS.setText(QtGui.QApplication.translate("Form", "Operating System:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProcFam.setText(QtGui.QApplication.translate("Form", "Processor Family:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNUsers.setText(QtGui.QApplication.translate("Form", "Number of Users Logged On:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUptime.setText(QtGui.QApplication.translate("Form", "System Uptime: ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "Composite System Status", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMemUsage.setText(QtGui.QApplication.translate("Form", "Memory Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_102.setText(QtGui.QApplication.translate("Form", "Composite CPU Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMaxMem.setText(QtGui.QApplication.translate("Form", "Max Mem:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCPUCount.setText(QtGui.QApplication.translate("Form", "CPU count:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "System", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("Form", "Hold Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLastUpdate.setText(QtGui.QApplication.translate("Form", "Last Update: ", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.setSortingEnabled(True)
        self.tableWidgetProcess.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Form", "PID", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Form", "USER", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Form", "CPU%", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Form", "MEM%", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Form", "NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("Form", "Processes", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCPU.setText(QtGui.QApplication.translate("Form", "Sort by CPU", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonMem.setText(QtGui.QApplication.translate("Form", "Sort by Memory", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("Form", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("Form", "Update Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton1Sec.setText(QtGui.QApplication.translate("Form", "1 Second", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton2Secs.setText(QtGui.QApplication.translate("Form", "2 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton5Secs.setText(QtGui.QApplication.translate("Form", "5 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton10Secs.setText(QtGui.QApplication.translate("Form", "10 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("Form", "Display Period", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton60Secs.setText(QtGui.QApplication.translate("Form", "60 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton300Secs.setText(QtGui.QApplication.translate("Form", "300 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton600Secs.setText(QtGui.QApplication.translate("Form", "600 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton3600Secs.setText(QtGui.QApplication.translate("Form", "3600 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("Form", "Options", None, QtGui.QApplication.UnicodeUTF8))

