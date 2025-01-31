from .english import ENGLISH_NUM_WORDS, ENGLISH_WORD_NUM


class GetLanguage:
    def get_language(self, language):
        if language == "en":
            return ENGLISH_WORD_NUM, ENGLISH_NUM_WORDS
        else:
            raise NotImplementedError(f"Language {language} is not supported.")
