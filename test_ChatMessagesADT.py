import unittest
from unittest import TestCase
from ChatMessagesADT import MessageADT, ChatMessagesADT, SentenceADT


class TestMessageADT(TestCase):
    """
    Tests ChatMessagesADT, MessageADT, SentenceADT objects
    """

    def test_SADT_init(self):
        """
        Checks init of SentenceADT.
        """
        s1 = SentenceADT('My dog is a cat... ')
        s1.emotion = 'sadness'

        self.assertTrue(s1.emotion == 'sadness')

    def test_SADT_str(self):
        """
        Checks str of SentenceADT.
        """

        s1 = SentenceADT('My dog is a cat... ')
        self.assertTrue(str(s1) == 'My dog is a cat... ')

    def test_MADT_init(self):
        """
        Checks init of MessageADT.
        """

        text = 'I hope it works. It should work!'
        message = MessageADT(text)
        self.assertTrue(len(message) == 2)

    def test_CMADT_init(self):
        """
        Checks init of ChatMessagesADT.
        """

        m1 = MessageADT('I love my dog. My dog is good! ')
        m2 = MessageADT('I hope it works. It should work! I hate it... ')

        chm1 = ChatMessagesADT([m1, m2])
        self.assertTrue(len(chm1.messages) == 2)

    def test_CMADT_add_message(self):
        """
        Check add_message method from ChatMessagesADT.
        """

        m1 = MessageADT('I love my dog. My dog is good! ')
        m2 = MessageADT('I hope it works. It should work! I hate it... ')

        chm1 = ChatMessagesADT([m1])
        self.assertTrue(
            str(len(chm1.messages) == 1))

        chm1.add_message(m2)

        self.assertTrue(chm1.is_empty() == False)
        self.assertTrue(
            str(len(chm1.messages) == 2))

    def test_CMADT_fill_emotion(self):
        """
        Check fill_emotion method from ChatMessagesADT.
        """
        s1 = SentenceADT('My dog is a cat... ')
        s1.emotion = 'sadness'

        m1 = MessageADT('I love my dog. My dog is good! ')
        m1._add_sentence(s1)
        m2 = MessageADT('I hope it works. It should work! ')
        m2._add_sentence(SentenceADT('I hate it... ', 'anger'))

        chm1 = ChatMessagesADT([m2])
        chm1.add_message(m1)
        self.assertTrue(chm1.emotions['sadness'] == 1)

    def test_CMADT_delete_sentences(self):
        """
        Check delete_sentences method from ChatMessagesADT.
        """
        m1 = MessageADT('I hope it works. It should work! ')
        m2 = MessageADT('I hope it works. It should work! ')
        m2._add_sentence(SentenceADT('I hate it... ', 'anger'))

        chm1 = ChatMessagesADT([m2])

        chm1.delete_sentences('anger')
        self.assertTrue(m2 == m1)

    def test_CMADT_get_sentences(self):
        """
        Check get_sentences method from ChatMessagesADT.
        """
        result = ChatMessagesADT(
            [MessageADT('I hope it works. ' + 'I hate it... ')])
        m1 = MessageADT()
        s1 = SentenceADT('I hope it works. ', 'anger')
        s2 = SentenceADT('It should work! ', 'confident')
        s3 = SentenceADT('I hate it... ', 'anger')

        m1._add_sentence(s1)
        m1._add_sentence(s2)
        m1._add_sentence(s3)

        chm1 = ChatMessagesADT([m1])

        chm1.get_sentences('anger')
        self.assertTrue(chm1 == result)

    def test_CMADT_get_percentage(self):
        """
        Check get_percentage method from ChatMessagesADT.
        """

        m1 = MessageADT()
        s1 = SentenceADT('I hope it works. ', 'anger')
        s2 = SentenceADT('It should work! ', 'confident')
        s3 = SentenceADT('I hate it... ', 'anger')

        m1._add_sentence(s1)
        m1._add_sentence(s2)
        m1._add_sentence(s3)

        chm1 = ChatMessagesADT([m1])

        result = chm1.get_percentage('anger')
        self.assertTrue(result == 66.67)

    def test_CMADT_delete_sentences(self):
        """
        Check delete_sentences method from ChatMessagesADT.
        """

        m1 = MessageADT('I love my dog. My dog is good! ')
        m2 = MessageADT('I hope it works. It should work! ')

        chm1 = ChatMessagesADT([m1, m2])
        chm1.delete_message(0)
        self.assertTrue(len(chm1) == 1)

    def test_CMADT_compare_ChatMessagesADT(self):
        """
        Compares two ChatMessagesADT.
        """

        m1 = MessageADT('I love my dog. My dog is good! ')
        m2 = MessageADT('I love my cat. My dog is good! ')

        chm1 = ChatMessagesADT([m1])
        chm2 = ChatMessagesADT([m2])

        self.assertTrue(chm1 != chm2)

    def test_compare_MessageADT(self):
        """
        Compares two MessagesADT.
        """

        m1 = MessageADT('I love my dog. My dog is good! ')
        m2 = MessageADT('I love my cat. My dog is good! ')

        self.assertTrue(m1 != m2)

    def test_compare_SentenceADT(self):
        """
        Compares two SentenceADT.
        """

        s1 = SentenceADT('I love my dog. ')
        s2 = SentenceADT('I love my cat. ')

        self.assertTrue(s1 != s2)

    def test_CMADT_contains(self):
        """
        Check __contains__ method from ChatMessagesADT.
        """

        m1 = MessageADT('I love my dog. My dog is good! ')
        m2 = MessageADT('I hope it works. It should work! ')

        chm1 = ChatMessagesADT([m1, m2])
        self.assertTrue('dog' in chm1)
        self.assertTrue('dogg' not in chm1)


if __name__ == "__main__":
    unittest.main()
