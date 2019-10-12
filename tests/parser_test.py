import sys
sys.path.insert(0, '/vagrant/lab/PyTTP')

import unittest
import config 
from core.parser import Parser
from core.exceptions import *
from core.document import *

class ParserTest(unittest.TestCase):

    '''
          [MethodName_StateUnderTest_ExpectedBehavior]
    '''

    def test_extractHref_anchorTagMissing_returnEmptyList(self):
        html = '<html></html>'
        value = Parser.extract_href('')
        print(value)
        self.assertEqual(value, [])

    def test_extractHref_anchorTagHrefAttrMissing_returnEmptyList(self):
        html =  '''<html>
                    <a>link1</a>
                    <a>link2</a>
                </html>'''
        value = Parser.extract_href(html)
        print(value)
        self.assertEqual(value, [])

    def test_extractHref_anchorTag_returnList(self):
        html = '<html><a href="/link1"></a><a href="/link 2"></a></html>'
        value = Parser.extract_href(html)
        print(value)
        self.assertIsNotNone(value)

    def test_resolvePath_srcAttrElements_returnFullPath(self):
        html = '<img src="/testing"/>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, f'<img src="{config.HOST}/testing"/>')
        
        html = '<iframe src="/testing"></iframe>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, f'<iframe src="{config.HOST}/testing"></iframe>')
    
    def test_resolvePath_hrefAttrElements_returnFullPath(self):
        html = '<a href="/testing"></a>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, f'<a href="{config.HOST}/testing"></a>')

        html = '<link href="/testing"/>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, f'<link href="{config.HOST}/testing"/>')

    def test_resolvePath_emptyArg_returnOrigin(self):
        html = ''
        value = Parser.resolve_path(html, '')
        print(value)
        self.assertEqual(value, html)

    def test_resolvePath_attrMissing_returnOrigin(self):
        html = '<img/>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, html)

        html = '<a></a>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, html)

    def test_resolvePath_emptyAttr_returnOrigin(self):
        html = '<a href=""></a>'
        value = Parser.resolve_path(html, config.HOST)
        print(value)
        self.assertEqual(value, html)

    def test_parseTableContents_validEntryPoint_returnStr(self):
        value = Parser.parse(url=config.ENTRYPOINT, section=Section.TABLE_CONTENTS)
        print('')
        self.assertIsInstance(value, str)

    def test_parseTableContents_exceptionThrown(self):
        print('')
        self.assertRaises(ParserError, Parser.parse, url=config.HOST, section=Section.TABLE_CONTENTS)

if __name__ == '__main__':
    unittest.main()


    
    
