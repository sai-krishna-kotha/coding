# O(n**2) sorting algorithms (bubble, selection, insertion)
def bubble(arr: list) -> list:
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if arr[mini] > arr[j]:
                mini = j
        if mini != i:
            arr[mini], arr[i] = arr[i], arr[mini]
    return arr

def insertion(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
print(bubble([4,1,3,5,2]))
print(selection([4,1,3,5,2]))
print(insertion([4,1,3,5,2]))