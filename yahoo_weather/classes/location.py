import json as json_handler

from yahoo_weather.classes.errors import Error


class Location:
    def __init__(self, city, country, lat, long, region, timezone_id):
        self.city = city
        self.country = country
        self.lat = lat
        self.long = long
        self.region = region
        self.timezone_id = timezone_id

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

        city = json_dict.get("city")
        country = json_dict.get("country")
        lat = json_dict.get("lat")
        long = json_dict.get("long")
        region = json_dict.get("region")
        timezone_id = json_dict.get("timezone_id")

        return cls(city=city, country=country, lat=lat, long=long, region=region, timezone_id=timezone_id)
