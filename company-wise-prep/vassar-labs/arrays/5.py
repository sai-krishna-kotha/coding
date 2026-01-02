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

def quick_sort(arr: list):
    n = len(arr)
    if n <= 1:
        return arr
    pivot = arr.pop()
    lesser_arr = []
    greater_arr = []
    for ele in arr:
        if ele < pivot:
            lesser_arr.append(ele)
        else:
            greater_arr.append(ele)
    return quick_sort(lesser_arr) + [pivot] + quick_sort(greater_arr)

def partition(arr, start, end):
    n = len(arr)
    pivot_idx = start
    pivot = arr[start]
    while start < end:
        while arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[end], arr[start] = arr[start], arr[end]
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    return end
def quick_sort1(arr, start, end):
    if start < end:
        p1 = partition(arr, start, end)
        quick_sort1(arr, start, p1-1)
        quick_sort1(arr, p1+1, end)
    return arr

print(merge_sort([4,1,3,5,2],0, 4))
print(quick_sort([4,1,3, 5, 2]))
print(quick_sort1([4,1,3,5,2], 0, 4))