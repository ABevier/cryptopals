
HEX_TO_INT_MAP = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7': 7, '8': 8,
    '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f':15
}

#Convert a hex string to actual hex digits.  It takes two chars in a hex string
#to represent a single hex number (0-255).  Each char is 4 bytes of the final digit
def to_hex_iterator(hex_str):
    for i in range(0, len(hex_str), 2):
        high = HEX_TO_INT_MAP[hex_str[i]]
        low = HEX_TO_INT_MAP[hex_str[i+1]]
        yield (high << 4) + low

#generators are cool and all but a list is nice too
def to_hex_list(hex_str):
    return list(to_hex_iterator(hex_str))

if __name__ == '__main__':
    iterator = to_hex_iterator('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    for digit in iterator:
        print(digit)