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

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  
        heapify(arr, i, 0)



print(merge_sort([4,1,3,5,2],0, 4))
print(quick_sort([4,1,3, 5, 2]))
print(quick_sort1([4,1,3,5,2], 0, 4))
arr = [4,1,3,5,2]
heap_sort(arr)
print(arr)