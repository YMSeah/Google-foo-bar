
# Author: Seah Yi-Min
# Date created: 13/01/2022

""" I simplify the problem by imagining reflections of the grid around the
original grid. That way, I can simply traverse into another grid instead
of dealing with rounding square-root/divisional errors associated with
reflections at non-integral coordinates.

In fact, I only need to take note of the coordinates of me and Commander Lambdas
elite bunny trainer (the enemy) for each grid. Then, I calculate the distance
and line associated with each match between my original position and myself or
the enemy that do not exceed the maximum distance. Each line is stored as a 
tuple (dx//g, dy//g) where g = gcd(dx, dy) instead of gradient (dx/dy) to avoid 
rounding errors and division by 0. For each line, find the person nearest to my
original position that lies on the line.

Note that lines are directed. i.e. (1, 0) != (-1, 0). Former goes left, latter
goes right.

There is a maximum of (2 points * (10000 dist / 2 min dist betw 2 pts on
different grids)^2 * 4 directions) points = O(200 million)"""

# from math import gcd # gcd not available on foobar -.-
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
from collections import defaultdict

def getDist(px, py, x, y):
    # distance from px, py to x, y
    return ((x - px) ** 2 + (y - py) ** 2) ** 0.5
def getDistSq(px, py, x, y):
    # distance from px, py to x, y
    return ((x - px) ** 2 + (y - py) ** 2)

        
def solution(dims, me, enemy, dist):
    n, m = dims
    xm, ym = me
    xe, ye = enemy
    
    # paste reflections of the grid around initial grid
    # consider all possible points. O(200,000,000)
    # Refer to each line with (dx//g, dy//g), where g = gcd(dx, dy)
    minDist = defaultdict(lambda:100005) # minDist[(dx//g, dy//g)] = minimumDist
    minDistOwner = dict() # store 1 if the nearest pt for this line is me, 0 if it's the enemy
    
    for xI, yI, person in ((xm, ym, 1), (xe, ye, 0)):
        for x in (xI, 2 * n - xI):
            while xm - (x - 2 * n) <= dist:
                x -= 2 * n
            
            while abs(xm - x) <= dist:
                for y in (yI, 2 * m - yI):
                    while getDistSq(xm, ym, x, y - 2 * m) <= dist * dist:
                        y -= 2 * m
                    # iterate y positively
                    while getDistSq(xm, ym, x, y) <= dist * dist:
                        d = getDist(xm, ym, x, y)
                        dx = x - xm; dy = y - ym
                        if not (dx == dy == 0):
                            g = gcd(abs(dx), abs(dy))
                            dx //= g; dy //= g
                            if d < minDist[(dx, dy)]:
                                minDist[(dx, dy)] = d
                                minDistOwner[(dx, dy)] = person
                        y += 2 * m
                x += 2 * n # iterate x positively
    ans = 0
    for v in minDistOwner.values():
        if v == 0:
            ans += 1
    return ans

def main():
    
    # SAMPLE TEST CASES
    
    q1 = [[3,2], [1,1], [2,1], 4] # 7
    q2 = [[300,275], [150,150], [185,100], 500] # 9
    
    assert solution(*q1) == 7
    assert solution(*q2) == 9
    
    return



import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ansArr):
    print('! {}'.format(' '.join([str(x) for x in ansArr])))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
import math
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()
