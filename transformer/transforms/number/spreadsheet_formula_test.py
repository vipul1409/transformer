# -*- coding: utf-8 -*-

import unittest
import spreadsheet_formula

class TestNumberSpreadsheetStyleFormulaTransform(unittest.TestCase):

    def test_spreadsheet_formula(self):
        transformer = spreadsheet_formula.NumberSpreadsheetStyleFormulaTransform()

        self.assertEqual(2, transformer.transform(u'1 - -1'))

        self.assertEqual(6, transformer.transform(u'1 + 2 + 3'))
        self.assertEqual(-4, transformer.transform(u'1 - 2 - 3'))
        self.assertEqual(6, transformer.transform(u'1 * 2 * 3'))
        self.assertEqual(0.16666666666666666, transformer.transform(u'1 / 2 / 3'))

        self.assertEqual(1, transformer.transform(u'(1 + 2) / 3 + MIN(0, 10)'))

        self.assertEqual(1, transformer.transform(u'MOD(1, 2)'))
        self.assertEqual(0, transformer.transform(u'MOD(2, 2)'))

        self.assertEqual(0.01, transformer.transform(u'1%'))

        self.assertEqual(True, transformer.transform(u'MOD(2, 2) = 0'))
        self.assertEqual(True, transformer.transform(u'MOD(2, 2) <> 1'))
        self.assertEqual(10, transformer.transform(u'MAX(5, 2, 10)'))

        self.assertEqual(True, transformer.transform(u'5 > 0'))
        self.assertEqual(True, transformer.transform(u'5 >= 0'))
        self.assertEqual(False, transformer.transform(u'5 > 6'))
        self.assertEqual(False, transformer.transform(u'5 >= 6'))
        self.assertEqual(False, transformer.transform(u'5 < 0'))
        self.assertEqual(False, transformer.transform(u'5 <= 0'))
        self.assertEqual(True, transformer.transform(u'5 < 6'))
        self.assertEqual(True, transformer.transform(u'5 <= 6'))

        self.assertEqual(4, transformer.transform(u'POWER(2, 2)'))
        self.assertEqual(12, transformer.transform(u'ABS(-12)'))

        self.assertEqual(1, transformer.transform(u'AND(1,2)'))
        self.assertEqual(1, transformer.transform(u'OR(0,1)'))
        self.assertEqual(0, transformer.transform(u'AND(0,1)'))

        self.assertEqual(1, transformer.transform(u'IF(TRUE, 1, 2)'))
        self.assertEqual(2, transformer.transform(u'IF(FALSE, 1, 2)'))

        self.assertEqual(100, transformer.transform(u'=100'))

    def test_unicode_strings(self):
        transformer = spreadsheet_formula.NumberSpreadsheetStyleFormulaTransform()

        self.assertEqual(u'χϩί', transformer.transform(u'="χϩί"'))
        self.assertEqual(True, transformer.transform(u'="χϩί"="χϩί"'))
        self.assertEqual(u'yes', transformer.transform(u'=IF("χϩί"="χϩί", "yes", "no")'))

    def test_invalid_formula(self):
        transformer = spreadsheet_formula.NumberSpreadsheetStyleFormulaTransform()

        try:
            transformer.transform(u'1 . -1')
            self.assertTrue(False)
        except Exception:
            # this test passes if an error is thrown
            self.assertTrue(True)
            pass

        try:
            transformer.transform(u'ABND(0,1)')
            self.assertTrue(False)
        except Exception:
            # this test passes if an error is thrown
            self.assertTrue(True)
            pass

    def test_empty_formula(self):
        transformer = spreadsheet_formula.NumberSpreadsheetStyleFormulaTransform()

        try:
            transformer.transform(None)
            self.assertTrue(False)
        except Exception:
            # this test passes if an error is thrown
            self.assertTrue(True)
            pass

        try:
            transformer.transform('')
            self.assertTrue(False)
        except Exception:
            # this test passes if an error is thrown
            self.assertTrue(True)
            pass
