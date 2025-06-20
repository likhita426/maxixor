n=int(input())
arr=list(map(int,input().split()))
maxi=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        maxi=max(maxi,arr[i]^arr[j])
print(maxi)        
        
    
  