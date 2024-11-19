# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # Recursively split and sort
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merge sorted halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Input data
X = [1, 5, 6, 4, 3, 3, 7, 7, 9, 0, 1, 1, 3, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("X:", X)

merge_sorted_X = X.copy()  # Use a copy to avoid modifying original array
print("Merge Sort:", merge_sorted_X)

quick_sorted_X = quick_sort(X)  # Quick Sort returns a new array
print("Quick Sort:", quick_sorted_X)

#Analisis
#1. Merge Sort
#Base Case: Ketika array sudah terurut. Namun, karena Merge Sort tetap membagi array dan menggabungkannya tanpa memeriksa apakah array sudah terurut, maka kompleksitas best case juga O(n log n).
#Wosrt Case: Ketika membagi array menjadi dua bagian, mengerjakan pengurutan di masing-masing bagian, dan menggabungkan hasilnya tanpa memedulikan bagaimana data awal diatur. Tidak ada perubahan dalam langkah atau jumlah operasi yang dilakukan meskipun array sudah terurut, tidak terurut, atau dalam kondisi acak. memiliki kompleksitas worst case sebesar O(n log n). 
#Average Case: Karena proses pembagian dan penggabungan selalu sama untuk semua input (terlepas dari apakah array terurut atau tidak), worst case dan average case memiliki kompleksitas yang sama: O(n log n).

#2. Quick Sort
#Base Case: Ketika array sudah terurut. Namun, karena Merge Sort tetap membagi array dan menggabungkannya tanpa memeriksa apakah array sudah terurut, maka kompleksitas best case juga O(n log n).
#Worst Case: terjadi ketika pivot yang dipilih adalah elemen terkecil atau terbesar. Hal ini menyebabkan pembagian array menjadi tidak seimbang, misalnya satu bagian memiliki hampir semua elemen dan bagian lainnya kosong.Menghasilkan kompleksitas total O(n^2).
#average Case:  average case terjadi ketika pivot dipilih secara acak, sehingga membagi array menjadi dua bagian yang relatif seimbang dengan ukuran mendekati n/2. kompleksitas rata-rata Quick Sort adalah O(n log n).

