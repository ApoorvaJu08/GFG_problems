def printPat(n):
    res=''
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            for k in range(i):
                res+= str(j)+" "
        res+="$"
    return res

for _ in range(int(input())):
    n = int(input())
    print(printPat(n))