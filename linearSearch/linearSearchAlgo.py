def iterative_linear(arr, n, key_element):
    for x in range(n):
        if arr[x] == key_element:
            return x
    return -1