
A=[]
while True:
    a=int(input('Enter number if less than zero the vector excluding the negative integer will be made final'))
    print(a)
    if a>=0:
        A.append(a)
    else:
        break

#Sort the vector in descending order

flag=True
print(A)
for i in range(0,len(A)):
    A.sort(reverse=True)
    print('Sorted')
    print(A)
    a=A[0]
    if a+1>=len(A):
        flag=False
        break
    A[0]=0
    for j in range(1,a+1):
        if A[j]>0:
            A[j]-=1
        else:
            flag=False
            A[j]-=1
    print('Decreased')
    print(A)
    if flag==False:
        break

for each in A:
    if each!=0:
        flag=False
if flag==False:
    print('The vector is not graphical')
else:
    print('The vector is graphical')