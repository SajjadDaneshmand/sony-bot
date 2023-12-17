from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from tools import append_file, is_valid_ip
from alert_windows import WarningAlert
import settings


class AddProxyWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/add_proxy.ui', self)

        # Spin max
        self.portLineSpinBox.setMaximum(65535)

        self.buttonBox.accepted.connect(self.write_proxy)
        self.buttonBox.rejected.connect(self._close_window)

        # Alerts Settings
        self.settings = self._setting('Alerts')

        # Alerts
        self.ip_warning_alert = WarningAlert(self.settings.ip_text, self.settings.ip_detail)

    def write_proxy(self):
        ip_text = self.ipLineEdit.text().strip()
        port_text = self.portLineSpinBox.value()
        if not is_valid_ip(ip_text):
            return self.ip_warning_alert.exec_()

        text = f'{ip_text}:{port_text}'
        append_file(settings.PROXIES_FILE_PATH, text)
        return self._close_window()

    def _close_window(self):
        self.close()

    @staticmethod
    def _setting(*args):
        return settings.Settings(*args)


class AddAccountsWindow(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/add_accounts.ui', self)

        self.buttonBox.accepted.connect(self.write_accounts)
        self.buttonBox.rejected.connect(self._close_window)

    def write_accounts(self):
        username_text = self.usernameLineEdit.text()
        password_text = self.passwordLineEdit.text()
        text = f'{username_text}:{password_text}'
        append_file(settings.ACCOUNTS_FILE_PATH, text)
        return self._close_window()

    def _close_window(self):
        self.close()


class ThreadCount(QDialog):
    def __init__(self):
        super().__init__()
        loadUi('ui/thread_count.ui', self)

        self.buttonBox.accepted.connect(self.set_thread)
        self.buttonBox.rejected.connect(self._close_window)

    def set_thread(self):
        thread_key = 'thread_count'
        thread_value = self.threadSpinBox.value()
        set_config = self._setting()
        set_config.set_conf(thread_key, thread_value)

        return self._close_window()

    def _close_window(self):
        self.close()

    @staticmethod
    def _setting(*args):
        return settings.Settings(*args)

