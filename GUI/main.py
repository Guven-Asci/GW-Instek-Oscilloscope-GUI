# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri Apr 29 16:40:07 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_oscillascopGui(object):
    def setupUi(self, oscillascopGui):
        oscillascopGui.setObjectName(_fromUtf8("oscillascopGui"))
        oscillascopGui.resize(1430, 802)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/icon.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        oscillascopGui.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(oscillascopGui)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.ch1volt = QtGui.QDial(self.centralwidget)
        self.ch1volt.setGeometry(QtCore.QRect(80, 510, 91, 101))
        self.ch1volt.setMaximum(10)
        self.ch1volt.setObjectName(_fromUtf8("ch1volt"))
        self.ch2volt = QtGui.QDial(self.centralwidget)
        self.ch2volt.setGeometry(QtCore.QRect(350, 510, 91, 111))
        self.ch2volt.setMaximum(10)
        self.ch2volt.setObjectName(_fromUtf8("ch2volt"))
        self.ch1VoltDivLabel = QtGui.QLabel(self.centralwidget)
        self.ch1VoltDivLabel.setGeometry(QtCore.QRect(110, 480, 46, 13))
        self.ch1VoltDivLabel.setObjectName(_fromUtf8("ch1VoltDivLabel"))
        self.timedial = QtGui.QDial(self.centralwidget)
        self.timedial.setGeometry(QtCore.QRect(610, 510, 91, 91))
        self.timedial.setMaximum(30)
        self.timedial.setObjectName(_fromUtf8("timedial"))
        self.ch2VoltDivLabel = QtGui.QLabel(self.centralwidget)
        self.ch2VoltDivLabel.setGeometry(QtCore.QRect(370, 480, 46, 13))
        self.ch2VoltDivLabel.setObjectName(_fromUtf8("ch2VoltDivLabel"))
        self.timDivLabel = QtGui.QLabel(self.centralwidget)
        self.timDivLabel.setGeometry(QtCore.QRect(630, 480, 46, 13))
        self.timDivLabel.setObjectName(_fromUtf8("timDivLabel"))
        self.CounterPos = Qwt5.QwtCounter(self.centralwidget)
        self.CounterPos.setGeometry(QtCore.QRect(40, 610, 161, 31))
        self.CounterPos.setNumButtons(3)
        self.CounterPos.setProperty("basicstep", 0.1)
        self.CounterPos.setMinValue(-50.0)
        self.CounterPos.setMaxValue(50.0)
        self.CounterPos.setStepButton1(3)
        self.CounterPos.setStepButton2(5)
        self.CounterPos.setProperty("value", 0.0)
        self.CounterPos.setObjectName(_fromUtf8("CounterPos"))
        self.tabMenu = QtGui.QTabWidget(self.centralwidget)
        self.tabMenu.setEnabled(True)
        self.tabMenu.setGeometry(QtCore.QRect(1120, 10, 281, 731))
        self.tabMenu.setTabPosition(QtGui.QTabWidget.East)
        self.tabMenu.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabMenu.setElideMode(QtCore.Qt.ElideRight)
        self.tabMenu.setUsesScrollButtons(True)
        self.tabMenu.setDocumentMode(False)
        self.tabMenu.setTabsClosable(False)
        self.tabMenu.setMovable(True)
        self.tabMenu.setObjectName(_fromUtf8("tabMenu"))
        self.Measure = QtGui.QWidget()
        self.Measure.setObjectName(_fromUtf8("Measure"))
        self.layoutWidget = QtGui.QWidget(self.Measure)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 660, 111, 61))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_14.setMargin(0)
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.PWidthCB = QtGui.QCheckBox(self.layoutWidget)
        self.PWidthCB.setObjectName(_fromUtf8("PWidthCB"))
        self.verticalLayout_14.addWidget(self.PWidthCB)
        self.PWidthLabel1 = QtGui.QLabel(self.layoutWidget)
        self.PWidthLabel1.setObjectName(_fromUtf8("PWidthLabel1"))
        self.verticalLayout_14.addWidget(self.PWidthLabel1)
        self.PWidthLabel2 = QtGui.QLabel(self.layoutWidget)
        self.PWidthLabel2.setObjectName(_fromUtf8("PWidthLabel2"))
        self.verticalLayout_14.addWidget(self.PWidthLabel2)
        self.layoutWidget1 = QtGui.QWidget(self.Measure)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 570, 101, 81))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_16.setMargin(0)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.NWidthCB = QtGui.QCheckBox(self.layoutWidget1)
        self.NWidthCB.setObjectName(_fromUtf8("NWidthCB"))
        self.verticalLayout_16.addWidget(self.NWidthCB)
        self.NWidthLabel1 = QtGui.QLabel(self.layoutWidget1)
        self.NWidthLabel1.setObjectName(_fromUtf8("NWidthLabel1"))
        self.verticalLayout_16.addWidget(self.NWidthLabel1)
        self.NWidthLabel2 = QtGui.QLabel(self.layoutWidget1)
        self.NWidthLabel2.setObjectName(_fromUtf8("NWidthLabel2"))
        self.verticalLayout_16.addWidget(self.NWidthLabel2)
        self.layoutWidget2 = QtGui.QWidget(self.Measure)
        self.layoutWidget2.setGeometry(QtCore.QRect(140, 30, 91, 81))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.FallCB = QtGui.QCheckBox(self.layoutWidget2)
        self.FallCB.setObjectName(_fromUtf8("FallCB"))
        self.verticalLayout_2.addWidget(self.FallCB)
        self.FallLabel1 = QtGui.QLabel(self.layoutWidget2)
        self.FallLabel1.setObjectName(_fromUtf8("FallLabel1"))
        self.verticalLayout_2.addWidget(self.FallLabel1)
        self.FallLabel2 = QtGui.QLabel(self.layoutWidget2)
        self.FallLabel2.setObjectName(_fromUtf8("FallLabel2"))
        self.verticalLayout_2.addWidget(self.FallLabel2)
        self.layoutWidget3 = QtGui.QWidget(self.Measure)
        self.layoutWidget3.setGeometry(QtCore.QRect(140, 210, 91, 81))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setMargin(0)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.PeriodCB = QtGui.QCheckBox(self.layoutWidget3)
        self.PeriodCB.setObjectName(_fromUtf8("PeriodCB"))
        self.verticalLayout_6.addWidget(self.PeriodCB)
        self.PeriodLabel1 = QtGui.QLabel(self.layoutWidget3)
        self.PeriodLabel1.setObjectName(_fromUtf8("PeriodLabel1"))
        self.verticalLayout_6.addWidget(self.PeriodLabel1)
        self.PeriodLabel2 = QtGui.QLabel(self.layoutWidget3)
        self.PeriodLabel2.setObjectName(_fromUtf8("PeriodLabel2"))
        self.verticalLayout_6.addWidget(self.PeriodLabel2)
        self.layoutWidget4 = QtGui.QWidget(self.Measure)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 210, 111, 81))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.RiseCB = QtGui.QCheckBox(self.layoutWidget4)
        self.RiseCB.setObjectName(_fromUtf8("RiseCB"))
        self.verticalLayout_5.addWidget(self.RiseCB)
        self.RiseLabel1 = QtGui.QLabel(self.layoutWidget4)
        self.RiseLabel1.setObjectName(_fromUtf8("RiseLabel1"))
        self.verticalLayout_5.addWidget(self.RiseLabel1)
        self.RiseLabel2 = QtGui.QLabel(self.layoutWidget4)
        self.RiseLabel2.setObjectName(_fromUtf8("RiseLabel2"))
        self.verticalLayout_5.addWidget(self.RiseLabel2)
        self.layoutWidget5 = QtGui.QWidget(self.Measure)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 120, 111, 81))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.FreCB = QtGui.QCheckBox(self.layoutWidget5)
        self.FreCB.setObjectName(_fromUtf8("FreCB"))
        self.verticalLayout_4.addWidget(self.FreCB)
        self.FreLabel1 = QtGui.QLabel(self.layoutWidget5)
        self.FreLabel1.setObjectName(_fromUtf8("FreLabel1"))
        self.verticalLayout_4.addWidget(self.FreLabel1)
        self.FreLabel2 = QtGui.QLabel(self.layoutWidget5)
        self.FreLabel2.setObjectName(_fromUtf8("FreLabel2"))
        self.verticalLayout_4.addWidget(self.FreLabel2)
        self.layoutWidget6 = QtGui.QWidget(self.Measure)
        self.layoutWidget6.setGeometry(QtCore.QRect(140, 120, 91, 81))
        self.layoutWidget6.setObjectName(_fromUtf8("layoutWidget6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget6)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.PDutyCB = QtGui.QCheckBox(self.layoutWidget6)
        self.PDutyCB.setObjectName(_fromUtf8("PDutyCB"))
        self.verticalLayout_3.addWidget(self.PDutyCB)
        self.PDutyLabel1 = QtGui.QLabel(self.layoutWidget6)
        self.PDutyLabel1.setObjectName(_fromUtf8("PDutyLabel1"))
        self.verticalLayout_3.addWidget(self.PDutyLabel1)
        self.PDutyLabel2 = QtGui.QLabel(self.layoutWidget6)
        self.PDutyLabel2.setObjectName(_fromUtf8("PDutyLabel2"))
        self.verticalLayout_3.addWidget(self.PDutyLabel2)
        self.layoutWidget7 = QtGui.QWidget(self.Measure)
        self.layoutWidget7.setGeometry(QtCore.QRect(140, 300, 91, 81))
        self.layoutWidget7.setObjectName(_fromUtf8("layoutWidget7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.layoutWidget7)
        self.verticalLayout_7.setMargin(0)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.VHighCB = QtGui.QCheckBox(self.layoutWidget7)
        self.VHighCB.setObjectName(_fromUtf8("VHighCB"))
        self.verticalLayout_7.addWidget(self.VHighCB)
        self.VHighLabel1 = QtGui.QLabel(self.layoutWidget7)
        self.VHighLabel1.setObjectName(_fromUtf8("VHighLabel1"))
        self.verticalLayout_7.addWidget(self.VHighLabel1)
        self.VHighLabel2 = QtGui.QLabel(self.layoutWidget7)
        self.VHighLabel2.setObjectName(_fromUtf8("VHighLabel2"))
        self.verticalLayout_7.addWidget(self.VHighLabel2)
        self.layoutWidget8 = QtGui.QWidget(self.Measure)
        self.layoutWidget8.setGeometry(QtCore.QRect(11, 300, 111, 81))
        self.layoutWidget8.setObjectName(_fromUtf8("layoutWidget8"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.layoutWidget8)
        self.verticalLayout_8.setMargin(0)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.VampCB = QtGui.QCheckBox(self.layoutWidget8)
        self.VampCB.setObjectName(_fromUtf8("VampCB"))
        self.verticalLayout_8.addWidget(self.VampCB)
        self.VampLabel1 = QtGui.QLabel(self.layoutWidget8)
        self.VampLabel1.setObjectName(_fromUtf8("VampLabel1"))
        self.verticalLayout_8.addWidget(self.VampLabel1)
        self.VampLabel2 = QtGui.QLabel(self.layoutWidget8)
        self.VampLabel2.setObjectName(_fromUtf8("VampLabel2"))
        self.verticalLayout_8.addWidget(self.VampLabel2)
        self.layoutWidget9 = QtGui.QWidget(self.Measure)
        self.layoutWidget9.setGeometry(QtCore.QRect(10, 390, 111, 81))
        self.layoutWidget9.setObjectName(_fromUtf8("layoutWidget9"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.layoutWidget9)
        self.verticalLayout_10.setMargin(0)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.VRmsCB = QtGui.QCheckBox(self.layoutWidget9)
        self.VRmsCB.setObjectName(_fromUtf8("VRmsCB"))
        self.verticalLayout_10.addWidget(self.VRmsCB)
        self.VRmsLabel1 = QtGui.QLabel(self.layoutWidget9)
        self.VRmsLabel1.setObjectName(_fromUtf8("VRmsLabel1"))
        self.verticalLayout_10.addWidget(self.VRmsLabel1)
        self.VRmsLabel2 = QtGui.QLabel(self.layoutWidget9)
        self.VRmsLabel2.setObjectName(_fromUtf8("VRmsLabel2"))
        self.verticalLayout_10.addWidget(self.VRmsLabel2)
        self.layoutWidget10 = QtGui.QWidget(self.Measure)
        self.layoutWidget10.setGeometry(QtCore.QRect(140, 390, 91, 81))
        self.layoutWidget10.setObjectName(_fromUtf8("layoutWidget10"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.layoutWidget10)
        self.verticalLayout_9.setMargin(0)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.VMaxCB = QtGui.QCheckBox(self.layoutWidget10)
        self.VMaxCB.setObjectName(_fromUtf8("VMaxCB"))
        self.verticalLayout_9.addWidget(self.VMaxCB)
        self.VMaxLabel1 = QtGui.QLabel(self.layoutWidget10)
        self.VMaxLabel1.setObjectName(_fromUtf8("VMaxLabel1"))
        self.verticalLayout_9.addWidget(self.VMaxLabel1)
        self.VMaxLabel2 = QtGui.QLabel(self.layoutWidget10)
        self.VMaxLabel2.setObjectName(_fromUtf8("VMaxLabel2"))
        self.verticalLayout_9.addWidget(self.VMaxLabel2)
        self.layoutWidget11 = QtGui.QWidget(self.Measure)
        self.layoutWidget11.setGeometry(QtCore.QRect(140, 480, 91, 81))
        self.layoutWidget11.setObjectName(_fromUtf8("layoutWidget11"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.layoutWidget11)
        self.verticalLayout_11.setMargin(0)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.VLowCB = QtGui.QCheckBox(self.layoutWidget11)
        self.VLowCB.setObjectName(_fromUtf8("VLowCB"))
        self.verticalLayout_11.addWidget(self.VLowCB)
        self.VLowLabel1 = QtGui.QLabel(self.layoutWidget11)
        self.VLowLabel1.setObjectName(_fromUtf8("VLowLabel1"))
        self.verticalLayout_11.addWidget(self.VLowLabel1)
        self.VLowLabel2 = QtGui.QLabel(self.layoutWidget11)
        self.VLowLabel2.setObjectName(_fromUtf8("VLowLabel2"))
        self.verticalLayout_11.addWidget(self.VLowLabel2)
        self.layoutWidget12 = QtGui.QWidget(self.Measure)
        self.layoutWidget12.setGeometry(QtCore.QRect(10, 30, 101, 81))
        self.layoutWidget12.setObjectName(_fromUtf8("layoutWidget12"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget12)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.VppCB = QtGui.QCheckBox(self.layoutWidget12)
        self.VppCB.setObjectName(_fromUtf8("VppCB"))
        self.verticalLayout.addWidget(self.VppCB)
        self.VppLabel1 = QtGui.QLabel(self.layoutWidget12)
        self.VppLabel1.setObjectName(_fromUtf8("VppLabel1"))
        self.verticalLayout.addWidget(self.VppLabel1)
        self.VppLabel2 = QtGui.QLabel(self.layoutWidget12)
        self.VppLabel2.setObjectName(_fromUtf8("VppLabel2"))
        self.verticalLayout.addWidget(self.VppLabel2)
        self.layoutWidget13 = QtGui.QWidget(self.Measure)
        self.layoutWidget13.setGeometry(QtCore.QRect(10, 480, 111, 81))
        self.layoutWidget13.setObjectName(_fromUtf8("layoutWidget13"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.layoutWidget13)
        self.verticalLayout_12.setMargin(0)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.VMinCB = QtGui.QCheckBox(self.layoutWidget13)
        self.VMinCB.setObjectName(_fromUtf8("VMinCB"))
        self.verticalLayout_12.addWidget(self.VMinCB)
        self.VMinLabel1 = QtGui.QLabel(self.layoutWidget13)
        self.VMinLabel1.setObjectName(_fromUtf8("VMinLabel1"))
        self.verticalLayout_12.addWidget(self.VMinLabel1)
        self.VMinLabel2 = QtGui.QLabel(self.layoutWidget13)
        self.VMinLabel2.setObjectName(_fromUtf8("VMinLabel2"))
        self.verticalLayout_12.addWidget(self.VMinLabel2)
        self.layoutWidget14 = QtGui.QWidget(self.Measure)
        self.layoutWidget14.setGeometry(QtCore.QRect(140, 570, 101, 81))
        self.layoutWidget14.setObjectName(_fromUtf8("layoutWidget14"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.layoutWidget14)
        self.verticalLayout_15.setMargin(0)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.VavCB = QtGui.QCheckBox(self.layoutWidget14)
        self.VavCB.setObjectName(_fromUtf8("VavCB"))
        self.verticalLayout_15.addWidget(self.VavCB)
        self.VavLabel1 = QtGui.QLabel(self.layoutWidget14)
        self.VavLabel1.setObjectName(_fromUtf8("VavLabel1"))
        self.verticalLayout_15.addWidget(self.VavLabel1)
        self.VavLabel2 = QtGui.QLabel(self.layoutWidget14)
        self.VavLabel2.setObjectName(_fromUtf8("VavLabel2"))
        self.verticalLayout_15.addWidget(self.VavLabel2)
        self.tabMenu.addTab(self.Measure, _fromUtf8(""))
        self.Trigger = QtGui.QWidget()
        self.Trigger.setObjectName(_fromUtf8("Trigger"))
        self.groupBox = QtGui.QGroupBox(self.Trigger)
        self.groupBox.setGeometry(QtCore.QRect(20, 80, 221, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.trgEdge = QtGui.QRadioButton(self.groupBox)
        self.trgEdge.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.trgEdge.setChecked(True)
        self.trgEdge.setObjectName(_fromUtf8("trgEdge"))
        self.trgVideo = QtGui.QRadioButton(self.groupBox)
        self.trgVideo.setGeometry(QtCore.QRect(120, 20, 82, 17))
        self.trgVideo.setObjectName(_fromUtf8("trgVideo"))
        self.trgPulse = QtGui.QRadioButton(self.groupBox)
        self.trgPulse.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.trgPulse.setObjectName(_fromUtf8("trgPulse"))
        self.trgDelay = QtGui.QRadioButton(self.groupBox)
        self.trgDelay.setGeometry(QtCore.QRect(120, 50, 82, 17))
        self.trgDelay.setObjectName(_fromUtf8("trgDelay"))
        self.triggerLevel = Qwt5.QwtCounter(self.Trigger)
        self.triggerLevel.setGeometry(QtCore.QRect(20, 20, 221, 31))
        self.triggerLevel.setNumButtons(3)
        self.triggerLevel.setProperty("basicstep", 0.1)
        self.triggerLevel.setMinValue(-50.0)
        self.triggerLevel.setMaxValue(50.0)
        self.triggerLevel.setStepButton1(3)
        self.triggerLevel.setStepButton2(5)
        self.triggerLevel.setProperty("value", 0.0)
        self.triggerLevel.setObjectName(_fromUtf8("triggerLevel"))
        self.trgTypeTab = QtGui.QTabWidget(self.Trigger)
        self.trgTypeTab.setGeometry(QtCore.QRect(20, 190, 221, 231))
        self.trgTypeTab.setObjectName(_fromUtf8("trgTypeTab"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 81, 101))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.edgeSCh1 = QtGui.QRadioButton(self.groupBox_2)
        self.edgeSCh1.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.edgeSCh1.setChecked(True)
        self.edgeSCh1.setObjectName(_fromUtf8("edgeSCh1"))
        self.edgeSCh2 = QtGui.QRadioButton(self.groupBox_2)
        self.edgeSCh2.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.edgeSCh2.setObjectName(_fromUtf8("edgeSCh2"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(110, 10, 91, 101))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.edgeMAuto = QtGui.QRadioButton(self.groupBox_3)
        self.edgeMAuto.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.edgeMAuto.setChecked(True)
        self.edgeMAuto.setObjectName(_fromUtf8("edgeMAuto"))
        self.edgeMNormal = QtGui.QRadioButton(self.groupBox_3)
        self.edgeMNormal.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.edgeMNormal.setObjectName(_fromUtf8("edgeMNormal"))
        self.edgeMSingle = QtGui.QRadioButton(self.groupBox_3)
        self.edgeMSingle.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.edgeMSingle.setObjectName(_fromUtf8("edgeMSingle"))
        self.edgeMALevel = QtGui.QRadioButton(self.groupBox_3)
        self.edgeMALevel.setGeometry(QtCore.QRect(10, 80, 82, 17))
        self.edgeMALevel.setObjectName(_fromUtf8("edgeMALevel"))
        self.trgTypeTab.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.trgTypeTab.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.trgTypeTab.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.trgTypeTab.addTab(self.tab_4, _fromUtf8(""))
        self.tabMenu.addTab(self.Trigger, _fromUtf8(""))
        self.Cursor = QtGui.QWidget()
        self.Cursor.setObjectName(_fromUtf8("Cursor"))
        self.groupBox_4 = QtGui.QGroupBox(self.Cursor)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 10, 120, 80))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.cursorSCh1 = QtGui.QRadioButton(self.groupBox_4)
        self.cursorSCh1.setGeometry(QtCore.QRect(30, 20, 82, 17))
        self.cursorSCh1.setChecked(True)
        self.cursorSCh1.setObjectName(_fromUtf8("cursorSCh1"))
        self.cursorSCh2 = QtGui.QRadioButton(self.groupBox_4)
        self.cursorSCh2.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.cursorSCh2.setObjectName(_fromUtf8("cursorSCh2"))
        self.cursorX1 = QtGui.QSlider(self.Cursor)
        self.cursorX1.setGeometry(QtCore.QRect(10, 160, 160, 19))
        self.cursorX1.setMinimum(1)
        self.cursorX1.setMaximum(249)
        self.cursorX1.setOrientation(QtCore.Qt.Horizontal)
        self.cursorX1.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cursorX1.setObjectName(_fromUtf8("cursorX1"))
        self.cursorX2 = QtGui.QSlider(self.Cursor)
        self.cursorX2.setGeometry(QtCore.QRect(10, 190, 160, 19))
        self.cursorX2.setMinimum(1)
        self.cursorX2.setMaximum(249)
        self.cursorX2.setOrientation(QtCore.Qt.Horizontal)
        self.cursorX2.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cursorX2.setObjectName(_fromUtf8("cursorX2"))
        self.cursorY1 = QtGui.QSlider(self.Cursor)
        self.cursorY1.setGeometry(QtCore.QRect(180, 110, 19, 160))
        self.cursorY1.setMinimum(1)
        self.cursorY1.setMaximum(199)
        self.cursorY1.setOrientation(QtCore.Qt.Vertical)
        self.cursorY1.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cursorY1.setObjectName(_fromUtf8("cursorY1"))
        self.cursorY2 = QtGui.QSlider(self.Cursor)
        self.cursorY2.setGeometry(QtCore.QRect(220, 110, 19, 160))
        self.cursorY2.setMinimum(1)
        self.cursorY2.setMaximum(199)
        self.cursorY2.setOrientation(QtCore.Qt.Vertical)
        self.cursorY2.setTickPosition(QtGui.QSlider.TicksAbove)
        self.cursorY2.setObjectName(_fromUtf8("cursorY2"))
        self.label = QtGui.QLabel(self.Cursor)
        self.label.setGeometry(QtCore.QRect(40, 390, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.deltaX = QtGui.QLabel(self.Cursor)
        self.deltaX.setGeometry(QtCore.QRect(30, 425, 81, 21))
        self.deltaX.setWordWrap(False)
        self.deltaX.setObjectName(_fromUtf8("deltaX"))
        self.deltaY = QtGui.QLabel(self.Cursor)
        self.deltaY.setGeometry(QtCore.QRect(30, 450, 71, 21))
        self.deltaY.setWordWrap(False)
        self.deltaY.setObjectName(_fromUtf8("deltaY"))
        self.cursorXenabled = QtGui.QCheckBox(self.Cursor)
        self.cursorXenabled.setGeometry(QtCore.QRect(170, 30, 70, 17))
        self.cursorXenabled.setChecked(True)
        self.cursorXenabled.setObjectName(_fromUtf8("cursorXenabled"))
        self.cursorYenabled = QtGui.QCheckBox(self.Cursor)
        self.cursorYenabled.setGeometry(QtCore.QRect(170, 60, 70, 17))
        self.cursorYenabled.setChecked(True)
        self.cursorYenabled.setObjectName(_fromUtf8("cursorYenabled"))
        self.tabMenu.addTab(self.Cursor, _fromUtf8(""))
        self.layoutWidget15 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget15.setGeometry(QtCore.QRect(0, 0, 2, 2))
        self.layoutWidget15.setObjectName(_fromUtf8("layoutWidget15"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget15)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.RunStopBut = QtGui.QPushButton(self.centralwidget)
        self.RunStopBut.setGeometry(QtCore.QRect(940, 560, 61, 51))
        self.RunStopBut.setObjectName(_fromUtf8("RunStopBut"))
        self.AutoSet = QtGui.QPushButton(self.centralwidget)
        self.AutoSet.setGeometry(QtCore.QRect(940, 490, 51, 41))
        self.AutoSet.setObjectName(_fromUtf8("AutoSet"))
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setGeometry(QtCore.QRect(10, 40, 1101, 351))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.takePicture = QtGui.QPushButton(self.centralwidget)
        self.takePicture.setGeometry(QtCore.QRect(414, 430, 91, 23))
        self.takePicture.setObjectName(_fromUtf8("takePicture"))
        self.carpan = QtGui.QLabel(self.centralwidget)
        self.carpan.setGeometry(QtCore.QRect(540, 370, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.carpan.setFont(font)
        self.carpan.setObjectName(_fromUtf8("carpan"))
        self.plotCh1text = QtGui.QLabel(self.centralwidget)
        self.plotCh1text.setGeometry(QtCore.QRect(80, 40, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.plotCh1text.setFont(font)
        self.plotCh1text.setText(_fromUtf8(""))
        self.plotCh1text.setObjectName(_fromUtf8("plotCh1text"))
        self.plotCh2text = QtGui.QLabel(self.centralwidget)
        self.plotCh2text.setGeometry(QtCore.QRect(990, 40, 91, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotCh2text.sizePolicy().hasHeightForWidth())
        self.plotCh2text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.plotCh2text.setFont(font)
        self.plotCh2text.setText(_fromUtf8(""))
        self.plotCh2text.setObjectName(_fromUtf8("plotCh2text"))
        self.CounterPos_2 = Qwt5.QwtCounter(self.centralwidget)
        self.CounterPos_2.setGeometry(QtCore.QRect(310, 610, 161, 31))
        self.CounterPos_2.setNumButtons(3)
        self.CounterPos_2.setProperty("basicstep", 0.1)
        self.CounterPos_2.setMinValue(-50.0)
        self.CounterPos_2.setMaxValue(50.0)
        self.CounterPos_2.setStepButton1(3)
        self.CounterPos_2.setStepButton2(5)
        self.CounterPos_2.setProperty("value", 0.0)
        self.CounterPos_2.setObjectName(_fromUtf8("CounterPos_2"))
        self.CounterPos_3 = Qwt5.QwtCounter(self.centralwidget)
        self.CounterPos_3.setGeometry(QtCore.QRect(570, 610, 161, 31))
        self.CounterPos_3.setNumButtons(3)
        self.CounterPos_3.setProperty("basicstep", 0.1)
        self.CounterPos_3.setMinValue(-50.0)
        self.CounterPos_3.setMaxValue(50.0)
        self.CounterPos_3.setStepButton1(3)
        self.CounterPos_3.setStepButton2(5)
        self.CounterPos_3.setProperty("value", 0.0)
        self.CounterPos_3.setObjectName(_fromUtf8("CounterPos_3"))
        self.aboutUs = QtGui.QCommandLinkButton(self.centralwidget)
        self.aboutUs.setGeometry(QtCore.QRect(910, 700, 185, 41))
        self.aboutUs.setObjectName(_fromUtf8("aboutUs"))
        oscillascopGui.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(oscillascopGui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1430, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        oscillascopGui.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(oscillascopGui)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        oscillascopGui.setStatusBar(self.statusbar)

        self.retranslateUi(oscillascopGui)
        self.tabMenu.setCurrentIndex(0)
        self.trgTypeTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(oscillascopGui)

    def retranslateUi(self, oscillascopGui):
        oscillascopGui.setWindowTitle(_translate("oscillascopGui", "GDS-806 Interface", None))
        self.ch1VoltDivLabel.setText(_translate("oscillascopGui", "TextLabel", None))
        self.ch2VoltDivLabel.setText(_translate("oscillascopGui", "TextLabel", None))
        self.timDivLabel.setText(_translate("oscillascopGui", "TextLabel", None))
        self.PWidthCB.setText(_translate("oscillascopGui", "PWidth", None))
        self.PWidthLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.PWidthLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.NWidthCB.setText(_translate("oscillascopGui", "NWidth", None))
        self.NWidthLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.NWidthLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.FallCB.setText(_translate("oscillascopGui", "Fall", None))
        self.FallLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.FallLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.PeriodCB.setText(_translate("oscillascopGui", "Period", None))
        self.PeriodLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.PeriodLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.RiseCB.setText(_translate("oscillascopGui", "Risetime", None))
        self.RiseLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.RiseLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.FreCB.setText(_translate("oscillascopGui", "Frequency", None))
        self.FreLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.FreLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.PDutyCB.setText(_translate("oscillascopGui", "Duty Cycle", None))
        self.PDutyLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.PDutyLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VHighCB.setText(_translate("oscillascopGui", "VHigh", None))
        self.VHighLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VHighLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VampCB.setText(_translate("oscillascopGui", "VAmp", None))
        self.VampLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VampLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VRmsCB.setText(_translate("oscillascopGui", "VRms", None))
        self.VRmsLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VRmsLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VMaxCB.setText(_translate("oscillascopGui", "VMax", None))
        self.VMaxLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VMaxLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VLowCB.setText(_translate("oscillascopGui", "VLow", None))
        self.VLowLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VLowLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VppCB.setText(_translate("oscillascopGui", "Vpp", None))
        self.VppLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VppLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VMinCB.setText(_translate("oscillascopGui", "VMin", None))
        self.VMinLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VMinLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VavCB.setText(_translate("oscillascopGui", "Vaverage", None))
        self.VavLabel1.setText(_translate("oscillascopGui", "TextLabel", None))
        self.VavLabel2.setText(_translate("oscillascopGui", "TextLabel", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.Measure), _translate("oscillascopGui", "Measure", None))
        self.groupBox.setTitle(_translate("oscillascopGui", "Trigger Type", None))
        self.trgEdge.setText(_translate("oscillascopGui", "Edge", None))
        self.trgVideo.setText(_translate("oscillascopGui", "Video", None))
        self.trgPulse.setText(_translate("oscillascopGui", "Pulse", None))
        self.trgDelay.setText(_translate("oscillascopGui", "Delay", None))
        self.groupBox_2.setTitle(_translate("oscillascopGui", "Source", None))
        self.edgeSCh1.setText(_translate("oscillascopGui", "CH1", None))
        self.edgeSCh2.setText(_translate("oscillascopGui", "CH2", None))
        self.groupBox_3.setTitle(_translate("oscillascopGui", "Mode", None))
        self.edgeMAuto.setText(_translate("oscillascopGui", "Auto", None))
        self.edgeMNormal.setText(_translate("oscillascopGui", "Normal", None))
        self.edgeMSingle.setText(_translate("oscillascopGui", "Single", None))
        self.edgeMALevel.setText(_translate("oscillascopGui", "Auto Level", None))
        self.trgTypeTab.setTabText(self.trgTypeTab.indexOf(self.tab), _translate("oscillascopGui", "Edge", None))
        self.trgTypeTab.setTabText(self.trgTypeTab.indexOf(self.tab_2), _translate("oscillascopGui", "Video", None))
        self.trgTypeTab.setTabText(self.trgTypeTab.indexOf(self.tab_3), _translate("oscillascopGui", "Pulse", None))
        self.trgTypeTab.setTabText(self.trgTypeTab.indexOf(self.tab_4), _translate("oscillascopGui", "Delay", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.Trigger), _translate("oscillascopGui", "Trigger", None))
        self.groupBox_4.setTitle(_translate("oscillascopGui", "Source", None))
        self.cursorSCh1.setText(_translate("oscillascopGui", "CH1", None))
        self.cursorSCh2.setText(_translate("oscillascopGui", "CH2", None))
        self.label.setText(_translate("oscillascopGui", "Delta", None))
        self.deltaX.setText(_translate("oscillascopGui", "X:", None))
        self.deltaY.setText(_translate("oscillascopGui", "Y:", None))
        self.cursorXenabled.setText(_translate("oscillascopGui", "X", None))
        self.cursorYenabled.setText(_translate("oscillascopGui", "Y", None))
        self.tabMenu.setTabText(self.tabMenu.indexOf(self.Cursor), _translate("oscillascopGui", "Cursor", None))
        self.RunStopBut.setText(_translate("oscillascopGui", "RunStop", None))
        self.AutoSet.setText(_translate("oscillascopGui", "AutoSet", None))
        self.takePicture.setText(_translate("oscillascopGui", "Take a Picture!", None))
        self.carpan.setText(_translate("oscillascopGui", "seconds", None))
        self.aboutUs.setText(_translate("oscillascopGui", "About Us!", None))

from PyQt4 import Qwt5
from matplotlibwidget import MatplotlibWidget


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    oscillascopGui = QtGui.QMainWindow()
    ui = Ui_oscillascopGui()
    ui.setupUi(oscillascopGui)
    oscillascopGui.show()
    sys.exit(app.exec_())
