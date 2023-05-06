# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ntd.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoTopDomain(object):
    def setupUi(self, NoTopDomain):
        NoTopDomain.setObjectName("NoTopDomain")
        NoTopDomain.resize(458, 447)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(9)
        NoTopDomain.setFont(font)
        self.centralwidget = QtWidgets.QWidget(NoTopDomain)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.PigeonGames = QtWidgets.QTabWidget(self.centralwidget)
        self.PigeonGames.setObjectName("PigeonGames")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.StudentRunning = QtWidgets.QLabel(self.tab)
        self.StudentRunning.setObjectName("StudentRunning")
        self.gridLayout_4.addWidget(self.StudentRunning, 0, 0, 1, 1)
        self.GBing = QtWidgets.QLabel(self.tab)
        self.GBing.setObjectName("GBing")
        self.gridLayout_4.addWidget(self.GBing, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.KillCurrent = QtWidgets.QPushButton(self.groupBox)
        self.KillCurrent.setEnabled(False)
        self.KillCurrent.setObjectName("KillCurrent")
        self.gridLayout_2.addWidget(self.KillCurrent, 0, 2, 1, 1)
        self.GBWindowed = QtWidgets.QPushButton(self.groupBox)
        self.GBWindowed.setObjectName("GBWindowed")
        self.gridLayout_2.addWidget(self.GBWindowed, 1, 0, 1, 1)
        self.KillSome = QtWidgets.QLineEdit(self.groupBox)
        self.KillSome.setObjectName("KillSome")
        self.gridLayout_2.addWidget(self.KillSome, 1, 2, 1, 1)
        self.KillTD = QtWidgets.QPushButton(self.groupBox)
        self.KillTD.setObjectName("KillTD")
        self.gridLayout_2.addWidget(self.KillTD, 0, 7, 1, 6)
        self.HangUpTD = QtWidgets.QPushButton(self.groupBox)
        self.HangUpTD.setObjectName("HangUpTD")
        self.gridLayout_2.addWidget(self.HangUpTD, 0, 0, 1, 1)
        self.TDPwd = QtWidgets.QLineEdit(self.groupBox)
        self.TDPwd.setEnabled(True)
        self.TDPwd.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.TDPwd.setReadOnly(True)
        self.TDPwd.setObjectName("TDPwd")
        self.gridLayout_2.addWidget(self.TDPwd, 1, 7, 1, 6)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.FireWall = QtWidgets.QCheckBox(self.groupBox_2)
        self.FireWall.setObjectName("FireWall")
        self.gridLayout_3.addWidget(self.FireWall, 2, 2, 1, 1)
        self.NoImg = QtWidgets.QPushButton(self.groupBox_2)
        self.NoImg.setObjectName("NoImg")
        self.gridLayout_3.addWidget(self.NoImg, 4, 1, 1, 1)
        self.feedback = QtWidgets.QPushButton(self.groupBox_2)
        self.feedback.setObjectName("feedback")
        self.gridLayout_3.addWidget(self.feedback, 3, 1, 1, 1)
        self.WebsiteYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.WebsiteYes.setObjectName("WebsiteYes")
        self.gridLayout_3.addWidget(self.WebsiteYes, 2, 0, 1, 1)
        self.ToolsYes = QtWidgets.QPushButton(self.groupBox_2)
        self.ToolsYes.setObjectName("ToolsYes")
        self.gridLayout_3.addWidget(self.ToolsYes, 4, 0, 1, 1)
        self.NoShutdown = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoShutdown.setObjectName("NoShutdown")
        self.gridLayout_3.addWidget(self.NoShutdown, 2, 1, 1, 1)
        self.USBYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.USBYes.setObjectName("USBYes")
        self.gridLayout_3.addWidget(self.USBYes, 0, 2, 1, 2)
        self.IamTop = QtWidgets.QCheckBox(self.groupBox_2)
        self.IamTop.setObjectName("IamTop")
        self.gridLayout_3.addWidget(self.IamTop, 0, 0, 1, 1)
        self.KeyboardYes = QtWidgets.QCheckBox(self.groupBox_2)
        self.KeyboardYes.setObjectName("KeyboardYes")
        self.gridLayout_3.addWidget(self.KeyboardYes, 0, 1, 1, 1)
        self.NoBlackScreen = QtWidgets.QCheckBox(self.groupBox_2)
        self.NoBlackScreen.setObjectName("NoBlackScreen")
        self.gridLayout_3.addWidget(self.NoBlackScreen, 3, 0, 1, 1)
        self.RestartExplorer = QtWidgets.QPushButton(self.groupBox_2)
        self.RestartExplorer.setObjectName("RestartExplorer")
        self.gridLayout_3.addWidget(self.RestartExplorer, 3, 2, 1, 2)
        self.NoRes = QtWidgets.QPushButton(self.groupBox_2)
        self.NoRes.setObjectName("NoRes")
        self.gridLayout_3.addWidget(self.NoRes, 4, 2, 1, 2)
        self.gridLayout_4.addWidget(self.groupBox_2, 2, 0, 1, 2)
        self.WhereIsMyFile = QtWidgets.QPushButton(self.tab)
        self.WhereIsMyFile.setObjectName("WhereIsMyFile")
        self.gridLayout_4.addWidget(self.WhereIsMyFile, 3, 0, 1, 2)
        self.PigeonGames.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_6.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_6.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 2, 0, 1, 1)
        self.PigeonGames.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.PigeonGames, 0, 0, 1, 1)
        NoTopDomain.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(NoTopDomain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 458, 26))
        self.menubar.setObjectName("menubar")
        NoTopDomain.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(NoTopDomain)
        self.statusbar.setObjectName("statusbar")
        NoTopDomain.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(NoTopDomain)
        self.action1.setObjectName("action1")
        self.action_1 = QtWidgets.QAction(NoTopDomain)
        self.action_1.setObjectName("action_1")
        self.action_2 = QtWidgets.QAction(NoTopDomain)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(NoTopDomain)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(NoTopDomain)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(NoTopDomain)
        self.action_5.setObjectName("action_5")

        self.retranslateUi(NoTopDomain)
        self.PigeonGames.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NoTopDomain)

    def retranslateUi(self, NoTopDomain):
        _translate = QtCore.QCoreApplication.translate
        NoTopDomain.setWindowTitle(_translate("NoTopDomain", "NoTopDomain v0.01 By LYX"))
        self.StudentRunning.setText(_translate("NoTopDomain", "极域：<span style=\"color:grey\">检测中</span>"))
        self.GBing.setText(_translate("NoTopDomain", "广播：<span style=\"color:grey\">检测中</span>"))
        self.groupBox.setTitle(_translate("NoTopDomain", "常用功能"))
        self.KillCurrent.setText(_translate("NoTopDomain", "杀掉进程↓"))
        self.GBWindowed.setText(_translate("NoTopDomain", "解冻全屏"))
        self.KillSome.setPlaceholderText(_translate("NoTopDomain", "*.exe/进程PID"))
        self.KillTD.setText(_translate("NoTopDomain", "杀掉极域！！！"))
        self.HangUpTD.setText(_translate("NoTopDomain", "挂起极域"))
        self.TDPwd.setText(_translate("NoTopDomain", "获取密码中..."))
        self.groupBox_2.setTitle(_translate("NoTopDomain", "限制解除"))
        self.FireWall.setText(_translate("NoTopDomain", "防火墙拦截(入站)"))
        self.NoImg.setText(_translate("NoTopDomain", "解除映像劫持"))
        self.feedback.setText(_translate("NoTopDomain", "反馈问题"))
        self.WebsiteYes.setText(_translate("NoTopDomain", "解除网站限制"))
        self.ToolsYes.setText(_translate("NoTopDomain", "解工具/限制"))
        self.NoShutdown.setText(_translate("NoTopDomain", "脱离远程关机"))
        self.USBYes.setText(_translate("NoTopDomain", "解除USB/应用限制"))
        self.IamTop.setText(_translate("NoTopDomain", "置顶窗口"))
        self.KeyboardYes.setText(_translate("NoTopDomain", "解除键盘限制"))
        self.NoBlackScreen.setText(_translate("NoTopDomain", "屏蔽黑屏安静"))
        self.RestartExplorer.setText(_translate("NoTopDomain", "重启资源管理器"))
        self.NoRes.setText(_translate("NoTopDomain", "尝试破解还原卡"))
        self.WhereIsMyFile.setText(_translate("NoTopDomain", "接收遗漏文件"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab), _translate("NoTopDomain", "极域"))
        self.checkBox.setText(_translate("NoTopDomain", "隐藏托盘"))
        self.checkBox_2.setText(_translate("NoTopDomain", "修复"))
        self.pushButton.setText(_translate("NoTopDomain", "以System权限重启"))
        self.PigeonGames.setTabText(self.PigeonGames.indexOf(self.tab_3), _translate("NoTopDomain", "设置"))
        self.action1.setText(_translate("NoTopDomain", "1"))
        self.action_1.setText(_translate("NoTopDomain", "关于"))
        self.action_2.setText(_translate("NoTopDomain", "设置"))
        self.action_3.setText(_translate("NoTopDomain", "启动TSK"))
        self.action_4.setText(_translate("NoTopDomain", "运行..."))
        self.action_5.setText(_translate("NoTopDomain", "映像劫持"))