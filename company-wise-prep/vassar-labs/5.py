# O(n log n) sorting algorithms (mergeSort, quickSort, heapSort) and min & max heap
def merge_sort(arr: list, low: int, high: int) -> list:
    if low < high:
        mid = (low + high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    return arr
def merge(arr: list, low: int, mid: int, high: int):
    i = low
    j = mid + 1
    merged = [0] * (high-low+1)
    k = 0
    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged[k] = arr[i]
            i += 1
        else:
            merged[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        merged[k] = arr[i]
        i += 1
        k += 1
    while j <= high:
        merged[k] = arr[j]
        j += 1
        k += 1
    for i in range(low, high+1):
        arr[i] = merged[i-low]

print(merge_sort([4,1,3,5,2],0, 4))