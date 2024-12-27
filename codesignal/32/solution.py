def solution(arrayA, arrayB):
    indexA, indexB, in_arrayA, result = 0, None, True, []
    while True:
        if in_arrayA:
            indexB = arrayA[indexA]
            if indexB not in result:
                result.append(indexB)
                indexA = arrayB[indexB - 1] - 1
            else:
                return result
        in_arrayA = not in_arrayA