## Project name: Emotion analyzer


### Description
The program is a telegram bot which analyzes messages in the chat and defines its specified emotional coloring.

The program can distinguish such emotions: anger, anticipation, disgust, fear, joy, sadness, surprise, trust, and neutrality and their percentage in message

The main purpose of the program is to track the reaction of other people to messages in the group chats.
### Input and output data

### Structure
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
       * h
### Table of Contents: 

### Installation: 
for Windows
```
$ git clone https://github.com/viktorpovazhuk/emotions_analyzer

$ cd C:\Users\user\path_to_project

$ pip install -r requirements.txt
```

### Usage: 

### Description of test examples

### Contributing: 

### Credits: 

### License:
MIT Licence
