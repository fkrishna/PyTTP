import weasyprint
import core.config as config
import core.utils as utils
from core.renderer import *
from core.exceptions import *
from core.document import *
from core.parser import Parser

class PyTTP:

    """ PyTTP class generate a pdf or html document of any readable 
        tutorials from https://www.tutorialspoint.com 
   
        Attrs:
            document (obj:core.Document): single HTML document of a tutorial chapter
        
    """

    def __init__(self):
        self.document = Document()

    @classmethod
    def execute(cls, entrypoint, dest=config.DEF_DEST_SRC, ext=config.DOC_EXTS[0]):

        """ Factory Method

        """

        ttp = PyTTP()
        ttp.parse(entrypoint)
        urls = Parser.extract_href(ttp.document.table_contents)
        ttp.extract(urls)
        doc = ttp.render()  
        ttp.write(data=doc, ext=ext)

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial from https://www.tutorialspoint.com 

        """

        print(f'- Parsing the entry point: {entrypoint}')

        if not utils.is_valid_hostname(entrypoint):
            raise InvalidHostName('not a valid url')

        self.document.title = entrypoint.split('/')[3]

        self.document.meta = Parser.resolve_path( 
            Parser.parse(url=entrypoint, sec=Section.META),
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

        print('- Extracting data from host...')

        for url in urls:
            content = Parser.parse(url=url, sec=Section.CONTENT)
            content = Parser.filter(content)
            content = Parser.resolve_path(content, config.HOST)
            status = 'OK' if content else 'FAILED'
            print(f'\t. {url} ........................{status}')
            self.document.contents.append(content)

    def render(self):

        """ Render a complete version of the HTML document

            Returns:
                (str): Html document
        """

        print('- Rendering document...')
        return Renderer.render(document=self.document)

    def write(self, data, ext='pdf'):

        """ Writting process of the data to PDF or HTML format

            Args:
                data (str): data to be processed
                ext (str): data type

        """

        print(f'- Writting ({ext}) document...')
        
        suffix = 'tutorial'
        filename = f'{self.document.title}-{suffix}.{ext}'
        
        if ext == 'pdf':
            weasyprint.HTML(string=data).write_pdf(filename)
        elif ext == 'html':
            utils.write_file(data=data, filename=filename)
 