n = int(input())

class_cnt = 0
floor_cnt = 0
bath_cnt = 0

for i in range(1, n + 1):

    if i % 12 == 0:
        bath_cnt += 1
    elif i % 3 == 0:
        floor_cnt += 1
    elif i % 2 == 0:
        class_cnt += 1

print(class_cnt, floor_cnt, bath_cnt)
