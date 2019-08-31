import core.config as config
import core.utils as utils
from core.parser import Parser

class PyTTP:

    """ PyTTP class generate a pdf version of any readable 
        tutorials from https://www.tutorialspoint.com 
   
        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self):
        pass

    @classmethod
    def createPDF(cls, entrypoint):

        """

        """

        ttp = PyTTP()
        head, chapters = ttp.parse(entrypoint)
        urls = Parser.extract_href(chapters)
        print(head, urls)  

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial 
                from https://www.tutorialspoint.com 

            Returns:
                Tuple(str): head, chapters

        """

        print('parsing the entry point...')
        
        if not utils.is_valid_hostname(entrypoint):
            raise InvalidHostName('not a valid url')

        head = Parser.resolve_path( 
            Parser.parse(url=entrypoint, el='head'),
            config.HOST
        )
        chapters = Parser.resolve_path( 
            Parser.parse(url=entrypoint, el='chapters'),
            config.HOST
        )
        return head, chapters