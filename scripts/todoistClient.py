#!/usr/bin/python3

from scripts import ConfigManager
import requests
import json

todoistURL = 'https://beta.todoist.com/API/v8/'
syncURL = 'https://todoist.com/sync/v8/'

class Todoist: 
    def __init__(self):
        self.configManager = ConfigManager();
        print 'finished init todoist'


    def getAllProjects(self):
        projects = self._get('projects')
        print json.dumps(projects)
        return projects

    def getTemplate(self, projectId):
        data = {
          'token': self.configManager.getTodoistAPIToken(),
          'project_id': projectId
        }
        response = self._post('templates/export_as_file', data)
        template = response.content
        print template
        return template


    def _get(self, path):
        return requests.get(todoistURL + path, headers={"Authorization": self._getAuth()}).json()

    def _post(self, path, data):
        return requests.post(syncURL + path, data=data)

    def _getAuth(self):
        return "Bearer %s" % self.configManager.getTodoistAPIToken()

