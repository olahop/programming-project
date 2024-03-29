'''This file provides a few of the 'tricky' elements of the Morse Code project: those
involving setting up and reading from the serial port.  

IMPORTANT!! If you are a MAC user, you will need to modify the actual device code for 
your serial port in arduino_connect.py '''

import arduino_connect  # This is the key import so that you can access the serial port.


# Codes for the 5 signals sent to this level from the Arduino

_dot = 1
_dash = 2
_symbol_pause = 4
_word_pause = 5
_reset = None


# Morse Code Class
class morsecoder():

# Note: the codes for dot and dash coming to Python via the serial port are 1 and 2, respectively, since those were most
# convenient at the Arduino level. However, I've switched to 0 and 1 in this dictionary, since it is a lot easier to
# read.  So O = dot, 1 = dash in the _morse_codes dictionary below.  You will need to remember that when looking
# up letters and digits in this dictionary.

    _morse_codes = {'01':'a','1000':'b','1010':'c','100':'d','0':'e','0010':'f','110':'g','0000':'h','00':'i','0111':'j',
               '101':'k','0100':'l','11':'m','10':'n','111':'o','0110':'p','1101':'q','010':'r','000':'s','1':'t',
               '001':'u','0001':'v','011':'w','1001':'x','1011':'y','1100':'z','01111':'1','00111':'2','00011':'3',
               '00001':'4','00000':'5','10000':'6','11000':'7','11100':'8','11110':'9','11111':'0'}

    serial_port = ''
    current_symbol = ''
    current_word = ''

	# This is where you set up the connection to the serial port.
    def __init__(self,sport=True):
        if sport:
            self.serial_port = arduino_connect.basic_connect()
        self.reset()

    def reset(self):
        self.current_message = ''
        self.current_word = ''
        self.current_symbol = ''

    # This should receive an integer in range 1-4 from the Arduino via a serial port
    def read_one_signal(self,port=None):
        connection = port if port else self.serial_port
        while True:
            # Reads the input from the arduino serial connection
            data = connection.readline()
            if data:
                return data
                
    # The signal returned by the serial port is one (sometimes 2) bytes, that represent characters of a string.  So,
    # a 2 looks like this: b'2', which is one byte whose integer value is the ascii code 50 (ord('2') = 50).  The use
    # of function 'int' on the string converts it automatically.   But, due to latencies, the signal sometimes
    # consists of 2 ascii codes, hence the little for loop to cycle through each byte of the signal.


    # takes the signal as input and sorts which kind of message it is and how it should be prosessed
    def process_signal(self, signal):
        if (signal == 1 or signal == 2) :
            self.update_current_symbol(signal)
        elif signal == 4:
            self.handle_symbol_end()
        elif signal == 5:
            self.handle_word_end()

    # called if input is dot or dash to update current symbol
    def update_current_symbol(self, signal):
        self.current_symbol += str(signal-1)
        if(len(self.current_symbol) > 5):
            self.current_symbol = ''

    # called if there is a short break in input
    def handle_symbol_end(self):
        if self.current_symbol and (self.current_symbol in self._morse_codes):
            morse_symbol = self._morse_codes[self.current_symbol]
            self.update_current_word(morse_symbol)

    # called of a symbol is ended and the word needs to be updated
    def update_current_word(self, symbol):
        self.current_word += symbol
        print("Current word: " + self.current_word)
        self.current_symbol = ''

    # called if there is a longer break in input
    def handle_word_end(self):
        if(self.current_word):
            self.handle_symbol_end()
            print(self.current_word)
            self.current_word = ''

    # the listener for input from arduino
    def decoding_loop(self):
        while True:
            s = self.read_one_signal(self.serial_port)
            for byte in s:
                self.process_signal(int(byte))

    
''' To test if this is working, do the following in a Python command window:

> from morse_skeleton import *
> m = morsecoder()
> m.decoding_loop()

If your Arduino is currently running and hooked up to the serial port, then this
simple decoding loop will print the raw signals that the Arduino sends to
the serial port.  Each time you press (or release) your morse-code device, a signal should
appear in your Python window. In Python, these signals typically look like this:
 b'5' or b'1' or b'3', etc.
'''
