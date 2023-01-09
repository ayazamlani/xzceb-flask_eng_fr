"""
Unit tests for translater app 
"""

import unittest
from translator import frenchToEnglish, englishToFrench

class testTranslater(unittest.TestCase):
    """
    Test class 
    """
    def test_french_to_english(self):
        """
        Testing french to english translations
        """
        self.assertEqual(frenchToEnglish(''), '')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
    
    def test_english_to_french(self):
        """
        Testing english to french translations
        """
        self.assertEqual(englishToFrench(''), '')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')