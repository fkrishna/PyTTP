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

  def test_parse_validHostNameValidEntrypoint_tutorialDocumentInstanceCreated(self):
    ep = gconf.ENTRYPOINT
    self.pyttp.parse(ep)
    print(self.pyttp.tutorial)
    self.assertIsInstance(self.pyttp.tutorial, TutorialDocument)

  def tearDown(self):
    del self.pyttp
  
if __name__ == '__main__':
    unittest.main()

