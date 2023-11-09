import string


class TextManipulation:
    
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