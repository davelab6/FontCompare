# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/fontCompare.ui'
#
# Created: Sun Jul 21 12:02:50 2013
# Created: Sun Jul 21 00:50:14 2013
#      by: PyQt4 UI code generator 4.9.3
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
        MainWindow.resize(801, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 801, 561))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(9, 29, 781, 241))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.groupBox_7 = QtGui.QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_7)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 50, 241, 149))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.layoutWidget_2)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_18 = QtGui.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_18)
        self.NumeralScoreBar = QtGui.QProgressBar(self.layoutWidget_2)
        self.NumeralScoreBar.setMaximum(10)
        self.NumeralScoreBar.setProperty("value", 0)
        self.NumeralScoreBar.setObjectName(_fromUtf8("NumeralScoreBar"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.NumeralScoreBar)
        self.label_19 = QtGui.QLabel(self.layoutWidget_2)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_19)
        self.ConsonantScoreBar = QtGui.QProgressBar(self.layoutWidget_2)
        self.ConsonantScoreBar.setMaximum(10)
        self.ConsonantScoreBar.setProperty("value", 0)
        self.ConsonantScoreBar.setObjectName(_fromUtf8("ConsonantScoreBar"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.ConsonantScoreBar)
        self.label_20 = QtGui.QLabel(self.layoutWidget_2)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_20)
        self.VowelScoreBar = QtGui.QProgressBar(self.layoutWidget_2)
        self.VowelScoreBar.setMaximum(10)
        self.VowelScoreBar.setProperty("value", 0)
        self.VowelScoreBar.setObjectName(_fromUtf8("VowelScoreBar"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.VowelScoreBar)
        self.label_21 = QtGui.QLabel(self.layoutWidget_2)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_21)
        self.MarkScoreBar = QtGui.QProgressBar(self.layoutWidget_2)
        self.MarkScoreBar.setMaximum(10)
        self.MarkScoreBar.setProperty("value", 0)
        self.MarkScoreBar.setObjectName(_fromUtf8("MarkScoreBar"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.MarkScoreBar)
        self.label_22 = QtGui.QLabel(self.layoutWidget_2)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_22)
        self.BasicConsistencyScoreBar = QtGui.QProgressBar(self.layoutWidget_2)
        self.BasicConsistencyScoreBar.setMaximum(10)
        self.BasicConsistencyScoreBar.setProperty("value", 0)
        self.BasicConsistencyScoreBar.setObjectName(_fromUtf8("BasicConsistencyScoreBar"))
        self.formLayout_3.setWidget(4, QtGui.QFormLayout.FieldRole, self.BasicConsistencyScoreBar)
        self.scriptRoundingLabel = QtGui.QLabel(self.layoutWidget_2)
        self.scriptRoundingLabel.setObjectName(_fromUtf8("scriptRoundingLabel"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.LabelRole, self.scriptRoundingLabel)
        self.RoundingScoreBar = QtGui.QProgressBar(self.layoutWidget_2)
        self.RoundingScoreBar.setMaximum(10)
        self.RoundingScoreBar.setProperty("value", 0)
        self.RoundingScoreBar.setObjectName(_fromUtf8("RoundingScoreBar"))
        self.formLayout_3.setWidget(5, QtGui.QFormLayout.FieldRole, self.RoundingScoreBar)
        self.horizontalLayout_3.addWidget(self.groupBox_7)
        self.groupBox_6 = QtGui.QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.layoutWidget = QtGui.QWidget(self.groupBox_6)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 241, 149))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.formLayout_2 = QtGui.QFormLayout(self.layoutWidget)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_12)
        self.highresScoreBar = QtGui.QProgressBar(self.layoutWidget)
        self.highresScoreBar.setMaximum(10)
        self.highresScoreBar.setProperty("value", 0)
        self.highresScoreBar.setObjectName(_fromUtf8("highresScoreBar"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.highresScoreBar)
        self.label_13 = QtGui.QLabel(self.layoutWidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_13)
        self.progressBar_10 = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar_10.setMaximum(10)
        self.progressBar_10.setProperty("value", 0)
        self.progressBar_10.setObjectName(_fromUtf8("progressBar_10"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.progressBar_10)
        self.label_14 = QtGui.QLabel(self.layoutWidget)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_14)
        self.progressBar_11 = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar_11.setMaximum(10)
        self.progressBar_11.setProperty("value", 0)
        self.progressBar_11.setObjectName(_fromUtf8("progressBar_11"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.progressBar_11)
        self.label_16 = QtGui.QLabel(self.layoutWidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_16)
        self.progressBar_13 = QtGui.QProgressBar(self.layoutWidget)
        self.progressBar_13.setMaximum(10)
        self.progressBar_13.setProperty("value", 0)
        self.progressBar_13.setObjectName(_fromUtf8("progressBar_13"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.progressBar_13)
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_5 = QtGui.QGroupBox(self.horizontalLayoutWidget_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.layoutWidget1 = QtGui.QWidget(self.groupBox_5)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 50, 241, 101))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.formLayout = QtGui.QFormLayout(self.layoutWidget1)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.NormalScoreBar = QtGui.QProgressBar(self.layoutWidget1)
        self.NormalScoreBar.setMaximum(10)
        self.NormalScoreBar.setProperty("value", 0)
        self.NormalScoreBar.setObjectName(_fromUtf8("NormalScoreBar"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.NormalScoreBar)
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.BoldScoreBar = QtGui.QProgressBar(self.layoutWidget1)
        self.BoldScoreBar.setMaximum(10)
        self.BoldScoreBar.setProperty("value", 0)
        self.BoldScoreBar.setObjectName(_fromUtf8("BoldScoreBar"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.BoldScoreBar)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.ItalicScoreBar = QtGui.QProgressBar(self.layoutWidget1)
        self.ItalicScoreBar.setMaximum(10)
        self.ItalicScoreBar.setProperty("value", 0)
        self.ItalicScoreBar.setObjectName(_fromUtf8("ItalicScoreBar"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.ItalicScoreBar)
        self.label_7 = QtGui.QLabel(self.layoutWidget1)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.BasicScoreBar = QtGui.QProgressBar(self.layoutWidget1)
        self.BasicScoreBar.setMaximum(10)
        self.BasicScoreBar.setProperty("value", 0)
        self.BasicScoreBar.setObjectName(_fromUtf8("BasicScoreBar"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.BasicScoreBar)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.languageBox = QtGui.QComboBox(self.groupBox_3)
        self.languageBox.setGeometry(QtCore.QRect(250, 220, 85, 23))
        self.languageBox.setEditable(True)
        self.languageBox.setObjectName(_fromUtf8("languageBox"))
        self.languageBox.addItem(_fromUtf8(""))
        self.languageBox.addItem(_fromUtf8(""))
        self.languageBox.addItem(_fromUtf8(""))
        self.languageBox.addItem(_fromUtf8(""))
        self.BeginTestButton = QtGui.QPushButton(self.groupBox_3)
        self.BeginTestButton.setGeometry(QtCore.QRect(290, 30, 95, 71))
        self.BeginTestButton.setObjectName(_fromUtf8("BeginTestButton"))
        self.loadTestpushButton = QtGui.QPushButton(self.groupBox_3)
        self.loadTestpushButton.setGeometry(QtCore.QRect(10, 50, 181, 31))
        self.loadTestpushButton.setObjectName(_fromUtf8("loadTestpushButton"))
        self.loadStandardpushButton = QtGui.QPushButton(self.groupBox_3)
        self.loadStandardpushButton.setGeometry(QtCore.QRect(10, 70, 181, 31))
        self.loadStandardpushButton.setObjectName(_fromUtf8("loadStandardpushButton"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(250, 200, 54, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 51, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(10, 220, 221, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 180, 211, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_4 = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.SaveMessageBoxButton = QtGui.QPushButton(self.groupBox_4)
        self.SaveMessageBoxButton.setGeometry(QtCore.QRect(20, 241, 91, 31))
        self.SaveMessageBoxButton.setObjectName(_fromUtf8("SaveMessageBoxButton"))
        self.ClearMessageBoxButton = QtGui.QPushButton(self.groupBox_4)
        self.ClearMessageBoxButton.setGeometry(QtCore.QRect(120, 241, 91, 31))
        self.ClearMessageBoxButton.setObjectName(_fromUtf8("ClearMessageBoxButton"))
        self.MessageBox = QtGui.QTextBrowser(self.groupBox_4)
        self.MessageBox.setGeometry(QtCore.QRect(15, 30, 371, 211))
        self.MessageBox.setObjectName(_fromUtf8("MessageBox"))
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoadTestFont = QtGui.QAction(MainWindow)
        self.actionLoadTestFont.setObjectName(_fromUtf8("actionLoadTestFont"))
        self.actionSaveTestResults = QtGui.QAction(MainWindow)
        self.actionSaveTestResults.setObjectName(_fromUtf8("actionSaveTestResults"))
        self.actionTest_Parameters = QtGui.QAction(MainWindow)
        self.actionTest_Parameters.setObjectName(_fromUtf8("actionTest_Parameters"))
        self.actionManual_Testing = QtGui.QAction(MainWindow)
        self.actionManual_Testing.setObjectName(_fromUtf8("actionManual_Testing"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionabout = QtGui.QAction(MainWindow)
        self.actionabout.setObjectName(_fromUtf8("actionabout"))
        self.menu_File.addAction(self.actionLoadTestFont)
        self.menu_File.addAction(self.actionSaveTestResults)
        self.menuHelp.addAction(self.actionabout)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Font Compare", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Categorised Scores", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Glyph Consistency", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Numerals", None, QtGui.QApplication.UnicodeUTF8))
        self.NumeralScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Consonants", None, QtGui.QApplication.UnicodeUTF8))
        self.ConsonantScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Vowels", None, QtGui.QApplication.UnicodeUTF8))
        self.VowelScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Marks", None, QtGui.QApplication.UnicodeUTF8))
        self.MarkScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Basic Test", None, QtGui.QApplication.UnicodeUTF8))
        self.BasicConsistencyScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.scriptRoundingLabel.setText(QtGui.QApplication.translate("MainWindow", "SRounding", None, QtGui.QApplication.UnicodeUTF8))
        self.RoundingScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Readability and Print Proof", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "High Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.highresScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Low Resolution ", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_10.setFormat(QtGui.QApplication.translate("MainWindow", "%p", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Low Light Read", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_11.setFormat(QtGui.QApplication.translate("MainWindow", "%p", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Size(s) ", None, QtGui.QApplication.UnicodeUTF8))
        self.progressBar_13.setFormat(QtGui.QApplication.translate("MainWindow", "%p", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Similarity to Standard font or Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Normal", None, QtGui.QApplication.UnicodeUTF8))
        self.NormalScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Bold ", None, QtGui.QApplication.UnicodeUTF8))
        self.BoldScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Italic ", None, QtGui.QApplication.UnicodeUTF8))
        self.ItalicScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Basic Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.BasicScoreBar.setFormat(QtGui.QApplication.translate("MainWindow", "%v", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Control Box", None, QtGui.QApplication.UnicodeUTF8))
        self.languageBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "All Range", None, QtGui.QApplication.UnicodeUTF8))
        self.languageBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Devanagri", None, QtGui.QApplication.UnicodeUTF8))
        self.languageBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Bengali ", None, QtGui.QApplication.UnicodeUTF8))
        self.languageBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.BeginTestButton.setText(QtGui.QApplication.translate("MainWindow", "Begin Test!", None, QtGui.QApplication.UnicodeUTF8))
        self.loadTestpushButton.setText(QtGui.QApplication.translate("MainWindow", "Load TestFont", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Script:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Purpose:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("MainWindow", "Body Text : Books ", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("MainWindow", "Body Text: Magazines", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("MainWindow", "Body Text: Newspapers", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("MainWindow", "Body Text: Dictionaries", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("MainWindow", "Body Text: Directories", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(6, QtGui.QApplication.translate("MainWindow", "Body Text: Greetings/Invitations", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(7, QtGui.QApplication.translate("MainWindow", "Body Text: Poetry", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(8, QtGui.QApplication.translate("MainWindow", "Body Text: Children Books", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(9, QtGui.QApplication.translate("MainWindow", "Body Text: Advertisements", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(10, QtGui.QApplication.translate("MainWindow", "Headline: Books", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(11, QtGui.QApplication.translate("MainWindow", "Headline: Magazines", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(12, QtGui.QApplication.translate("MainWindow", "Headline: Newspapers", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(13, QtGui.QApplication.translate("MainWindow", "Headline: Advertisements", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(14, QtGui.QApplication.translate("MainWindow", "Display: Posters/Signboards", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(15, QtGui.QApplication.translate("MainWindow", "Display: Glow Signs", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(16, QtGui.QApplication.translate("MainWindow", "Display: LED Display", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(17, QtGui.QApplication.translate("MainWindow", "Display: TV/Mobiles Display", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Additional Meta Information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Additional Meta Information: ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Test Results", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveMessageBoxButton.setText(QtGui.QApplication.translate("MainWindow", "Save To File", None, QtGui.QApplication.UnicodeUTF8))
        self.ClearMessageBoxButton.setText(QtGui.QApplication.translate("MainWindow", "Clear All", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Hel&p", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoadTestFont.setText(QtGui.QApplication.translate("MainWindow", "Load TestFont", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveTestResults.setText(QtGui.QApplication.translate("MainWindow", "Save Test Results", None, QtGui.QApplication.UnicodeUTF8))
        self.actionTest_Parameters.setText(QtGui.QApplication.translate("MainWindow", "Test Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.actionManual_Testing.setText(QtGui.QApplication.translate("MainWindow", "Manual Testing", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionabout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

