import random

random.seed(40)
random_numbers = [random.randint(0, 100) for _ in range(50)]

# Naive Sort:iterating and swapping
def naive_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

sorted_by_naive_sort = naive_sort(random_numbers.copy())

# Print the sorted numbers
print("Random Numbers:", random_numbers)
print("\nNaive Sort:", sorted_by_naive_sort)
