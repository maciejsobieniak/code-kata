import math

def solution(arr1, arr2):
    # TODO: Implement this function
    result_output = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] + arr2[j] >= 0:
                if math.sqrt(arr1[i] + arr2[j]).is_integer():
                    result_output.append((arr1[i], arr2[j]))
    return result_output