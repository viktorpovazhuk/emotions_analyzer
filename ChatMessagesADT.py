# from my_array import Array
from node import Node


class ChatMessagesADT:
    """
    Generates ChatMessages object based on list filled
    with Message objects.
    """

    def __init__(self, messages=None):
        '''
        Parameters
        '''
        self.messages = [] if messages is None else messages
        self.emotions = {'anger': 0,
                         'fear': 0,
                         'joy': 0,
                         'analytical': 0,
                         'confident': 0,
                         'tentative': 0,
                         'sadness': 0
                         }

        if self.messages:
            self.fill_emotions()

    def fill_emotions(self):
        '''
        Fills emotions dict
        '''
        for message in self.messages:

            if message is not None:
                for sentence in message:

                    if sentence is not None and sentence.emotion:
                        self.emotions[sentence.emotion] += 1

    def add_message(self, message):
        '''
        Adds Message object
        '''
        self.messages.append(message)
        for sentence in message:
            if sentence.emotion:
                self.emotions[sentence.emotion] += 1

    def get_sentences(self, emotion):
        '''
        Returns sentences
        with specific tone
        '''
        filtered = self._filter_sentences(emotion)
        return str(filtered)

    def _filter_sentences(self, emotion):
        '''
        Returns new ChatMessagesADT with sentences
        with specific tone
        '''
        filtered = ChatMessagesADT(self.messages)

        for emo in self.emotions.keys():

            if emo == emotion:
                continue

            filtered = filtered.delete_sentences(emo)
        return filtered

    def get_percentage(self, emotion):
        number_sentences = sum(self.emotions.values())
        percentage = (self.emotions[emotion] / number_sentences
                      if number_sentences != 0 else 0)
        return round(percentage * 100, 2)

    def delete_old(self, save_period):
        '''
        Deletes messages, which period has expired
        '''

        for idx, message in enumerate(self.messages):

            if message.created > save_period:
                self.delete_message(idx)

        self.fill_emotions()

    def delete_message(self, idx):
        '''
        Deletes a message from ChatMessagesADT
        '''
        self.messages[idx] = None
        self.fill_emotions()

    def delete_sentences(self, emotion):
        '''
        Filters sentences with specific tone in messages
        Returns new object
        '''
        filtered = ChatMessagesADT(self.messages)

        for message in filtered.messages:
            message.delete_sentences(emotion)

        filtered.emotions[emotion] = 0

        return filtered

    def __len__(self):
        '''
        Returns the number of Messages
        '''
        return len(self.messages)

    def __contains__(self, text):
        '''
        Checks, if the searched sentence is in the message.
        '''
        for message in self.messages:

            if message:
                if text in message.original:
                    return True

        return False

    def is_empty(self):
        '''
        Checks if self.messages is empty
        '''
        return len(self) == 0

    def __iter__(self):
        '''
        Iterates through messages
        '''
        return self.messages.__iter__()

    def __str__(self):
        '''
        Represents object as a whole str
        '''
        whole_chat = []

        for message in self.messages:
            if message:
                whole_chat.append(str(message))

        return '\n'.join(whole_chat)


class MessageADT:
    """
    Generates Message object based on array filled
    with Sentence objects.
    """

    def __init__(self, text='', created=None):
        '''
        Parameters
        '''
        self.original = text
        self.created = created
        self._front = self._rear = None
        self._size = 0
        if text != '':
            self.fill_sentences(text.replace('!', '.').replace(
                '?', '.').replace('...', '.'))

    def fill_sentences(self, text):
        '''
        Generates Array filled with Sentence objects
        '''
        text = text.split('.')
        text = [sentence.strip() for sentence in text]
        while '' in text:
            text.remove('')

        # sentences = LinkedQueue(text)

        for sentence in text:
            if sentence:
                self._add_sentence(SentenceADT(sentence))

    def _add_sentence(self, item):
        new_node = Node(item)
        if self.is_empty():
            self._front = new_node
            self._rear = self._front
        else:
            self._rear.next = new_node
            self._rear.next.previous = self._rear
            self._rear = self._rear.next
        self._size += 1

    # def pop(self, idx):
    #     '''
    #     Pops element by entered index
    #     '''
    #     self.sentences[idx] = None

    def delete_sentences(self, emotion):
        '''
        Removes sentences with a given tone
        '''
        # idx = 0
        # for sentence in self.sentences:
        #
        #     if sentence is not None and sentence.emotion == emotion:
        #         self.pop(idx)
        #
        #     idx += 1
        cur_node = self._front
        while cur_node is not None:

            if cur_node.data.emotion == emotion:

                if cur_node is self._front:
                    self._front = self._front.next

                if cur_node is self._rear:
                    self._rear = cur_node.previous

                if cur_node.previous is not None:
                    cur_node.previous.next = cur_node.next

                if cur_node.next is not None:
                    cur_node.next.previous = cur_node.previous

                self._size -= 1
            cur_node = cur_node.next

    def __len__(self):
        '''
        Returns number of sentences
        '''
        return self._size

    # def __getitem__(self, idx):
    #     '''
    #     Returns Sentence by given index
    #     '''
    #     return self.sentences[idx]

    def __iter__(self):
        '''
        Iterates through sentences
        '''
        return _MessageIterator(self._front)

    def __contains__(self, sentence):
        '''
        Checks, if the searched sentence is in the message.
        '''
        if sentence in self.original:
            return True

        return False

    def is_empty(self):
        '''
        Checks, if message is not empty
        '''
        if self._front:
            return False

        return True

    def __str__(self):
        '''
        Represents message
        '''
        # sentences = self.sentences
        message = []

        for sentence in self:
            if sentence:
                message.append(sentence.text)

        return '. '.join(message) + '.' if len(message) > 0 else ''


class _MessageIterator:
    """ Iterates through message's elements
    Source: 'Fundamentals of Python: Data structures'
    Author: Kenneth A. Lambert """

    def __init__(self, the_head):
        self._head = the_head
        self._cur_node = the_head

    def __iter__(self):
        self._cur_node = self._head
        return self

    def __next__(self):
        if self._cur_node is not None:
            entry = self._cur_node.data
            self._cur_node = self._cur_node.next
            return entry
        else:
            raise StopIteration


class SentenceADT:
    """
    Generates Sentence object. Receives a sentence as
    a text attribute.
    """

    def __init__(self, text='', emotion=None):
        self.text = text
        self.emotion = emotion

    # don't need
    # def match_emotion(self, emotion):
    #     '''
    #     Matches sentences with a specific tone
    #     '''
    #     return self.emotion == emotion

    def __str__(self):
        """
        Represents sentence
        """
        return self.text + '.'


if __name__ == '__main__':
    m1 = MessageADT('I love my dog. My dog is good! My dog is a cat... ')
    m2 = MessageADT('I hope it works. It should work! Hate it... ')

    m1[1].emotion = 'anger'

    chm1 = ChatMessagesADT([m1, m2])
    print('-' * 50)
    for elem in chm1:
        print(elem)
    print('-' * 50)
    print(chm1.emotions)
    print('-' * 50)

    filtered = chm1.delete_sentences('anger')

    print(filtered.emotions)
