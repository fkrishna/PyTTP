import sys
sys.path.insert(0, '/vagrant/lab/PYTTP')

import unittest
import core.config as config

from core.parser import Parser
from core.exceptions import *
from core.document import *

class ParserTest(unittest.TestCase):

    def test_extractHrefProperty_noAnchorTag_returnEmptyArray(self):
        link = '<html></html>'
        urls = Parser.extract_href('')
        print(urls)
        self.assertEqual(urls, [])

    def test_extractHrefProperty_withAnchorTag_returnArray(self):
        html = '<html><a href="/link 1"></a><a href="/link 2"></a></html>'
        urls = Parser.extract_href(html)
        print(urls)
        self.assertIsNotNone(urls)

    def test_resolvePath_linkTagArg_returnFullPath(self):
        html = '<link href="/favicon.ico"/>'
        path = Parser.resolve_path(html, config.HOST)
        print(path)
        self.assertEqual(path, f'<link href="{config.HOST}/favicon.ico"/>')

    def test_resolvePath_imgTagArg_returnFullPath(self):
        html = '<img src="/img.png"/>'
        path = Parser.resolve_path(html, config.HOST)
        print(path)
        self.assertEqual(path, f'<img src="{config.HOST}/img.png"/>')

    def test_resolvePath_anchorTagArg_returnFullPath(self):
        html = '<a href="/contact.htm">contact</a>'
        path = Parser.resolve_path(html, config.HOST)
        print(path)
        self.assertEqual(path, f'<a href="{config.HOST}/contact.htm">contact</a>')

    def test_parseChapters(self):
        chapters = Parser.parse(url=config.DEFAULT_ENTRYPOINT, sec=Section.TABLE_CONTENTS)
        print(chapters[:25] + '...')
        self.assertIsNotNone(chapters)

    def test_parseChapters_exceptionThrown(self):
        ep = config.HOST
        print('')
        self.assertRaises(ParserError, Parser.parse, url=ep, sec=Section.TABLE_CONTENTS)


if __name__ == '__main__':
    unittest.main()


    
    
