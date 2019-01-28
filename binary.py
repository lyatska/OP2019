def binary_search(lst,value):
    low = 0
    high = len(lst) -1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binary_search([1,32,3,5,7,8,95,3], 95))
