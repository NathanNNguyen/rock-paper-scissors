def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            
bubbleSort([99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0])