import configparser
import logging


class ConfigManager:
    CONFIG_FILE = 'Tattler.cfg'
    config = {}
    projects = None

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

        config['General'] = {'Projects': []}

        config['Logging'] = {'Level': logging.NOTSET,
                             'Log_File': 'Tattler.log'}

        config['Discord'] = {'Token': '',
                             'Report_Channel': 'ANY'}

        config['Discord_Optional'] = {'Announcement_Channel': '',
                                      'Dump_Errors_To_General': False}

        with open(ConfigManager.CONFIG_FILE, 'w') as configfile:
            config.write(configfile)

    def get_projects(self):
        if not self.projects:
            self.projects = ConfigManager.translate_list(self.General['projects'])

        return self.projects

    def load(self):
        config = configparser.ConfigParser()

        if not config.read(self.CONFIG_FILE):
            self.generate_config()
            if not config.read(self.CONFIG_FILE):
                raise FileNotFoundError

        for section, value in config.items():
            self.config[section] = value

    @staticmethod
    def is_list(value):
        return isinstance(value, str) and value.startswith('[') and value.endswith(']')

    @staticmethod
    def translate_list(value):
        if ConfigManager.is_list(value):
            value = value[1:-1].split(',')
            return [x.strip() for x in value]

        return None
