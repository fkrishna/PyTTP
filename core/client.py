import requests as requests
import core.consts
from contextlib import closing

session = requests.Session()

def get(url, headers = None):

    if headers:
        session.headers.update(headers)     

    # try:
    #     with closing(session.get(url)) as response:
    #         return response
    # except requests.exceptions.ConnectionError as errc:
    #     raise Exception("Please check your internet connection and try again", e)
    # except requests.exceptions.RequestException as e:
    #     raise Exception("An unexpected error has occured, please try again", e)

    with closing(session.get(url)) as response:
        return response