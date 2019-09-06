USER_AGENT = 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0'

APP_NAME = 'PyTTP'

APP_DESCRIPTION = 'CLI application that generate a pdf or html document of any readable tutorials from https://www.tutorialspoint.com'

DOC_EXTS = ['pdf', 'html']

DEF_DEST_SRC = '/vagrant/lab/PYTTP/'

HOST = 'https://www.tutorialspoint.com' 

DEFAULT_ENTRYPOINT = 'https://www.tutorialspoint.com/reactjs/reactjs_component_api.htm'

DOCSEC_CLASSMAP = { 'chapters': 'toc chapters', 'content': 'tutorial-content' }

TAGS_FILTER = ['script', 'hr']

HTMLCLASS_FILTER = [
    'pre-btn', 
    'print-btn center', 
    'pdf-btn', 
    'nxt-btn', 
    'top-ad-heading',
    'button-borders',
    'bottomadtag', 
    'bottomgooglead', 
    'tutorial-menu', 
    'clearer', 
    'google-bottom-ads', 
    'space-bottom'
]


