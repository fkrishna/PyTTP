import core.utils as utils 
from core.parser import Parser

class PyTTP:

    """ PyTTP class generate a pdf version 
    of any readable tutorials from https://www.tutorialspoint.com 
   
    Attributes:
        attr1 (str): Description of `attr1`.
        attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self):
        head, chapters, content = self.parse('https://www.tutorialspoint.com/html/index.htm')

        print(chapters, content)

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial 
                from https://www.tutorialspoint.com 

            Returns:
                object: document
        """

        print('parsing the entry point...')
        
        if not utils.is_valid_hostname(entrypoint):
            raise InvalidHostName('not a valid url')

        head = Parser.parse(url=entrypoint, el='head')
        chapters = Parser.parse(url=entrypoint, el='chapters')
        content = Parser.parse(url=entrypoint, el='content')

        return head, chapters, content