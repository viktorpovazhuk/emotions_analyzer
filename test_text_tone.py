import unittest
from unittest import TestCase
from text_tone import detect_tone


class TestTextTone(TestCase):
    def test_detect_tone(self):
        text = 'I love my dog'
        emotion = detect_tone(text)
        self.assertTrue(emotion == 'joy')



if __name__ == "__main__":
    unittest.main()