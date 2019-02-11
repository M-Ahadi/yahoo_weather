import json as json_handler

from yahoo_weather.classes.errors import Error

class Atmosphere:
    def __init__(self, humidity, pressure, rising, visibility):
        self.humidity = humidity
        self.pressure = pressure
        self.rising = rising
        self.visibility = visibility

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

        humidity = json_dict.get("humidity")
        pressure = json_dict.get("pressure")
        rising = json_dict.get("rising")
        visibility = json_dict.get("visibility")

        return cls(humidity=humidity,pressure=pressure, rising=rising, visibility=visibility)