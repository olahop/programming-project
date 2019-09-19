"""
cypher sub class affine
"""

import random
from cypher import Cypher
from caesar import Caesar
from multiplicative import Multiplicative
from sender import Sender
from receiver import Receiver


class Affine(Cypher):
    """affine class"""

    def encode(self, plain_text, senders_key):
        caesar = Caesar()
        multiplicative = Multiplicative()
        multiplicative_cyphered = multiplicative.encode(plain_text, senders_key[0])
        double_cyphered = caesar.encode(multiplicative_cyphered, senders_key[1])
        return double_cyphered

    def decode(self, cypher_text, receivers_key):
        caesar = Caesar()
        multiplicative = Multiplicative()
        multiplicative_cyphered = caesar.decode(cypher_text, receivers_key[1])
        plain_text = multiplicative.decode(multiplicative_cyphered, receivers_key[0])
        return plain_text

    def generate_keys(self, sender, receiver):
        key_combinations_multi = [[2, 48], [48, 2], [3, 32], [32, 3], [
            4, 24], [24, 4], [8, 12], [12, 8], [16, 6], [6, 16]]
        multi_key = key_combinations_multi[random.randint(0, 9)]
        caesar_key = random.randint(0, 95)
        sender.set_key([multi_key[0], caesar_key])
        receiver.set_key([multi_key[1], 95-caesar_key])

    def verify(self, plain_text):
        sender = Sender(self)
        receiver = Receiver(self)
        self.generate_keys(sender, receiver)
        cypher_text = self.encode(plain_text, sender.get_key())
        decoded_text = self.decode(cypher_text, receiver.get_key())
        if plain_text == decoded_text:
            return True
        return False
