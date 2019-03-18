import json

from YTClient.YTClient import YTClient
from YTClient.YTDataClasses import Command


class YouTrackTracker:
    SET_FIELDS_CMD = 'Set {field} {value}'
    ADD_TAG_CMD = 'Add tag {tag}'

    user_field = ''

    request_type = 'Task'
    bug_type = 'Bug'

    request_tag = 'Feature Request'

    def __init__(self, url, token):
        self.ytClient = YTClient(url=url, token=token)

    def create_issue(self, project_id, user, summary, description, issue_type):
        user_command = self.SET_FIELDS_CMD.format(field=self.user_field, value=user)

        if issue_type == 'Request':
            type_command = self.SET_FIELDS_CMD.format(field='Type', value=self.request_type)
            if self.request_tag and self.request_tag.strip() != '':
                type_command = '{} {}'.format(type_command, self.ADD_TAG_CMD.format(tag=self.request_tag))

        else:
            type_command = self.SET_FIELDS_CMD.format(field='Type', value=self.bug_type)

        cmd = '{} {}'.format(user_command, type_command)

        issue_id = self.ytClient.create_issue(project_id, summary, description, return_fields='id')
        self.ytClient.run_command(Command(issues='[{}]'.format(issue_id), query=cmd))

        return json.loads(issue_id, encoding='utf-8')
