import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pprint import pprint
from deep_translator import GoogleTranslator


def translate_to_en(text):

    text = text.split('. ')
    to_en = []

    for sentence in text:
        if sentence:
            translated = GoogleTranslator(
                source='auto', target='en').translate(text=sentence)
            to_en.append(translated + '. ')

    return ''.join(to_en)


def detect_tone(text, api_key, service_url):
    authenticator = IAMAuthenticator(api_key)

    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url(service_url)

    tone_analysis = tone_analyzer.tone(
        {'text': text},
        content_type='application/json'
    ).get_result()

    return json.dumps(tone_analysis, indent=4)


ukr = '''Лишилось тільки ще спакуватись... Се було одно з тих незчисленних "треба", \
які мене так утомили і не давали спати. Дарма, чи те "треба" мале, чи велике, — \
вагу те має, що кожен раз воно вимагає уваги, що не я їм, а воно мною уже керує. \
Фактично стаєш невільником сього многоголового звіра. Хоч на час увільнитись \
від нього, забути, спочити. Я утомився. '''

en = translate_to_en(ukr)

output = detect_tone(en, 'Yy-P5OCreKDNC9ib2RARfMcU3CPEbybYrm5tKQGyp7w_',
                     'https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/instances/094eb0dc-d562-4a31-b130-1076bb4493bd')

print(output)
