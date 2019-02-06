N = int(input().strip())
arr = list(map(int, input().split()))

if max(arr) * 2 - sum(arr) >= 0:
    print('No')
else:
    print('Yes')