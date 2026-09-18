
sum_i = 0
cnt = 0

for _ in range(10):
    i = int(input())
    if 0 <= i <= 200:
        sum_i += i
        cnt += 1

avg_i = sum_i / cnt
print(f"{sum_i} {avg_i:.1f}")

