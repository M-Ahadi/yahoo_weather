import json as json_handler

from yahoo_weather.classes.errors import Error


class Wind:
    def __init__(self, chill, direction, speed):
        self.chill = chill
        self.direction = direction
        self.speed = speed

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

        chill = json_dict.get("chill")
        direction = json_dict.get("direction")
        speed = json_dict.get("speed")

        return cls(chill=chill, direction=direction, speed=speed)
