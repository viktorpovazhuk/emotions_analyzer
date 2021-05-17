from ChatMessagesADT import ChatMessagesADT, MessageADT
from text_tone import detect_tone


class DataWorker:
    def __init__(self):
        self.chat_messages = ChatMessagesADT()

    def load_messages_to_adt(self, messages_text):
        """Load list of messages to ChatMessagesADT"""

        for message_text in messages_text:

            if message_text is None:
                continue
            try:
                message = MessageADT(message_text)

                for sentence in message:

                    emotion = detect_tone(sentence.text)
                    if not emotion:
                        emotion = 'unrecognized'
                    sentence.emotion = emotion

                self.chat_messages.add_message(message)

            except Exception as ex:
                print(ex)

    def save_emotion_messages(self, emotion, path):
        """Save sentences with particular
        emotion from messages to file"""
        filtered_messages = self.chat_messages.get_sentences(emotion)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(filtered_messages)

    def delete_and_save_emotion_messages(self, emotion, path):
        """Delete sentences with
        specified emotion from ChatMessagesADT and save deleted
        sentences"""
        deleted_messages = self.chat_messages.delete_sentences(emotion)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(deleted_messages)

    def delete_old_messages(self, save_period):
        """Delete messages that were written
        earlier than save_period from ChatMessagesADT"""
        pass

    def get_emotions(self):
        """Return list of emotions"""
        return list(self.chat_messages.emotions.keys())


data_worker = DataWorker()
