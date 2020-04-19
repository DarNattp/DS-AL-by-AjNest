def binarySearch(data, target, low, high):
    if low > high:
        return False
    else:        
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            return binarySearch(data, target, low, mid-1)
        else:
            return binarySearch(data, target, mid+1, high)

data = [1, 3, 4, 6, 8, 9, 11, 11, 22, 27, 33, 35, 36, 38, 44, 55, 66, 99, 111]
print(binarySearch(data, 9, 0, len(data)-1))
print(binarySearch(data, 23, 0, len(data)-1))
print(binarySearch(data, 66, 0, len(data)-1))
print(binarySearch(data, 3, 0, len(data)-1))