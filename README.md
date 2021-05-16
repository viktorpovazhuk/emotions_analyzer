## Project name: Emotion analyzer


### Description:
---
The program is a telegram bot which analyzes messages in the chat and defines its specified emotional coloring.

The program can distinguish such emotions: anger, anticipation, disgust, fear, joy, sadness, surprise, trust, and neutrality and their percentage in message.

The main purpose of the program is to track the reaction of other people to messages and their mood in the telegram chats. You can see the percentage of possible emotions in the messages, delete messages with specified emotion and filter messages that correspond specified emotion.
### Input and output data:
---
The program gets messages from telegram chat and forms list of them.

The program returns string with information about emotion percentage in messages or file with mesagges that correspond specified emotion. It depends on user's choice.
### Structure:
---
1. bot.py - bot module
   - def create_application() - initialize app
   - def load_session_string() - load saved earlier session string from storage file
   - def save_session_string() - save session string to storage file
   - def download_chat_messages(_, msg) - download chat messages to loaded messages list
   - def idle_app() - idle app before chat is selected
2. ChatMessagesADT.py - necessary ADTs module
   - class ChatMessagesADT - generates ChatMessages object based on list filled with Message objects.
   - class MessageADT - generates Message object based on array filled with Sentence objects
   - class _MessageIterator - iterates through message's elements
   - class SentenceADT - generates Sentence object, receives a sentence as a text attribute.
   More about these classes and their methods you can read in wiki
3. data_worker.py - module to process data
    - class DataWorker - class to process data
       * def load_messages_to_adt(self, messages_text) - loads message to MessageADT
       * def save_emotion_messages(self, emotion, path) - saves messages thet correspond specified emotion in file
       * def delete_emotion_messages(self, emotion) - deletes messages which correspond specified emotion
       * def get_emotions(self) - returns list of possible emotions
4. main.py - main module with menu
   - class Menu - menu of the program
       * def start(self) - runs menu
       * def download_messages(self) - loads messages from telegram
       * def get_percentage(self) - returns information about percentage of emotion in messsages
       * def choose_emotion(self) - allows user to choose emotion
       * def choose_path(self) - Allows user to choose path to save
       * def delete_emotion(self) - deletes messages which correspond specified emotion
       * def extract_emotion(self) - ectracts messages which correspond specified emotion
       * def exit(self) - allows user to exit the program

### Installation: 
---
for Windows
```
$ git clone https://github.com/viktorpovazhuk/emotions_analyzer

$ cd C:\Users\user\path_to_project

$ pip install -r requirements.txt
```

### Usage: 
---
To use the program you need to install it.
Then in folder credentials you need to create file  with name config.ini
Insert the following code into this file
```
[pyrogram]
api_id = 12345
api_hash = 0123456789abcdef0123456789abcdef
```
Change given api id and api hash with your own telegram api id and api hash.

Run main.py.

You will be asked to enter action. Enter 'dm'.

Then enter number of messages you want to analyze.
```
Welcome to Emotion Analyzer!
Menu: 
- Download messages: dm
- Get percentage of emotions: gp
- Get all percentages of emotions: ga
- Delete sentences with emotion: de
- Save sentences with emotion to file: se
- Exit: ex
Enter action: dm
Enter limit of messages to download: 100 
```
Follow given instructions that will ask you to enter any message to telegram chat, messages which you want to analyze in.

Don't worry, the message will be immediately deleted. This is made only to choose the chat.

Then as the instructions say enter Ctr + C in terminal or Ctr + F2 in PyCharm.

It may take time to download.

Now you are ready to use it!

You can:
- Get percentage of emotions - you get string with percentage of specified emotion in the messages
- Get all percentages of emotions - you get string with percentages of all emotions that can be distinguished in the messages
- Delete sentences with emotion - deletes sentences with specified emotion
- Save sentences with emotion to file - you get file with messages that correspond specified emotion
### Example of usage:
---
These examples are based on developers' personal chat. You will have different percentages of the emotions
```
Enter action: ga
All percentages of emotions:
ANGER: 5.56
FEAR: 0.0
JOY: 16.67
ANALYTICAL: 16.67
CONFIDENT: 5.56
TENTATIVE: 0.0
SADNESS: 11.11
UNRECOGNIZED: 44.44
Menu:
- Download messages: dm
- Get percentage of emotions: gp
- Get all percentages of emotions: ga
- Delete sentences with emotion: de
- Save sentences with emotion to file: se
- Exit: ex
```
```
Enter action: gp
List of emotions:
1. anger
2. fear
3. joy
4. analytical
5. confident
6. tentative
7. sadness
8. unrecognized
Enter number of emotion: 1
Percentage of anger is: 5.56
```

### License:
---
MIT Licence
