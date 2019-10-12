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
        pass

    @classmethod
    def execute(cls, entrypoint, dest, ext=config.DOCEXTS[0], debug=False):

        """ Factory Method

        """

        ttp = PyTTP()
        print(f'- Parsing the entry point: {entrypoint}')
        tutorial = ttp.parse(entrypoint)

        print(f'- Extracting content from host for {tutorial}')
        urls = Parser.extract_href(tutorial.table_contents)
        ttp.extract(tutorial, urls[:2])

        print(f'- Rendering object')
        html = ttp.render(tutorial) 

        print(f'- Writting ({ext}) document on disk')
        try:
            ttp.write(filename=tutorial.name, data=html, dest=dest, ext=ext)
        except OSError as err:
            print(err)

    def __parse_tutorial_name(self, entrypoint):
        name = ''
        try:
            name = entrypoint.split('/')[3]
        except:
            pass
        return name

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

        name = self.__parse_tutorial_name(entrypoint)

        return Tutorial(name, meta, table_contents)
        
    def extract(self, tutorial, urls = [], trace=True):

        """ Extracting content section from each given url
        
            Args:
                tutorial (document.Tutorial): tutorial object
                urls (list): urls
                trace (boolean): print the current url that is being parse
        """

        if not isinstance(tutorial, Tutorial):
            return

        for url in urls:
            if trace: print(f'\t. {url}....................')
            content = Parser.parse(url=url, section=Section.CONTENT)
            tutorial.contents.append(content)

    def render(self, tutorial):

        """ Render a single HTML document of tutorial

            Args:
                tutorial (document.Tutorial): tutorial object
            Returns:
                (str): Html document
        """

        if not isinstance(tutorial, Tutorial):
            return

        doc = Renderer.render(document=tutorial)
        doc = Parser.filter(doc)
        doc = Parser.resolve_path(doc, config.HOST)
        return doc

    def write(self, data, filename, dest, ext='pdf'):

        """ Writting process of the data to PDF or HTML format on disk

            Args:
                data (str): data to be processed
                dest (str): destination source
                ext (str): file type (html or pdf)

        """
        
        if type(data) is not str: raise TypeError('data argument must be string')
        if not os.path.isdir(dest): raise IOError('directory not found')
        if ext not in config.DOCEXTS: raise ValueError(f'{ext} is not a valid file extension')

        filename = f'{filename}.{ext}'
        if ext == 'pdf':
            weasyprint.HTML(string=data).write_pdf(filename)
        elif ext == 'html':
            write_file(data=data, filename=filename)
 