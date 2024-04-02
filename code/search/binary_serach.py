def search(arr, target):
    l = 0
    r = len(arr)-1
    i = 0
    while l<=r:
        mid = (l+r)//2
        # print(mid)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            l = mid+1
        if arr[mid] > target:
            r = mid-1
    return -1

arr = [0, 2, 2, 4, 4, 5, 7, 8, 8, 9]
print(search(arr, 9))
