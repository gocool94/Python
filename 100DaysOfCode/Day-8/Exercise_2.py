def prime(num):
    count =0
    for i in range(2,int(num/2)+1):
        if(num%i==0):
            count+=1

    if(count>0):
        return ("Not prime")
    else:
        return ("prime")

for i in range(2,100):
    print(f"number {i} is {prime(i)}")
