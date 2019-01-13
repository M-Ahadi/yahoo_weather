import json as json_handler
from yahoo_weather.classes.errors import Error


class Astronomy:
    def __init__(self, sunrise, sunset):
        self.sunrise = sunrise
        self.sunset = sunset

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

        sunrise = json_dict.get("sunrise")
        sunset = json_dict.get("sunset")

        return cls(sunset=sunset,sunrise=sunrise)
