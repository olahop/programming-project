"""
cypher sub class unbreakable
"""

import random
from cypher import Cypher

class Unbreakable(Cypher):
    """unbreakable class"""

    def encode(self, plain_text, senders_key):
        cypher_text = ''
        counter = 0
        for char in plain_text:
            moves = ord(senders_key[counter % (len(senders_key)-1)])-32
            encode_value = ((ord(char)-32) + moves) % 95
            cypher_text += chr(encode_value + 32)
            counter += 1
        return cypher_text

    def decode(self, cypher_text, receivers_key):
        plain_text = ''
        counter = 0
        for char in cypher_text:
            moves = ord(receivers_key[counter % (len(receivers_key)-1)]) - 32
            decode_value = ((ord(char) - 32) + moves) % 95
            plain_text += chr(decode_value + 32)
            counter += 1
        return plain_text

    def generate_keys(self, sender, receiver):
        file = open("english_words.txt", "r")
        word_nr = random.randint(0, 109582)
        counter = 0
        for word in file:
            if counter == word_nr:
                key = word
                break
            counter += 1
        file.close()
        sender.set_key(key)
        receivers_key = ''
        for char in key:
            char_value = (ord(char) - 32)
            receivers_key += chr(95 - char_value + 32)
        receiver.set_key(receivers_key)
