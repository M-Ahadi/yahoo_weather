from yahoo_weather.api_handler import request_api, _get_city_url, _get_location_url
from yahoo_weather.classes.API_param import yahoo_API_parameters
from yahoo_weather.classes.atmosphere import Atmosphere
from yahoo_weather.classes.astronomy import Astronomy
from yahoo_weather.classes.condition import Condition
from yahoo_weather.classes.current_observation import Current_Observation
from yahoo_weather.classes.current_weather import Current_Weather
from yahoo_weather.classes.forecasts import Forecasts
from yahoo_weather.classes.location import Location
from yahoo_weather.classes.wind import Wind
from yahoo_weather.config.units import Unit


class Yahoo_Weather:
    def __init__(self, APP_ID, apikey, apisecret):
        self.APP_ID = APP_ID
        self.apikey = apikey
        self.apisecret = apisecret
        self.api_param = yahoo_API_parameters(APP_ID, apikey, apisecret)

    def get_yahoo_weather_by_city(self, city, unit=Unit.celsius):
        req = _get_city_url(self.api_param, city, unit)
        # Create our request. Change method, etc. accordingly.
        self._get_yahoo_data(req)

    def get_yahoo_weather_by_location(self, lat, long, unit=Unit.celsius):
        req = _get_location_url(self.api_param, lat, long, unit)
        # Create our request. Change method, etc. accordingly.
        return self._get_yahoo_data(req)

    def _get_yahoo_data(self, req):
        try:
            api_result = request_api(req, self.api_param)
            if api_result.status_code == 200:
                result = api_result.json()
                loc = result.get("location")
                current_observation = result.get("current_observation")
                astronomy = current_observation.get("astronomy")
                atmosphere = current_observation.get("atmosphere")
                condition = current_observation.get("condition")
                wind = current_observation.get("wind")
                forecasts = result.get("forecasts")

                self.location = Location.load_from_json(loc)
                pubDate = current_observation.get("pubDate")
                self.astronomy = Astronomy.load_from_json(astronomy)
                self.atmosphere = Atmosphere.load_from_json(atmosphere)
                self.condition = Condition.load_from_json(condition)
                self.wind = Wind.load_from_json(wind)
                self.forecasts = []

                for forcast in forecasts:
                    self.forecasts.append(Forecasts.load_from_json(forcast))

                self.current_observation = Current_Observation(astronomy=self.astronomy,
                                                               atmosphere=self.atmosphere,
                                                               condition=self.condition,
                                                               pubDate=pubDate,
                                                               wind=self.wind)

                return Current_Weather(current_observation=self.current_observation,
                                       forecasts=self.forecasts,
                                       location=self.location)
        except Exception as e:
            print(e)
        return None

    def get_location(self):
        return self.location

    def get_forcasts(self):
        return self.forecasts

    def get_wind(self):
        return self.wind

    def get_condition(self):
        return self.condition

    def get_atmosphere(self):
        return self.atmosphere

    def get_astronomy(self):
        return self.astronomy

    def get_current_observation(self):
        return self.current_observation

