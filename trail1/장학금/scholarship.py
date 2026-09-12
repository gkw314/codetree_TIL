N, M = map(int, input().split())

if N >= 90 and M >= 95:
    print(100000)
elif N >= 90 and M >= 90:
    print(50000)
else:
    print(0)