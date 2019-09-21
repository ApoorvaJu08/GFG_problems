for _ in range(int(input())):
    size = int(input())
    x = [int(x) for x in input().split()]
    for i in range(0, size):
        if x[i+1] < x[i]:
            print(x[i+1], end = " ")
        else:
            print("-1")

#correction to be done