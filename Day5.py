#  Problem : Find the Leaders in an Array
def find_leaders(arr):
    n = len(arr)
    result = []
    max_from_right = float('-inf')
    seen = set()

    for i in range(n - 1, -1, -1):
        if arr[i] > max_from_right:
            if arr[i] not in seen:
                result.append(arr[i])
                seen.add(arr[i])
            max_from_right = arr[i]

    return result[::-1] 
