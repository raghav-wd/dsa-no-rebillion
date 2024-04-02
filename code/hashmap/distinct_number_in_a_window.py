def __main__ ():
    arr = [1, 2, 2, 1, 3, 3, 1]
    k = 4
    storage = {}

    for i in range(0, k):
        storage[arr[i]] = storage.get(arr[i], 0) + 1

    print(storage, end=" Distincts are: ")
    print(len(storage))

    for i in range(k, len(arr)):
        storage[arr[i]] = storage.get(arr[i], 0) + 1

        if storage.get(arr[i-k]) == 1:
            storage.pop(arr[i-k])
        else:
            storage[arr[i-k]] = storage[arr[i-k]] - 1

        print(storage, end=" Distincts are: ")
        print(len(storage))

__main__()