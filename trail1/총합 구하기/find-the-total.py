A, B = map(int, input().split())

sum_i = 0
for i in range(A, B+1):
    if i % 6 == 0 and i % 8 != 0:
        sum_i += i
print(sum_i)