import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from pprint import pprint
from deep_translator import GoogleTranslator
import logging

logging.basicConfig(handlers=[logging.FileHandler(filename="text_tone.log",
                                                  encoding='utf-8')], level=logging.DEBUG)


def translate_to_en(text):
    """
    Thanslates the data to English for tone analyzis.
    """
    text = text.split('. ')
    to_en = []

    for sentence in text:
        if sentence:

            translated = GoogleTranslator(
                source='auto', target='en').translate(text=sentence)
            to_en.append(translated + '. ')

    return ''.join(to_en).replace('!.', '! ').replace('?.', '? ').replace('..', '. ')


def detect_tone(ukr_text):
    """
    Detects text's tone by using IBM tine analyzer.
    """
    api_key = 'Yy-P5OCreKDNC9ib2RARfMcU3CPEbybYrm5tKQGyp7w_'
    service_url = 'https://api.eu-gb.tone-analyzer.watson.cloud.ibm.com/' \
                  'instances/094eb0dc-d562-4a31-b130-1076bb4493bd'

    en_text = translate_to_en(ukr_text)
    authenticator = IAMAuthenticator(api_key)

    tone_analyzer = ToneAnalyzerV3(
        version='2017-09-21',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url(service_url)

    tone_analysis = tone_analyzer.tone(
        {'text': en_text},
        content_type='application/json'
    ).get_result()

    tone = None

    try:
        tone = json_to_tone(tone_analysis)

    except IndexError as ex:
        logging.error(f"Emotion wasn't found for text: "
                      f"{en_text} "
                      f"Original error: {str(ex)}")
    return tone


def json_to_tone(json_object):
    """
    Receives json and returns the tone of the sentence.
    """
    tone = json_object['document_tone']['tones'][0]

    return tone['tone_id']


if __name__ == '__main__':
    en = 'sad'
    result = detect_tone(en)
    print(result)
