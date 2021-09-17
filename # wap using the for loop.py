# wap using the for loop

n=int(input("enter the no of rows:"))

for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end=" ")
    print()