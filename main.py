from data_worker import data_worker
import sys
import bot


class Menu:
    def __init__(self):
        self.options = {'dm': self.download_messages,
                        'gp': self.get_percentage,
                        'ga': self.get_all_percentages,
                        'de': self.delete_emotion,
                        'se': self.extract_emotion,
                        'do': self.delete_old,
                        'ex': self.exit}

    def start(self):
        # chat_id = ""
        # while chat_id == "":
        #     chat_id = input("Enter your chat id to load messages: ")
        # print("Downloading...")
        self.welcome_message()
        while True:
            print('Menu: ',
                  '- Download messages: dm',
                  '- Get percentage of emotions: gp',
                  '- Get all percentages of emotions: ga',
                  '- Delete sentences with emotion: de',
                  '- Save sentences with emotion to file: se',
                  '- Delete old sentences [option in development]: do',
                  '- Exit: ex',
                  sep='\n')
            option = input('Enter action: ')
            if option in self.options:
                self.options[option]()

    def welcome_message(self):
        print("Welcome to Emotion Analyzer!")

    def download_messages(self):
        mess_limit = 0
        while mess_limit <= 0:
            try:
                mess_limit = int(input("Enter limit of messages to download: "))
            except:
                print("Enter correct number")
        bot.messages_limit = mess_limit
        bot.app.start()
        print("Go into target chat and send any message in it",
              "to download messages from this chat.",
              "Message will be deleted, but it can be still visible",
              "in users notifications.",
              "After message is sent send signal one time",
              "to stop application (e. g.: Ctr + C in terminal ",
              "or Ctr + F2 in PyCharm).",
              sep="\n")
        bot.idle_app()
        bot.app.stop()
        print("Loading to program...")
        data_worker.load_messages_to_adt(bot.loaded_messages)
        print('Loaded')

    def get_percentage(self):
        """Display percent of emotion to user"""
        emotion = self.choose_emotion()
        percentage = data_worker.chat_messages.get_percentage(emotion)
        print(f'Percentage of {emotion} is: {percentage}')

    def get_all_percentages(self):
        """Display percents of all emotions to user"""
        emotions = data_worker.get_emotions()
        # emotions_percentage = {}
        # for emotion in emotions:
        #     percentage = data_worker.chat_messages.get_percentage(emotion)
        #     emotions_percentage[emotion] = percentage
        emotions_percentage = ''
        for idx, emotion in enumerate(emotions):
            percentage = data_worker.chat_messages.get_percentage(emotion)
            emotions_percentage += f"{emotion.upper()}: {percentage}"
            if idx != len(emotions) - 1:
                emotions_percentage += "\n"

        print(f'All percentages of emotions:',
              f'{emotions_percentage}',
              sep="\n")

    def choose_emotion(self):
        """Allows user to choose emotion"""
        print('List of emotions: \n1. anger, \n2. fear, \n3. joy, '
              '\n4. analytical, \n5. confident, \n6. tentative,'
              '\n7. sadness')
        emotions = {1: 'anger',
                    2: 'fear',
                    3: 'joy',
                    4: 'analytical',
                    5: 'confident',
                    6: 'tentative',
                    7: 'sadness'
                    }
        while True:
            try:
                emotion_number = int(input('Enter number of emotion: '))
                if 1 <= emotion_number <= len(emotions.keys()):
                    emotion = emotions[emotion_number]
                    break
            except:
                print('Enter correct number of emotion')
        return emotion

    def choose_path(self):
        """Allows user to choose path to save"""
        path = input('Enter file path to save (default is filtered_mess.txt): ')
        return 'filtered_mess.txt' if path == '' else path

    def choose_period(self):
        period = input("Enter (in days) how old messages save: ")
        return period

    def delete_emotion(self):
        emotion = self.choose_emotion()
        data_worker.delete_emotion_messages(emotion)
        print('Deleted!')

    def extract_emotion(self):
        emotion = self.choose_emotion()
        path = self.choose_path()
        data_worker.save_emotion_messages(emotion, path)
        print('Saved')

    def delete_old(self):
        period = self.choose_period()
        pass

    def exit(self):
        print("Thanks for using EA today!")
        sys.exit()


if __name__ == "__main__":
    menu = Menu()
    menu.start()
