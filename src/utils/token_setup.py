import configparser
import os


class BotTokenSetup:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("Settings.ini")

    @property
    def api_token(self):
        return (
            os.environ.get("TOKEN", False)
            if os.environ.get("TOKEN", False)
            else self.config["TG"]["token"]
        )

    @property
    def mongo_token(self):
        return (
            os.environ.get("DB", False)
            if os.environ.get("DB", False)
            else self.config["Mongo"]["db"]
        )


def get_api_token():
    return BotTokenSetup().api_token


def get_mongo_token():
    return BotTokenSetup().mongo_token
