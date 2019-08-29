import requests
import core.config as config
from contextlib import closing

session = requests.Session()

def get(url, headers = None):

    if headers:
        session.headers.update(headers)     

    try:
        with closing(session.get(url)) as response:
            response.raise_for_status()
            return response
    except requests.exceptions.ConnectionError as errc:
        raise Exception("Please check your internet connection and try again")
    except requests.exceptions.RequestException as e:
        raise Exception("An unexpected error has occured, please try again")