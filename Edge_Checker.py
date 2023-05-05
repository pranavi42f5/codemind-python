m,n=map(int,input().split())
if(n>0 and m>0):
    if n==m+1 or n==m-1 or n==10 or n==1 and m==1 or m==10:
        print("Yes")
    else:
        print("No")