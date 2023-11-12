from translate import Translator
from time import sleep
import string, unidecode, re

class TextManipulation:
    
    @staticmethod
    def normalizer(text: str) -> str: 
        text = unidecode.unidecode(text)
        text = re.sub('\n', '', text)
        text = TextManipulation.convert_to_lower(text)
        text = TextManipulation.remove_spaces_from_sides(text)
        text = TextManipulation.remove_scores(text)
        text = TextManipulation.translate_text_to_english(text)
        return text

    @staticmethod
    def convert_to_lower(text: str) -> str:
        return text.lower()

    @staticmethod
    def remove_spaces_from_sides(text: str) -> str:
        return text.strip()

    @staticmethod
    def remove_scores(text: str) -> str:
        scores = string.punctuation
        scores = scores.replace("'", "")
        return text.translate( str.maketrans( "", "", scores ) )
    
    @staticmethod
    def translate_text_to_english(text):
        translator = Translator(from_lang='pt', to_lang='en')
        text = translator.translate(text)
        sleep(2)
        return text