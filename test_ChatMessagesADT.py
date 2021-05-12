import unittest
from unittest import TestCase
from ChatMessagesADT import MessageADT


class TestMessageADT(TestCase):
    def test_init(self):
        text = 'I hope it works. It should work!'
        message = MessageADT(text)
        self.assertTrue(len(message) == 2)
        self.assertTrue([sentence.text for sentence in message.sentences] == ['I hope it works', 'It should work'])



if __name__ == "__main__":
    unittest.main()
