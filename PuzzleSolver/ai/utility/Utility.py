#utility file

def gcdcount(a, b):
    '''
    Find the gcd of a and b (with a >= b)
    '''
    if(a < b):
       t= b
       b=a
       a=t
    count = 1
    q,r = divmod(a,b)
    while r != 0:
        count = count + 1
        a = b
        b = r
        q,r = divmod(a,b)
    return count

