p1_N, p1_M = input().split()
p2_N, p2_M = input().split()
p3_N, p3_M = input().split()

p1_M= int(p1_M)
p2_M= int(p2_M)
p3_M= int(p3_M)

A = 0

if p1_N == 'Y' and p1_M >= 37:
    A += 1

if p2_N == 'Y' and p2_M >= 37:
    A += 1

if p3_N == 'Y' and p3_M >= 37:
    A += 1

if A >= 2:
    print('E')
else:
    print('N')