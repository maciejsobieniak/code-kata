def solution(sentence):
    result_output = ''
    words = sentence.split(' ')
    for word in words:
        if len(word) % 2 != 0:
            for i in range(0, len(word), 2):
                result_output += word[i]
    return result_output[::-1]