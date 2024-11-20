def solution(s):
    result = ''
    current_group_char = None
    current_group_length = 0
    if len(s) >= 500:
        print('Input string is to long')
    else:
        for i in range(0, len(s), 2):
            if s[i:i+2] == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    result += current_group_char + str(current_group_length)
                    current_group_char = s[i:i+2]
                    current_group_length = 1
                else:
                    current_group_char = s[i:i+2]
                    current_group_length = 1
        if current_group_char is not None:
            result += current_group_char + str(current_group_length)
    return result