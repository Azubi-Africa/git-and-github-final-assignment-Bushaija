def iterative_linear(arr, n, key_element):
    for x in range(n):
        if arr[x] == key_element:
            return x
    return -1

arr = [2, 3, 5, 7, 9, 1, 4, 6, 8, 10]
max_size = len(arr)
key = 8
result = iterative_linear(arr, max_size - 1, key)

if result != -1:
    print("The element", key, "is found at index", result, "and in position", result + 1)
else:
    print("The element", key, "is not present in the given array")
