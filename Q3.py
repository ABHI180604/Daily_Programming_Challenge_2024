def findDuplicate(arr):
    array1 = arr[0]
    array2 = arr[0]
    while True:
        array1 = arr[array1]
        array2 = arr[arr[array2]]
        if array1 == array2:
            break
    array1 = arr[0]
    while array1 != array2:
        array1 = arr[array1]
        array2 = arr[array2]

    return array1

arr = [3, 1, 3, 4, 2]
print("Duplicate number:", findDuplicate(arr))
