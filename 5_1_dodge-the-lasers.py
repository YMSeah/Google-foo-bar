
# def getN2(n1): # Original Function that gave rounding errors
#     return int((pow(2, 0.5) - 1) * n1)

def getN2Calculator():
    # Find x where x = root(2) * pow(10, y), to use in calculating
    # n2 so as to avoid rounding errors.
    y = 1000
    target = 2 * pow(10, 2 * y)
    lo = -1
    hi = target
    while lo < hi:
        m = (lo + hi + 1) // 2
        if pow(m, 2) <= target:
            lo = m
        else:
            hi = m - 1
    x = lo
    # x is now root(2) * pow(10, y)
    multiple = x - 1 * pow(10, y)
    
    def n2Calculator(n1):
        temp = multiple * n1
        for _ in range(y):
            temp //= 10
        return temp
    
    return n2Calculator

def BeattySolve(n):
    # Using recursive solution of sum of Beatty sequence
    # https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s
    if n == 0: return 0
    if n == 1: return 1
    # n2Calculator = getN2Calculator()
    n1 = n; n2 = n2Calculator(n1)
    return n1 * n2 + (n1 * (n1 + 1)) // 2 - (n2 * (n2 + 1)) // 2 - BeattySolve(n2)

n2Calculator = getN2Calculator() # initialize as global variable to avoid recomputation

def solution(s):
    # Your code here
    n = int(s)
    ans = BeattySolve(n)
    return str(ans)
