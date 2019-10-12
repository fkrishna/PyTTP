import sys
sys.path.insert(0, '/vagrant/lab/PyTTP')

import unittest
import config as gconf
from core.pyttp import *
from core.exceptions import *
from core.document import *

class PyTTPTest(unittest.TestCase):

  '''
    [MethodName_StateUnderTest_ExpectedBehavior]
  '''

  def setUp(self):
    self.pyttp = PyTTP()

  def test_parse_invalidHostName_exceptionThrown(self):
    ep = 'https://example.com'
    print(ep)
    self.assertRaises(InvalidHostName, self.pyttp.parse, entrypoint=ep)

  def test_parse_validHostNameBadEntrypoint_exceptionThrown(self):
    ep = gconf.HOST
    print(ep)
    self.assertRaises(ParserError, self.pyttp.parse, entrypoint=ep)

  def test_parse_validHostNameValidEntrypoint_returnTutorialInstance(self):
    ep = gconf.ENTRYPOINT
    doc = self.pyttp.parse(ep)
    print(doc)
    self.assertIsInstance(doc, Tutorial)

  def test_write_invalidTypeForDataParam_exceptionThrown(self):
    kwargs = {
      'data': [],
      'dest': gconf.DEST,
      'ext': 'html'
    }
    print(type(kwargs['data']))
    self.assertRaises(TypeError, self.pyttp.write, **kwargs)

  def test_write_invalidDestinationPath_exceptionThrown(self):
    kwargs = {
      'data': '<h1>Test</h1>',
      'dest': '/dir/test/',
      'ext': 'html'
    }
    print(kwargs['dest'])
    self.assertRaises(IOError, self.pyttp.write, **kwargs)

  def test_write_invalidExtension_exceptionThrown(self):
    kwargs = {
      'data': '<h1>Test</h1>',
      'dest': gconf.DEST,
      'ext': 'cpp'
    }
    print(kwargs['ext'])
    self.assertRaises(ValueError, self.pyttp.write, **kwargs)

  def tearDown(self):
    del self.pyttp
  
if __name__ == '__main__':
    unittest.main()

