import unittest
import encode_base64

class TestStringEncodebase64Transform(unittest.TestCase):
    def test_encodeascii(self):
        transformer = encode_base64.StringEncodebase64Transform()
        self.assertEqual(transformer.transform(""), "")
        self.assertEqual(transformer.transform(u'ls -lathr'), "bHMgLWxhdGhy")
        self.assertEqual(transformer.transform(None), "")
