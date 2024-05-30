def largest_even_number(s):
    digits=set(char for char in s if char.isdigit())
    if not digits:
        print("-1")
    evens=[d for d in digits if int(d)%2==0]
    odds=[d for d in digits if int(d)%2!=0]
    if not evens:
        print("-1")
    sorted_digits=sorted(digits, reverse=True)
    if int(sorted_digits[-1])%2!=0:
        smallest_even=min(evens, key=int)
        sorted_digits.remove(smallest_even)
        sorted_digits.append(smallest_even)
    print(''.join(sorted_digits))
input_string=input()
res=largest_even_number(input_string)
