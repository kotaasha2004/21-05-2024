def depth(expression):
    token=list(expression)
    depth=0
    i=0
    while i<len(token):
        tokens=token[i]
        if tokens=="(":
            depth=depth+1
        elif tokens==")":
            if depth==0:
                return False
            depth=depth-1
        elif tokens.isdigit():
             if int(tokens)!=depth:
                    return False
        i=i+1
    return depth == 0
input_depth=input()
res=depth(input_depth)
print(res)
