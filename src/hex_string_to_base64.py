from utils import to_hex_list

# Set 1 - problem 1

base64_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
mask = 0b111111

def to_base64_char(source_octets, offset, needs_pad=False):
    #grab 6 bytes from our source octets
    index = (source_octets >> (offset * 6)) & mask
    return base64_chars[index]

#Base64 takes 3 bytes in and converts to 4 bytes
#It takes 2 hex chars per byte so we need input in 
#multiples of 6.
def hex_string_to_base64(hex_str):
    base64_str = ''

    hex_list = to_hex_list(hex_str)

    for idx in range(0, len(hex_list), 3):
        print(idx)
        i = hex_list[idx]

        if idx + 1 < len(hex_list):
            j = hex_list[idx + 1]
            needs_pad_1 = False
        else:
            j = 0
            needs_pad_1 = True

        if idx + 2 < len(hex_list):
            k = hex_list[idx + 2]
            needs_pad_2 = False
        else:
            k = 0
            needs_pad_2 = True

        #grab 3 bytes at a time and add them all up
        source_octets = (i << 16) + (j << 8) + k

        #Convert the 3 octets to four base64 chars
        base64_str += to_base64_char(source_octets, 3) + \
                      to_base64_char(source_octets, 2) + \
                      ('=' if needs_pad_1 else to_base64_char(source_octets, 1)) + \
                      ('=' if needs_pad_2 else to_base64_char(source_octets, 0))

    return base64_str

    
if __name__ == '__main__':
    result = hex_string_to_base64('49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d')
    print(result)