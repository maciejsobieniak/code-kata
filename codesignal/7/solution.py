def solution(s):
    result = []
    current_group_char = None
    current_group_length = 0
    if len(s) > 500:
        print('Input string is to long')
    else:
        for char in s[::-1]: # u can use ''.join(reversed(s)
            if char == current_group_char:
                current_group_length += 1
            else:
                if current_group_char is not None:
                    result.append((current_group_char, current_group_length))
                    current_group_length = 1
                    current_group_char = char
                else:
                    current_group_length += 1
                    current_group_char = char
        if current_group_char is not None:
             result.append((current_group_char, current_group_length))
    return result