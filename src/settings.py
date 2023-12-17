import configparser
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

CONFIGS_FILE_PATH = os.path.join(BASE_DIR, 'configs.conf')
PROXIES_FILE_PATH = os.path.join(BASE_DIR, 'proxies.txt')
ACCOUNTS_FILE_PATH = os.path.join(BASE_DIR, 'accounts.txt')
SONY_ICON_PATH = os.path.join(BASE_DIR, 'src/ui/icons/playstation-symbol.svg')
WARNING_ICON_PATH = os.path.join(BASE_DIR, 'src/ui/icons/alert-warning.png')
INFO_ICON_PATH = os.path.join(BASE_DIR, 'src/ui/icons/alert-circle.svg')
ERROR_ICON_PATH = os.path.join(BASE_DIR, 'src/ui/icons/alert-octagon.svg')


class Settings(object):
    """Settings Class"""
    def __init__(self, name=None):
        self._dict = dict()
        self.config = configparser.ConfigParser()

        if name is None:
            self.file_path = CONFIGS_FILE_PATH
        else:
            suffix = '.conf'
            name = name.strip()
            name += suffix
            self.file_path = os.path.join(BASE_DIR, name)

        self.config.read(self.file_path)

        self._default = 'CONFIGS'
        self._load_file()

    def _load_file(self):
        for section in self.config.sections():
            self._dict[section] = {}
            for key, value in self.config.items(section):
                self._dict[section][key] = value
                setattr(self, key, value)

    def set_conf(self, key, value, section=None):
        if section is None:
            section = self._default
        if not self.config.has_section(section):
            self.config.add_section(section)

        self.config[section][key] = str(value)

        with open(self.file_path, 'w') as configfile:
            self.config.write(configfile)

        if self._dict.get(section):
            self._dict[section][key] = self.config[section][key]
        else:
            self._dict.update({section: {key: value}})
        return setattr(self, key, value)

    def as_dict(self):
        return self._dict
