from TattlerDIR.TattlerConfigManager import ConfigManager


class TattlerTrackerManager(object):

    def __init__(self, config_manager=None):
        if not config_manager:
            config_manager = ConfigManager()
            config_manager.load()

        self.config_manager = config_manager
        self.issue_trackers = dict()
        self.trackers = dict()

    def register_issue_tracker(self, name, issue_tracker):
        if name not in self.issue_trackers:
            self.issue_trackers[name] = issue_tracker
            return True

        return False

    def register_project(self, project_name):
        if project_name not in self.config_manager:
            return False

        return self.setup_tracker(self.config_manager[project_name]['issue_tracker'],
                                  self.config_manager[project_name]['url'],
                                  self.config_manager[project_name]['token'],
                                  self.config_manager[project_name]['discord'],
                                  self.config_manager[project_name]['project_id'],
                                  self.config_manager[project_name]['user_field'])

    def setup_tracker(self, tracker, url, token, discord, project_id, user_field):
        if tracker not in self.issue_trackers or discord in self.trackers:
            return False

        self.trackers[discord] = {'project_id': project_id, 'tracker': self.issue_trackers[tracker](url=url,
                                                                                                    token=token,
                                                                                                    user_field=user_field)}
        return True

    def get_tracker(self, discord):
        if discord in self.trackers:
            return self.trackers[discord]

        return None

    def create_bug(self, discord, username, title, body):
        tracker = self.get_tracker(discord)
        if tracker is None:
            raise KeyError()

        return tracker['tracker'].create_issue(tracker['project_id'], username, title, body, 'Bug')

    def create_request(self, discord, username, title, body):
        tracker = self.get_tracker(discord)
        if tracker is None:
            raise KeyError()
        
        return tracker['tracker'].create_issue(tracker['project_id'], username, title, body, 'Request')
