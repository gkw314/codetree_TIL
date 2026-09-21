A, B = map(int, input().split())

sum_i = 1
for i in range(1, B+1):
    if i % A == 0:
        sum_i *= i

print(sum_i)