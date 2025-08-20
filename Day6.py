def find_zero_sum_subarrays(arr):
    prefix_sum = 0
    sum_map = {}  
    result = []
    sum_map[0] = [-1]

    for i, num in enumerate(arr):
        prefix_sum += num

        if prefix_sum in sum_map:
            for start_index in sum_map[prefix_sum]:
                result.append((start_index + 1, i))

        sum_map.setdefault(prefix_sum, []).append(i)

    return result
