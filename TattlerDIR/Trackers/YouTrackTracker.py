import json

from YTClient.YTClient import YTClient
from YTClient.YTDataClasses import Command, Project


class YouTrackTracker:
    SET_FIELDS_CMD = '{field} {value}'
    ADD_TAG_CMD = 'tag {tag}'

    def __init__(self, url, token, user_field):
        self.ytClient = YTClient(url=url, token=token)
        self.user_field = user_field

        self.request_type = 'Task'
        self.bug_type = 'Bug'

        self.request_tag = 'Feature Request'

    def create_issue(self, project_id, user, summary, description, issue_type):
        user_command = self.SET_FIELDS_CMD.format(field=self.user_field, value='"{user}"')
        user_command = user_command.format(user=user)

        if not isinstance(project_id, Project):
            project = Project(id=project_id)
        else:
            project = project_id

        if issue_type == 'Request':
            type_command = self.SET_FIELDS_CMD.format(field='Type', value=self.request_type)
            if self.request_tag and self.request_tag.strip() != '':
                type_command = '{} {}'.format(type_command, self.ADD_TAG_CMD.format(tag=self.request_tag))

        else:
            type_command = self.SET_FIELDS_CMD.format(field='Type', value=self.bug_type)

        cmd = '{} {}'.format(user_command, type_command)

        issue_id = self.ytClient.create_issue(project, summary, description, return_fields=['id', 'idReadable'])
        self.ytClient.run_command(Command(issues=[issue_id], query=cmd))

        return issue_id
