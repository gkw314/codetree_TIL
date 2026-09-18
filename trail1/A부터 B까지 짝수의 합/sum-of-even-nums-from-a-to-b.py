A, B = map(int, input().split())

sum_i = 0



for i in range(A, B+1):
    if i % 2 == 0:
        sum_i += i
print(sum_i)