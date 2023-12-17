from PyQt5.QtWidgets import QDialog
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

from settings import WARNING_ICON_PATH


class WarningAlert(QDialog):
    def __init__(self, text, detail):
        super().__init__()
        self.system_text = text
        self.system_detail = detail
        loadUi('ui/alerts/warning_alert.ui', self)

        # Set icon
        pixmap = QPixmap(WARNING_ICON_PATH)

        resized_pixmap = pixmap.scaled(82, 82)
        self.warningLogo.setPixmap(resized_pixmap)
        self.warningLogo.setScaledContents(True)

        self.text.setText(self.system_text)
        self.detail.setText(self.system_detail)

        # Confirm
        self.okButton.clicked.connect(self._close_window)

    def _close_window(self):
        self.close()

