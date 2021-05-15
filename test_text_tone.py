import unittest
from unittest import TestCase
from text_tone import detect_tone, translate_to_en


class TestTextTone(TestCase):

    def test_detect_tone(self):

        text1 = 'I love my dog'
        emotion = detect_tone(text1)
        self.assertTrue(emotion == 'joy')

        text2 = '''Лишилось тільки ще спакуватись... Се було одно з тих незчисленних "треба", \
які мене так утомили і не давали спати. Дарма, чи те "треба" мале, чи велике, — \
вагу те має, що кожен раз воно вимагає уваги, що не я їм, а воно мною уже керує. \
Фактично стаєш невільником сього многоголового звіра. Хоч на час увільнитись \
від нього, забути, спочити. Я утомився. '''
        emotion = detect_tone(text2)
        self.assertTrue(emotion == 'sadness')


if __name__ == "__main__":
    unittest.main()
