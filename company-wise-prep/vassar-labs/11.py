def remove_duplicates_sorted(arr: list):
    temp = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr[temp] = arr[i]
            temp += 1
    return arr

print(remove_duplicates_sorted([0,0,1,1,1,2,2,3,3,4]))