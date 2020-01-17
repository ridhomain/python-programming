### Write a function named median which take 3 numbers and return the median

import statistics

def bigger(a,b):
    if a>b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger (a,bigger(b,c))

def exercise5(a,b,c):
    if biggest(a,b,c)==a:
        if b>c or b==c:
            return b
        else:
            return c    
    elif biggest(a,b,c)==b:
        if a>c or a==c:
            return a
        else:
            return c 
    else:
        if a>b or a==b:
            return a
        else:
            return b
