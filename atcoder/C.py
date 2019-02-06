N, M = list(map(int, input().split()))
arr = list(map(int, input().split()))

arr.sort()

diff = [abs(b - a) for a, b in zip(arr, arr[1:])]

diff.sort()

print(sum(diff[:-(N-1)]))
