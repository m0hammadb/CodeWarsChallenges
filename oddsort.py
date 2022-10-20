def sort_array(source_array):
    for i in range(len(source_array)):
        if(source_array[i] % 2 != 0):
            for j in range(i,len(source_array)):
                if(source_array[j] % 2 != 0):
                    if(source_array[i] > source_array[j]):
                        source_array[i],source_array[j] = source_array[j],source_array[i]
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))
