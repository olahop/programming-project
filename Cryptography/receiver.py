"""
person sub class receiver class
"""

from person import Person


class Receiver(Person):
    """receiver class"""

    def operate_cipher(self, text_input):
        """decrypts cypher text"""
        plain_text = self.cypher_algorithm.decode(text_input, self.get_key())
        return plain_text
