N = int(input())

satisfied = True

if N <= 1:
    satisfied = False

for i in range(2, N):
    if N % i == 0:
        satisfied = False
        break

if satisfied == True:
    print("P")
else:
    print("C")