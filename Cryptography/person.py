"""
super class person
"""

class Person():
    """person class"""
    key = None
    cypher_algorithm = ''

    def __init__(self, cypher_algorithm):
        """sets this persons algorithm"""
        self.cypher_algorithm = cypher_algorithm

    def set_key(self, key):
        """sets this persons key"""
        self.key = key

    def get_key(self):
        """returns this persons key"""
        return self.key

    def operate_cipher(self, text_input):
        """uses the cypher algorithm"""
