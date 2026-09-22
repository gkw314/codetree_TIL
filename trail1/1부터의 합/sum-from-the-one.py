N = int(input())

sum_i = 0
for i in range(1, 101):
    sum_i += i

    if sum_i >= N:
        print(i)
        break
        
    
