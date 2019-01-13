import time

import oauth2 as oauth
import requests

from yahoo_weather.config.config import yahoo
from yahoo_weather.config.units import Unit


def _get_city_url(API_param, city, unit=Unit.celsius):
    return oauth.Request(method="GET", url=yahoo.url_city.format(city=city, unit=unit), parameters=_get_parameters(API_param))


def _get_location_url(API_param, lat, long, unit=Unit.celsius):
    return oauth.Request(method="GET", url=yahoo.url_location.format(lat=lat, lon=long, unit=unit), parameters=_get_parameters(API_param))


def _get_parameters(API_param):
    # Set the base oauth_* parameters along with any other parameters required
    # for the API call.
    return {
        "Yahoo-App-Id": API_param.APP_ID,
        'oauth_timestamp': str(int(time.time())),
        'oauth_signature_method': "HMAC-SHA1",
        'oauth_version': "1.0",
        'oauth_nonce': oauth.generate_nonce(),
        'oauth_consumer_key': API_param.apikey
    }

def _get_consumer(API_param):
    # Setup the Consumer with the api_keys given by the provider
    return oauth.Consumer(key=API_param.apikey, secret=API_param.apisecret)


def request_api(req,API_param):
    # Create the signature
    signature = oauth.SignatureMethod_HMAC_SHA1().sign(req, _get_consumer(API_param), None)

    # Add the Signature to the request
    req['oauth_signature'] = signature

    api_result = requests.get(req.to_url())
    return api_result