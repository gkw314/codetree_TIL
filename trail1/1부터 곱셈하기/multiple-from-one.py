N = int(input())


multi_i=1

for i in range(1, 11):
    multi_i *= i
    if multi_i >= N:
        print(i)
        break

        
    
