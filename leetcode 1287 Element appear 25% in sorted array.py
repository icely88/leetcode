import collections
arr = [1,2,2,6,6,6,6,7,10]
count=collections.Counter(arr)
max_count=max(count.values())
for x in count:
    if count[x]==max_count:
        print(x)
