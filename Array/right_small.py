n=int(input())
l=input()
lt=l.split()
newl=[]
for i in lt:
    newl.append(int(i))
    
output = []

i=n-2
output.append(newl[n-1])
sum=newl[n-1]
while i>=0:
    if newl[i]>=sum:
        output.append(newl[i])

from collections import deque
for _ in range(int(input())):
    size = int(input())
    x = [int(x) for x in input().split()]
    d = int(input())
    x = x[d:] + x[:d] 
    print(x)
    sum=newl[i]
    i=i-1
    
    output.reverse()
    for i in output:
        print(i,end=" ")
    print()    

    testcase=testcase-1


# for _ in range(int(input())):
#     size = int(input())
#     x = [int(x) for x in input().split()]
#     for i in range(0, size-1):
#         flag = 0
#         for j in range(i+1, size):
#             if x[j] > x[i]:
#                 flag = 1
#                 break
#         if flag == 0:
#             print(x[i], end = " ")
#     print(x[-1])
    