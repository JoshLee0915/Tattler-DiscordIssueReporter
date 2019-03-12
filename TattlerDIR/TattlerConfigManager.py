import configparser
import logging


class ConfigManager:
    CONFIG_FILE = 'Tattler.cfg'
    config = {}

    def __getitem__(self, section):
        return self.config[section]

    def __getattr__(self, item):
        if item in self.config:
            return self.config[item]
        else:
            super.__getattribute__(item)

    @staticmethod
    def generate_config():
        config = configparser.ConfigParser()

        config['Logging'] = {'Level': logging.NOTSET,
                             'LogFile': 'Tattler.log'}

        config['Discord_Required'] = {'Token': '',
                                      'ReportChannel': 'ANY'}

        config['Discord_Optional'] = {'AnnouncementChannel': '',
                                      'DumpErrorsToGeneral': False}

        config['YouTrack'] = {}

        with open(ConfigManager.CONFIG_FILE, 'w') as configfile:
            config.write(configfile)

    def load(self):
        config = configparser.ConfigParser()

        if not config.read(self.CONFIG_FILE):
            self.generate_config()
            if not config.read(self.CONFIG_FILE):
                raise FileNotFoundError

        for section, value in config.items():
            self.config[section] = value
