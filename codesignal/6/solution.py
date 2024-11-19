def encode_rle(s):
    result = ''
    current_group_char = None
    current_group_length = 0
    if len(s) >= 500:
        print('Input string is to long')
    else:
        for char in s:
            if char.isdigit() or char.isalpha():
                if char == current_group_char:
                    current_group_length += 1
                else:
                    if current_group_char is not None:
                        result += current_group_char + str(current_group_length)
                    current_group_char = char
                    current_group_length = 1
        if current_group_char is not None:
            result += current_group_char + str(current_group_length)
        return result