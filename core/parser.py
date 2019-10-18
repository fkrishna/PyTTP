import bs4
import core.client as client
import core.utils as utils
import core.consts as config
import core.exceptions as exceptions
from core.document import *

class Parser:

    """ Tutorial document parser """

    @staticmethod
    def extract_href(html):

        """ Extract the href property of an anchor html tag

            Args:
                html (str): html to be parsed

            Returns:
                (array[str]): value of all hrefs property from the html

        """

        urls = []
        soup = bs4.BeautifulSoup(html, 'html.parser') 
        for a in soup.find_all('a'):
            value = a.get('href')
            if value: urls.append(value)

        return urls

    @staticmethod
    def resolve_path(html, host):

        """ Prefix the resource path with the hostname

            Args:
                html (str): html to be parsed
                host (str): host name (e.g: https://www.tutorialspoint.com)

            Returns:
                (str): the full path of the ressource
            
        """
        
        auth_tags = config.HTML_ATTRS['href'] + config.HTML_ATTRS['src']
        soup = bs4.BeautifulSoup(html, 'html.parser') 
        tags = soup.find_all(auth_tags)
        
        for tag in tags:
            target_attr = None
            if tag.name in config.HTML_ATTRS['src']:
                target_attr = 'src'
            elif tag.name in config.HTML_ATTRS['href']:
                target_attr = 'href'

            attr_value = tag[target_attr] if target_attr in tag.attrs.keys() else ''
            if tag.name in auth_tags and attr_value and attr_value[0] == '/':
                tag[target_attr] = host + tag[target_attr]
                    
        return utils.to_str(soup)

    @staticmethod
    def filter(html):

        """ Remove tags elements from html

            Args:
                html (str): html to be parsed

            Return: 
                soup (str): cleaned version of the html argument

        """

        soup = bs4.BeautifulSoup(html, 'html.parser') 
        tags = soup.find_all(config.HTML_TAGS_FILTER)
        for tag in tags:
            tag.decompose()
            
        tags = soup.find_all(True, {'class': config.HTML_CLASS_FILTER})
        for tag in tags:
            tag.decompose()

        tags = soup.find_all('a', {'href': True})
        for tag in tags:
            if tag['href'][0] == '/':
                del tag['href']

        return str(soup)

    @staticmethod
    def parse(url, section):

        """ Parse a specific section of the HTML tutorial document

            Args:
                url (str): url of any readable tutorial from https://www.tutorialspoint.com 
                section (document.Section Enum): section of the document that need to be parsed: 
                (document.Section.HEAD, document.Section.TABLE_CONTENTS, document.Section.Content)
            
            Returns:
                (str): the parsed section of the HTML document
                
        """

        switcher = {
            Section.META: Parser.__get_meta,
            Section.TABLE_CONTENTS: Parser.__get_table_contents,
            Section.CONTENT: Parser.__get_content
        } 

        try:
            response = client.get(url, {'User-Agent': config.USER_AGENT})
        except Exception as e:
            pass
        else:
            soup = bs4.BeautifulSoup(response.content, 'html.parser')  
            fn = switcher.get(section) 
            return ''.join([str(tag) for tag in fn(soup)])
            
    @staticmethod
    def __get_meta(soup):
        return soup.find_all(['style', 'link']) 
    
    @staticmethod
    def __get_table_contents(soup):
        uls = soup.find_all(lambda tag: tag.name == 'ul' and utils.is_iterable(tag.get('class')) and \
        ' '.join(tag.get('class')) == config.HTML_DOCSEC_CLASSMAP['chapters']) 
        if not uls: raise exceptions.EntryPointError('Not a valid entry point')
        return uls   
    
    @staticmethod
    def __get_content(soup):
        class_ = config.HTML_DOCSEC_CLASSMAP['content']
        return soup.select(f'div.{class_}')
    
    
  

                
