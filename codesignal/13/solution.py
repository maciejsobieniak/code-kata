def solution(input_string):
    result = ''
    num = ''
    for i, char in enumerate(input_string):
        if char.isdigit():
            num += char
        elif num and char.isspace():
            continue
        elif num and char.isalpha():
            # Add the letter before the number
            result += char + num
            num = ''
        else:
            result += char
    return result