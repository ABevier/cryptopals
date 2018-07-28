from utils import to_hex_list, digits_to_hex_str, hex_digits_to_ascii_str
from word_scoring import score_word

#set 1 - challenge 2
def fixed_xor_hex_str(hex_str1, hex_str2):
    hex_digits = fixed_xor(to_hex_list(hex_str1), to_hex_list(hex_str2))
    return digits_to_hex_str(hex_digits)


def fixed_xor(hex_list1, hex_list2):
    #assuming equal length
    result_digits = []
    for i in range(0, len(hex_list1)):
        result_digits.append(hex_list1[i] ^ hex_list2[i])

    return result_digits


#set 2 - challenge 3
def single_byte_xor_cipher(hex_str):
    input_list = to_hex_list(hex_str)

    max_score = 0
    best_word = ''

    for value in range(0, 255):
        value_list = [value] * len(input_list)  # list of single value repeated
        xor_digits = fixed_xor(input_list, value_list)
        word = hex_digits_to_ascii_str(xor_digits)
        score = score_word(word)

        print('{}-{}-{}'.format(chr(value), word, score))

        if score > max_score:
            max_score = score
            best_word = word

    return best_word


if __name__ == '__main__':
    #TODO: unit tests!!
    #shoudl produce - 746865206b696420646f6e277420706c6179
    #result = fixed_xor_hex_str('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')

    result = single_byte_xor_cipher('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    print(result)