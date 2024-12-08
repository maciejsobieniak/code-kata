def common_elements(listA, listB):
    result_list = []
    if len(listA) > 0 and len(listB) > 0:
        for i in range(len(listA)):
            if listA[i] in listB:
                result_list.append(listA[i])
    return result_list
