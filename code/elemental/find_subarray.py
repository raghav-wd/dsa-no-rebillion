def subarray():
    arr = [2, 1, 2, 5, 4, 0, 6, 7, 2, 9, 2, 0]
    
    for l in range(0, len(arr)):
        for u in range(l+1, len(arr)):
            for i in range(l, u):
                print(arr[i], end=", ")
            print()

subarray()