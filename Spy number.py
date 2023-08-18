n=int(input("enter the number= "))
k=n
s1=0
s2=1
while k>0:
    p=int(k%10)
    s1=s1+p
    s2=s2*p
    k=int(k/10)
if(s1==s2):
    print("spy number")
else:
    print("not spy number")