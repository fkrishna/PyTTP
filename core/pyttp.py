import weasyprint
import core.config as config
import core.utils as utils

from core.exceptions import *
from core.document import *
from core.parser import Parser


class PyTTP:

    """ PyTTP class generate a pdf version of any readable 
        tutorials from https://www.tutorialspoint.com 
   
        Attrs:
            document (obj:document): single HTML document of a tutorial chapter
        
    """

    def __init__(self):
        self.document = Document()

    @classmethod
    def createPDF(cls, entrypoint):

        """ Factory Method

        """

        ttp = PyTTP()
        ttp.parse(entrypoint)
        urls = Parser.extract_href(ttp.document.table_contents)
        ttp.extract(urls)
        htmldoc = ttp.render()  
        ttp.write(doc=htmldoc, filename='test.pdf')

    def parse(self, entrypoint):

        """ Parse the entry point

            Args:
                entrypoint (str): url of any readable tutorial from https://www.tutorialspoint.com 

        """

        print(f'- Parsing the entry point: {entrypoint}')
        
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

        print('- Extracting data from host...')

        for url in urls:
            content = Parser.parse(url=url, sec=Section.CONTENT)
            content = Parser.filter(content)
            status = 'OK' if content else 'FAILED'
            print(f'{url} ........................{status}')
            self.document.contents.append(content)

    def render(self):

        """ Render a complete version of the HTML document

            Returns:
                htmldoc (str): Html document
        """

        print('- Rendering document...')

        htmldoc = f'''
        <html>
            <head>{ self.document.head }</head>
            <body>
                <div>{ self.document.table_contents }</div>
                <div>{ ''.join(self.document.contents) }</div>
            </body>
        </html>
        '''

        return Parser.resolve_path(htmldoc, config.HOST, True)

    def write(self, obj, filename, kind='pdf'):

        """

        """

        print(f'- Writting ({kind}) objects...')
        
        if kind == 'pdf':
            weasyprint.HTML(string=obj).write_pdf(filename)
        elif kind == 'html':
            utils.write_file(data=obj, filename=filename)
 