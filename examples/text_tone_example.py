from text_tone import translate_to_en, detect_tone, json_to_tone


def demonstrate_analyzer():
    """
    Demonstrates how text_tone module works.
    """
    ukr = '''Лишилось тільки ще спакуватись... Се було одно з тих незчисленних "треба", \
    які мене так утомили і не давали спати. Дарма, чи те "треба" мале, чи велике, — \
    вагу те має, що кожен раз воно вимагає уваги, що не я їм, а воно мною уже керує. \
    Фактично стаєш невільником сього многоголового звіра. Хоч на час увільнитись \
    від нього, забути, спочити. Я утомився. '''

    print('Translating from Ukrainian to English...', end='\n\n')
    en = translate_to_en(ukr)

    output = detect_tone(ukr)
    print('Defining the tone of the message...', end='\n\n')
    print('Reading json file...', end='\n\n')

    print('-' * 30, end='\n')
    print("message's tone:", output)
    print('-' * 30, end='\n')
    print('\nOriginal text: \n\n', ukr)


if __name__ == '__main__':
    demonstrate_analyzer()
