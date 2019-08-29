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
