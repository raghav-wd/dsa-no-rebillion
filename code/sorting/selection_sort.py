def sort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min]):
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    print(arr)

arr = [6, 3, 8, 7, 6, 5, 8, 0, 0, 3]
sort(arr)
arr = [8, 8, 4, 0, 7, 2, 5, 4, 9, 2]
sort(arr)