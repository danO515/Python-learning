k = 5
for i in range (1,6):
    for k in range (i-1):
        print(" ", end = "")

    for j in range (6-i):
        print("*", end = "")

    print()
