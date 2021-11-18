def flatten(array):
    if type(array[0]) != list:
        return array
    flattened_array = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            flattened_array.append(array[i][j])