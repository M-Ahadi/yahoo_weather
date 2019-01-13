import datetime
import json as json_handler

from classes.errors import Error

class Current_Observation:
    def __init__(self, astronomy, atmosphere, condition, pubDate, wind):
        self.astronomy = astronomy
        self.atmosphere = atmosphere
        self.condition = condition
        self.pubDate = datetime.datetime.fromtimestamp(pubDate)
        self.wind = wind

    def as_dict(self):
        return self.__dict__

