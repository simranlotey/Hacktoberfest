def findingDuplicates(arr):
    tortoise = arr[0]
    hare = arr[arr[0]]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]

    hare = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return tortoise


arr = [2, 5, 3, 1, 0, 3]
ans = findingDuplicates(arr)
print(ans)
