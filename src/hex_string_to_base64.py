# Set 1 - problem 1

hex_to_int_map = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6':6, '7': 7, '8': 8,
    '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f':15
}

base64_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

mask = 0b111111

#Two chars = 1 hex digit
#4 bytes are represented per char
#This dies if hex digits are odd - but that's fine
def extract_hex_digit(list, index):
    if(index >= len(list)):
        return 0

    high = hex_to_int_map[list[index]]
    low = hex_to_int_map[list[index+1]]
    return (high << 4) + low

def to_base64_char(source_octets, offset, needs_pad=False):
    #grab 6 bytes from our source octets
    index = (source_octets >> (offset * 6)) & mask
    if index == 0 and needs_pad:
        return '='
    else:
        return base64_chars[index]

#Base64 takes 3 bytes in and converts to 4 bytes
#It takes 2 hex chars per byte so we need input in 
#multiples of 6.
def hex_string_to_base64(input):
    result = ''
    for i in range(0, len(input), 6):
        needs_pad = i + 6 > len(input)

        #Grab 3 octects and add them all up
        source_octets = (extract_hex_digit(input, i) << 16) + \
                        (extract_hex_digit(input, i+2) << 8) + \
                        extract_hex_digit(input, i+4)

        #Convert the 3 octets to four base64 chars
        result += to_base64_char(source_octets, 3) + \
                to_base64_char(source_octets, 2) + \
                to_base64_char(source_octets, 1, needs_pad) + \
                to_base64_char(source_octets, 0, needs_pad)

    return result

    
if __name__ == '__main__':
    result = hex_string_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    print(result)