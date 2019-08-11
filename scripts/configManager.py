#!/usr/bin/python3
import json

class ConfigManager:
    def __init__(self):
        with open('configs/todoistConfig.json') as todoistConfigJson:
                todoistConfig = json.load(todoistConfigJson)
                self.todoistConfig = todoistConfig;
                print(todoistConfig)

    def getTodoistAPIToken(self):
        return self.todoistConfig['apiToken']
