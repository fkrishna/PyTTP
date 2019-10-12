from core.client import requests

class ConnectionError(requests.exceptions.ConnectionError):
    def __init__(self, *args, **kwargs):
        requests.exceptions.ConnectionError.__init__(self, *args, **kwargs)

class InvalidHostName(requests.exceptions.InvalidURL):
    def __init__(self, *args, **kwargs):
        requests.exceptions.InvalidURL.__init__(self, *args, **kwargs)

class ParserError(RuntimeError):
    def __init__(self, *args, **kwargs):
        RuntimeError.__init__(self, *args, **kwargs)

class fileBusy(RuntimeError):
    def __init__(self, *args, **kwargs):
        RuntimeError.__init__(self, *args, **kwargs)

