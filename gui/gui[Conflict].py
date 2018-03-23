# -*- coding: utf-8 -*-
import matplotlib
import pandas as pd
import time
import numpy as np

matplotlib.use('Qt5Agg')
import os
import logging.handlers
import pytesseract
import threading
import datetime
import sys
from PIL import Image
from PyQt5 import QtWidgets, QtGui

import matplotlib
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
from weakref import proxy
from PyQt5.QtWidgets import QMessageBox
import os


from PyQt5 import QtCore, QtGui, QtWidgets


"""
1. Single text line for changing messages.
2. A block of text presenting the text from the terminal client
3. Some way to nicely display numerical data. Meters and gauges would be nice. Also perhaps a table set up nicely.
4. Somewhere that allows the presentation of images.
5. Plot presentation.
6. If possible, present floor plans somewhere somehow

"""
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(722, 748)
        Form.setMinimumSize(QtCore.QSize(722, 748))
        Form.setMaximumSize(QtCore.QSize(722, 748))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combobox_strategy = QtWidgets.QComboBox(Form)
        self.combobox_strategy.setObjectName("combobox_strategy")
        self.horizontalLayout.addWidget(self.combobox_strategy)
        self.combobox_gamestage = QtWidgets.QComboBox(Form)
        self.combobox_gamestage.setObjectName("combobox_gamestage")
        self.horizontalLayout.addWidget(self.combobox_gamestage)
        self.combobox_actiontype = QtWidgets.QComboBox(Form)
        self.combobox_actiontype.setObjectName("combobox_actiontype")
        self.horizontalLayout.addWidget(self.combobox_actiontype)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 2)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 4, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 4, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.EquityHistogram = QtWidgets.QWidget()
        self.EquityHistogram.setObjectName("EquityHistogram")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.EquityHistogram)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 261, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vLayout_bar = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_bar.setObjectName("vLayout_bar")
        self.widget_2 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.vLayout_bar.addWidget(self.widget_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.EquityHistogram)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(280, 140, 411, 411))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.horizontalLayoutWidget_3)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3.addWidget(self.widget_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.EquityHistogram)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 681, 121))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.vLayout_fundschange = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.vLayout_fundschange.setObjectName("vLayout_fundschange")
        self.widget = QtWidgets.QWidget(self.verticalLayoutWidget_2)
        self.widget.setObjectName("widget")
        self.vLayout_fundschange.addWidget(self.widget)
        self.tabWidget.addTab(self.EquityHistogram, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.WorstGames = QtWidgets.QWidget()
        self.WorstGames.setObjectName("WorstGames")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.WorstGames)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView = QtWidgets.QTableView(self.WorstGames)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableView.setFont(font)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.WorstGames, "")
        self.gridLayout.addWidget(self.tabWidget, 5, 0, 1, 3)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Strategy Analyser"))
        self.label_4.setText(_translate("Form", "Strategy Analyser"))
        self.label.setText(_translate("Form", "Strategy"))
        self.label_2.setText(_translate("Form", "Game Stage"))
        self.label_3.setText(_translate("Form", "Action Type"))
        self.combobox_strategy.setToolTip(_translate("Form", "<html><head/><body><p>Choose the strategy you would like to analyse. \'.*\' means all strategies together.</p></body></html>"))
        self.combobox_gamestage.setToolTip(_translate("Form", "Choose the game stage you want to focus on."))
        self.combobox_actiontype.setToolTip(_translate("Form", "Choose what kind of decision you want to analyse in more detail."))
        self.label_6.setText(_translate("Form", "Total played hands"))
        self.label_5.setText(_translate("Form", "Return in bb per 100 hands"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EquityHistogram), _translate("Form", "Equity Histogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Scatter Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WorstGames), _translate("Form", "Worst Hands"))


class AiInterface(object):
    def setupUi(self, AI):
        AI.setObjectName("AI")
        AI.setEnabled(True)
        AI.resize(617, 713)
        AI.setMinimumSize(QtCore.QSize(617, 713))
        AI.setMaximumSize(QtCore.QSize(617, 713))
        font = QtGui.QFont()
        font.setPointSize(12)
        AI.setFont(font)
        AI.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(AI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.vLayout = QtWidgets.QVBoxLayout()
        self.vLayout.setObjectName("vLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.vLayout.addWidget(self.widget_3)
        self.gridLayout.addLayout(self.vLayout, 8, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 2)
        self.vLayout4 = QtWidgets.QVBoxLayout()
        self.vLayout4.setObjectName("vLayout4")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.vLayout4.addWidget(self.widget_2)
        self.gridLayout.addLayout(self.vLayout4, 9, 3, 1, 3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.button_resume = QtWidgets.QPushButton(self.centralwidget)
        self.button_resume.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_resume.setFont(font)
        self.button_resume.setObjectName("button_resume")
        self.verticalLayout_7.addWidget(self.button_resume)
        self.button_pause = QtWidgets.QPushButton(self.centralwidget)
        self.button_pause.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_pause.setFont(font)
        self.button_pause.setObjectName("button_pause")
        self.verticalLayout_7.addWidget(self.button_pause)
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.verticalLayout_7.addWidget(self.button_2)
        self.verticalLayout_7.addWidget(self.button_1)
        self.gridLayout.addLayout(self.verticalLayout_7, 5, 0, 1, 3)
        self.vLayout2 = QtWidgets.QVBoxLayout()
        self.vLayout2.setObjectName("vLayout2")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setObjectName("widget_4")
        self.vLayout2.addWidget(self.widget_4)
        self.gridLayout.addLayout(self.vLayout2, 8, 3, 1, 3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.last_decision = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.last_decision.setFont(font)
        self.last_decision.setAutoFillBackground(False)
        self.last_decision.setFrameShape(QtWidgets.QFrame.Panel)
        self.last_decision.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.last_decision.setScaledContents(False)
        self.last_decision.setAlignment(QtCore.Qt.AlignCenter)
        self.last_decision.setIndent(-1)
        self.last_decision.setObjectName("last_decision")
        self.gridLayout_2.addWidget(self.last_decision, 2, 0, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.progress_bar.setProperty("value", 0)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_2.addWidget(self.progress_bar, 5, 0, 1, 1)
        self.comboBox_current_strategy = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_current_strategy.setFont(font)
        self.comboBox_current_strategy.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_current_strategy.setObjectName("comboBox_current_strategy")
        self.gridLayout_2.addWidget(self.comboBox_current_strategy, 6, 0, 1, 1)
        self.status = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.status.setFont(font)
        self.status.setToolTip("")
        self.status.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.gridLayout_2.addWidget(self.status, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 5, 3, 1, 3)
        self.vLayout3 = QtWidgets.QVBoxLayout()
        self.vLayout3.setObjectName("vLayout3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.vLayout3.addWidget(self.widget)
        self.gridLayout.addLayout(self.vLayout3, 9, 0, 1, 3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.winnings = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.winnings.setFont(font)
        self.winnings.setText("")
        self.winnings.setObjectName("winnings")
        self.verticalLayout_6.addWidget(self.winnings)
        self.assumed_players = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.assumed_players.setFont(font)
        self.assumed_players.setText("")
        self.assumed_players.setObjectName("assumed_players")
        self.verticalLayout_6.addWidget(self.assumed_players)
        self.mincallequity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mincallequity.setFont(font)
        self.mincallequity.setText("")
        self.mincallequity.setObjectName("mincallequity")
        self.verticalLayout_6.addWidget(self.mincallequity)
        self.minbetequity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.minbetequity.setFont(font)
        self.minbetequity.setText("")
        self.minbetequity.setObjectName("minbetequity")
        self.verticalLayout_6.addWidget(self.minbetequity)
        self.required_mincall = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.required_mincall.setFont(font)
        self.required_mincall.setText("")
        self.required_mincall.setObjectName("required_mincall")
        self.verticalLayout_6.addWidget(self.required_mincall)
        self.required_minbet = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.required_minbet.setFont(font)
        self.required_minbet.setText("")
        self.required_minbet.setObjectName("required_minbet")
        self.verticalLayout_6.addWidget(self.required_minbet)
        self.round_pot = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.round_pot.setFont(font)
        self.round_pot.setText("")
        self.round_pot.setObjectName("round_pot")
        self.verticalLayout_6.addWidget(self.round_pot)
        self.pot_multiple = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pot_multiple.setFont(font)
        self.pot_multiple.setText("")
        self.pot_multiple.setObjectName("pot_multiple")
        self.verticalLayout_6.addWidget(self.pot_multiple)
        self.calllimit = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calllimit.setFont(font)
        self.calllimit.setText("")
        self.calllimit.setObjectName("calllimit")
        self.verticalLayout_6.addWidget(self.calllimit)
        self.betlimit = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.betlimit.setFont(font)
        self.betlimit.setText("")
        self.betlimit.setObjectName("betlimit")
        self.verticalLayout_6.addWidget(self.betlimit)
        self.outs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.outs.setFont(font)
        self.outs.setText("")
        self.outs.setObjectName("outs")
        self.verticalLayout_6.addWidget(self.outs)
        self.gridLayout.addLayout(self.verticalLayout_6, 3, 5, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.verticalLayout_5.addWidget(self.label1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_5.addWidget(self.label_21)
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_5.addWidget(self.label_23)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 3, 1, 2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.equity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.equity.setFont(font)
        self.equity.setText("")
        self.equity.setObjectName("equity")
        self.verticalLayout_3.addWidget(self.equity)
        self.range_equity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.range_equity.setFont(font)
        self.range_equity.setText("")
        self.range_equity.setObjectName("range_equity")
        self.verticalLayout_3.addWidget(self.range_equity)
        self.relative_equity = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.relative_equity.setFont(font)
        self.relative_equity.setText("")
        self.relative_equity.setObjectName("relative_equity")
        self.verticalLayout_3.addWidget(self.relative_equity)
        self.sheetname = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sheetname.setFont(font)
        self.sheetname.setText("")
        self.sheetname.setObjectName("sheetname")
        self.verticalLayout_3.addWidget(self.sheetname)
        self.opponent_range = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.opponent_range.setFont(font)
        self.opponent_range.setText("")
        self.opponent_range.setObjectName("opponent_range")
        self.verticalLayout_3.addWidget(self.opponent_range)
        self.mycards = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.mycards.setFont(font)
        self.mycards.setText("")
        self.mycards.setObjectName("mycards")
        self.verticalLayout_3.addWidget(self.mycards)
        self.tablecards = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tablecards.setFont(font)
        self.tablecards.setText("")
        self.tablecards.setObjectName("tablecards")
        self.verticalLayout_3.addWidget(self.tablecards)
        self.collusion_cards = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.collusion_cards.setFont(font)
        self.collusion_cards.setText("")
        self.collusion_cards.setObjectName("collusion_cards")
        self.verticalLayout_3.addWidget(self.collusion_cards)
        self.runs = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.runs.setFont(font)
        self.runs.setText("")
        self.runs.setObjectName("runs")
        self.verticalLayout_3.addWidget(self.runs)
        self.initiative = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.initiative.setFont(font)
        self.initiative.setText("")
        self.initiative.setObjectName("initiative")
        self.verticalLayout_3.addWidget(self.initiative)
        self.gamenumber = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.gamenumber.setFont(font)
        self.gamenumber.setText("")
        self.gamenumber.setObjectName("gamenumber")
        self.verticalLayout_3.addWidget(self.gamenumber)
        self.gridLayout.addLayout(self.verticalLayout_3, 3, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_4.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_4.addWidget(self.label_20)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_4.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_4.addWidget(self.label_17)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_4.addWidget(self.label_15)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_4.addWidget(self.label_18)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_4, 3, 0, 1, 2)
        AI.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AI)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        AI.setStatusBar(self.statusbar)

        self.retranslateUi(AI)
        QtCore.QMetaObject.connectSlotsByName(AI)

    def retranslateUi(self, AI):
        _translate = QtCore.QCoreApplication.translate
        AI.setWindowTitle(_translate("AI", "AI"))
        self.label_11.setText(_translate("AI", "AI Interface"))
        self.button_resume.setText(_translate("AI", "Start"))
        self.button_pause.setText(_translate("AI", "Stop"))
        self.button_1.setText(_translate("AI", "Button 1"))
        self.button_2.setText(_translate("AI", "Button 2"))
        self.last_decision.setText(_translate("AI", "This is a bard that displays text"))
        self.status.setText(_translate("AI", "This label displays messages"))
        self.label1.setText(_translate("AI", "Label"))
        self.label_10.setText(_translate("AI", "Label"))
        self.label_6.setText(_translate("AI", "Label"))
        self.label1.setText(_translate("AI", "Label"))
        self.label_5.setText(_translate("AI", "Label"))
        self.label_7.setText(_translate("AI", "Label"))
        self.label_8.setText(_translate("AI", "Label"))
        self.label_21.setText(_translate("AI", "Label"))
        self.label_23.setText(_translate("AI", "Label"))
        self.label_3.setText(_translate("AI", "Label"))
        self.label_4.setText(_translate("AI", "Label"))
        self.label_12.setText(_translate("AI", "Label"))
        self.label_2.setText(_translate("AI", "Label"))
        self.label_19.setText(_translate("AI", "Label"))
        self.label_20.setText(_translate("AI", "Label"))
        self.label_9.setText(_translate("AI", "Label"))
        self.label_13.setText(_translate("AI", "Label"))
        self.label_14.setText(_translate("AI", "Label"))
        self.label_16.setText(_translate("AI", "Label"))
        self.label_17.setText(_translate("AI", "Label"))
        self.label_15.setText(_translate("AI", "Label"))
        self.label_18.setText(_translate("AI", "Label"))
        self.label.setText(_translate("AI", "Label"))



class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table_analysers view with a pandas dataframe
    """

    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.values[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


class UIActionAndSignals(QObject):
    signal_progressbar_increase = QtCore.pyqtSignal(int)
    signal_progressbar_reset = QtCore.pyqtSignal()

    signal_status = QtCore.pyqtSignal(str)
    signal_decision = QtCore.pyqtSignal(str)

    signal_bar_chart_update = QtCore.pyqtSignal(object, str)
    signal_funds_chart_update = QtCore.pyqtSignal(object)
    signal_pie_chart_update = QtCore.pyqtSignal(dict)
    signal_curve_chart_update1 = QtCore.pyqtSignal(float, float, float, float, float, float, str, str)
    signal_curve_chart_update2 = QtCore.pyqtSignal(float, float, float, float, float, float, float, float, float, float, float)
    signal_lcd_number_update = QtCore.pyqtSignal(str, float)
    signal_label_number_update = QtCore.pyqtSignal(str, str)
    make_selection_from_bar = QtCore.pyqtSignal(str)

    signal_update_strategy_sliders = QtCore.pyqtSignal(str)
    signal_open_setup = QtCore.pyqtSignal(object, object)

    def __init__(self, ui_main_window):
        self.logger = logging.getLogger('gui')

        p=self.p = {}
        
        self.pause_thread = True
        self.exit_thread = False

        QObject.__init__(self)
        data = np.array([[1,2,3,4],[1,2,3,4]])

        self.ui = ui_main_window
        self.progressbar_value = 0

        # Main Window matplotlip widgets
        self.gui_funds = FundsPlotter(ui_main_window, p)
        self.gui_bar = BarPlotter(ui_main_window, p)
        self.gui_curve = CurvePlot(ui_main_window, p)
        self.gui_pie = PiePlotter(ui_main_window, winnerCardTypeList={'Highcard': 22})

        # main window status update signal connections
        self.signal_progressbar_increase.connect(self.increase_progressbar)
        self.signal_progressbar_reset.connect(self.reset_progressbar)
        self.signal_status.connect(self.update_mainwindow_status)
        self.signal_decision.connect(self.update_mainwindow_decision)

        self.signal_lcd_number_update.connect(self.update_lcd_number)
        self.signal_label_number_update.connect(self.update_label_number)

        self.signal_bar_chart_update.connect(lambda: self.gui_bar.drawfigure(data,p.current_strategy))

        self.signal_funds_chart_update.connect(lambda: self.gui_funds.drawfigure(data))
        self.signal_curve_chart_update1.connect(self.gui_curve.update_plots)
        self.signal_curve_chart_update2.connect(self.gui_curve.update_lines)
        self.signal_pie_chart_update.connect(self.gui_pie.drawfigure)

        ui_main_window.button_1.clicked.connect(lambda: self.button_1_action())
        ui_main_window.button_2.clicked.connect(lambda: self.button_2_action)
        ui_main_window.button_pause.clicked.connect(lambda: self.pause(ui_main_window, p))
        ui_main_window.button_resume.clicked.connect(lambda: self.resume(ui_main_window, p))


        self.signal_update_strategy_sliders.connect(lambda: self.update_strategy_editor_sliders(p.current_strategy))
        
        # These arethe items on the drop down menu
        lst = ["item1","item2"]
        ui_main_window.comboBox_current_strategy.addItems(lst)
        ui_main_window.comboBox_current_strategy.currentIndexChanged[str].connect(
            lambda: self.make_selection_from_bar(data, p))
        for i in [i for i, x in enumerate(lst) if x == "item1"]:
            idx = i
        ui_main_window.comboBox_current_strategy.setCurrentIndex(idx)

    def make_selection_from_bar(self, l, p):
        # Do something
        pass
    def pause(self, ui, p):
        ui.button_resume.setEnabled(True)
        ui.button_pause.setEnabled(False)
        self.pause_thread = True

    def resume(self, ui, p):
        ui.button_resume.setEnabled(False)
        ui.button_pause.setEnabled(True)
        self.pause_thread = False

    def increase_progressbar(self, value):
        self.progressbar_value += value
        if self.progressbar_value > 100: self.progressbar_value = 100
        self.ui.progress_bar.setValue(self.progressbar_value)

    def reset_progressbar(self):
        self.progressbar_value = 0
        self.ui.progress_bar.setValue(0)

    def update_mainwindow_status(self, text):
        self.ui.status.setText(text)

    def update_mainwindow_decision(self, text):
        self.ui.last_decision.setText(text)

    def update_lcd_number(self, item, value):
        func = getattr(self.ui, item)
        func.display(value)

    def update_label_number(self, item, value):
        func = getattr(self.ui, item)
        func.setText(str(value))

    def button_2_action(self, p, l):
        self.signal_progressbar_reset.emit()
        self.stragegy_analyser_form = QtWidgets.QWidget()
        self.ui_analyser = Ui_Form()
        self.ui_analyser.setupUi(self.stragegy_analyser_form)
        self.stragegy_analyser_form.show()

        self.gui_fundschange = FundsChangePlot(self.ui_analyser)
        self.gui_fundschange.drawfigure()

        self.ui_analyser.combobox_actiontype.addItems(
            ['Fold', 'Check', 'Call', 'Bet', 'BetPlus', 'Bet half pot', 'Bet pot', 'Bet Bluff'])
        self.ui_analyser.combobox_gamestage.addItems(['PreFlop', 'Flop', 'Turn', 'River'])
        self.ui_analyser.combobox_strategy.addItems(l.get_played_strategy_list())

        index = self.ui_analyser.combobox_strategy.findText(p.current_strategy, QtCore.Qt.MatchFixedString)
        if index >= 0:
            self.ui_analyser.combobox_strategy.setCurrentIndex(index)

        self.gui_histogram = HistogramEquityWinLoss(self.ui_analyser)
        self.gui_scatterplot = ScatterPlot(self.ui_analyser)

        self.ui_analyser.combobox_gamestage.currentIndexChanged[str].connect(
            lambda: self.strategy_analyser_update_plots(l, p))
        self.ui_analyser.combobox_actiontype.currentIndexChanged[str].connect(
            lambda: self.strategy_analyser_update_plots(l, p))
        self.ui_analyser.combobox_strategy.currentIndexChanged[str].connect(lambda: self.update_strategy_analyser(l, p))

        self.gui_bar2 = BarPlotter2(self.ui_analyser, l)
        self.gui_bar2.drawfigure(l, self.ui_analyser.combobox_strategy.currentText())
        self.update_strategy_analyser(l, p)

    def button_1_action(self):
        pass

    def strategy_analyser_update_plots(self, l, p):
        p_name = str(self.ui_analyser.combobox_strategy.currentText())
        game_stage = str(self.ui_analyser.combobox_gamestage.currentText())
        decision = str(self.ui_analyser.combobox_actiontype.currentText())

        self.gui_histogram.drawfigure(p_name, game_stage, decision, l)

        if p_name == '.*':
            p.read_strategy()
        else:
            p.read_strategy(p_name)

        call_or_bet = 'Bet' if decision[0] == 'B' else 'Call'

        max_value = float(p.selected_strategy['initialFunds'])
        min_equity = float(p.selected_strategy[game_stage + 'Min' + call_or_bet + 'Equity'])
        max_equity = float(
            p.selected_strategy['PreFlopMaxBetEquity']) if game_stage == 'PreFlop' and call_or_bet == 'Bet' else 1
        power = float(p.selected_strategy[game_stage + call_or_bet + 'Power'])
        max_X = .86 if game_stage == "Preflop" else 1

        self.gui_scatterplot.drawfigure(p_name, game_stage, decision, l,
                                        float(p.selected_strategy['smallBlind']),
                                        float(p.selected_strategy['bigBlind']),
                                        max_value,
                                        min_equity,
                                        max_X,
                                        max_equity,
                                        power)

    def strategy_analyser_update_table(self, l):
        p_name = str(self.ui_analyser.combobox_strategy.currentText())
        df = l.get_worst_games(p_name)
        model = PandasModel(df)
        self.ui_analyser.tableView.setModel(model)

    def update_strategy_editor_sliders(self, strategy_name):
        self.p.read_strategy(strategy_name)
        for key, value in self.strategy_items_with_multipliers.items():
            func = getattr(self.ui_editor, key)
            func.setValue(100)
            v = float(self.p.selected_strategy[key]) * value
            func.setValue(v)
            # print (key)

        self.ui_editor.pushButton_save_current_strategy.setEnabled(False)
        try:
            if self.p.selected_strategy['computername'] == os.environ['COMPUTERNAME'] or \
                            os.environ['COMPUTERNAME'] == 'NICOLAS-ASUS' or os.environ['COMPUTERNAME'] == 'Home-PC-ND':
                self.ui_editor.pushButton_save_current_strategy.setEnabled(True)
        except Exception as e:
            pass

        # This has to be loaded from somewhere
        possible_selections = ["something", "something_else"]
        selection = "Something"
        for i in [i for i, x in enumerate(possible_selections) if x == selection]:
            idx = i


class FundsPlotter(FigureCanvas):
    def __init__(self, ui, p):
        self.p = p
        self.ui = proxy(ui)
        self.fig = Figure(dpi=50)
        super(FundsPlotter, self).__init__(self.fig)
        # self.drawfigure()
        self.ui.vLayout.insertWidget(1, self)

    def drawfigure(self, data):
        Strategy = str(self.p.current_strategy)
        data = np.cumsum(data)
        self.fig.clf()
        self.axes = self.fig.add_subplot(111)  # create an axis
        self.axes.clear() # discards the old graph
        self.axes.set_title('My Funds')
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('$')
        self.axes.plot(data, '-')  # plot data
        self.draw()


class BarPlotter(FigureCanvas):
    def __init__(self, ui, p):
        self.p = p
        self.ui = proxy(ui)
        self.fig = Figure(dpi=50)
        super(BarPlotter, self).__init__(self.fig)
        # self.drawfigure()
        self.ui.vLayout2.insertWidget(1, self)

    def drawfigure(self, data, strategy):
        self.axes = self.fig.add_subplot(111)  # create an axis


        N = 11
        Bluff = data[0]
        BP = data[1]
        BHP = data[2]
        Bet = data[3]
        Call = data[4]
        Check = data[5]
        Fold = data[6]
        ind = np.arange(N)  # the x locations for the groups
        width = 1  # the width of the bars: can also be len(x) sequence

        self.p0 = self.axes.bar(ind, Bluff, width, color='y')
        self.p1 = self.axes.bar(ind, BP, width, color='k', bottom=Bluff)
        self.p2 = self.axes.bar(ind, BHP, width, color='b', bottom=[sum(x) for x in zip(Bluff, BP)])
        self.p3 = self.axes.bar(ind, Bet, width, color='c', bottom=[sum(x) for x in zip(Bluff, BP, BHP)])
        self.p4 = self.axes.bar(ind, Call, width, color='g', bottom=[sum(x) for x in zip(Bluff, BP, BHP, Bet)])
        self.p5 = self.axes.bar(ind, Check, width, color='w', bottom=[sum(x) for x in zip(Bluff, BP, BHP, Bet, Call)])
        self.p6 = self.axes.bar(ind, Fold, width, color='r',
                                bottom=[sum(x) for x in zip(Bluff, BP, BHP, Bet, Call, Check)])

        self.axes.set_ylabel('Profitability')
        self.axes.set_title('FinalFundsChange ABS')
        self.axes.set_xlabel(['PF Win', 'Loss', '', 'F Win', 'Loss', '', 'T Win', 'Loss', '', 'R Win', 'Loss'])
        self.axes.legend((self.p0[0], self.p1[0], self.p2[0], self.p3[0], self.p4[0], self.p5[0], self.p6[0]),
                         ('Bluff/Decept.', 'BetPot', 'BetHfPot', 'Bet/Bet+', 'Call', 'Check', 'Fold'),
                         labelspacing=0.03,
                         prop={'size': 12})
        maxh = float(self.p.selected_strategy['bigBlind']) * 20
        i = 0
        for rect0, rect1, rect2, rect3, rect4, rect5, rect6 in zip(self.p0.patches, self.p1.patches,
                                                                   self.p2.patches,
                                                                   self.p3.patches, self.p4.patches,
                                                                   self.p5.patches, self.p6.patches):
            g = list(zip(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            height = g[i]
            i += 1
            rect0.set_height(height[0])
            rect1.set_y(height[0])
            rect1.set_height(height[1])
            rect2.set_y(height[0] + height[1])
            rect2.set_height(height[2])
            rect3.set_y(height[0] + height[1] + height[2])
            rect3.set_height(height[3])
            rect4.set_y(height[0] + height[1] + height[2] + height[3])
            rect4.set_height(height[4])
            rect5.set_y(height[0] + height[1] + height[2] + height[3] + height[4])
            rect5.set_height(height[5])
            rect6.set_y(height[0] + height[1] + height[2] + height[3] + height[4] + height[5])
            rect6.set_height(height[6])
            maxh = max(height[0] + height[1] + height[2] + height[3] + height[4] + height[5] + height[6], maxh)

        self.axes.set_ylim((0, maxh))

        self.draw()


class BarPlotter2(FigureCanvas):
    def __init__(self, ui_analyser, l):
        self.ui_analyser = proxy(ui_analyser)
        self.fig = Figure(dpi=70)
        super(BarPlotter2, self).__init__(self.fig)
        self.drawfigure(l, self.ui_analyser.combobox_strategy.currentText())
        self.ui_analyser.vLayout_bar.insertWidget(1, self)

    def drawfigure(self, l, strategy):
        self.fig.clf()
        self.axes = self.fig.add_subplot(111)  # create an axis

        p_name = str(strategy)
        data = l.get_stacked_bar_data('Template', p_name, 'stackedBar')

        N = 11
        Bluff = data[0]
        BP = data[1]
        BHP = data[2]
        Bet = data[3]
        Call = data[4]
        Check = data[5]
        Fold = data[6]
        ind = np.arange(N)  # the x locations for the groups
        width = 1  # the width of the bars: can also be len(x) sequence

        self.p0 = self.axes.bar(ind, Bluff, width, color='y')
        self.p1 = self.axes.bar(ind, BP, width, color='k', bottom=Bluff)
        self.p2 = self.axes.bar(ind, BHP, width, color='b', bottom=[sum(x) for x in zip(Bluff, BP)])
        self.p3 = self.axes.bar(ind, Bet, width, color='c', bottom=[sum(x) for x in zip(Bluff, BP, BHP)])
        self.p4 = self.axes.bar(ind, Call, width, color='g', bottom=[sum(x) for x in zip(Bluff, BP, BHP, Bet)])
        self.p5 = self.axes.bar(ind, Check, width, color='w', bottom=[sum(x) for x in zip(Bluff, BP, BHP, Bet, Call)])
        self.p6 = self.axes.bar(ind, Fold, width, color='r',
                                bottom=[sum(x) for x in zip(Bluff, BP, BHP, Bet, Call, Check)])

        self.axes.set_ylabel('Profitability')
        self.axes.set_title('FinalFundsChange ABS')
        self.axes.set_xlabel(['PF Win', 'Loss', '', 'F Win', 'Loss', '', 'T Win', 'Loss', '', 'R Win', 'Loss'])
        # plt.yticks(np.arange(0,10,0.5))
        # self.c.tight_layout()
        self.axes.legend((self.p0[0], self.p1[0], self.p2[0], self.p3[0], self.p4[0], self.p5[0], self.p6[0]),
                         ('Bluff', 'BetPot', 'BetHfPot', 'Bet/Bet+', 'Call', 'Check', 'Fold'), labelspacing=0.03,
                         prop={'size': 12})
        i = 0
        maxh = 0.02
        for rect0, rect1, rect2, rect3, rect4, rect5, rect6 in zip(self.p0.patches, self.p1.patches,
                                                                   self.p2.patches,
                                                                   self.p3.patches, self.p4.patches,
                                                                   self.p5.patches, self.p6.patches):
            g = list(zip(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
            height = g[i]
            i += 1
            rect0.set_height(height[0])
            rect1.set_y(height[0])
            rect1.set_height(height[1])
            rect2.set_y(height[0] + height[1])
            rect2.set_height(height[2])
            rect3.set_y(height[0] + height[1] + height[2])
            rect3.set_height(height[3])
            rect4.set_y(height[0] + height[1] + height[2] + height[3])
            rect4.set_height(height[4])
            rect5.set_y(height[0] + height[1] + height[2] + height[3] + height[4])
            rect5.set_height(height[5])
            rect6.set_y(height[0] + height[1] + height[2] + height[3] + height[4] + height[5])
            rect6.set_height(height[6])
            maxh = max(height[0] + height[1] + height[2] + height[3] + height[4] + height[5] + height[6], maxh)

        # self.axes.set_ylim((0, maxh))

        self.draw()


class HistogramEquityWinLoss(FigureCanvas):
    def __init__(self, ui):
        self.ui = proxy(ui)
        self.fig = Figure(dpi=50)
        super(HistogramEquityWinLoss, self).__init__(self.fig)
        # self.drawfigure(template,game_stage,decision)
        self.ui.horizontalLayout_3.insertWidget(1, self)

    def drawfigure(self, p_name, game_stage, decision, l):
        data = l.get_histrogram_data('Template', p_name, game_stage, decision)
        wins = data[0]
        losses = data[1]
        bins = np.linspace(0, 1, 50)

        self.fig.clf()
        self.axes = self.fig.add_subplot(111)  # create an axis

        self.axes.set_title('Histogram')
        self.axes.set_xlabel('Equity')
        self.axes.set_ylabel('Number of hands')

        self.axes.hist(wins, bins, alpha=0.5, label='wins', color='g')
        self.axes.hist(losses, bins, alpha=0.5, label='losses', color='r')
        self.axes.legend(loc='upper right')
        self.draw()


class PiePlotter(FigureCanvas):
    def __init__(self, ui, winnerCardTypeList):
        self.ui = proxy(ui)
        self.fig = Figure(dpi=50)
        super(PiePlotter, self).__init__(self.fig)
        # self.drawfigure(winnerCardTypeList)
        self.ui.vLayout4.insertWidget(1, self)

    def drawfigure(self, winnerCardTypeList):
        self.fig.clf()
        self.axes = self.fig.add_subplot(111)  # create an axis
        self.axes.clear()
        self.axes.pie([float(v) for v in winnerCardTypeList.values()],
                      labels=[k for k in winnerCardTypeList.keys()], autopct=None)
        self.axes.set_title('Winning probabilities')
        self.draw()


class CurvePlot(FigureCanvas):
    def __init__(self, ui, p, layout='vLayout3'):
        self.p=p
        self.ui = proxy(ui)
        self.fig = Figure(dpi=50)
        super(CurvePlot, self).__init__(self.fig)
        self.drawfigure()
        layout = getattr(self.ui, layout)
        func = getattr(layout, 'insertWidget')
        func(1, self)

    def drawfigure(self):
        self.axes = self.fig.add_subplot(111)  # create an axis


        self.axes.axis((0, 1, 0, 1))
        self.axes.set_title('Some plot')
        self.axes.set_xlabel('X')
        self.axes.set_ylabel('Y')
        self.draw()

    def update_plots(self, X, Y):

        self.dots1h, = self.axes.plot(X, Y, 'wo')
        self.dots2h, = self.axes.plot(X, Y, 'wo')

        self.draw()

    def update_lines(self, power1, power2, minEquityCall, minEquityBet, smallBlind, bigBlind, maxValue, maxvalue_bet, maxEquityCall,
                     max_X,
                     maxEquityBet):
        x2 = np.linspace(0, 1, 100)

        minimum_curve_value = 0 
        minimum_curve_value2 = 0
        x = np.arange(0, 1, 0.01)
        y = np.arange(0,1,0.01)
        try:
            self.line1.remove()
            self.line2.remove()
        except:
            pass

        self.line1, = self.axes.plot(x, y, 'b-')  # Returns a tuple of line objects, thus the comma
        self.line2, = self.axes.plot(x, y, 'r-')  # Returns a tuple of line objects, thus the comma
        self.axes.legend((self.line1, self.line2), ('Maximum call limit', 'Maximum bet limit'), loc=2)

        self.axes.set_ylim(0, max(1, maxValue, maxvalue_bet))

        stage = 'Flop'
        xmin = 0.2  # float(self.p.selected_strategy[stage+'BluffMinEquity'])
        xmax = 0.3  # float(self.p.selected_strategy[stage+'BluffMaxEquity'])
        # self.axes.axvline(x=xmin, ymin=0, ymax=1, linewidth=1, color='g')
        # self.axes.axvline(x=xmax, ymin=0, ymax=1, linewidth=1, color='g')

        self.draw()


class FundsChangePlot(FigureCanvas):
    def __init__(self, ui_analyser):
        self.ui_analyser = proxy(ui_analyser)
        self.fig = Figure(dpi=50)
        super(FundsChangePlot, self).__init__(self.fig)
        self.drawfigure()
        self.ui_analyser.vLayout_fundschange.insertWidget(1, self)

    def drawfigure(self, data):
        LogFilename = 'log'
        p_name = str(self.ui_analyser.combobox_strategy.currentText())
        self.fig.clf()
        self.axes = self.fig.add_subplot(111)  # create an axis
        self.axes.clear()   # discards the old graph
        self.axes.set_title('My Funds')
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('$')
        self.axes.plot(data, '-')  # plot data
        self.draw()


class ScatterPlot(FigureCanvas):
    def __init__(self, ui):
        self.ui = proxy(ui)
        self.fig = Figure()
        super(ScatterPlot, self).__init__(self.fig)
        self.ui.horizontalLayout_4.insertWidget(1, self)

    def drawfigure(self, p_name, game_stage, decision, l, smallBlind, bigBlind, maxValue, minEquityBet, max_X,
                   maxEquityBet,
                   power):
        wins, losses = l.get_scatterplot_data('Template', p_name, game_stage, decision)
        self.fig.clf()
        self.axes = self.fig.add_subplot(111)  # create an axis
        self.axes.set_title('Wins and Losses')
        self.axes.set_xlabel('Equity')
        self.axes.set_ylabel('Minimum required call')

        try:
            self.axes.set_ylim(0, max(wins['minCall'].tolist() + losses['minCall'].tolist()) * 1.1)
        except:
            self.axes.set_ylim(0, 1)
        self.axes.set_xlim(0, 1)

        # self.axes.set_xlim(.5, .8)
        # self.axes.set_ylim(0, .2)

        area = np.pi * (50 * wins['FinalFundsChange'])  # 0 to 15 point radiuses
        green_dots = self.axes.scatter(x=wins['equity'].tolist(), y=wins['minCall'], s=area, c='green', alpha=0.5)

        area = np.pi * (50 * abs(losses['FinalFundsChange']))
        red_dots = self.axes.scatter(x=losses['equity'].tolist(), y=losses['minCall'], s=area, c='red', alpha=0.5)

        self.axes.legend((green_dots, red_dots),
                         ('Wins', 'Losses'), loc=2)

        x2 = np.linspace(0, 1, 100)
        y2 = np.arange(0, 1, 0.01)
        self.line3, = self.axes.plot(x2, y2,
                                     'r-')  # Returns a tuple of line objects, thus the comma

        self.axes.grid()
        self.draw()

class ThreadManager(threading.Thread):
    def __init__(self, threadID, name, counter, gui_signals):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.gui_signals = gui_signals
        self.logger = logging.getLogger('main')
        self.logger.setLevel(logging.DEBUG)


    def update_most_gui_items(self, preflop_state, p, m, t, d, h, gui_signals):
        try:
            sheet_name = t.preflop_sheet_name
        except:
            sheet_name = ''
        gui_signals.signal_decision.emit(str(d.decision + " " + sheet_name))
        gui_signals.signal_status.emit(d.decision)
        range2 = ''
        if hasattr(t, 'reverse_sheet_name'):
            range = t.reverse_sheet_name
            if hasattr(preflop_state, 'range_column_name'):
                range2 = " " + preflop_state.range_column_name + ""

        else:
            range = str(m.opponent_range)
        if range == '1': range = 'All cards'

        if t.gameStage != 'PreFlop' and p.selected_strategy['preflop_override']:
            sheet_name=preflop_state.preflop_sheet_name

        gui_signals.signal_label_number_update.emit('equity', str(np.round(t.abs_equity * 100, 2)) + "%")
        gui_signals.signal_label_number_update.emit('required_minbet', str(np.round(t.minBet,2)))
        gui_signals.signal_label_number_update.emit('required_mincall', str(np.round(t.minCall,2)))
        # gui_signals.signal_lcd_number_update.emit('potsize', t.totalPotValue)
        gui_signals.signal_label_number_update.emit('gamenumber',
                                                    str(int(self.game_logger.get_game_count(p.current_strategy))))
        gui_signals.signal_label_number_update.emit('assumed_players', str(int(t.assumedPlayers)))
        gui_signals.signal_label_number_update.emit('calllimit', str(np.round(d.finalCallLimit,2)))
        gui_signals.signal_label_number_update.emit('betlimit', str(np.round(d.finalBetLimit,2)))
        gui_signals.signal_label_number_update.emit('runs', str(int(m.runs)))
        gui_signals.signal_label_number_update.emit('sheetname', sheet_name)
        gui_signals.signal_label_number_update.emit('collusion_cards', str(m.collusion_cards))
        gui_signals.signal_label_number_update.emit('mycards', str(t.mycards))
        gui_signals.signal_label_number_update.emit('tablecards', str(t.cardsOnTable))
        gui_signals.signal_label_number_update.emit('opponent_range', str(range) + str(range2))
        gui_signals.signal_label_number_update.emit('mincallequity', str(np.round(t.minEquityCall, 2) * 100) + "%")
        gui_signals.signal_label_number_update.emit('minbetequity', str(np.round(t.minEquityBet, 2) * 100) + "%")
        gui_signals.signal_label_number_update.emit('outs', str(d.outs))
        gui_signals.signal_label_number_update.emit('initiative', str(t.other_player_has_initiative))
        gui_signals.signal_label_number_update.emit('round_pot', str(np.round(t.round_pot_value,2)))
        gui_signals.signal_label_number_update.emit('pot_multiple', str(np.round(d.pot_multiple,2)))

        if t.gameStage != 'PreFlop' and p.selected_strategy['use_relative_equity']:
            gui_signals.signal_label_number_update.emit('relative_equity', str(np.round(t.relative_equity,2) * 100) + "%")
            gui_signals.signal_label_number_update.emit('range_equity', str(np.round(t.range_equity,2) * 100) + "%")
        else:
            gui_signals.signal_label_number_update.emit('relative_equity', "")
            gui_signals.signal_label_number_update.emit('range_equity', "")



        # gui_signals.signal_lcd_number_update.emit('zero_ev', round(d.maxCallEV, 2))

        gui_signals.signal_pie_chart_update.emit(t.winnerCardTypeList)
        gui_signals.signal_curve_chart_update1.emit(h.histEquity, h.histMinCall, h.histMinBet, t.equity,
                                                    t.minCall, t.minBet,
                                                    'bo',
                                                    'ro')

        gui_signals.signal_curve_chart_update2.emit(t.power1, t.power2, t.minEquityCall, t.minEquityBet,
                                                    t.smallBlind, t.bigBlind,
                                                    t.maxValue_call,t.maxValue_bet,
                                                    t.maxEquityCall, t.max_X, t.maxEquityBet)

    def run(self):

        while True:
            if self.gui_signals.pause_thread:
                while self.gui_signals.pause_thread == True:
                    time.sleep(1)
                    if self.gui_signals.exit_thread == True: sys.exit()

            ready = False
            

            if not self.gui_signals.pause_thread:
                if self.gui_signals.exit_thread: sys.exit()


# ==== MAIN PROGRAM =====

def main():

    # Back up the reference to the exceptionhook
    sys._excepthook = sys.excepthook

    def exception_hook(exctype, value, traceback):
        # Print the error and traceback
        logger = logging.getLogger('main')
        logger.setLevel(logging.DEBUG)
        print(exctype, value, traceback)
        logger.error(str(exctype))
        logger.error(str(value))
        logger.error(str(traceback))
        # Call the normal Exception hook after
        sys.__excepthook__(exctype, value, traceback)
        sys.exit(1)


    # Set the exception hook to our wrapping function
    sys.__excepthook__ = exception_hook

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    global ui
    ui= AiInterface()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon('icon.ico'))

    global gui_signals
    gui_signals = UIActionAndSignals(ui)

    t1 = ThreadManager(1, "Thread-1", 1, gui_signals)
    t1.start()

    MainWindow.show()
    try:
        sys.exit(app.exec_())
    except:
        gui_signals.exit_thread = True


    pass

if __name__ == '__main__':
    main()