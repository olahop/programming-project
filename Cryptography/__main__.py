

from caesar import Caesar
from multiplicative import Multiplicative
from affine import Affine
from unbreakable import Unbreakable
from rsa import RSA
from sender import Sender
from receiver import Receiver
from hacker import Hacker


"""RSA
algorithm = RSA()
sender = Sender(algorithm)
receiver = Receiver(algorithm)
algorithm.generate_keys(sender, receiver)
print("Keys: " + str(sender.get_key()) + " and " + str(receiver.get_key()))
encrypted = sender.operate_cipher(word)
print("Encrypted: " + encrypted)
decrypted = receiver.operate_cipher(encrypted)
print("Decrypted: " + decrypted)
print("Verified: " + str(algorithm.verify("verify text")))

"""

#Unbreakable
algorithm = Unbreakable()
sender = Sender(algorithm)
receiver = Receiver(algorithm)
algorithm.generate_keys(sender, receiver)
print("Keys: " + str(sender.get_key()) + " and " + str(receiver.get_key()))
encrypted = sender.operate_cipher("hello world")
print("Encrypted: " + encrypted)
decrypted = receiver.operate_cipher(encrypted)
print("Decrypted: " + decrypted)
print("Verified: " + str(algorithm.verify("verify text")))
hacker = Hacker()
hacker_result = hacker.operate_cipher(encrypted)
print("Hacked: " + hacker_result)


"""Affine
algorithm = Affine()
sender = Sender(algorithm)
receiver = Receiver(algorithm)
algorithm.generate_keys(sender, receiver)
print("Keys: " + str(sender.get_key()) + " and " + str(receiver.get_key()))
encrypted = sender.operate_cipher("hello world")
print("Encrypted: " + encrypted)
decrypted = receiver.operate_cipher(encrypted)
print("Decrypted: " + decrypted)
print("Verified: " + str(algorithm.verify("verify text")))
hacker = Hacker()
hacker_result = hacker.operate_cipher(encrypted)
print("Hacked: " + hacker_result)
"""

"""Multiplicative
algorithm = Multiplicative()
sender = Sender(algorithm)
receiver = Receiver(algorithm)
algorithm.generate_keys(sender, receiver)
print("Keys: " + str(sender.get_key()) + " and " + str(receiver.get_key()))
encrypted = sender.operate_cipher("hello world")
print("Encrypted: " + encrypted)
decrypted = receiver.operate_cipher(encrypted)
print("Decrypted: " + decrypted)
print("Verified: " + str(algorithm.verify("verify text")))
hacker = Hacker()
hacker_result = hacker.operate_cipher(encrypted)
print("Hacked: " + hacker_result)
"""

"""Caesar
algorithm = Caesar()
sender = Sender(algorithm)
receiver = Receiver(algorithm)
algorithm.generate_keys(sender, receiver)
print("Keys: " + str(sender.get_key()) + " and " + str(receiver.get_key()))
encrypted = sender.operate_cipher("hello world")
print("Encrypted: " + encrypted)
decrypted = receiver.operate_cipher(encrypted)
print("Decrypted: " + decrypted)
print("Verified: " + str(algorithm.verify("verify text")))
hacker = Hacker()
hacker_result = hacker.operate_cipher(encrypted)
print("Hacked: " + hacker_result)
"""
