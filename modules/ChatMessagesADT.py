from node import Node


class ChatMessagesADT:
    """
    Generates ChatMessages object based on list filled
    with Message objects.
    """

    def __init__(self, messages=None):
        '''
        Parameters:
        self.messages contains all messages objects from the chat in a list.

        self.emotions contains a number of messages with specific emotion
        in a dict, where self.emotions[emotion] = number of messages with 
        a such emotion.

        Preconditions:
        messages: is used for self.messages without copying
        '''
        self.messages = [] if messages is None else messages
        self.emotions = {'anger': 0,
                         'fear': 0,
                         'joy': 0,
                         'analytical': 0,
                         'confident': 0,
                         'tentative': 0,
                         'sadness': 0,
                         'unrecognized': 0
                         }

        if self.messages:
            self.fill_emotions()

    def fill_emotions(self):
        '''
        Fills self.emotions.
        '''
        for message in self.messages:

            if message is not None:
                for sentence in message:

                    if sentence is not None and sentence.emotion:
                        self.emotions[sentence.emotion] += 1

                    elif sentence is not None and not sentence.emotion:
                        sentence.emotion = 'unrecognized'
                        self.emotions[sentence.emotion] += 1

    def add_message(self, message):
        '''
        Adds Message object.
        '''
        self.messages.append(message)
        for sentence in message:

            if sentence.emotion:
                self.emotions[sentence.emotion] += 1

    def get_sentences(self, emotion):
        '''
        Returns sentences with specific tone.
        '''
        filtered_messages = []

        # get filtered text for each message
        for message in self.messages:
            filtered_sentences = message.filter_sentences(emotion)
            if filtered_sentences is not None:
                filtered_messages.append(filtered_sentences)

        return '\n'.join(filtered_messages)

    def get_percentage(self, emotion):
        """
        Returns the percentage of the specific emotion
        in relation to all the messages, downloaded from
        the chat.
        """
        number_sentences = sum(self.emotions.values())
        percentage = (self.emotions[emotion] / number_sentences
                      if number_sentences != 0 else 0)
        return round(percentage * 100, 2)

    def delete_old(self, save_period):
        '''
        Deletes messages, which period has expired.
        '''

        for idx, message in enumerate(self.messages):

            # rewrite to compare real time
            if message.created > save_period:
                self.delete_message(idx)

        self.fill_emotions()

    def delete_message(self, idx):
        '''
        Deletes a message from ChatMessagesADT.
        '''
        self.messages.pop(idx)
        self.fill_emotions()

    def delete_sentences(self, emotion):
        '''
        Deletes sentences with specific tone in messages
        and returns deleted sentences
        '''
        # get sentences with specified emotion
        filtered_sentences = self.get_sentences(emotion)

        # delete sentences with specified emotion
        for message in self.messages:
            message.delete_sentences(emotion)

        self.emotions[emotion] = 0

        return filtered_sentences

    def __len__(self):
        '''
        Returns the number of Messages.
        '''
        return len(self.messages)

    def __eq__(self, other: object) -> bool:

        first = str(self)
        second = str(other)

        for i in range(len(first)):

            if first[i] != second[i]:
                return False

        return True

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

        result = '\n'.join(whole_chat)

        if result[-2:] != '. ':
            result += '. '

        return result.replace('. .', '.').replace('..', '.')


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
                '?', '.').replace('...', '.').replace('  ', ' '))

    def fill_sentences(self, text):
        '''
        Generates Array filled with Sentence objects
        '''
        text = text.split('.')
        text = [sentence.strip() for sentence in text]
        while '' in text:
            text.remove('')

        for sentence in text:
            if sentence:
                self._add_sentence(SentenceADT(sentence))

    def _add_sentence(self, item):
        """
        Adds sentence to the MessageADT.
        """

        new_node = Node(item)

        if self.is_empty():
            self._front = new_node
            self._rear = self._front

        else:
            self._rear.next = new_node
            self._rear.next.previous = self._rear
            self._rear = self._rear.next

        self._size += 1

    def delete_sentences(self, emotion):
        '''
        Removes sentences with a given tone
        '''

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

    def filter_sentences(self, emotion):
        """Returns sentences string with specified emotion
        or None if no sentences is found"""
        filtered_sentences = ''
        for sentence in self:
            if sentence.emotion == emotion:
                filtered_sentences += sentence.text + '. '
        filtered_sentences = filtered_sentences.strip()
        return filtered_sentences if filtered_sentences != '' else None

    def __len__(self):
        '''
        Returns number of sentences
        '''
        return self._size

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

    def __eq__(self, other: object) -> bool:

        first = str(self)
        second = str(other)

        for i in range(len(first)):

            if first[i] != second[i]:
                return False

        return True

    def __str__(self):
        '''
        Represents message
        '''
        message = []

        for sentence in self:
            if sentence:
                message.append(sentence.text.replace('!', '.').replace(
                    '?', '.').replace('...', '.').replace('  ', ' '))

        return '. '.join(message) if len(message) > 0 else ''


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

    def __eq__(self, other: object) -> bool:

        first = str(self)
        second = str(other)

        for i in range(len(first)):

            if first[i] != second[i]:
                return False

        return True

    def __str__(self):
        """
        Represents sentence
        """
        return self.text
