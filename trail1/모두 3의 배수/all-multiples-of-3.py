arr = [int(input()) for _ in range(5)]

ans = 1
for i in arr:
    if i % 3 != 0:
        ans = 0
        break

print(ans)









