# Python Library for Yahoo Weather (New API)
On 3 Jan 2019 Yahoo changed its Weather API to use OAuth1 Authentication. This new method requires authentication to use the API. This library helps you to handle the new API.
In order to use the new API you have to get an API key from [Yahoo!](https://developer.yahoo.com/weather/?guccounter=1)


```
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

data = YahooWeather(APP_ID="Your App ID",
                     api_key="Your API KEY",
                     api_secret="Your API secret")
                     
data.get_yahoo_weather_by_city("tehran", Unit.celsius)
print(data.condition.text)
print(data.condition.temperature)

data.get_yahoo_weather_by_location(35.67194, 51.424438)
print(data.condition.text)
print(data.condition.temperature)
```
