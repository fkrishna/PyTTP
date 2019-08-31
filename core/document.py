from enum import Enum

class Section(Enum):

    """ Document section enumeration """
    
    HEAD = 1
    TABLE_CONTENTS = 2
    CONTENT = 3

class Document:
    
    """ Representation of a single HTML document of a tutorial
    
        A single HTML document of a tutorial is divided into three sections: (Head, Table Contents, Content) 
        
        Attrs:
            head (str): HTML metadata
            table_contents (str): tutorial chapters
            contents (array): main content of each chapter
    """

    def __init__(self, head=None, table_contents=None, contents=None):
        self.head = head,
        self.table_contents = table_contents,
        self.contents = contents