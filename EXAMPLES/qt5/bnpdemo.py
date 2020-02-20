#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_bnpdemo import Ui_BNPDemo  # <1>

class BNPDemoMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # <2>
        self.ui = Ui_BNPDemo()  # <3>
        self.ui.setupUi(self)  # <4>

        # Connect up menu actions
        self.ui.actionQuit.triggered.connect(self.close)

        # Connect up buttons.
        self.ui.button1.clicked.connect(self._update_statusbar)

        self.ui.button2.clicked.connect(self._get_entry)

    def _update_statusbar(self):
        self.ui.statusbar.showMessage('Ouch!', 3000)

    def _get_entry(self):
        # entry = self.ui.lineEdit.text()
        date = self.ui.calendarWidget.selectedDate().month()
        self.ui.statusbar.showMessage(str(date), 5000)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = BNPDemoMain()
    main.show()
    sys.exit(app.exec_())


