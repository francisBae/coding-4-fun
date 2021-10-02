import sys, random

rd = lambda : sys.stdin.readline()

N,M = map(int,rd().split())
arr = [""]*N
cntArr = [0]*N

for i in range(N):
    arr[i] = rd().strip()[2:]

print("==Result after "+str(M)+" iterations==")
for _ in range(M):
    cntArr[random.randrange(0,N)]+=1

maxNum = -1
maxIdx = -1

for i in range(N):
    print(i+1,end=') ')
    print(arr[i]+" : ",end='')
    print(cntArr[i]/M,end='%\n')

    if maxNum<cntArr[i]:
        maxNum = cntArr[i]
        maxIdx = i


print("\nvisit ",end='')
print(arr[maxIdx])
