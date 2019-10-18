from core.client import requests

class ConnectionError(requests.exceptions.ConnectionError):
    def __init__(self, *args, **kwargs):
        requests.exceptions.ConnectionError.__init__(self, *args, **kwargs)

class HostNameError(requests.exceptions.InvalidURL):
    def __init__(self, *args, **kwargs):
        requests.exceptions.InvalidURL.__init__(self, *args, **kwargs)

class EntryPointError(RuntimeError):
    def __init__(self, *args, **kwargs):
        RuntimeError.__init__(self, *args, **kwargs)

class FileTypeError(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)
