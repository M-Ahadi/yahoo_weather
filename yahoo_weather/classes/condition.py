import json as json_handler
from yahoo_weather.classes.errors import Error


class Condition:
    def __init__(self, code, temperature, text):
        self.code = code
        self.temperature = temperature
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
        temperature = json_dict.get("temperature")
        text = json_dict.get("text")

        return cls(code=code, temperature=temperature, text=text)
