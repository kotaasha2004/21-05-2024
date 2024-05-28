def uniqueness(N,Z,array):
    if len(array)==len(set(array)):
        print("YES")
    else:
        print("NO")
    unique=len(set(array))
    if unique==Z:
        print("Good")
    elif unique<Z:
        print("Bad")
    else:
        print("Average")
n_z=input().split()
arr=input().split()
N_Z=list(map(int,n_z))
arry=list(map(int,arr))
res=uniqueness(N_Z[0],N_Z[1],arry)
