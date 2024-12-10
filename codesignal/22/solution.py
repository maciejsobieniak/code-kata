def solution(listA, listB):
    result_output = []
    for i in range(len(listA)):
        for j in range(len(listB)):
            if listA[i] > listB[j]:
                if (listA[i], listB[j]) not in result_output:
                    result_output.append((listA[i], listB[j]))
    return result_output