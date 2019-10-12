import weasyprint
import os
import core.consts as config
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
        ttp.extract(urls[0:2])

        print(f'- Rendering object')
        document = ttp.render() 

        print(f'- Writting ({ext}) document on disk')
        ttp.write(data=document, dest=dest, ext=ext)

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial from HOST

        """

        if not is_valid_hostname(entrypoint):
            raise InvalidHostName('not a valid url')

        
        meta = Parser.resolve_path( 
            Parser.parse(url=entrypoint, section=Section.META),
            config.HOST
        )
        table_contents = Parser.resolve_path( 
            Parser.parse(url=entrypoint, section=Section.TABLE_CONTENTS),
            config.HOST
        )

        name = entrypoint.split('/')[3]
        self.tutorial = TutorialDocument(name, meta, table_contents)
        

    def extract(self, urls = [], debug=True):

        """ Extracting the content section from each given url
        
            Args:
                urls (list): urls
        """

        for url in urls:
            if debug: print(f'\t. {url}....................')
            content = Parser.parse(url=url, section=Section.CONTENT)
            self.tutorial.contents.append(content)

    def render(self):

        """ Render a single HTML document of tutorial object

            Returns:
                (str): Html document
        """

        doc = Renderer.render(document=self.tutorial)
        doc = Parser.filter(doc)
        doc = Parser.resolve_path(doc, config.HOST)
        return to_str(doc)

    def write(self, data, dest, ext='pdf'):

        """ Writting process of the data to PDF or HTML format

            Args:
                data (str): data to be processed
                ext (str): file type (html or pdf)

        """
        
        
        #refactor
        filename = f'{self.tutorial.name}-{config.SUFFIX_NAME}.{ext}'

        if not os.path.isdir(dest):
            raise IOError('directory not found')

            
        print('pk')
        
        # if ext == 'pdf':
        #     try:
        #         weasyprint.HTML(string=data).write_pdf(filename)
        #     except Exception as e:
        #         print(e)
        #         pass
        # elif ext == 'html':
        #     write_file(data=data, filename=filename)
 