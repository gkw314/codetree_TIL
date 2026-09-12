P1_age, P1_sex = input().split()
P2_age, P2_sex = input().split()

P1_age = int(P1_age)
P2_age = int(P2_age)

if (P1_age >= 19 and P1_sex == 'M') or (P2_age >= 19 and P2_sex == 'M'):
    print(1)
else:
    print(0)