"""
cypher sub class caesar
"""

import random
from cypher import Cypher
from receiver import Receiver
from sender import Sender


class Caesar(Cypher):
    """caesar class"""

    def encode(self, plain_text, senders_key):
        cypher_text = ''
        for char in plain_text:
            value = ord(char)-32
            encode_value = (value+senders_key) % 95
            cypher_text += chr(encode_value + 32)
        return cypher_text

    def decode(self, cypher_text, receivers_key):
        plain_text = ''
        for char in cypher_text:
            value = ord(char) - 32
            decode_value = (value+receivers_key) % 95
            plain_text += chr(decode_value + 32)
        return plain_text

    def generate_keys(self, sender, receiver):
        key = random.randint(0, 95)
        sender.set_key(key)
        receiver.set_key(95-key)

    def verify(self, plain_text):
        sender = Sender(self)
        receiver = Receiver(self)
        self.generate_keys(sender, receiver)
        cypher_text = self.encode(plain_text, sender.get_key())
        decoded_text = self.decode(cypher_text, receiver.get_key())
        if plain_text == decoded_text:
            return True
        return False
