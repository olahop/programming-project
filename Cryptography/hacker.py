"""
person sub class hacker class
"""

from person import Person
from caesar import Caesar
from multiplicative import Multiplicative
from affine import Affine
from unbreakable import Unbreakable


class Hacker(Person):
    """hacker class"""

    def __init__(self):
        """init"""

    def operate_cipher(self, text_input):
        """tries to hack cyphered text with different approaches"""
        algorithm = Caesar()
        for key in range(0, 95):
            test_text = algorithm.decode(text_input, key)
            if evaluate_test(test_text):
                print("Caesar hack, receiver key: " + str(key))
                return test_text
        algorithm = Multiplicative()
        possible_receiver_keys = [2, 3, 4, 6, 8, 12, 16, 24, 32, 48]
        for key in possible_receiver_keys:
            test_text = algorithm.decode(text_input, key)
            if evaluate_test(test_text):
                print("Multiplicative hack, receiver key: " + str(key))
                return test_text
        algorithm = Affine()
        for multi_key in possible_receiver_keys:
            for caesar_key in range(0, 95):
                key = [multi_key, caesar_key]
                test_text = algorithm.decode(text_input, key)
                if evaluate_test(test_text):
                    print("Affine hack, receiver key: " + str(key))
                    return test_text
        algorithm = Unbreakable()
        file = open("english_words.txt", "r")
        for word in file:
            key = ''
            for char in word:
                char_value = (ord(char) - 32)
                key += chr(95 - char_value + 32)
            test_text = algorithm.decode(text_input, key)
            if evaluate_test(test_text):
                print("Unbreakable hack, receiver key: " + str(key))
                file.close()
                return test_text
        file.close()
        return "Don't know.."


def evaluate_test(test_text):
    """tests a text against file of English words"""
    test_words = test_text.split()
    for test_word in test_words:
        match = False
        file = open("english_words.txt", "r")
        for word in file:
            if word.strip() == test_word.strip():
                match = True
                file.close()
                break
        if not match:
            return False
    file.close()
    return True
