"""
cypher sub class multiplicative
"""

import random
from cypher import Cypher
from receiver import Receiver
from sender import Sender


class Multiplicative(Cypher):
    """multiplicative class"""

    def encode(self, plain_text, senders_key):
        cypher_text = ''
        for char in plain_text:
            value = ord(char)-32
            encode_value = (value*senders_key) % 95
            cypher_text += chr(encode_value + 32)
        return cypher_text

    def decode(self, cypher_text, receivers_key):
        plain_text = ''
        for char in cypher_text:
            value = ord(char) - 32
            decode_value = (value*receivers_key) % 95
            plain_text += chr(decode_value + 32)
        return plain_text

    def generate_keys(self, sender, receiver):
        possible_key_combinations = [[2, 48], [48, 2], [3, 32], [32, 3],
                                     [4, 24], [24, 4], [8, 12], [12, 8],
                                     [16, 6], [6, 16]]
        keys = possible_key_combinations[random.randint(0, 9)]
        sender.set_key(keys[0])
        receiver.set_key(keys[1])

    def verify(self, plain_text):
        sender = Sender(self)
        receiver = Receiver(self)
        self.generate_keys(sender, receiver)
        cypher_text = self.encode(plain_text, sender.get_key())
        decoded_text = self.decode(cypher_text, receiver.get_key())
        if plain_text == decoded_text:
            return True
        return False
