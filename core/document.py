from enum import Enum

class Section(Enum):

    """ Document section enumeration """
    
    META = 1
    TABLE_CONTENTS = 2
    CONTENT = 3

class TutorialDocument:
    
    """ Representation of a single tutorial
    
        Attrs:
            name (str): tutorial name
            meta (list): HTML metadata
            table_contents (list): tutorial chapters
            contents (list): main content for each chapters
    """

    def __init__(self, name=None, meta=[], table_contents=None, contents=[]):
        self.name = name
        self.meta = meta
        self.table_contents = table_contents
        self.contents = contents

    def __repr__(self):
        return self.name