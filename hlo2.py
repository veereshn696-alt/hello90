marks=int(input("enter marks :"))
if(marks>90) :
    print("grade A")
elif(marks>80) :
    print("grade B")
elif(marks>70) :
    print("grade C")
elif(marks>60) :
    print("grade D")
marks=[]
for i in range(1,6) :
    marks=int(input("enter subject marks :"))
    avg=sum(marks)/5
if(avg>=85) :
    print("grade A")
else :
    print("fail")