#container with most water
def container_with_most_water(arr: list):
    ans = 0
    left = 0
    right = len(arr)-1
    while left < right:
        ans = max(ans, min(arr[left], arr[right])* (right - left))
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return ans