def median(nums1 , nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    fin = nums1.union(nums2)
    fin = list(fin)
    fin.sort()
    n = len(fin)
    print(len(fin))
    if n % 2 == 0:
        return (fin[int(n/2)-1] + fin[int(n/2)])/2
    else:
        return fin[int((n+1)/2)-1]

print(median([1,3],[2]))
print(median([1,2],[3,4]))