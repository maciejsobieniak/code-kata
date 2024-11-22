def solution(input_str):
    result = ''
    result_reversed = []
    list_char = []
    transform_word = ''
    words = input_str.split()
    for word in words:
        transform_word = ''
        for char in word:
            if char.isupper():
                transform_word += chr(ord('Z') + ord('A') - ord(char))
            else:
                transform_word += chr(ord('z') + ord('a') - ord(char))
        list_char.append(transform_word)

    if len(list_char) > 1:
        list_char = [list_char[-1]] + list_char[:-1]
        result = ' '.join(list_char)
    else:
        result = ''.join(list_char)

    return result