def partition(arr, l, h):
    pivot = arr[l]
    i = l
    j = h
    while(i < j):
        while(i <= h and arr[i] <= pivot):
            i = i+1
        while(arr[j] > pivot):
            j = j-1
        if i<j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[j], arr[l] = arr[l], arr[j]
    return j

def sort(arr, l, h):
    if l<h:
        pivot = partition(arr, l, h)
        sort(arr, l, pivot-1)
        sort(arr, pivot+1, h)
    return arr


arr = [4, 6, 2, 5, 7, 9, 1, 3]
print(sort(arr,0, len(arr)-1))
arr = [8, 8, 4, 0, 7, 2, 5, 4, 9, 2]
print(sort(arr,0, len(arr)-1))
arr = [3, 2]
print(sort(arr,0, len(arr)-1))