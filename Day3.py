def find_duplicate(arr):
    low = 1
    high = len(arr) - 1 
    while low < high:
        mid = (low + high) // 2
      
        count = sum(num <= mid for num in arr)

        if count > mid:
            high = mid  
        else:
            low = mid + 1  
    return low
