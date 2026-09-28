while True:

    arr = input().split()
    w = int(arr[0])
    h = int(arr[1])
    c = arr[2]

    print(w * h)

    if c == "C":
        break