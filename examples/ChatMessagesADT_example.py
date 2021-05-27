from ChatMessagesADT import ChatMessagesADT, MessageADT, SentenceADT
from pprint import pprint


def demonstrate_ADT():
    """
    Test module to see how ChatMessagesADT, MessageADT, SentenceADT
    work.
    """

    print('-' * 45, end='\n')
    s1 = SentenceADT('My dog is a cat... ', 'anger')
    print(
        f'Creating SentenceADT object:\n\n{s1}\nemotion:{s1.emotion}', end='\n\n')

    m1 = MessageADT('I love my dog. My dog is good! ')
    print('-' * 45, end='\n')
    print(f'MessageADT object before adding SentenceADT:\n\n{m1}')

    m1._add_sentence(s1)
    print('-' * 45, end='\n')
    print(f'\nMessageADT object after adding SentenceADT:\n\n{m1}')

    m2 = MessageADT('I hope it works. It should work! I hate it... ')
    chm1 = ChatMessagesADT([m1, m2])

    print('-' * 45, end='\n\n')
    print('Here are two following messages added to ChatMessagesADT:', end='\n\n')
    for elem in chm1:
        print(elem)

    print('\n'+'-' * 45, end='\n\n')
    print('Representation of emotions in chat before changes:', end='\n\n')
    pprint(chm1.emotions)
    print('-' * 45, end='\n\n')

    chm1.delete_sentences('anger')

    print('Representation of emotions in chat after changes:', end='\n\n')
    pprint(chm1.emotions)
    print('-' * 45, end='\n\n')
    print('Chat after filtering process:', end='\n\n')
    print(chm1)


if __name__ == '__main__':
    demonstrate_ADT()
