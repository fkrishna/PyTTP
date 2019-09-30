import weasyprint
import core.config as config
from core.utils import * 
from core.renderer import *
from core.exceptions import *
from core.document import *
from core.parser import Parser

class PyTTP:

    """ PyTTP class generate a pdf or html document of any readable 
        tutorials from https://www.tutorialspoint.com 
   
        Attrs:
            document (obj:core.Document): representation of a single tutorial
        
    """

    def __init__(self):
        self.tutorial = None

    @classmethod
    def execute(cls, entrypoint, dest, ext=config.DOCEXTS[0], debug=False):

        """ Factory Method

        """

        ttp = PyTTP()
        print(f'- Parsing the entry point: {entrypoint}')
        ttp.parse(entrypoint)

        print(f'- Extracting data from host for {ttp.tutorial} tutorial')
        urls = Parser.extract_href(ttp.tutorial.table_contents)
        ttp.extract(urls)

        print(f'- Rendering object')
        document = ttp.render() 

        print(f'- Writting ({ext}) document on disk')
        ttp.write(data=document, ext=ext)

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial from HOST

        """

        if not is_valid_hostname(entrypoint):
            raise InvalidHostName('not a valid url')

        name = entrypoint.split('/')[3]

        meta = Parser.resolve_path( 
            Parser.parse(url=entrypoint, section=Section.META),
            config.HOST
        )
        table_contents = Parser.resolve_path( 
            Parser.parse(url=entrypoint, section=Section.TABLE_CONTENTS),
            config.HOST
        )
        self.tutorial = TutorialDocument(name, meta, table_contents)

    def extract(self, urls):

        """ Extracting the content section from each given url
        
            Args:
                urls (array[:str]): list of urls to extract the content section from 
        """

        for url in urls:
            content = Parser.parse(url=url, section=Section.CONTENT)
            print(f'\t. {url}....................')
            self.tutorial.contents.append(content)

    def render(self):

        """ Render HTML document of tutorial

            Returns:
                (str): Html document
        """

        document = Renderer.render(document=self.tutorial)
        document = Parser.filter(document)
        document = Parser.resolve_path(document, config.HOST)
        return to_str(document)

    def write(self, data, ext='pdf'):

        """ Writting process of the data to PDF or HTML format

            Args:
                data (str): data to be processed
                ext (str): data type

        """
        
        filename = f'{self.tutorial.name}-{config.SUFFIX_NAME}.{ext}'
        
        if ext == 'pdf':
            weasyprint.HTML(string=data).write_pdf(filename)
        elif ext == 'html':
            write_file(data=data, filename=filename)
 