class MySoundex(object):
    max_code_length = 4
    not_a_digit = "*"
    empty_string = ""
    encodingsMap = dict({
        'b': '1', 'f': '1', 'p': '1', 'v': '1',
        'c': '2', 'g': '2', 'j': '2', 'k': '2', 'q': '2', 's': '2', 'x': '2', 'z': '2',
        'd': '3', 't': '3',
        'l': '4',
        'm': '5', 'n': '5',
        'r': '6'
    })

    def __init__(self):
        pass

    def encode(self, word):
        return self.__zero_pad(self.__upper_front(self.__head(word)) + self.__tail(self.__encoded_digits(word)))

    def encoded_digit(self, letter):
        lower_letter = self.__lower(letter)
        if lower_letter in self.encodingsMap:
            return self.encodingsMap[lower_letter]
        else:
            return self.not_a_digit

    def __encoded_digits(self, word):
        encoding = self.__encode_head(word)
        encoding += self.__encode_tail(encoding, word)
        return encoding

    def __encode_head(self, word):
        if len(word) is 0:
            return self.empty_string
        return self.encoded_digit(word[:1])

    def __encode_tail(self, encoding, word):
        word_length = len(word)
        for letter_index in range(1, word_length):
            if self.__is_complete(encoding) is False:
                encoding = self.__encode_letter(encoding, word[letter_index], word[letter_index - 1])

        return encoding

    def __encode_letter(self, encoding, letter, last_letter):
        digit = self.encoded_digit(letter)
        if digit != self.not_a_digit and (digit is not self.__last_digit(encoding) or self.__is_vowel(last_letter)):
            encoding += digit

        return encoding

    def __last_digit(self, encoding):
        encoding_len = len(encoding)
        if encoding_len is 0:
            return self.not_a_digit
        return encoding[encoding_len - 1]

    def __is_complete(self, encoding):
        return len(encoding) is self.max_code_length

    @staticmethod
    def __lower(character):
        return character.lower()

    @staticmethod
    def __upper_front(string):
        return string[0].upper()

    @staticmethod
    def __head(string):
        return string[0]

    def __tail(self, word):
        if len(word) < 1:
            return self.empty_string
        return word[1:]

    def __zero_pad(self, word):
        zeros_needed = self.max_code_length - len(word)

        for x in range(0, zeros_needed):
            word += "0"

        return word

    @staticmethod
    def __is_vowel(last_letter):
        return last_letter in "aeiouy"
