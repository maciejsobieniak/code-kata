def solution(input_str):
    result = ''
    words = input_str.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    result = ' '.join(words)
    return result