def OTP(array):
    new_list=[]
    new=""
    for i in array:
        if i%2!=0:
            new=new+str(i*i)
    if len(new)<4:
        print("-1")
    else:
        print(new[0:4])
integer_input=input().split()
list_input=list(map(int, integer_input))
res=OTP(list_input)
