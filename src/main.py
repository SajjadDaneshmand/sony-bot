import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap

from child_windows import *
from settings import SONY_ICON_PATH
from interface import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set icon
        pixmap = QPixmap(SONY_ICON_PATH)
        resized_pixmap = pixmap.scaled(111, 87)
        self.ui.sonyLogo.setPixmap(resized_pixmap)
        self.ui.sonyLogo.setScaledContents(True)

        self.add_proxy_window = AddProxyWindow()
        self.add_accounts_window = AddAccountsWindow()
        self.thread_count = ThreadCount()

        self.show()
        self.ui.addProxy.clicked.connect(lambda: self.add_proxy_window.exec_())
        self.ui.addAccounts.clicked.connect(lambda: self.add_accounts_window.exec_())
        self.ui.threads.clicked.connect(lambda: self.thread_count.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
