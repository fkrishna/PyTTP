from enum import Enum

class Section(Enum):

    """ Document section enumeration """
    
    META = 1
    TABLE_CONTENTS = 2
    CONTENT = 3

class Document:
    
    """ Representation of a single HTML document of a tutorial
    
        A single HTML document of a tutorial is divided into three sections: (Head, Table Contents, Content) 
        
        Attrs:
            meta (str): HTML metadata
            table_contents (str): tutorial chapters
            contents (array[:str]): main content of each chapter
    """

    def __init__(self, meta=None, title=None, table_contents=None, contents=[]):
        self.meta = meta
        self.title = title
        self.table_contents = table_contents
        self.contents = contents