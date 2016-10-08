import math, random ,timeit
from ADDS1 import *
from ADDS2 import *
from ADDS3 import *
from ADDS1VAR import *
from ADDS2VAR import *


def tadd (a,b,len,ADD):
    r="0"
    c=""
    for i in range(-1,-(len+1),-1):
        (c_tmp,r_tmp)=ADD(a[i],b[i])
        (c_tmp,r)=ADD(r,c_tmp)
        r=r if r!= '0' else r_tmp
        c=c_tmp+c
    if(r!="0"):
        c=r+c
    return c


def tfunc1():
    for a in "0123456789":
        for b in"0123456789":
            ADDS1(a,b)

def tfunc2():
    for a in "0123456789":
        for b in "0123456789":
            ADDS2(a,b)

def tfunc3():
    for a in "0123456789":
        for b in "0123456789":
            ADDS3(a,b)

for k in (1, 10, 100, 1000, 10000, 100000, 1000000) :
    a = str(random.getrandbits(k))
    b = str(random.getrandbits(k))
    l = min(len(a),len(b))
    timeit.timeit('tadd(a,b,l, ADDS1)', setup= "from __main__ import tadd, a, b, l,ADDS1", number=10 )

for k in (1, 10, 100, 1000, 10000, 100000, 1000000) :
    a = str(random.getrandbits(k))
    b = str(random.getrandbits(k))
    l = min(len(a),len(b))
    timeit.timeit('tadd(a,b,l, ADDS2)', setup= "from __main__ import tadd, a, b, l,ADDS2", number=10 

for k in (1, 10, 100, 1000, 10000, 100000, 1000000) :
    a = str(random.getrandbits(k))
    b = str(random.getrandbits(k))
    l = min(len(a),len(b))
    timeit.timeit('tadd(a,b,l, ADDS3)', setup= "from __main__ import tadd, a, b, l,ADDS3", number=10 )

timeit.timeit( 'tfunc1()', setup= "from __main__ import tfunc1", number=10000 )
timeit.timeit( 'tfunc2()', setup= "from __main__ import tfunc1", number=10000 )
timeit.timeit( 'tfunc3()', setup= "from __main__ import tfunc1", number=10000 )

tousChiffres="0123456789ABCDEF"
chiffres=tousChiffres[0:base]
def tfuncVar(ADD):
    for a in chiffres:
        for b in chiffres:
            ADD(a,b)

chiffres=tousChiffres[0:2]
timeit.timeit('tfuncVar(ADDS1B2)', setup= "from __main__ import tfuncVar,ADDS1B2", number=100)
timeit.timeit('tfuncVar(ADDS2B2)', setup= "from __main__ import tfuncVar,ADDS2B2", number=100)
timeit.timeit('tfuncVar(ADDS3B2)', setup= "from __main__ import tfuncVar,ADDS3B2", number=100)

chiffres=tousChiffres[0:3]
timeit.timeit('tfuncVar(ADDS1B3)', setup= "from __main__ import tfuncVar,ADDS1B3", number=100)
timeit.timeit('tfuncVar(ADDS2B3)', setup= "from __main__ import tfuncVar,ADDS2B3", number=100)
timeit.timeit('tfuncVar(ADDS3B3)', setup= "from __main__ import tfuncVar,ADDS3B3", number=100)
                  
chiffres=tousChiffres[0:4]
timeit.timeit('tfuncVar(ADDS1B4)', setup= "from __main__ import tfuncVar,ADDS1B4", number=100)
timeit.timeit('tfuncVar(ADDS2B4)', setup= "from __main__ import tfuncVar,ADDS2B4", number=100)
timeit.timeit('tfuncVar(ADDS3B4)', setup= "from __main__ import tfuncVar,ADDS3B4", number=100)
                  
chiffres=tousChiffres[0:5]
timeit.timeit('tfuncVar(ADDS1B5)', setup= "from __main__ import tfuncVar,ADDS1B5", number=100)
timeit.timeit('tfuncVar(ADDS2B5)', setup= "from __main__ import tfuncVar,ADDS2B5", number=100)
timeit.timeit('tfuncVar(ADDS3B5)', setup= "from __main__ import tfuncVar,ADDS3B5", number=100)

chiffres=tousChiffres[0:6]
timeit.timeit('tfuncVar(ADDS1B6)', setup= "from __main__ import tfuncVar,ADDS1B6", number=100)
timeit.timeit('tfuncVar(ADDS2B6)', setup= "from __main__ import tfuncVar,ADDS2B6", number=100)
timeit.timeit('tfuncVar(ADDS3B6)', setup= "from __main__ import tfuncVar,ADDS3B6", number=100)
                  
chiffres=tousChiffres[0:7]                 
timeit.timeit('tfuncVar(ADDS1B7)', setup= "from __main__ import tfuncVar,ADDS1B7", number=100)
timeit.timeit('tfuncVar(ADDS2B7)', setup= "from __main__ import tfuncVar,ADDS2B7", number=100)

chiffres=tousChiffres[0:8]
timeit.timeit('tfuncVar(ADDS1B8)', setup= "from __main__ import tfuncVar,ADDS1B8", number=100)
timeit.timeit('tfuncVar(ADDS2B28)', setup= "from __main__ import tfuncVar,ADDS2B8", number=100)
timeit.timeit('tfuncVar(ADDS3B28)', setup= "from __main__ import tfuncVar,ADDS3B8", number=100)
                  
chiffres=tousChiffres[0:9]
timeit.timeit('tfuncVar(ADDS1B9)', setup= "from __main__ import tfuncVar,ADDS1B9", number=100)
timeit.timeit('tfuncVar(ADDS2B9)', setup= "from __main__ import tfuncVar,ADDS2B9", number=100)
timeit.timeit('tfuncVar(ADDS3B9)', setup= "from __main__ import tfuncVar,ADDS3B9", number=100)
                  
chiffres=tousChiffres[0:10]
timeit.timeit('tfuncVar(ADDS1B10)', setup= "from __main__ import tfuncVar,ADDS1B10", number=100)
timeit.timeit('tfuncVar(ADDS2B10)', setup= "from __main__ import tfuncVar,ADDS2B10", number=100)
timeit.timeit('tfuncVar(ADDS3B10)', setup= "from __main__ import tfuncVar,ADDS3B10", number=100)
                  
chiffres=tousChiffres[0:11]
timeit.timeit('tfuncVar(ADDS1B11)', setup= "from __main__ import tfuncVar,ADDS1B11", number=100)
timeit.timeit('tfuncVar(ADDS2B11)', setup= "from __main__ import tfuncVar,ADDS2B11", number=100)

chiffres=tousChiffres[0:12]
timeit.timeit('tfuncVar(ADDS1B12)', setup= "from __main__ import tfuncVar,ADDS1B12", number=100)
timeit.timeit('tfuncVar(ADDS2B12)', setup= "from __main__ import tfuncVar,ADDS2B12", number=100)

chiffres=tousChiffres[0:13]
timeit.timeit('tfuncVar(ADDS1B13)', setup= "from __main__ import tfuncVar,ADDS1B13", number=100)
timeit.timeit('tfuncVar(ADDS2B13)', setup= "from __main__ import tfuncVar,ADDS2B13", number=100)

chiffres=tousChiffres[0:14]
timeit.timeit('tfuncVar(ADDS1B14)', setup= "from __main__ import tfuncVar,ADDS1B14", number=100)
timeit.timeit('tfuncVar(ADDS2B14)', setup= "from __main__ import tfuncVar,ADDS2B14", number=100)

chiffres=tousChiffres[0:15]
timeit.timeit('tfuncVar(ADDS1B15)', setup= "from __main__ import tfuncVar,ADDS1B15", number=100)
timeit.timeit('tfuncVar(ADDS2B2)', setup= "from __main__ import tfuncVar,ADDS2B15", number=100)

chiffres=tousChiffres[0:16]
timeit.timeit('tfuncVar(ADDS1B16)', setup= "from __main__ import tfuncVar,ADDS1B16", number=100)
timeit.timeit('tfuncVar(ADDS2B16)', setup= "from __main__ import tfuncVar,ADDS2B16", number=100)


        
        
