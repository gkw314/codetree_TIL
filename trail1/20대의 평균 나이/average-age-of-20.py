
total_sum = 0
cnt = 0

while True:
    age = int(input())
    if age < 20 or age > 29:
        break
        
    total_sum += age
    cnt += 1

print(f"{total_sum / cnt:.2f}")