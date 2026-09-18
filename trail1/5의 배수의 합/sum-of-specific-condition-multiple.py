A, B = map(int, input().split())

sum_i = 0
start = min(A, B)
end = max(A, B)


for i in range(start, end+1):
    if i % 5 == 0:
        sum_i += i


print(sum_i)