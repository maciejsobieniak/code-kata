def spot_swaps(source: str, target: str) -> list:
    result_list = []
    for i in range(len(source) - 1):
        if source[i] == target[i + 1] and source[i + 1] == target[i]:
            result_list.append((i, source[i], source[i + 1]))
    return result_list
