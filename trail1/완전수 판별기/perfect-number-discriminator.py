N = int(input())

sum_i = 0

for i in range(1, N):
    if N % i == 0:
        sum_i += i

if sum_i == N:
    print("P")
else:
    print("N")
