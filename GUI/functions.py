# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 13:20:21 2016

@author: 1101050035
"""

from PyQt4 import QtCore, QtGui
from main import Ui_oscillascopGui
import numpy as np
import sys
import serial
import immain

global s
s=serial.Serial('COM1',38400)

s.timeout=1

class pencere(QtGui.QMainWindow, Ui_oscillascopGui):
    run=True
    def __init__(self,parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        
        self.teksefer=QtCore.QTimer()
        self.teksefer.setSingleShot(True)
        self.teksefer.timeout.connect(self.tekseferto)
        
        
        self.timerMain = QtCore.QTimer()
        self.timerMain.timeout.connect(self.updateMAIN)
        self.updateMAIN()
        
        
        self.measureTimer = QtCore.QTimer()
        self.measureTimer.timeout.connect(self.getMeasure)
        self.measureTimer.start(500)
        
        self.triggerTimer = QtCore.QTimer()
        self.triggerTimer.timeout.connect(self.getTrigger)
        
        self.cursorTimer = QtCore.QTimer()
        self.cursorTimer.timeout.connect(self.getCursor)
        
        
        
        self.x1crsrtimer = QtCore.QTimer()
        self.x1crsrtimer.setSingleShot(True)
        self.x1crsrtimer.timeout.connect(self.x1crsr)
        self.x2crsrtimer = QtCore.QTimer()
        self.x2crsrtimer.setSingleShot(True)
        self.x2crsrtimer.timeout.connect(self.x2crsr)
        self.y1crsrtimer = QtCore.QTimer()
        self.y1crsrtimer.setSingleShot(True)
        self.y1crsrtimer.timeout.connect(self.y1crsr)
        self.y2crsrtimer = QtCore.QTimer()
        self.y2crsrtimer.setSingleShot(True)
        self.y2crsrtimer.timeout.connect(self.y2crsr)        
   
        
   
        self.ch1volt.valueChanged.connect(self.changingvoltage1)
        self.ch2volt.valueChanged.connect(self.changingvoltage2)
        self.timedial.valueChanged.connect(self.changingtime)
        self.CounterPos.valueChanged.connect(self.counterchanging)
        self.CounterPos_2.valueChanged.connect(self.counterchanging2)
        self.CounterPos_3.valueChanged.connect(self.counterchanging3)
        self.tabMenu.currentChanged.connect(self.updateTimer)
        self.trgEdge.toggled.connect(self.trgTypeUpdate)
        self.trgVideo.toggled.connect(self.trgTypeUpdate)
        self.trgPulse.toggled.connect(self.trgTypeUpdate)
        self.trgDelay.toggled.connect(self.trgTypeUpdate)
        self.trgTypeUpdate()
        self.triggerLevel.valueChanged.connect(self.triggerChanging)
        self.trgTypeTab.currentChanged.connect(self.trgTabChanging)
        self.RunStopBut.clicked.connect(self.runstopclick)        
        self.AutoSet.clicked.connect(self.autosetclick)
        self.edgeSCh1.toggled.connect(self.triggerSourceChange)
        self.edgeMAuto.toggled.connect(self.triggerModeChange)
        self.edgeMNormal.toggled.connect(self.triggerModeChange)        
        self.edgeMSingle.toggled.connect(self.triggerModeChange)
        self.edgeMALevel.toggled.connect(self.triggerModeChange)    
        self.cursorSCh1.toggled.connect(self.cursorSourceChange)
        self.cursorX1.valueChanged.connect(self.x1change)
        self.cursorX2.valueChanged.connect(self.x2change)
        self.cursorY1.valueChanged.connect(self.y1change)
        self.cursorY2.valueChanged.connect(self.y2change)
        self.cursorXenabled.toggled.connect(self.xenable)
        self.cursorYenabled.toggled.connect(self.yenable)
        self.takePicture.clicked.connect(self.takingpicture)
        self.aboutUs.clicked.connect(self.aboutclicked)
        
        self.timerMain.start(900)
        
        
        
        
        
    def updateMAIN(self):
        self.ch1volt.setValue(self.ch1voltindex())
        self.ch2volt.setValue(self.ch2voltindex())
        self.timedial.setValue(self.timeindex())
        
    
    
    def changingvoltage1(self):
        y = ["0.002","0.005","0.01","0.02","0.05","0.1","0.2","0.5","1","2","5"]
        index = self.ch1volt.value()
        s.write(":CHAN1:SCAL "+y[index]+"\r")
        
        label=["2 mV","5 mV", "10 mV", "20 mV","50 mV","100 mV", "200 mV", "500 mV", "1 V","2 V","5 V"]
        self.ch1VoltDivLabel.setText(label[index])
        
  

    def ch1voltindex(self):
         s.write(":CHAN1:SCAL?\r")
         x = s.readline()
         a = ["2.00mV\n","5.00mV\n","10.0mV\n","20.0mV\n","50.0mV\n","100mV\n","200mV\n","500mV\n","1.00V\n","2.00V\n","5.00V\n"]
         
         
         index = 0
           
         while (x != a[index]):
             index += 1
               
         self.ch1VoltDivLabel.setText(x)
         return index
        
         
    def changingvoltage2(self):
        y = ["0.002","0.005","0.01","0.02","0.05","0.1","0.2","0.5","1","2","5"]
        index = self.ch2volt.value()
        s.write(":CHAN2:SCAL "+y[index]+"\r")
        label=["2 mV","5 mV", "10 mV", "20 mV","50 mV","100 mV", "200 mV", "500 mV", "1 V","2 V","5 V"]
        self.ch2VoltDivLabel.setText(label[index])
  

    def ch2voltindex(self):
         s.write(":CHAN2:SCAL?\r")
         x = s.readline()
           
         a = ["2.00mV\n","5.00mV\n","10.0mV\n","20.0mV\n","50.0mV\n","100mV\n","200mV\n","500mV\n","1.00V\n","2.00V\n","5.00V\n"]
           
         index = 0
           
         while (x != a[index]):
             index += 1
         
         self.ch2VoltDivLabel.setText(x)
         return index
         
        

        
    def changingtime(self):
        t=["1e-9","2.5e-9","5e-9","10e-9","25e-9","50e-9","100e-9","250e-9","500e-9",
        "1e-6","2.5e-6","5e-6","10e-6","25e-6","50e-6","100e-6","250e-6","500e-6",
        "1e-3","2.5e-3","5e-3","10e-3","25e-3","50e-3","100e-3","250e-3","500e-3",
        "1","2.5","5","10"]
        index= self.timedial.value()
        
        s.write(":TIMebase:SCALe "+t[index]+"\r")
        
        label=["1 ns","2.5 ns","5 ns","10 ns","25 ns","50 ns", "100 ns","250 ns", "500 ns",
               "1 us","2.5 us","5 us","10 us","25 us","50 us", "100 us","250 us", "500 us",
               "1 ms","2.5 ms","5 ms","10 ms","25 ms","50 ms", "100 ms","250 ms", "500 ms",
               "1 s","2.5 s","5 s","10 s"]
        self.timDivLabel.setText(label[index])
        
        
    def timeindex(self):
        s.write(":TIMebase:SCALe?\r")
        y=s.readline()
        
        a=["1.000ns\n","2.500ns\n","5.000ns\n","10.00ns\n","25.00ns\n","50.00ns\n","100.0ns\n","250.0ns\n","500.0ns\n",
        "1.000us\n","2.500us\n","5.000us\n","10.00us\n","25.00us\n","50.00us\n","100.0us\n","250.0us\n","500.0us\n",
        "1.000ms\n","2.500ms\n","5.000ms\n","10.00ms\n","25.00ms\n","50.00ms\n","100.0ms\n","250.0ms\n","500.0ms\n",
        "1.000s\n","2.500s\n","5.000s\n","10.00s\n"]

        
        index = 0
        
        while(y != a[index]):
            index +=1
            
        self.timDivLabel.setText(y)
        return index


       
    def counterchanging(self):
        index=self.ch1voltindex()
        value=self.CounterPos.value()
        if(index<5):
            self.CounterPos.setStep(0.00001)
            self.CounterPos.setMinValue(-0.50)
            self.CounterPos.setMaxValue(0.50)
            self.CounterPos.setStepButton1(8)
            self.CounterPos.setStepButton2(16)
            self.CounterPos.setStepButton3(32)
            s.write(":CHANnel1:OFFSet "+str(value)+"\r")
            
        elif(index<7):
            self.CounterPos.setStep(0.001)
            self.CounterPos.setMinValue(-5.0)
            self.CounterPos.setMaxValue(5.0)
            self.CounterPos.setStepButton1(8)
            self.CounterPos.setStepButton2(16)
            self.CounterPos.setStepButton3(32)
            s.write(":CHANnel1:OFFSet "+str(value)+"\r")            
        
        else:
            self.CounterPos.setStep(0.01)
            self.CounterPos.setMinValue(-50.0)
            self.CounterPos.setMaxValue(50.0)
            self.CounterPos.setStepButton1(8)
            self.CounterPos.setStepButton2(16)
            self.CounterPos.setStepButton3(32)
            s.write(":CHANnel1:OFFSet "+str(value)+"\r")
            
    def counterchanging2(self):
        index=self.ch2voltindex()
        value=self.CounterPos_2.value()
        if(index<5):
            self.CounterPos_2.setStep(0.00001)
            self.CounterPos_2.setMinValue(-0.50)
            self.CounterPos_2.setMaxValue(0.50)
            self.CounterPos_2.setStepButton1(8)
            self.CounterPos_2.setStepButton2(16)
            self.CounterPos_2.setStepButton3(32)
            s.write(":CHANnel2:OFFSet "+str(value)+"\r")
            
        elif(index<7):
            self.CounterPos_2.setStep(0.001)
            self.CounterPos_2.setMinValue(-5.0)
            self.CounterPos_2.setMaxValue(5.0)
            self.CounterPos_2.setStepButton1(8)
            self.CounterPos_2.setStepButton2(16)
            self.CounterPos_2.setStepButton3(32)
            s.write(":CHANnel2:OFFSet "+str(value)+"\r")            
        else:
            self.CounterPos_2.setStep(0.01)
            self.CounterPos_2.setMinValue(-50.0)
            self.CounterPos_2.setMaxValue(50.0)
            self.CounterPos_2.setStepButton1(8)
            self.CounterPos_2.setStepButton2(16)
            self.CounterPos_2.setStepButton3(32)
            s.write(":CHANnel2:OFFSet "+str(value)+"\r")
            
    def counterchanging3(self):
        index=self.timeindex()
        value=self.CounterPos_3.value()
        if(index<10):
            self.CounterPos_3.setStep(0.00001)
            self.CounterPos_3.setMinValue(-0.50)
            self.CounterPos_3.setMaxValue(0.50)
            self.CounterPos_3.setStepButton1(8)
            self.CounterPos_3.setStepButton2(16)
            self.CounterPos_3.setStepButton3(32)
            s.write(":TIMebase:DELay "+str(value)+"\r")
            
        elif(index<20):
            self.CounterPos_3.setStep(0.001)
            self.CounterPos_3.setMinValue(-5.0)
            self.CounterPos_3.setMaxValue(5.0)
            self.CounterPos_3.setStepButton1(8)
            self.CounterPos_3.setStepButton2(16)
            self.CounterPos_3.setStepButton3(32)
            s.write(":TIMebase:DELay "+str(value)+"\r")            
        else:
            self.CounterPos_3.setStep(0.01)
            self.CounterPos_3.setMinValue(-50.0)
            self.CounterPos_3.setMaxValue(50.0)
            self.CounterPos_3.setStepButton1(8)
            self.CounterPos_3.setStepButton2(16)
            self.CounterPos_3.setStepButton3(32)
            s.write(":TIMebase:DELay "+str(value)+"\r")
             
            
            
    def updateTimer(self):
        if(self.tabMenu.currentIndex()==0):
            self.triggerTimer.stop()
            self.cursorTimer.stop()
            self.measureTimer.start(250)
            
        elif(self.tabMenu.currentIndex()==1):
            self.measureTimer.stop()
            self.cursorTimer.stop()
            self.triggerTimer.start(250)
        else:
            self.measureTimer.stop()
            self.triggerTimer.stop()
            self.cursorTimer.start(250)
            if(self.cursorXenabled.isChecked()):
                s.write(":CURSor:XDISplay 1\r")
            else:
                s.write(":CURSor:XDISplay 0\r")
            if(self.cursorYenabled.isChecked()):
                s.write(":CURSor:YDISplay 1\r")
            else:
                s.write(":CURSor:YDISplay 0\r")
            
            
    def getTrigger(self):
        self.triggerSourceUpdate()
        self.triggerModeUpdate()
    
    def getCursor(self):
        self.cursorSourceUpdate()
        self.getdelta()
        #self.cursorUpdate()
            
    def getMeasure(self):
        if(self.VppCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VPP?\r")
            x = s.readline()
            self.VppLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VPP?\r")
            x = s.readline()
            self.VppLabel2.setText("2: "+x)
        else:
            self.VppLabel1.clear()
            self.VppLabel2.clear()
            
    
        if(self.FallCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:FALL?\r")
            x = s.readline()
            self.FallLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:FALL?\r")
            x = s.readline()
            self.FallLabel2.setText("2: "+x)
        else:
            self.FallLabel1.clear()
            self.FallLabel2.clear()
            
        
        if(self.FreCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:FREQuency?\r")
            x = s.readline()
            self.FreLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:FREQuency?\r")
            x = s.readline()
            self.FreLabel2.setText("2: "+x)
        else:
            self.FreLabel1.clear()
            self.FreLabel2.clear()
            
        
        if(self.NWidthCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:NWIDth?\r")
            x = s.readline()
            self.NWidthLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:NWIDth?\r")
            x = s.readline()
            self.NWidthLabel2.setText("2: "+x)
        else:
            self.NWidthLabel1.clear()
            self.NWidthLabel2.clear()    
            
        
        if(self.PDutyCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:PDUTy?\r")
            x = s.readline()
            self.PDutyLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:PDUTy?\r")
            x = s.readline()
            self.PDutyLabel2.setText("2: "+x)
        else:
            self.PDutyLabel1.clear()
            self.PDutyLabel2.clear()
            
        
        if(self.PeriodCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:PERiod?\r")
            x = s.readline()
            self.PeriodLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:PERiod?\r")
            x = s.readline()
            self.PeriodLabel2.setText("2: "+x)
        else:
            self.PeriodLabel1.clear()
            self.PeriodLabel2.clear()
            
        
        if(self.RiseCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:RISe?\r")
            x = s.readline()
            self.RiseLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:RISe?\r")
            x = s.readline()
            self.RiseLabel2.setText("2: "+x)
        else:
            self.RiseLabel1.clear()
            self.RiseLabel2.clear()
            
          
        if(self.PWidthCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:PWIDth?\r")
            x = s.readline()
            self.PWidthLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:PWIDth?\r")
            x = s.readline()
            self.PWidthLabel2.setText("2: "+x)
        else:
            self.PWidthLabel1.clear()
            self.PWidthLabel2.clear()  
            
        
        if(self.VampCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VAMPlitude?\r")
            x = s.readline()
            self.VampLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VAMPlitude?\r")
            x = s.readline()
            self.VampLabel2.setText("2: "+x)
        else:
            self.VampLabel1.clear()
            self.VampLabel2.clear()
            
            
            
        if(self.VavCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VAVerage?\r")
            x = s.readline()
            self.VavLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VAVerage?\r")
            x = s.readline()
            self.VavLabel2.setText("2: "+x)
        else:
            self.VavLabel1.clear()
            self.VavLabel2.clear()
            
            
        if(self.VHighCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VHI?\r")
            x = s.readline()
            self.VHighLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VHI?\r")
            x = s.readline()
            self.VHighLabel2.setText("2: "+x)
        else:
            self.VHighLabel1.clear()
            self.VHighLabel2.clear()
            
            
        if(self.VLowCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VLO?\r")
            x = s.readline()
            self.VLowLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VLO?\r")
            x = s.readline()
            self.VLowLabel2.setText("2: "+x)
        else:
            self.VLowLabel1.clear()
            self.VLowLabel2.clear()
            
            
        if(self.VMaxCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VMAX?\r")
            x = s.readline()
            self.VMaxLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VMAX?\r")
            x = s.readline()
            self.VMaxLabel2.setText("2: "+x)
        else:
            self.VMaxLabel1.clear()
            self.VMaxLabel2.clear()
            
        
        if(self.VMinCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VMIN?\r")
            x = s.readline()
            self.VMinLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VMIN?\r")
            x = s.readline()
            self.VMinLabel2.setText("2: "+x)
        else:
            self.VMinLabel1.clear()
            self.VMinLabel2.clear()
            
            
        if(self.VRmsCB.isChecked()):
            s.write(":MEASure:SOURce 1\r")
            s.write(":MEASure:VRMS?\r")
            x = s.readline()
            self.VRmsLabel1.setText("1: "+x)
            s.write(":MEASure:SOURce 2\r")
            s.write(":MEASure:VRMS?\r")
            x = s.readline()
            self.VRmsLabel2.setText("2: "+x)
        else:
            self.VRmsLabel1.clear()
            self.VRmsLabel2.clear()
            
    def trgTypeUpdate(self):
        if(self.trgEdge.isChecked()):
            s.write(":TRIGger:TYPe 0\r")
            self.trgTypeTab.setCurrentIndex(0)
        elif(self.trgVideo.isChecked()):
            s.write(":TRIGger:TYPe 1\r")
            self.trgTypeTab.setCurrentIndex(1)
        elif(self.trgPulse.isChecked()):
            s.write(":TRIGger:TYPe 2\r")
            self.trgTypeTab.setCurrentIndex(2)
        elif(self.trgDelay.isChecked()):
            s.write(":TRIGger:TYPe 3\r")
            self.trgTypeTab.setCurrentIndex(3)
            
    def triggerChanging(self):
        s.write(":TRIGger:SOURce ?\r")
        x = s.readline()
        index=0
        if(x=="1\n"):
            index=self.ch1voltindex()
        elif(x=="2\n"):
            index=self.ch1voltindex()
        value=self.triggerLevel.value()
        if(index<5):
            self.triggerLevel.setStep(0.00001)
            self.triggerLevel.setMinValue(-0.50)
            self.triggerLevel.setMaxValue(0.50)
            self.triggerLevel.setStepButton1(8)
            self.triggerLevel.setStepButton2(16)
            self.triggerLevel.setStepButton3(32)
            s.write(":TRIGger:LEVel "+str(value)+"\r")
            
        elif(index<7):
            self.triggerLevel.setStep(0.001)
            self.triggerLevel.setMinValue(-5.0)
            self.triggerLevel.setMaxValue(5.0)
            self.triggerLevel.setStepButton1(8)
            self.triggerLevel.setStepButton2(16)
            self.triggerLevel.setStepButton3(32)
            s.write(":TRIGger:LEVel "+str(value)+"\r")            
               
        else:
            self.triggerLevel.setStep(0.01)
            self.triggerLevel.setMinValue(-50.0)
            self.triggerLevel.setMaxValue(50.0)
            self.triggerLevel.setStepButton1(8)
            self.triggerLevel.setStepButton2(16)
            self.triggerLevel.setStepButton3(32)
            s.write(":TRIGger:LEVel "+str(value)+"\r")               
       
    def trgTabChanging(self):
        if(self.trgTypeTab.currentIndex()==0):
            self.trgEdge.setChecked(True)
        elif(self.trgTypeTab.currentIndex()==1):
            self.trgVideo.setChecked(True)
        elif(self.trgTypeTab.currentIndex()==2):
            self.trgPulse.setChecked(True)
        elif(self.trgTypeTab.currentIndex()==3):
            self.trgDelay.setChecked(True)
      
    def runstopclick(self):
        if(self.run==True):
            s.write(":STOP\r")
            self.run=False
            self.statusbar.showMessage("Display Stopped")
            
            
        elif(self.run==False):
            s.write(":RUN\r")
            self.run=True
            self.statusbar.showMessage("Display Running")
            
            
            
    def autosetclick(self):
        self.timerMain.stop()
        s.write(":AUToset\r")
        self.statusbar.showMessage("AutoSet")
        self.teksefer.start(5000)
        
    def tekseferto(self):
        self.statusbar.showMessage("")
        self.timerMain.start(250)
      
      
    def triggerSourceChange(self):
        if(self.edgeSCh1.isChecked()):
            s.write(":TRIGger:SOURce 0\r")
        elif(self.edgeSCh2.isChecked()):
            s.write(":TRIGger:SOURce 1\r")
      
      
      
    def closeEvent(self, event):
       
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
            self.measureTimer.stop()
            self.triggerTimer.stop()
            self.cursorTimer.stop()
            self.timerMain.stop()
            s.close()            
        else:
            event.ignore()
            
    def triggerSourceUpdate(self):
        s.write(":TRIGger:SOURce ?\r")
        x = s.readline()
        
        if(x=="0\n"):
            self.edgeSCh1.setChecked(True)
        elif(x=="1\n"):
            self.edgeSCh2.setChecked(True)
        else:
            self.statusbar.showMessage("Only CH1 and CH2 available.")
            self.teksefer.start(200)
            
            
    def triggerModeChange(self):
        if(self.edgeMAuto.isChecked()):
            s.write(":TRIGger:MODe 1\r")
        elif(self.edgeMNormal.isChecked()):
            s.write(":TRIGger:MODe 2\r")
        elif(self.edgeMSingle.isChecked()):
            s.write(":TRIGger:MODe 3\r")
        elif(self.edgeMALevel.isChecked()):
            s.write(":TRIGger:MODe 0\r")
            
    def triggerModeUpdate(self):
        s.write(":TRIGger:MODe ?\r")
        x = s.readline()
        
        if(x=="0\n"):
            self.edgeMALevel.setChecked(True)
        elif(x=="1\n"):
            self.edgeMAuto.setChecked(True)
        elif(x=="2\n"):
            self.edgeMNormal.setChecked(True)
        elif(x=="3\n"):
            self.edgeMSingle.setChecked(True)
    
    def cursorSourceChange(self):
        if(self.cursorSCh1.isChecked()):
            s.write(":CURSor:SOURce 1\r")
        else:
            s.write(":CURSor:SOURce 2\r")
            
    def cursorSourceUpdate(self):
        s.write(":CURSor:SOURce?\r")
        x = s.readline()
            
        if(x=="1\n"):
            self.cursorSCh1.setChecked(True)
        elif(x=="2\n"):
            self.cursorSCh2.setChecked(True)
            
    def cursorUpdate(self):
        s.write(":CURSor:X1Position?\r")
        x=s.readline()
        self.cursorX1.setValue(int(x))
        
        s.write(":CURSor:X2Position?\r")
        x=s.readline()
        self.cursorX2.setValue(int(x))
        
        s.write(":CURSor:Y1Position?\r")
        x=s.readline()
        self.cursorY1.setValue(int(x))
        
        s.write(":CURSor:Y2Position?\r")
        x=s.readline()
        self.cursorY2.setValue(int(x))
            
            
            
    def x1change(self):
        self.x1crsrtimer.start(20)
        
    def x2change(self):
        self.x2crsrtimer.start(20)
        
    def y1change(self):
        self.y1crsrtimer.start(20)
        
    def y2change(self):
        self.y2crsrtimer.start(20)
        
    def x1crsr(self):
        s.write(":CURSor:X1Position "+str(self.cursorX1.value())+"\r")
        
    def x2crsr(self):
        s.write(":CURSor:X2Position "+str(self.cursorX2.value())+"\r")
        
    def y1crsr(self):
        s.write(":CURSor:Y1Position "+str(200-self.cursorY1.value())+"\r")
        
    def y2crsr(self):
        s.write(":CURSor:Y2Position "+str(200-self.cursorY2.value())+"\r")
    
    def getdelta(self):
        if(self.cursorXenabled.isChecked()):
            s.write(":CURSor:XDELta?\r")
            x=s.readline()
            self.deltaX.setText("X:"+x)
        if(self.cursorXenabled.isChecked()):
            s.write(":CURSor:YDELta?\r")
            x=s.readline()
            self.deltaY.setText("Y:"+x)
            
            
    def xenable(self):
        if(self.cursorXenabled.isChecked()):
            s.write(":CURSor:XDISplay 1\r")
        else:
            s.write(":CURSor:XDISplay 0\r")
            
    def yenable(self):
        if(self.cursorYenabled.isChecked()):
            s.write(":CURSor:YDISplay 1\r")
        else:
            s.write(":CURSor:YDISplay 0\r")
            
            
    def takingpicture(self):
        
        s.write(":ACQuire:MODe 0\r")
        s.write(":ACQuire:LENGth 0\r")
        s.write(":ACQuire1:POINt\r")
        x=s.read(2000)
        s.write(":TIMebase:SCALe?\r")
        
        timeStr=s.readline()
        if(timeStr[5]=='m'):
            self.carpan.setText("miliseconds")
        elif(timeStr[5]=='u'):
            self.carpan.setText("microseconds")
        elif(timeStr[5]=='n'):
            self.carpan.setText("nanoseconds")
        else:
            self.carpan.setText("seconds")
        timeDIV=float(timeStr[:4])
        
        s.write(":CHAN1:SCAL?\r")
        volt1str=s.readline()
        if(volt1str.find('m')>0):
            self.plotCh1text.setText("miliVolts")
        else:
            self.plotCh1text.setText("Volts")
        voltDIV1 = float(volt1str[:3])
        y=map(ord,x[14:])
        i=0
        j=0
        a=[]
        if(y!=[]):
            while(i<1000):
                a.append(256*y[i]+y[i+1])
                if a[j]> 32767:
                    a[j]=(65536-a[j])*(-1)
                a[j]= a[j]*voltDIV1/25.6
                i+=2
                j+=1
                 
            
        s.write(":ACQuire2:POINt\r")
        x=s.read(2000)
        s.write(":CHAN2:SCAL?\r")
        volt2str=s.readline()
        if(volt2str.find('m')>0):
            self.plotCh2text.setText("miliVolts")
        else:
            self.plotCh2text.setText("Volts")
        voltDIV2 = float(volt2str[:3])
        y=map(ord,x[14:])
        i=0
        j=0
        b=[]
        if(y!=[]):
            while(i<1000):
                b.append(256*y[i]+y[i+1])
                if b[j]> 32767:
                    b[j]=(65536-b[j])*(-1)
                b[j]= b[j]*voltDIV2/25.6
                i+=2
                j+=1
        
        
        t = np.linspace(-10*timeDIV,10*timeDIV,500)       
        if(a!=[] and b!=[]):
            
            ax1=self.mplwidget.figure.add_subplot(111)
            ax2=ax1.twinx()
            ax1.plot(t,a,'b')
            ax2.plot(t,b,'g')
            ax1.axis([-10*timeDIV,10*timeDIV,-4*voltDIV1,4*voltDIV1])
            ax2.axis([-10*timeDIV,10*timeDIV,-4*voltDIV2,4*voltDIV2])
            self.mplwidget.axes.xaxis.set_ticks(np.linspace(-10*timeDIV,10*timeDIV,21))
            self.mplwidget.axes.grid()
            
            self.mplwidget.draw()
            ax2.set_visible(False)
            #ax2.clear()
            
            
            
        elif(a!=[]):
            self.plotCh2text.setText("")
            self.mplwidget.axes.plot(t,a)
            self.mplwidget.axes.xaxis.set_ticks(np.linspace(-10*timeDIV,10*timeDIV,21))
            self.mplwidget.axes.grid()
            self.mplwidget.axes.axis([-10*timeDIV,10*timeDIV,-4*voltDIV1,4*voltDIV1])
            self.mplwidget.draw()
        elif(b!=[]):
            self.plotCh2text.setText("")
            self.mplwidget.axes.plot(t,b,'g')
            self.mplwidget.axes.xaxis.set_ticks(np.linspace(-10*timeDIV,10*timeDIV,21))
            self.mplwidget.axes.grid()
            self.mplwidget.axes.axis([-10*timeDIV,10*timeDIV,-4*voltDIV2,4*voltDIV2])
            self.mplwidget.draw()
        else:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Both of the channels are closed.")
            msgBox.setInformativeText("Please check the connections!")
            msgBox.setWindowTitle("Warning!!!")
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.exec_()
            
            
            
            
    def aboutclicked(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText(u"Server Özbaş(serverozbas@gmail.com)\nCaner Ertem(caner.ertem7@gmail.com)\nGüven Aşcı(guvenasci93@gmail.com")
        msgBox.setWindowTitle("Contact Us")
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.exec_()
            
            
            
            
            
            
app = QtGui.QApplication(sys.argv)
MainApp = pencere()
MainApp.show()
app.exec_()

