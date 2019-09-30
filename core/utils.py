import re

def is_valid_hostname(url):

    ''' Determine if the given url is a valid hostname
        
        Args:
            url (str): url

        Returns:
            bool: True for success, False otherwise.
    '''

    regex = r'(https?):\/\/(w{3}.)?tutorialspoint\.com(\/.*)?'
   
    if re.search(regex, url) is not None:
        return True

    return False

def is_iterable(arg):
    return True if type(arg) is list or type(arg) is tuple else False

def to_str(tags):
    tags = list(tags)
    string = ''
    for tag in tags:
        string += ''.join(str(tag))
    return string

def get(config, key):

    '''
    docstring
    '''
    
    if key not in config:
        return None
    
    return config[key]

def type_of(*args):
    for arg in args:
        print(type(arg))

def write_file(data, filename):
    with open(filename, 'w') as f:
        try:
            f.write(data)
        except Exception as e:
            print('An unexpected error has occured', e)