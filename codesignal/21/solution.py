def stringSearch(sourceArray, searchArray):
    result_output = []
    for i in range(len(sourceArray)):
        for j in range(len(searchArray)):
            if sourceArray[i][1] in searchArray[j][1]:
                if sourceArray[i][0] <= searchArray[j][0]:
                    result_output.append(sourceArray[i])
                    break
    return result_output