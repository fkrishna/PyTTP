import core.config as config
import core.utils as utils

from core.document import *
from core.parser import Parser


class PyTTP:

    """ PyTTP class generate a pdf version of any readable 
        tutorials from https://www.tutorialspoint.com 
   
        Attributes:
            attr1 (str): Description of `attr1`.
            attr2 (:obj:`int`, optional): Description of `attr2`.

    """

    def __init__(self):
        self.document = Document()

    @classmethod
    def createPDF(cls, entrypoint):

        """

        """

        ttp = PyTTP()
        ttp.parse(entrypoint)
        urls = Parser.extract_href(ttp.document.table_contents)
        print(urls)  

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial from https://www.tutorialspoint.com 

        """

        print('parsing the entry point...')
        
        if not utils.is_valid_hostname(entrypoint):
            raise InvalidHostName('not a valid url')

        self.document.head = Parser.resolve_path( 
            Parser.parse(url=entrypoint, sec=Section.HEAD),
            config.HOST
        )
        self.document.table_contents = Parser.resolve_path( 
            Parser.parse(url=entrypoint, sec=Section.TABLE_CONTENTS),
            config.HOST
        )
        