A, B = map(int, input().split())

mult_i = 1
for i in range(A, B+1):

    mult_i *= i

print(mult_i)