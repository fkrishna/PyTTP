from core.client import requests

class InvalidHostName(requests.exceptions.InvalidURL):
    def __init__(self, *args, **kwargs):
        requests.exceptions.InvalidURL.__init__(self, *args, **kwargs)

class ParserError(RuntimeError):
    def __init__(self, *args, **kwargs):
        RuntimeError.__init__(self, *args, **kwargs)

