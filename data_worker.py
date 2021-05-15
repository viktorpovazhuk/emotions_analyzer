from ChatMessagesADT import ChatMessagesADT, MessageADT
from text_tone import detect_tone


class DataWorker:
    def __init__(self):
        self.chat_messages = ChatMessagesADT()

    def load_messages_to_adt(self, messages_text):

        for message_text in messages_text:

            if message_text is None:
                continue
            try:
                message = MessageADT(message_text)

                for sentence in message:

                    emotion = detect_tone(sentence.text)
                    if not emotion:
                        emotion == 'unrecognized'
                    sentence.emotion = emotion

                self.chat_messages.add_message(message)

            except Exception as ex:
                print(ex)

    def save_emotion_messages(self, emotion, path):
        # TODO: filter sentences with emotion == None
        filtered_messages = self.chat_messages.get_sentences(emotion)

        # lines = ''
        # for message in filtered_messages:
        #     lines += str(message)
        #     lines += '------------------------\n'

        with open(path, 'w', encoding='utf-8') as f:
            f.write(filtered_messages)

    def delete_emotion_messages(self, emotion):
        self.chat_messages = self.chat_messages.delete_sentences(emotion)
        # TODO: save deleted messages to file

    def delete_old_messages(self, save_period):
        pass

    def get_emotions(self):
        return list(self.chat_messages.emotions.keys())


data_worker = DataWorker()
