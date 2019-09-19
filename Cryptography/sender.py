"""
person sub class sender class
"""

from person import Person

class Sender(Person):
    """sender class"""

    def operate_cipher(self, text_input):
        """encrypts plain text"""
        cypher_text = self.cypher_algorithm.encode(text_input, self.get_key())
        return cypher_text
