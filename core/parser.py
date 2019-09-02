import bs4
import core.client as client
import core.utils as utils
import core.config as config
import core.exceptions as exceptions

from core.document import *

class Parser:

    """ DOM Parser """

    @staticmethod
    def extract_href(html):

        """ Extract the href property of anchor html tag

            Args:
                html (str): html to be parsed

            Returns:
                (array[str]): all hrefs property from the html

        """

        soup = bs4.BeautifulSoup(html, 'html.parser') 
        return [a['href'] for a in soup.find_all('a')]

    @staticmethod
    def resolve_path(html, host, d=False):

        """ Prefix the resource path with the host name

            Args:
                html (str): html to be parsed
                host (str): the host name (e.g: https://www.tutorialspoint.com)

            Returns:
                (str): the full path of the ressource
            
        """
        
        auth_tags = ['link', 'a', 'img', 'iframe']
        soup = bs4.BeautifulSoup(html, 'html.parser') 
        tags = soup.find_all(auth_tags)

        for tag in tags:
            attr = None
            
            if tag.name == 'img' or tag.name == 'iframe':
                attr = 'src'
            elif tag.name == 'link' or tag.name == 'a':
                attr = 'href'

            tagsrc = tag[attr] if attr in tag.attrs.keys() else ''

            if tag.name in auth_tags and tagsrc and tagsrc[0] == '/':
                tag[attr] = host + tag[attr]
                    
        return str(soup)

    @staticmethod
    def filter(html):

        """ Remove specific tags or html classes from the given argument

            Args:
                html (str): html to be parsed

            Return: 
                soup (str): cleaned version of the html argument

        """

        soup = bs4.BeautifulSoup(html, 'html.parser') 

        tags = soup.find_all(config.TAGS_FILTER)
        for tag in tags:
            tag.decompose()

        tags = soup.find_all(True, {'class': config.HTMLCLASS_FILTER})
        for tag in tags:
            tag.decompose()

        tags = soup.find_all('a', {'href': True})
        for tag in tags:
            if tag['href'][0] == '/':
                del tag['href']

        return str(soup)

    @staticmethod
    def parse(url, sec):

        """ Parse a specific section from the HTML document of a given url

            Args:
                url (str): url of any readable tutorial from https://www.tutorialspoint.com 
                sec (document.Section Enum): section of the document that need to be parsed: 
                (document.Section.HEAD, document.Section.TABLE_CONTENTS, document.Section.Content)
            
            Returns:
                (str): the parsed section of the HTML document
                
        """

        switcher = {
            Section.HEAD: Parser.__get_head,
            Section.TABLE_CONTENTS: Parser.__get_chapters,
            Section.CONTENT: Parser.__get_content
        } 

        try:
            response = client.get(url, {'User-Agent': config.USER_AGENT})
        except Exception as e:
            print(e)
        else:
            soup = bs4.BeautifulSoup(response.content, 'html.parser')  
            fn = switcher.get(sec) 
            return ''.join([str(tag) for tag in fn(soup)])
            
    @staticmethod
    def __get_head(soup):
        return soup.find_all(['style', 'link']) 
    
    @staticmethod
    def __get_chapters(soup):
        uls = soup.find_all(lambda tag: tag.name == 'ul' and utils.is_iterable(tag.get('class')) and \
        ' '.join(tag.get('class')) == config.DOCSEC_CLASSMAP['chapters']) 
        
        if not uls: raise exceptions.ParserError('Not a valid entry point')
        return uls   
    
    @staticmethod
    def __get_content(soup):
        class_ = config.DOCSEC_CLASSMAP['content']
        return soup.select(f'div.{class_}')
    
    
  

                
