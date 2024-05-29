def Distinct_elements(array):
    new_set=set(array)
    new_list=list(new_set)
    sorted_list=sorted(new_list)
    head=0
    tail=len(sorted_list)-1
    result=[]
    turn=True
    while head<=tail:
        if turn:
            result.append(sorted_list[head])
            head +=1
        else:
            result.append(sorted_list[tail])
            tail -=1
        turn=not turn
    print(' '.join(map(str, result)))
input_arr=input().split()
input_arry=list(map(int, input_arr))
res=Distinct_elements(input_arry)
