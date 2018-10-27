def diff21(n):
    '''Given an int n, return the absolute difference between n and 21,
     except return double the absolute difference if n is over 21. '''
    CHECK_NUMBER = 21
    return_val = (n - CHECK_NUMBER)

    if n > CHECK_NUMBER:
        return 2*(n - CHECK_NUMBER)
    else:
        return (CHECK_NUMBER - n)
