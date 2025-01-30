from utility import GetLanguage


class NumberToWord:
    def __init__(self, lang="en"):
        self.units = GetLanguage().get_language(lang)[1]["UNIT"]
        self.teens = GetLanguage().get_language(lang)[1]["TEENS"]
        self.tens = GetLanguage().get_language(lang)[1]["TENS"]
        self.thousands = GetLanguage().get_language(lang)[1]["THOUSANDS"]

    def convert_hundreds(self, number):
        if number > 99:
            return self.units[number // 100] + " hundred " + self.convert_tens(number % 100)
        else:
            return self.convert_tens(number)

    def convert_tens(self, number):
        if number < 10:
            return self.units[number]
        elif number < 20:
            return self.teens[number - 10]
        else:
            return self.tens[number // 10] + " " + self.units[number % 10]

    def convert_thousands(self, number):
        if number == 0:
            return ""
        elif number < 1000:
            return self.convert_hundreds(number).strip()
        else:
            for idx, word in enumerate(self.thousands):
                if number < 1000 ** (idx + 1):
                    return self.convert_thousands(number // (1000 ** idx)) + " " + self.thousands[idx] + " " + self.convert_thousands(number % (1000 ** idx))

    def convert_decimal(self, number):
        decimal_part = str(number).split(".")[1]
        decimal_words = " ".join(self.units[int(digit)] for digit in decimal_part)
        return "point " + decimal_words

    def convert(self, number):
        if number == 0:
            return "zero"
        elif number < 0:
            return "negative " + self.convert(-number)
        else:
            if "." in str(number):
                integer_part = int(str(number).split(".")[0])
                return self.convert_thousands(integer_part).strip() + " " + self.convert_decimal(number)
            else:
                return self.convert_thousands(number).strip()
