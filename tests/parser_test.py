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
        res = Parser.extract_href('')
        print(res)
        self.assertEqual(res, [])

    def test_extractHref_anchorTagHrefAttrMissing_returnEmptyList(self):
        html =  '''<html>
                    <a>link1</a>
                    <a>link2</a>
                </html>'''
        res = Parser.extract_href(html)
        print(res)
        self.assertEqual(res, [])

    def test_extractHref_anchorTag_returnList(self):
        html = '<html><a href="/link1"></a><a href="/link 2"></a></html>'
        res = Parser.extract_href(html)
        print(res)
        self.assertIsNotNone(res)

    def test_resolvePath_srcAttrElements_returnFullPath(self):
        html = '<img src="/testing"/>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, f'<img src="{config.HOST}/testing"/>')
        
        html = '<iframe src="/testing"></iframe>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, f'<iframe src="{config.HOST}/testing"></iframe>')
    
    def test_resolvePath_hrefAttrElements_returnFullPath(self):
        html = '<a href="/testing"></a>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, f'<a href="{config.HOST}/testing"></a>')

        html = '<link href="/testing"/>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, f'<link href="{config.HOST}/testing"/>')

    def test_resolvePath_emptyArg_returnOrigin(self):
        html = ''
        res = Parser.resolve_path(html, '')
        print(res)
        self.assertEqual(res, html)

    def test_resolvePath_attrMissing_returnOrigin(self):
        html = '<img/>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, html)

        html = '<a></a>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, html)

    def test_resolvePath_emptyAttr_returnOrigin(self):
        html = '<a href=""></a>'
        res = Parser.resolve_path(html, config.HOST)
        print(res)
        self.assertEqual(res, html)

    def test_parseTableContents_validEntryPoint_returnStr(self):
        res = Parser.parse(url=config.ENTRYPOINT, section=Section.TABLE_CONTENTS)
        print('')
        self.assertIsInstance(res, str)

    def test_parseTableContents_exceptionThrown(self):
        print('')
        self.assertRaises(EntryPointError, Parser.parse, url=config.HOST, section=Section.TABLE_CONTENTS)

if __name__ == '__main__':
    unittest.main()


    
    
