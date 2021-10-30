import unittest
from utils.find_executed_exports import find_executed_exports
from utils.find_exports import find_exports
from utils.typescript_file_filter import typescript_file_filter


class TestSingle(unittest.TestCase):
    files = typescript_file_filter("tests/data")
  
    def test_find_typescript_files(self):
      self.assertEqual(len(self.files), 2)

    def test_finds_single_export(self):
      exports = find_exports(self.files)
      self.assertEqual(len(exports), 1)

    def test_checks_export(self):
      exports = find_exports(self.files)
      unused_exports = find_executed_exports(exports, self.files)
      self.assertEqual(len(unused_exports), 0)
