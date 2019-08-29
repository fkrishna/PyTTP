import bs4
import core.client as client
import core.utils as utils
import core.config as config
import core.exceptions as exceptions

class Parser:

    """ DOM Parser """

    @staticmethod
    def extract_href(html):

        """ Extract the href property of anchor html tag

            Args:
                html (str): html to be parsed
            Returns:
                array[str]: href property
        """

        soup = bs4.BeautifulSoup(html, 'html.parser') 
        return [a['href'] for a in soup.find_all('a')]

    @staticmethod
    def parse(url, el):

        """ Parse a specific element from HTML document of a given url

            Args:
                url (str): url of any readable tutorial 
                from https://www.tutorialspoint.com 

                el (str): element that need to be parsed: (head, chapters, content)
            
            Returns:
                Fn: 
        """

        switcher = {
            'head': Parser.__get_head,
            'chapters': Parser.__get_chapters,
            'content': Parser.__get_content
        } 

        try:
            response = client.get(url, {'User-Agent': config.USER_AGENT})
        except Exception as e:
            print(e)
        else:
            soup = bs4.BeautifulSoup(response.content, 'html.parser')  
            fn = switcher.get(el) 
            return fn(soup)
            
    @staticmethod
    def __get_head(soup):
        return soup.find_all(['style', 'link']) 
    
    @staticmethod
    def __get_chapters(soup):
        uls = soup.find_all(lambda tag: tag.name == 'ul' and utils.is_iterable(tag.get('class')) and \
        ' '.join(tag.get('class')) == config.HTML_CLASSES['chapters']) 
        
        if not uls: raise exceptions.ParserError('Not a valid entry point')
        return uls   
    
    @staticmethod
    def __get_content(soup):
        class_ = config.HTML_CLASSES['content']
        return soup.select(f'div.{class_}')
    
    
  

                
