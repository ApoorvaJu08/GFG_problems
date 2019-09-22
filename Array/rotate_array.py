from collections import deque
for _ in range(int(input())):
    size = int(input())
    x = [int(x) for x in input().split()]
    d = int(input())
    x = x[d:] + x[:d] 
    print(x)