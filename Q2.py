def find_missing_number(array, n):
    total_sum = n * (n + 1) // 2
    arr_sum = sum(array)
    missing_number = total_sum - arr_sum
    return missing_number
array1 = [1, 2, 4, 5]
n = 5
print(f"Missing number: {find_missing_number(array1, n)}")
