import datetime
import json as json_handler

from yahoo_weather.classes.errors import Error


class Forecasts:
    def __init__(self, code, date, day, high, low, text):
        self.code = code
        self.date = datetime.datetime.fromtimestamp(date)
        self.day = day
        self.high = high
        self.low = low
        self.text = text

    def as_dict(self):
        return self.__dict__

    @classmethod
    def load_from_json(cls, json):
        if isinstance(json, dict):
            json_dict = json
        elif isinstance(json, str):
            json_dict = json_handler.loads(json)
        else:
            raise ValueError(Error.unacceptable_json)

        code = json_dict.get("code")
        date = json_dict.get("date")
        day = json_dict.get("day")
        high = json_dict.get("high")
        low = json_dict.get("low")
        text = json_dict.get("text")

        return cls(code=code, date=date, day=day, high=high, low=low, text=text)
