USER_AGENT = 'Mozilla/5.0 (Windows NT x.y; rv:10.0) Gecko/20100101 Firefox/10.0'
HOST = 'https://www.tutorialspoint.com'
DOCEXTS = ['pdf', 'html']
HTML_DOCSEC_CLASSMAP = { 'chapters': 'toc chapters', 'content': 'tutorial-content' }
HTML_TAGS_FILTER = ['script', 'hr']
HTML_CLASS_FILTER = [
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
HTML_ATTRS = {
    'href': ['a', 'area', 'base', 'link'],
    'src': ['audio','embed','iframe','img','input','script','source','track','video']
}