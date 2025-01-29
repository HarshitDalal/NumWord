from .english import ENGLISH
from .word_to_num import WordToNum

class GetLanguage:
    def get_language(self, language):
        if language == "en":
            return ENGLISH
        else:
            raise NotImplementedError(f"Language {language} is not supported.")