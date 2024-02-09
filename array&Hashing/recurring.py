arr = [1, 2, 3, 4, 5, 5, 43, 53, 432, 1, 4]

def recurring(arr):
    map = {}
    for n in arr:
        if map.get(n):
            return map[n]
        map[n] = n
    return None

print(recurring(arr))
