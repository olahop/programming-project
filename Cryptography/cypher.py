"""
super class cypher
"""


class Cypher():
    """cypher class"""

    def encode(self, plain_text, senders_key):
        """creates a coded encrypted message"""

    def decode(self, cypher_text, receivers_key):
        """decrypts the input message"""

    def verify(self, plain_text):
        """decodes the cypher text and compare it to the plain text"""

    def generate_keys(self, sender, receiver):
        """generates cypher keys to the sender and receiver"""
