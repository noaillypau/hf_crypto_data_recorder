# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from python_classes.config_generator.exchange import Exchange
from python_classes.config_generator.functions import get_list_exchange
import importlib, json, numpy as np, pandas as pd, os
import subprocess as sp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 961, 401))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_saveConfig = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_saveConfig.setGeometry(QtCore.QRect(840, 360, 75, 23))
        self.pushButton_saveConfig.setObjectName("pushButton_saveConfig")
        self.groupBox_Preview = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_Preview.setGeometry(QtCore.QRect(320, 230, 611, 121))
        self.groupBox_Preview.setObjectName("groupBox_Preview")
        self.label_5 = QtWidgets.QLabel(self.groupBox_Preview)
        self.label_5.setGeometry(QtCore.QRect(30, 23, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_Preview)
        self.label_6.setGeometry(QtCore.QRect(30, 60, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_Preview)
        self.label_7.setGeometry(QtCore.QRect(30, 93, 91, 16))
        self.label_7.setObjectName("label_7")
        self.textBrowser_previewLOB = QtWidgets.QTextBrowser(self.groupBox_Preview)
        self.textBrowser_previewLOB.setGeometry(QtCore.QRect(130, 20, 61, 21))
        self.textBrowser_previewLOB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_previewLOB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_previewLOB.setObjectName("textBrowser_previewLOB")
        self.textBrowser_previewTradelimit = QtWidgets.QTextBrowser(self.groupBox_Preview)
        self.textBrowser_previewTradelimit.setGeometry(QtCore.QRect(130, 57, 61, 21))
        self.textBrowser_previewTradelimit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_previewTradelimit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_previewTradelimit.setObjectName("textBrowser_previewTradelimit")
        self.comboBox_previewSymbol = QtWidgets.QComboBox(self.groupBox_Preview)
        self.comboBox_previewSymbol.setGeometry(QtCore.QRect(130, 90, 111, 22))
        self.comboBox_previewSymbol.setObjectName("comboBox_previewSymbol")
        self.groupBox_Preview_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_Preview_2.setGeometry(QtCore.QRect(320, 20, 291, 201))
        self.groupBox_Preview_2.setObjectName("groupBox_Preview_2")
        self.label_11 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_11.setGeometry(QtCore.QRect(30, 30, 31, 16))
        self.label_11.setObjectName("label_11")
        self.textBrowser_base = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_base.setGeometry(QtCore.QRect(70, 30, 51, 21))
        self.textBrowser_base.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_base.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_base.setObjectName("textBrowser_base")
        self.label_12 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_12.setGeometry(QtCore.QRect(30, 70, 31, 16))
        self.label_12.setObjectName("label_12")
        self.textBrowser_quote = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_quote.setGeometry(QtCore.QRect(70, 70, 51, 21))
        self.textBrowser_quote.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_quote.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_quote.setObjectName("textBrowser_quote")
        self.textBrowser_maker = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_maker.setGeometry(QtCore.QRect(70, 110, 51, 21))
        self.textBrowser_maker.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_maker.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_maker.setObjectName("textBrowser_maker")
        self.label_13 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_13.setGeometry(QtCore.QRect(30, 110, 31, 16))
        self.label_13.setObjectName("label_13")
        self.textBrowser_taker = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_taker.setGeometry(QtCore.QRect(70, 150, 51, 21))
        self.textBrowser_taker.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_taker.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_taker.setObjectName("textBrowser_taker")
        self.label_14 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_14.setGeometry(QtCore.QRect(30, 150, 31, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_15.setGeometry(QtCore.QRect(160, 150, 61, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_16.setGeometry(QtCore.QRect(160, 30, 31, 16))
        self.label_16.setObjectName("label_16")
        self.textBrowser_costmin = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_costmin.setGeometry(QtCore.QRect(210, 110, 51, 21))
        self.textBrowser_costmin.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_costmin.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_costmin.setObjectName("textBrowser_costmin")
        self.textBrowser_pricestep = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_pricestep.setGeometry(QtCore.QRect(210, 150, 51, 21))
        self.textBrowser_pricestep.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_pricestep.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_pricestep.setObjectName("textBrowser_pricestep")
        self.textBrowser_active = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_active.setGeometry(QtCore.QRect(210, 70, 51, 21))
        self.textBrowser_active.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_active.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_active.setObjectName("textBrowser_active")
        self.label_17 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_17.setGeometry(QtCore.QRect(160, 70, 31, 16))
        self.label_17.setObjectName("label_17")
        self.textBrowser_type = QtWidgets.QTextBrowser(self.groupBox_Preview_2)
        self.textBrowser_type.setGeometry(QtCore.QRect(210, 30, 51, 21))
        self.textBrowser_type.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_type.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_type.setObjectName("textBrowser_type")
        self.label_18 = QtWidgets.QLabel(self.groupBox_Preview_2)
        self.label_18.setGeometry(QtCore.QRect(160, 110, 51, 16))
        self.label_18.setObjectName("label_18")
        self.groupBox_editSettings = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_editSettings.setGeometry(QtCore.QRect(20, 230, 291, 121))
        self.groupBox_editSettings.setObjectName("groupBox_editSettings")
        self.label = QtWidgets.QLabel(self.groupBox_editSettings)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_editSettings)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_2.setObjectName("label_2")
        self.spinBox_lob = QtWidgets.QSpinBox(self.groupBox_editSettings)
        self.spinBox_lob.setGeometry(QtCore.QRect(110, 27, 42, 22))
        self.spinBox_lob.setObjectName("spinBox_lob")
        self.spinBox_trades = QtWidgets.QSpinBox(self.groupBox_editSettings)
        self.spinBox_trades.setGeometry(QtCore.QRect(110, 67, 42, 22))
        self.spinBox_trades.setObjectName("spinBox_trades")
        self.groupBox_symbolSelection = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_symbolSelection.setGeometry(QtCore.QRect(20, 20, 291, 201))
        self.groupBox_symbolSelection.setObjectName("groupBox_symbolSelection")
        self.label_3 = QtWidgets.QLabel(self.groupBox_symbolSelection)
        self.label_3.setGeometry(QtCore.QRect(30, 43, 91, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_symbolSelection)
        self.label_4.setGeometry(QtCore.QRect(30, 83, 111, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox_exchange = QtWidgets.QComboBox(self.groupBox_symbolSelection)
        self.comboBox_exchange.setGeometry(QtCore.QRect(130, 40, 121, 22))
        self.comboBox_exchange.setObjectName("comboBox_exchange")
        self.comboBox_symbol = QtWidgets.QComboBox(self.groupBox_symbolSelection)
        self.comboBox_symbol.setGeometry(QtCore.QRect(130, 80, 121, 22))
        self.comboBox_symbol.setObjectName("comboBox_symbol")
        self.pushButton_addSymbol = QtWidgets.QPushButton(self.groupBox_symbolSelection)
        self.pushButton_addSymbol.setGeometry(QtCore.QRect(20, 150, 91, 31))
        self.pushButton_addSymbol.setObjectName("pushButton_addSymbol")
        self.groupBox_appSettings = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_appSettings.setGeometry(QtCore.QRect(630, 20, 311, 201))
        self.groupBox_appSettings.setObjectName("groupBox_appSettings")
        self.label_8 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_9.setGeometry(QtCore.QRect(20, 53, 111, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_symbolFilterSorter = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterSorter.setGeometry(QtCore.QRect(140, 20, 111, 22))
        self.comboBox_symbolFilterSorter.setObjectName("comboBox_symbolFilterSorter")
        self.comboBox_symbolFilterSorter.addItem("")
        self.comboBox_symbolFilterSorter.addItem("")
        self.comboBox_symbolFilterSorter.addItem("")
        self.comboBox_symbolFilterSorter.addItem("")
        self.comboBox_symbolFilterSorter.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_10.setGeometry(QtCore.QRect(20, 83, 121, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox_symbolFilterBase = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterBase.setGeometry(QtCore.QRect(140, 50, 111, 22))
        self.comboBox_symbolFilterBase.setObjectName("comboBox_symbolFilterBase")
        self.comboBox_symbolFilterBase.addItem("")
        self.comboBox_symbolFilterQuote = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterQuote.setGeometry(QtCore.QRect(140, 80, 111, 22))
        self.comboBox_symbolFilterQuote.setObjectName("comboBox_symbolFilterQuote")
        self.comboBox_symbolFilterQuote.addItem("")
        self.comboBox_symbolFilterType = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterType.setGeometry(QtCore.QRect(140, 110, 111, 22))
        self.comboBox_symbolFilterType.setObjectName("comboBox_symbolFilterType")
        self.comboBox_symbolFilterType.addItem("")
        self.label_19 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_19.setGeometry(QtCore.QRect(20, 113, 121, 16))
        self.label_19.setObjectName("label_19")
        self.comboBox_symbolFilterMaker = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterMaker.setGeometry(QtCore.QRect(140, 140, 111, 22))
        self.comboBox_symbolFilterMaker.setObjectName("comboBox_symbolFilterMaker")
        self.comboBox_symbolFilterMaker.addItem("")
        self.label_20 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_20.setGeometry(QtCore.QRect(20, 143, 121, 16))
        self.label_20.setObjectName("label_20")
        self.comboBox_symbolFilterTaker = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterTaker.setGeometry(QtCore.QRect(140, 170, 111, 22))
        self.comboBox_symbolFilterTaker.setObjectName("comboBox_symbolFilterTaker")
        self.comboBox_symbolFilterTaker.addItem("")
        self.label_21 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_21.setGeometry(QtCore.QRect(20, 173, 121, 16))
        self.label_21.setObjectName("label_21")
        self.pushButton_resetExchangeConfig = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_resetExchangeConfig.setGeometry(QtCore.QRect(90, 360, 141, 21))
        self.pushButton_resetExchangeConfig.setObjectName("pushButton_resetExchangeConfig")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 430, 961, 291))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 271, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_22.setObjectName("label_22")
        self.comboBox_recorderSelectExchange = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_recorderSelectExchange.setGeometry(QtCore.QRect(110, 27, 121, 22))
        self.comboBox_recorderSelectExchange.setObjectName("comboBox_recorderSelectExchange")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 110, 271, 161))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_25 = QtWidgets.QLabel(self.groupBox_4)
        self.label_25.setGeometry(QtCore.QRect(20, 100, 91, 16))
        self.label_25.setObjectName("label_25")
        self.textBrowser_recorderPreviewTradelimit = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_recorderPreviewTradelimit.setGeometry(QtCore.QRect(120, 64, 61, 21))
        self.textBrowser_recorderPreviewTradelimit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_recorderPreviewTradelimit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_recorderPreviewTradelimit.setObjectName("textBrowser_recorderPreviewTradelimit")
        self.label_23 = QtWidgets.QLabel(self.groupBox_4)
        self.label_23.setGeometry(QtCore.QRect(20, 30, 71, 16))
        self.label_23.setObjectName("label_23")
        self.textBrowser_recorderPreviewLOB = QtWidgets.QTextBrowser(self.groupBox_4)
        self.textBrowser_recorderPreviewLOB.setGeometry(QtCore.QRect(120, 27, 61, 21))
        self.textBrowser_recorderPreviewLOB.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_recorderPreviewLOB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_recorderPreviewLOB.setObjectName("textBrowser_recorderPreviewLOB")
        self.label_24 = QtWidgets.QLabel(self.groupBox_4)
        self.label_24.setGeometry(QtCore.QRect(20, 67, 71, 16))
        self.label_24.setObjectName("label_24")
        self.comboBox_recorderPreviewSymbol = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_recorderPreviewSymbol.setGeometry(QtCore.QRect(120, 100, 111, 22))
        self.comboBox_recorderPreviewSymbol.setObjectName("comboBox_recorderPreviewSymbol")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(310, 30, 351, 241))
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_recorderLaunch = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_recorderLaunch.setGeometry(QtCore.QRect(20, 30, 131, 23))
        self.pushButton_recorderLaunch.setObjectName("pushButton")
        self.label_27 = QtWidgets.QLabel(self.groupBox_5)
        self.label_27.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.label_27.setObjectName("label_27")
        self.comboBox_recorderExchangesRunning = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_recorderExchangesRunning.setGeometry(QtCore.QRect(180, 80, 121, 22))
        self.comboBox_recorderExchangesRunning.setObjectName("comboBox_recorderExchangesRunning")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(180, 240, 351, 121))
        self.groupBox_7.setObjectName("groupBox_7")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 30, 131, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_28 = QtWidgets.QLabel(self.groupBox_7)
        self.label_28.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.label_28.setObjectName("label_28")
        self.comboBox_exchange_4 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_exchange_4.setGeometry(QtCore.QRect(180, 80, 121, 22))
        self.comboBox_exchange_4.setObjectName("comboBox_exchange_4")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(690, 160, 251, 111))
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_uploaderStartDaily = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_uploaderStartDaily.setGeometry(QtCore.QRect(20, 30, 151, 23))
        self.pushButton_uploaderStartDaily.setObjectName("pushButton_uploaderStartDaily")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox.setGeometry(QtCore.QRect(60, 80, 81, 21))
        self.checkBox.setObjectName("checkBox")
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_8.setGeometry(QtCore.QRect(690, 30, 251, 111))
        self.groupBox_8.setObjectName("groupBox_8")
        self.pushButton_recorderStopExchange = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_recorderStopExchange.setGeometry(QtCore.QRect(20, 70, 211, 23))
        self.pushButton_recorderStopExchange.setObjectName("pushButton_recorderStopExchange")
        self.label_29 = QtWidgets.QLabel(self.groupBox_8)
        self.label_29.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_29.setObjectName("label_29")
        self.comboBox_recorderEchangeToStop = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_recorderEchangeToStop.setGeometry(QtCore.QRect(110, 30, 91, 22))
        self.comboBox_recorderEchangeToStop.setObjectName("comboBox_recorderEchangeToStop")
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_8)
        self.groupBox_9.setGeometry(QtCore.QRect(180, 240, 351, 121))
        self.groupBox_9.setObjectName("groupBox_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_9)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 30, 131, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_30 = QtWidgets.QLabel(self.groupBox_9)
        self.label_30.setGeometry(QtCore.QRect(20, 80, 171, 16))
        self.label_30.setObjectName("label_30")
        self.comboBox_exchange_6 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_exchange_6.setGeometry(QtCore.QRect(180, 80, 121, 22))
        self.comboBox_exchange_6.setObjectName("comboBox_exchange_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        #----------------------------------------------------------------------------| Config generator |--------------------------------------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        # exchange
        self.list_ex = get_list_exchange()
        self.ex = Exchange(self.list_ex[0],json.load(open('config.json','r')))

        # symbol selection
        self.pushButton_addSymbol.clicked.connect(self.add_symbol)
        self.comboBox_exchange.clear()
        for ex in self.list_ex:
            self.comboBox_exchange.addItem("")
            self.comboBox_exchange.setItemText(self.comboBox_exchange.count()-1, self._translate("MainWindow", ex))
            # signal
        self.comboBox_exchange.currentTextChanged.connect(self.onExchangeChanged)
        self.comboBox_symbol.currentTextChanged.connect(self.onSymbolChanged)
            # init
        #self.comboBox_exchange.setCurrentText(self.list_ex[0])


        # edit settings
        self.spinBox_trades.valueChanged.connect(self.onTradesLimitChanged)
        self.spinBox_lob.valueChanged.connect(self.onLobChanged)


        # symbol preview

        # preview


        # symbol filter
        self.comboBox_symbolFilterSorter.currentTextChanged.connect(self.onChangedSorter)
        self.comboBox_symbolFilterBase.currentTextChanged.connect(self.onChangedFilter)
        self.comboBox_symbolFilterQuote.currentTextChanged.connect(self.onChangedFilter)
        self.comboBox_symbolFilterType.currentTextChanged.connect(self.onChangedFilter)
        self.comboBox_symbolFilterMaker.currentTextChanged.connect(self.onChangedFilter)
        self.comboBox_symbolFilterTaker.currentTextChanged.connect(self.onChangedFilter)

        # save config
        self.pushButton_saveConfig.clicked.connect(self.save_config)

        self.init_all()        


        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------| Data recorder launch |-------------------------------------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        # select exchange
        self.init_recorderSelectExchange()
        self.comboBox_recorderSelectExchange.currentTextChanged.connect(self.onChangedExchangeSelectRecorder)

        # preview config

        # launch data recorder
        self.dict_recorder_runing = {}
        self.init_recorderExchangeRunning()
        self.pushButton_recorderLaunch.clicked.connect(self.lauch_recorder)

        # stop data recorder
        self.init_recorderRecorderRunning()
        self.pushButton_recorderStopExchange.clicked.connect(self.stop_recorder)

        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
        #-------------------------------------------------------------------------| Uploader Launch |------------------------------------------------------------------------------------#
        #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        self.pushButton_uploaderStartDaily.clicked.connect(self.start_daily_uploader)
        self.uploader_is_online = False

    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Data Recorder HF"))
        self.groupBox.setTitle(self._translate("MainWindow", "Create Config"))
        self.pushButton_saveConfig.setText(self._translate("MainWindow", "Save config"))
        self.groupBox_Preview.setTitle(self._translate("MainWindow", "Preview"))
        self.label_5.setText(self._translate("MainWindow", "LOB limit:"))
        self.label_6.setText(self._translate("MainWindow", "Trades limit:"))
        self.label_7.setText(self._translate("MainWindow", "List of symbols:"))
        self.groupBox_Preview_2.setTitle(self._translate("MainWindow", "Symbol Preview"))
        self.label_11.setText(self._translate("MainWindow", "base:"))
        self.label_12.setText(self._translate("MainWindow", "quote:"))
        self.label_13.setText(self._translate("MainWindow", "maker:"))
        self.label_14.setText(self._translate("MainWindow", "taker:"))
        self.label_15.setText(self._translate("MainWindow", "price step:"))
        self.label_16.setText(self._translate("MainWindow", "type:"))
        self.label_17.setText(self._translate("MainWindow", "active:"))
        self.label_18.setText(self._translate("MainWindow", "cost min:"))
        self.groupBox_editSettings.setTitle(self._translate("MainWindow", "Edit settings"))
        self.label.setText(self._translate("MainWindow", "LOB limit:"))
        self.label_2.setText(self._translate("MainWindow", "Trades limit:"))
        self.groupBox_symbolSelection.setTitle(self._translate("MainWindow", "Symbol Selection"))
        self.label_3.setText(self._translate("MainWindow", "Select Exchange:"))
        self.label_4.setText(self._translate("MainWindow", "Select Symbol:"))
        self.pushButton_addSymbol.setText(self._translate("MainWindow", "Add Symbol"))
        self.groupBox_appSettings.setTitle(self._translate("MainWindow", "Symbol filter"))
        self.label_8.setText(self._translate("MainWindow", "Symbol sorter:"))
        self.label_9.setText(self._translate("MainWindow", "Symbol base currency:"))
        self.comboBox_symbolFilterSorter.setItemText(0, self._translate("MainWindow", "alphabet quote"))
        self.comboBox_symbolFilterSorter.setItemText(1, self._translate("MainWindow", "alphabet base"))
        self.comboBox_symbolFilterSorter.setItemText(2, self._translate("MainWindow", "24h quote volume"))
        self.comboBox_symbolFilterSorter.setItemText(3, self._translate("MainWindow", "24h base volume"))
        self.comboBox_symbolFilterSorter.setItemText(4, self._translate("MainWindow", "vwap price"))
        self.label_10.setText(self._translate("MainWindow", "Symbol quote currency:"))
        self.comboBox_symbolFilterBase.setItemText(0, self._translate("MainWindow", "no filter"))
        self.comboBox_symbolFilterQuote.setItemText(0, self._translate("MainWindow", "no filter"))
        self.comboBox_symbolFilterType.setItemText(0, self._translate("MainWindow", "no filter"))
        self.label_19.setText(self._translate("MainWindow", "Symbol type:"))
        self.comboBox_symbolFilterMaker.setItemText(0, self._translate("MainWindow", "no filter"))
        self.label_20.setText(self._translate("MainWindow", "Symbol maker fee:"))
        self.comboBox_symbolFilterTaker.setItemText(0, self._translate("MainWindow", "no filter"))
        self.label_21.setText(self._translate("MainWindow", "Symbol maker fee:"))
        self.pushButton_resetExchangeConfig.setText(self._translate("MainWindow", "Reset exchange config"))
        self.groupBox_2.setTitle(self._translate("MainWindow", "Deploy Data Recorder"))
        self.groupBox_3.setTitle(self._translate("MainWindow", "Select Config"))
        self.label_22.setText(self._translate("MainWindow", "Select Exchange:"))
        self.groupBox_4.setTitle(self._translate("MainWindow", "Preview Config"))
        self.label_25.setText(self._translate("MainWindow", "List of symbols:"))
        self.label_23.setText(self._translate("MainWindow", "LOB limit:"))
        self.label_24.setText(self._translate("MainWindow", "Trades limit:"))
        self.groupBox_5.setTitle(self._translate("MainWindow", "Launch data recorder"))
        self.pushButton_recorderLaunch.setText(self._translate("MainWindow", "Launch Data Recording"))
        self.label_27.setText(self._translate("MainWindow", "list exchange recorder running:"))
        self.groupBox_7.setTitle(self._translate("MainWindow", "Launch data recorder"))
        self.pushButton_3.setText(self._translate("MainWindow", "Launch Data Recording"))
        self.label_28.setText(self._translate("MainWindow", "list exchange recorder running:"))
        self.groupBox_6.setTitle(self._translate("MainWindow", "Lauch data uploader"))
        self.pushButton_uploaderStartDaily.setText(self._translate("MainWindow", "Start daily Uploader"))
        self.checkBox.setText(self._translate("MainWindow", "is Online"))
        self.groupBox_8.setTitle(self._translate("MainWindow", "Stop data recorder"))
        self.pushButton_recorderStopExchange.setText(self._translate("MainWindow", "Stop recording for selected exchange"))
        self.label_29.setText(self._translate("MainWindow", "recorder running:"))
        self.groupBox_9.setTitle(self._translate("MainWindow", "Launch data recorder"))
        self.pushButton_5.setText(self._translate("MainWindow", "Launch Data Recording"))
        self.label_30.setText(self._translate("MainWindow", "list exchange recorder running:"))

    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------------------------------------| Generate config section |----------------------------------------------------------------------------#
    # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def init_all(self):
        # symbol selection
        self.comboBox_exchange.setCurrentText(self.list_ex[0])

        # edit settings
        self.spinBox_trades.setMaximum(500)
        self.spinBox_trades.setValue(100)
        self.spinBox_lob.setMaximum(20)
        self.spinBox_lob.setValue(20)

        # symbol preview

        # filter
        self.init_filter()

        # preview

        # symbol filter
        self.comboBox_previewSymbol.clear()

        # save config

    # symbol selection
    def add_symbol(self):
        self.ex.config.add_symbol(self.comboBox_symbol.currentText())
        self.reset_symbol_preview()
        self.preview_add_symbol(self.comboBox_symbol.currentText())

    def onExchangeChanged(self):
        if self.comboBox_exchange.currentText() in self.list_ex:
            self.ex = Exchange(self.comboBox_exchange.currentText(),json.load(open('config.json','r')))
            self.refresh_combo_symbol(self.ex.get_list_symbol())
            self.init_filter()
            print('selected ex',self.comboBox_exchange.currentText())
            self.comboBox_previewSymbol.clear()

    def onSymbolChanged(self):
        if self.comboBox_symbol.currentText() != '':
            self.refresh_symbol_preview(self.comboBox_symbol.currentText())
            print('selected symbol',self.comboBox_symbol.currentText())

    def refresh_combo_symbol(self, list_symbol):
        if len(list_symbol) > 0:
            self.comboBox_symbol.clear()
            for symbol in list_symbol:
                self.comboBox_symbol.addItem("")
                self.comboBox_symbol.setItemText(self.comboBox_symbol.count()-1, self._translate("MainWindow", symbol))
            self.comboBox_symbol.setCurrentText(list_symbol[0])
            self.current_list_symbol = list_symbol


    # edit settings
    def onTradesLimitChanged(self):
        self.ex.config.trades_limit = self.spinBox_trades.value()
        self.textBrowser_previewTradelimit.setPlainText(str(self.spinBox_trades.value()))
    
    def onLobChanged(self):
        self.ex.config.lob_limit = self.spinBox_lob.value()
        self.textBrowser_previewLOB.setPlainText(str(self.spinBox_lob.value()))


    # symbol preview
    def reset_symbol_preview(self):
        self.textBrowser_type.setPlainText("")
        self.textBrowser_active.setPlainText("")
        self.textBrowser_pricestep.setPlainText("")
        self.textBrowser_costmin.setPlainText("")
        self.textBrowser_taker.setPlainText("")
        self.textBrowser_maker.setPlainText("")
        self.textBrowser_quote.setPlainText("")
        self.textBrowser_base.setPlainText("")

    def refresh_symbol_preview(self, symbol):
        self.textBrowser_type.setPlainText(str(self.ex.symbol_get_type(symbol)))
        self.textBrowser_active.setPlainText(str(self.ex.symbol_get_active(symbol)))
        self.textBrowser_pricestep.setPlainText(str(self.ex.symbol_get_priceStep(symbol)))
        self.textBrowser_costmin.setPlainText(str(self.ex.symbol_get_costMin(symbol)))
        self.textBrowser_taker.setPlainText(str(self.ex.symbol_get_taker(symbol)))
        self.textBrowser_maker.setPlainText(str(self.ex.symbol_get_maker(symbol)))
        self.textBrowser_quote.setPlainText(str(self.ex.symbol_get_quote(symbol)))
        self.textBrowser_base.setPlainText(str(self.ex.symbol_get_base(symbol)))
        print('symbol preview has been updated for quote ',str(self.ex.symbol_get_quote(symbol)))


    # preview
    def preview_add_symbol(self, symbol):
        self.comboBox_previewSymbol.addItem("")
        self.comboBox_previewSymbol.setItemText(self.comboBox_previewSymbol.count()-1, self._translate("MainWindow", symbol))


    # symbol filter
    def init_filter(self):
        # clear
        self.comboBox_symbolFilterBase.clear()
        self.comboBox_symbolFilterQuote.clear()
        self.comboBox_symbolFilterType.clear()
        self.comboBox_symbolFilterMaker.clear()
        self.comboBox_symbolFilterTaker.clear()
        # int no filter
        self.comboBox_symbolFilterBase.addItem("")
        self.comboBox_symbolFilterBase.setItemText(0, self._translate("MainWindow", "no filter"))
        self.comboBox_symbolFilterQuote.addItem("")
        self.comboBox_symbolFilterQuote.setItemText(0, self._translate("MainWindow", "no filter"))
        self.comboBox_symbolFilterType.addItem("")
        self.comboBox_symbolFilterType.setItemText(0, self._translate("MainWindow", "no filter"))
        self.comboBox_symbolFilterMaker.addItem("")
        self.comboBox_symbolFilterMaker.setItemText(0, self._translate("MainWindow", "no filter"))
        self.comboBox_symbolFilterTaker.addItem("")
        self.comboBox_symbolFilterTaker.setItemText(0, self._translate("MainWindow", "no filter"))
        # get list_filters
        filters_Base = self.ex.get_possible_base()
        filters_Quote = self.ex.get_possible_quote()
        filters_Type = self.ex.get_possible_type()
        filters_Maker = self.ex.get_possible_maker()
        filters_Taker = self.ex.get_possible_taker()
        # add filters
        for filt in filters_Base:
            self.comboBox_symbolFilterBase.addItem("")
            self.comboBox_symbolFilterBase.setItemText(self.comboBox_symbolFilterBase.count()-1, self._translate("MainWindow", str(filt)))
        for filt in filters_Quote:
            self.comboBox_symbolFilterQuote.addItem("")
            self.comboBox_symbolFilterQuote.setItemText(self.comboBox_symbolFilterQuote.count()-1, self._translate("MainWindow", str(filt)))
        for filt in filters_Type:
            self.comboBox_symbolFilterType.addItem("")
            self.comboBox_symbolFilterType.setItemText(self.comboBox_symbolFilterType.count()-1, self._translate("MainWindow", str(filt)))
        for filt in filters_Maker:
            self.comboBox_symbolFilterMaker.addItem("")
            self.comboBox_symbolFilterMaker.setItemText(self.comboBox_symbolFilterMaker.count()-1, self._translate("MainWindow", str(filt)))
        for filt in filters_Taker:
            self.comboBox_symbolFilterTaker.addItem("")
            self.comboBox_symbolFilterTaker.setItemText(self.comboBox_symbolFilterTaker.count()-1, self._translate("MainWindow", str(filt)))
        # init
        self.comboBox_symbolFilterBase.setCurrentText("no filter")
        self.comboBox_symbolFilterQuote.setCurrentText("no filter")
        self.comboBox_symbolFilterType.setCurrentText("no filter")
        self.comboBox_symbolFilterMaker.setCurrentText("no filter")
        self.comboBox_symbolFilterTaker.setCurrentText("no filter")

    def onChangedFilter(self):
        print('updating filter')
        base = self.comboBox_symbolFilterBase.currentText()
        if base == "no filter":
            base = None
        quote = self.comboBox_symbolFilterQuote.currentText()
        if quote == "no filter":
            quote = None
        typee = self.comboBox_symbolFilterType.currentText()
        if typee == "no filter":
            typee = None
        taker = self.comboBox_symbolFilterTaker.currentText()
        if taker == "no filter":
            taker = None
        maker = self.comboBox_symbolFilterMaker.currentText()
        if maker == "no filter":
            maker = None
        filtered_symbol_list = self.ex.filter_markets(base, quote, typee, taker, maker)
        print(len(filtered_symbol_list),len(self.ex.list_markets))
        self.refresh_combo_symbol(filtered_symbol_list)

    def onChangedSorter(self):
        print('updating sorter')
        list_symbol = self.ex.order_symbol_list(self.current_list_symbol, self.comboBox_symbolFilterSorter.currentText())
        self.refresh_combo_symbol(list_symbol)

    # save config
    def save_config(self):
        self.ex.config.save()
        print('config have been saved')
        self.init_recorderSelectExchange()

    # reset config
    def reset_config(self):
        self.ex.config.reset()
        self.init_all()
        print('reset done')


    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # -----------------------------------------------------------------------------| Launch subprocess data recorder |-------------------------------------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    # select exchange
    def onChangedExchangeSelectRecorder(self):
        exchange_selected = self.comboBox_recorderSelectExchange.currentText()
        self.update_recorder_exchange_preview(exchange_selected)

    def init_recorderSelectExchange(self):
        # get list of supported exchanges (i.e exchange for which there exist a config.py in path_configs_exchange_folder)
        list_exchange = []
        for filename in os.listdir(json.load(open('config.json','r'))['path_configs_exchange_folder']):
            if '.py' in filename:
                list_exchange.append(filename.split('.py')[0])
        # refresh comboBox
        self.comboBox_recorderSelectExchange.clear()
        for ex in list_exchange:
            self.comboBox_recorderSelectExchange.addItem("")
            self.comboBox_recorderSelectExchange.setItemText(self.comboBox_recorderSelectExchange.count()-1, self._translate("MainWindow", ex))
        if len(list_exchange) > 0:
            self.comboBox_recorderSelectExchange.setCurrentText(list_exchange[0])


    # preview config
    def update_recorder_exchange_preview(self, exchange_selected):
        if exchange_selected != '':
            path_config = json.load(open('config.json','r'))['path_configs_exchange_folder']
            spec = importlib.util.spec_from_file_location(exchange_selected, path_config+'/{}.py'.format(exchange_selected))
            config_picked_exchange = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config_picked_exchange)
            self.textBrowser_recorderPreviewLOB.setPlainText(str(config_picked_exchange.LOB_LIMIT))
            self.textBrowser_recorderPreviewTradelimit.setPlainText(str(config_picked_exchange.TRADES_LIMIT))
            self.comboBox_recorderPreviewSymbol.clear()
            for symbol in config_picked_exchange.LIST_SYMBOL:
                self.comboBox_recorderPreviewSymbol.addItem("")
                self.comboBox_recorderPreviewSymbol.setItemText(self.comboBox_recorderPreviewSymbol.count()-1, self._translate("MainWindow", symbol))

    
    # launch data recorder
    def init_recorderExchangeRunning(self):
        self.comboBox_recorderExchangesRunning.clear()
        for ex in self.dict_recorder_runing.keys():
            self.comboBox_recorderExchangesRunning.addItem("")
            self.comboBox_recorderExchangesRunning.setItemText(self.comboBox_recorderExchangesRunning.count()-1, self._translate("MainWindow", ex))

    def lauch_recorder(self):
        name_exchange = self.comboBox_recorderSelectExchange.currentText()
        if name_exchange not in self.dict_recorder_runing.keys():
            self.dict_recorder_runing[name_exchange] = sp.Popen(['python','{}/recorder/main_record_exchange.py'.format(json.load(open('config.json','r'))['path_python_classes_folder']),name_exchange],creationflags=sp.CREATE_NEW_CONSOLE)
            self.init_recorderRecorderRunning()
            self.init_recorderExchangeRunning()
            status = sp.Popen.poll(self.dict_recorder_runing[name_exchange])
            print('open subprocess status is ',status)
        else:
            print('error, this exchange has already a recorder running, stop it before you can launch the new one')

    # stop data recorder
    def init_recorderRecorderRunning(self):
        self.comboBox_recorderEchangeToStop.clear()
        for ex in self.dict_recorder_runing.keys():
            self.comboBox_recorderEchangeToStop.addItem("")
            self.comboBox_recorderEchangeToStop.setItemText(self.comboBox_recorderEchangeToStop.count()-1, self._translate("MainWindow", ex))

    def stop_recorder(self):
        name_exchange = self.comboBox_recorderEchangeToStop.currentText()
        if name_exchange in self.dict_recorder_runing.keys():
            sp.Popen.terminate(self.dict_recorder_runing[name_exchange])
            status = sp.Popen.poll(self.dict_recorder_runing[name_exchange])
            del self.dict_recorder_runing[name_exchange]
            print('current dict process is ',self.dict_recorder_runing)
            self.init_recorderRecorderRunning()
            self.init_recorderExchangeRunning()
            print('closed subprocess status is ',status)
        else:
            print('error, this exchange is not currently recording')


    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------| Uploader Launch |------------------------------------------------------------------------------------#
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

    def start_daily_uploader(self):
        # launch a subprocess 
        if not self.uploader_is_online:
            self.checkBox.setCheckState(True)
            self.uploader_is_online = True
        else:
            self.checkBox.setCheckState(False)
            self.uploader_is_online = False


if __name__ == "__main__":
    try:
        os.listdir(json.load(open('config.json','r'))['path_configs_exchange_folder'])
    except:
        os.makedirs(json.load(open('config.json','r'))['path_configs_exchange_folder'])
    try:
        os.listdir(json.load(open('config.json','r'))['path_python_classes_folder'])
    except:
        os.makedirs(json.load(open('config.json','r'))['path_python_classes_folder'])
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
