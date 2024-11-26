import random

random.seed(40)
random_numbers = [random.randint(0, 100) for _ in range(50)]

# Merge Sort 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))
    sorted_array.extend(left or right)
    return sorted_array

sorted_by_merge_sort = merge_sort(random_numbers.copy())

# Print the sorted numbers
print("Random Numbers:", random_numbers)
print("\nMerge Sort:", sorted_by_merge_sort)
