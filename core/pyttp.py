import core.config as config
import core.utils as utils

from core.document import *
from core.parser import Parser


class PyTTP:

    """ PyTTP class generate a pdf version of any readable 
        tutorials from https://www.tutorialspoint.com 
   
        Attrs:
            document (obj:document): single HTML document of a tutorial
        
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
        ttp.extract(urls[:1])  

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial from https://www.tutorialspoint.com 

        """

        print(f'parsing the entry point: {entrypoint}')
        
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

    def extract(self, urls):

        """ Extracting the content section from each given url
        
            Args:
                urls (array[:str]): list of urls to extract the content section from 
        """

        print('extracting data from host...')

        for url in urls:
            content = Parser.parse(url=url, sec=Section.CONTENT)
            content = Parser.filter(content)
            status = 'OK' if content else 'FAILED'
            print(f'{url} .................. {status}')
            self.document.contents.append(content)