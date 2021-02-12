# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from functions import Exchange, get_list_exchange


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_symbolSelection = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_symbolSelection.setGeometry(QtCore.QRect(20, 10, 291, 201))
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
        self.groupBox_Preview = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Preview.setGeometry(QtCore.QRect(330, 220, 601, 121))
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
        self.groupBox_editSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_editSettings.setGeometry(QtCore.QRect(20, 220, 291, 111))
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
        self.pushButton_resetExchangeConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_resetExchangeConfig.setGeometry(QtCore.QRect(80, 340, 161, 31))
        self.pushButton_resetExchangeConfig.setObjectName("pushButton_resetExchangeConfig")
        self.groupBox_appSettings = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_appSettings.setGeometry(QtCore.QRect(630, 10, 311, 201))
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
        self.comboBox_symbolFilterQuote = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterQuote.setGeometry(QtCore.QRect(140, 80, 111, 22))
        self.comboBox_symbolFilterQuote.setObjectName("comboBox_symbolFilterQuote")
        self.comboBox_symbolFilterType = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterType.setGeometry(QtCore.QRect(140, 110, 111, 22))
        self.comboBox_symbolFilterType.setObjectName("comboBox_symbolFilterType")
        self.label_19 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_19.setGeometry(QtCore.QRect(20, 113, 121, 16))
        self.label_19.setObjectName("label_19")
        self.comboBox_symbolFilterMaker = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterMaker.setGeometry(QtCore.QRect(140, 140, 111, 22))
        self.comboBox_symbolFilterMaker.setObjectName("comboBox_symbolFilterMaker")
        self.label_20 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_20.setGeometry(QtCore.QRect(20, 143, 121, 16))
        self.label_20.setObjectName("label_20")
        self.comboBox_symbolFilterTaker = QtWidgets.QComboBox(self.groupBox_appSettings)
        self.comboBox_symbolFilterTaker.setGeometry(QtCore.QRect(140, 170, 111, 22))
        self.comboBox_symbolFilterTaker.setObjectName("comboBox_symbolFilterTaker")
        self.label_21 = QtWidgets.QLabel(self.groupBox_appSettings)
        self.label_21.setGeometry(QtCore.QRect(20, 173, 121, 16))
        self.label_21.setObjectName("label_21")
        self.groupBox_Preview_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Preview_2.setGeometry(QtCore.QRect(320, 10, 291, 201))
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
        self.pushButton_saveConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_saveConfig.setGeometry(QtCore.QRect(840, 350, 75, 23))
        self.pushButton_saveConfig.setObjectName("pushButton_saveConfig")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # exchange
        self.list_ex = get_list_exchange()
        self.ex = Exchange(self.list_ex[0])

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



    def retranslateUi(self, MainWindow):
        self._translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(self._translate("MainWindow", "Config Generator"))
        self.groupBox_symbolSelection.setTitle(self._translate("MainWindow", "Symbol Selection"))
        self.label_3.setText(self._translate("MainWindow", "Select Exchange:"))
        self.label_4.setText(self._translate("MainWindow", "Select Symbol:"))
        self.pushButton_addSymbol.setText(self._translate("MainWindow", "Add Symbol"))
        self.groupBox_Preview.setTitle(self._translate("MainWindow", "Preview"))
        self.label_5.setText(self._translate("MainWindow", "LOB limit:"))
        self.label_6.setText(self._translate("MainWindow", "Trades limit:"))
        self.label_7.setText(self._translate("MainWindow", "List of symbols:"))
        self.groupBox_editSettings.setTitle(self._translate("MainWindow", "Edit settings"))
        self.label.setText(self._translate("MainWindow", "LOB limit:"))
        self.label_2.setText(self._translate("MainWindow", "Trades limit:"))
        self.pushButton_resetExchangeConfig.setText(self._translate("MainWindow", "Reset exchange config"))
        self.groupBox_appSettings.setTitle(self._translate("MainWindow", "Symbol filter"))
        self.label_8.setText(self._translate("MainWindow", "Symbol sorter:"))
        self.label_9.setText(self._translate("MainWindow", "Symbol base currency:"))
        self.comboBox_symbolFilterSorter.setItemText(0, self._translate("MainWindow", "alphabet quote"))
        self.comboBox_symbolFilterSorter.setItemText(1, self._translate("MainWindow", "alphabet base"))
        self.comboBox_symbolFilterSorter.setItemText(2, self._translate("MainWindow", "24h quote volume"))
        self.comboBox_symbolFilterSorter.setItemText(3, self._translate("MainWindow", "24h base volume"))
        self.comboBox_symbolFilterSorter.setItemText(4, self._translate("MainWindow", "vwap price"))
        self.label_10.setText(self._translate("MainWindow", "Symbol quote currency:"))
        self.label_19.setText(self._translate("MainWindow", "Symbol type:"))
        self.label_20.setText(self._translate("MainWindow", "Symbol maker fee:"))
        self.label_21.setText(self._translate("MainWindow", "Symbol maker fee:"))
        self.groupBox_Preview_2.setTitle(self._translate("MainWindow", "Symbol Preview"))
        self.label_11.setText(self._translate("MainWindow", "base:"))
        self.label_12.setText(self._translate("MainWindow", "quote:"))
        self.label_13.setText(self._translate("MainWindow", "maker:"))
        self.label_14.setText(self._translate("MainWindow", "taker:"))
        self.label_15.setText(self._translate("MainWindow", "price step:"))
        self.label_16.setText(self._translate("MainWindow", "type:"))
        self.label_17.setText(self._translate("MainWindow", "active:"))
        self.label_18.setText(self._translate("MainWindow", "cost min:"))
        self.pushButton_saveConfig.setText(self._translate("MainWindow", "Save config"))

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
            self.ex = Exchange(self.comboBox_exchange.currentText())
            self.refresh_combo_symbol(self.ex.get_list_symbol())
            self.init_filter()
            print('selected ex',self.comboBox_exchange.currentText())

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

    # reset config
    def reset_config(self):
        self.ex.config.reset()
        self.init_all()
        print('reset done')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
