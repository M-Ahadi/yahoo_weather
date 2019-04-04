from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

weather = YahooWeather(APP_ID="Your App ID",
                     api_key="Your API KEY",
                     api_secret="Your API secret")

weather.get_yahoo_weather_by_city("tehran", Unit.celsius)
print(weather.condition.text)
print(weather.condition.temperature)

weather.get_yahoo_weather_by_location(35.67194, 51.424438)
print(weather.condition.text)
print(weather.condition.temperature)
