
def findMatrix(nums):
    nc = {}
    for i in set(nums):
        nc[i] = 0
    for n in nums:
        nc[n] += 1


    items = [list(x) for x in [*nc.items()]]
    print(items)
    ans = []
    while (len(items) != 0):
        row = []
        for i in range(len(items)):
            row.append(items[i][0])
            items[i][1] -= 1
        print(items)
        items = list(filter(lambda x: x[1]>0, items))
        ans.append(row)
        print(items)
    return ans

findMatrix([5,4,3,3,3,3])