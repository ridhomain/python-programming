### Write a function that takes year(integer) as an input and compute
### whether the given year is leap year or not

def exercise6(a):
    if a%4 ==0:
        if a%100 ==0:
            if a%400 ==0:
                return True
            else:
                return False
        else:
            return True            
    else:
        return False