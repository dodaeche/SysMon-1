# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SysMon.ui'
#
# Created: Tue Sep 09 16:13:55 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(392, 323)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(336, 282))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 260))
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setMinimumSize(QtCore.QSize(351, 121))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.widget = QtGui.QWidget(self.groupBox_3)
        self.widget.setGeometry(QtCore.QRect(10, 20, 342, 91))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.labelComputerName = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelComputerName.sizePolicy().hasHeightForWidth())
        self.labelComputerName.setSizePolicy(sizePolicy)
        self.labelComputerName.setMinimumSize(QtCore.QSize(340, 0))
        self.labelComputerName.setObjectName(_fromUtf8("labelComputerName"))
        self.verticalLayout_2.addWidget(self.labelComputerName)
        self.labelOS = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelOS.sizePolicy().hasHeightForWidth())
        self.labelOS.setSizePolicy(sizePolicy)
        self.labelOS.setMinimumSize(QtCore.QSize(340, 0))
        self.labelOS.setObjectName(_fromUtf8("labelOS"))
        self.verticalLayout_2.addWidget(self.labelOS)
        self.labelProcFam = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelProcFam.sizePolicy().hasHeightForWidth())
        self.labelProcFam.setSizePolicy(sizePolicy)
        self.labelProcFam.setMinimumSize(QtCore.QSize(340, 0))
        self.labelProcFam.setObjectName(_fromUtf8("labelProcFam"))
        self.verticalLayout_2.addWidget(self.labelProcFam)
        self.labelNUsers = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelNUsers.sizePolicy().hasHeightForWidth())
        self.labelNUsers.setSizePolicy(sizePolicy)
        self.labelNUsers.setMinimumSize(QtCore.QSize(340, 0))
        self.labelNUsers.setObjectName(_fromUtf8("labelNUsers"))
        self.verticalLayout_2.addWidget(self.labelNUsers)
        self.labelUptime = QtGui.QLabel(self.widget)
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
        self.progressBarStatusMemory.setGeometry(QtCore.QRect(130, 20, 201, 23))
        self.progressBarStatusMemory.setProperty(_fromUtf8("value"), 24)
        self.progressBarStatusMemory.setObjectName(_fromUtf8("progressBarStatusMemory"))
        self.progressBarStatusCPU = QtGui.QProgressBar(self.groupBox_5)
        self.progressBarStatusCPU.setGeometry(QtCore.QRect(130, 60, 201, 23))
        self.progressBarStatusCPU.setProperty(_fromUtf8("value"), 24)
        self.progressBarStatusCPU.setObjectName(_fromUtf8("progressBarStatusCPU"))
        self.label_101 = QtGui.QLabel(self.groupBox_5)
        self.label_101.setGeometry(QtCore.QRect(20, 20, 101, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_101.setFont(font)
        self.label_101.setObjectName(_fromUtf8("label_101"))
        self.label_102 = QtGui.QLabel(self.groupBox_5)
        self.label_102.setGeometry(QtCore.QRect(20, 60, 111, 16))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.label_102.setFont(font)
        self.label_102.setObjectName(_fromUtf8("label_102"))
        self.labelMaxMem = QtGui.QLabel(self.groupBox_5)
        self.labelMaxMem.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.labelMaxMem.setObjectName(_fromUtf8("labelMaxMem"))
        self.labelCPUCount = QtGui.QLabel(self.groupBox_5)
        self.labelCPUCount.setGeometry(QtCore.QRect(20, 80, 91, 16))
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
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame = QtGui.QFrame(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
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
        self.labelLastUpdate.setGeometry(QtCore.QRect(100, 10, 200, 20))
        self.labelLastUpdate.setMinimumSize(QtCore.QSize(200, 0))
        self.labelLastUpdate.setMaximumSize(QtCore.QSize(210, 16777215))
        self.labelLastUpdate.setObjectName(_fromUtf8("labelLastUpdate"))
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
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
        self.gridLayout_4.addWidget(self.tableWidgetProcess, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
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
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuUpdate_Rate = QtGui.QMenu(self.menuOptions)
        self.menuUpdate_Rate.setObjectName(_fromUtf8("menuUpdate_Rate"))
        self.menuUpdate_Rate_2 = QtGui.QMenu(self.menuOptions)
        self.menuUpdate_Rate_2.setObjectName(_fromUtf8("menuUpdate_Rate_2"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.action60Seconds = QtGui.QAction(MainWindow)
        self.action60Seconds.setObjectName(_fromUtf8("action60Seconds"))
        self.action300Seconds = QtGui.QAction(MainWindow)
        self.action300Seconds.setObjectName(_fromUtf8("action300Seconds"))
        self.action600Seconds = QtGui.QAction(MainWindow)
        self.action600Seconds.setObjectName(_fromUtf8("action600Seconds"))
        self.action3600Seconds = QtGui.QAction(MainWindow)
        self.action3600Seconds.setObjectName(_fromUtf8("action3600Seconds"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionCheck_Matlab_Licenses = QtGui.QAction(MainWindow)
        self.actionCheck_Matlab_Licenses.setObjectName(_fromUtf8("actionCheck_Matlab_Licenses"))
        self.action1_Second = QtGui.QAction(MainWindow)
        self.action1_Second.setObjectName(_fromUtf8("action1_Second"))
        self.action2_Seconds = QtGui.QAction(MainWindow)
        self.action2_Seconds.setObjectName(_fromUtf8("action2_Seconds"))
        self.action5_Seconds = QtGui.QAction(MainWindow)
        self.action5_Seconds.setObjectName(_fromUtf8("action5_Seconds"))
        self.action10_Seconds = QtGui.QAction(MainWindow)
        self.action10_Seconds.setObjectName(_fromUtf8("action10_Seconds"))
        self.menuFile.addAction(self.actionExit)
        self.menuUpdate_Rate.addAction(self.action60Seconds)
        self.menuUpdate_Rate.addAction(self.action300Seconds)
        self.menuUpdate_Rate.addAction(self.action600Seconds)
        self.menuUpdate_Rate.addAction(self.action3600Seconds)
        self.menuUpdate_Rate_2.addAction(self.action1_Second)
        self.menuUpdate_Rate_2.addAction(self.action2_Seconds)
        self.menuUpdate_Rate_2.addAction(self.action5_Seconds)
        self.menuUpdate_Rate_2.addAction(self.action10_Seconds)
        self.menuOptions.addAction(self.menuUpdate_Rate_2.menuAction())
        self.menuOptions.addAction(self.menuUpdate_Rate.menuAction())
        self.menuOptions.addAction(self.actionCheck_Matlab_Licenses)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "System Monitor", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "System Info", None, QtGui.QApplication.UnicodeUTF8))
        self.labelComputerName.setText(QtGui.QApplication.translate("MainWindow", "Computer Name: ", None, QtGui.QApplication.UnicodeUTF8))
        self.labelOS.setText(QtGui.QApplication.translate("MainWindow", "Operating System:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelProcFam.setText(QtGui.QApplication.translate("MainWindow", "Processor Family:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelNUsers.setText(QtGui.QApplication.translate("MainWindow", "Number of Users Logged On:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUptime.setText(QtGui.QApplication.translate("MainWindow", "System Uptime: ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Composite System Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_101.setText(QtGui.QApplication.translate("MainWindow", "Memory Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_102.setText(QtGui.QApplication.translate("MainWindow", "CPU Usage", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMaxMem.setText(QtGui.QApplication.translate("MainWindow", "Max Mem:", None, QtGui.QApplication.UnicodeUTF8))
        self.labelCPUCount.setText(QtGui.QApplication.translate("MainWindow", "CPU count:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "System", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonUpdate.setText(QtGui.QApplication.translate("MainWindow", "Hold Updates", None, QtGui.QApplication.UnicodeUTF8))
        self.labelLastUpdate.setText(QtGui.QApplication.translate("MainWindow", "Last Update: ", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.setSortingEnabled(True)
        self.tableWidgetProcess.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "PID", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "USER", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "CPU%", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "MEM%", None, QtGui.QApplication.UnicodeUTF8))
        self.tableWidgetProcess.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "NAME", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Processes", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonCPU.setText(QtGui.QApplication.translate("MainWindow", "Sort by CPU", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButtonMem.setText(QtGui.QApplication.translate("MainWindow", "Sort by Memory", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Users", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUpdate_Rate.setTitle(QtGui.QApplication.translate("MainWindow", "Display Period", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUpdate_Rate_2.setTitle(QtGui.QApplication.translate("MainWindow", "Update Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.action60Seconds.setText(QtGui.QApplication.translate("MainWindow", "60 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.action300Seconds.setText(QtGui.QApplication.translate("MainWindow", "300 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.action600Seconds.setText(QtGui.QApplication.translate("MainWindow", "600 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.action3600Seconds.setText(QtGui.QApplication.translate("MainWindow", "3600 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCheck_Matlab_Licenses.setText(QtGui.QApplication.translate("MainWindow", "Check Matlab Licenses", None, QtGui.QApplication.UnicodeUTF8))
        self.action1_Second.setText(QtGui.QApplication.translate("MainWindow", "1 Second", None, QtGui.QApplication.UnicodeUTF8))
        self.action2_Seconds.setText(QtGui.QApplication.translate("MainWindow", "2 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.action5_Seconds.setText(QtGui.QApplication.translate("MainWindow", "5 Seconds", None, QtGui.QApplication.UnicodeUTF8))
        self.action10_Seconds.setText(QtGui.QApplication.translate("MainWindow", "10 Seconds", None, QtGui.QApplication.UnicodeUTF8))

