import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0] *(n+1)

for i in range(n):
    t, p = arr[i]
    dp[i] = max(dp[i], dp[i-1])
    if i + t <=n :
        dp[i+t] = max(dp[i+t], dp[i]+p)
print(max(dp))