def ADDS2B2 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B3 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B4 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B5 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B6 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B7 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B8 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B9 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B10 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B11 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
        if(b== 'A' ):
            return(  'A' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  'A' , '0' )
        if(b== 'A' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  'A' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
        if(b== 'A' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  'A' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
        if(b== 'A' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  'A' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
        if(b== 'A' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  'A' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
        if(b== 'A' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  'A' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
        if(b== 'A' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  'A' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
        if(b== 'A' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  'A' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
        if(b== 'A' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  'A' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
        if(b== 'A' ):
            return(  '8' , '1' )
    if(a== 'A' ):
        if(b== '0' ):
            return(  'A' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
        if(b== 'A' ):
            return(  '9' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B12 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
        if(b== 'A' ):
            return(  'A' , '0' )
        if(b== 'B' ):
            return(  'B' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  'A' , '0' )
        if(b== 'A' ):
            return(  'B' , '0' )
        if(b== 'B' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  'A' , '0' )
        if(b== '9' ):
            return(  'B' , '0' )
        if(b== 'A' ):
            return(  '0' , '1' )
        if(b== 'B' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  'A' , '0' )
        if(b== '8' ):
            return(  'B' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
        if(b== 'A' ):
            return(  '1' , '1' )
        if(b== 'B' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  'A' , '0' )
        if(b== '7' ):
            return(  'B' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
        if(b== 'A' ):
            return(  '2' , '1' )
        if(b== 'B' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  'A' , '0' )
        if(b== '6' ):
            return(  'B' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
        if(b== 'A' ):
            return(  '3' , '1' )
        if(b== 'B' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  'A' , '0' )
        if(b== '5' ):
            return(  'B' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
        if(b== 'A' ):
            return(  '4' , '1' )
        if(b== 'B' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  'A' , '0' )
        if(b== '4' ):
            return(  'B' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
        if(b== 'A' ):
            return(  '5' , '1' )
        if(b== 'B' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  'A' , '0' )
        if(b== '3' ):
            return(  'B' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
        if(b== 'A' ):
            return(  '6' , '1' )
        if(b== 'B' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  'A' , '0' )
        if(b== '2' ):
            return(  'B' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
        if(b== 'A' ):
            return(  '7' , '1' )
        if(b== 'B' ):
            return(  '8' , '1' )
    if(a== 'A' ):
        if(b== '0' ):
            return(  'A' , '0' )
        if(b== '1' ):
            return(  'B' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
        if(b== 'A' ):
            return(  '8' , '1' )
        if(b== 'B' ):
            return(  '9' , '1' )
    if(a== 'B' ):
        if(b== '0' ):
            return(  'B' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
        if(b== 'A' ):
            return(  '9' , '1' )
        if(b== 'B' ):
            return(  'A' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B13 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
        if(b== 'A' ):
            return(  'A' , '0' )
        if(b== 'B' ):
            return(  'B' , '0' )
        if(b== 'C' ):
            return(  'C' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  'A' , '0' )
        if(b== 'A' ):
            return(  'B' , '0' )
        if(b== 'B' ):
            return(  'C' , '0' )
        if(b== 'C' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  'A' , '0' )
        if(b== '9' ):
            return(  'B' , '0' )
        if(b== 'A' ):
            return(  'C' , '0' )
        if(b== 'B' ):
            return(  '0' , '1' )
        if(b== 'C' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  'A' , '0' )
        if(b== '8' ):
            return(  'B' , '0' )
        if(b== '9' ):
            return(  'C' , '0' )
        if(b== 'A' ):
            return(  '0' , '1' )
        if(b== 'B' ):
            return(  '1' , '1' )
        if(b== 'C' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  'A' , '0' )
        if(b== '7' ):
            return(  'B' , '0' )
        if(b== '8' ):
            return(  'C' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
        if(b== 'A' ):
            return(  '1' , '1' )
        if(b== 'B' ):
            return(  '2' , '1' )
        if(b== 'C' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  'A' , '0' )
        if(b== '6' ):
            return(  'B' , '0' )
        if(b== '7' ):
            return(  'C' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
        if(b== 'A' ):
            return(  '2' , '1' )
        if(b== 'B' ):
            return(  '3' , '1' )
        if(b== 'C' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  'A' , '0' )
        if(b== '5' ):
            return(  'B' , '0' )
        if(b== '6' ):
            return(  'C' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
        if(b== 'A' ):
            return(  '3' , '1' )
        if(b== 'B' ):
            return(  '4' , '1' )
        if(b== 'C' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  'A' , '0' )
        if(b== '4' ):
            return(  'B' , '0' )
        if(b== '5' ):
            return(  'C' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
        if(b== 'A' ):
            return(  '4' , '1' )
        if(b== 'B' ):
            return(  '5' , '1' )
        if(b== 'C' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  'A' , '0' )
        if(b== '3' ):
            return(  'B' , '0' )
        if(b== '4' ):
            return(  'C' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
        if(b== 'A' ):
            return(  '5' , '1' )
        if(b== 'B' ):
            return(  '6' , '1' )
        if(b== 'C' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  'A' , '0' )
        if(b== '2' ):
            return(  'B' , '0' )
        if(b== '3' ):
            return(  'C' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
        if(b== 'A' ):
            return(  '6' , '1' )
        if(b== 'B' ):
            return(  '7' , '1' )
        if(b== 'C' ):
            return(  '8' , '1' )
    if(a== 'A' ):
        if(b== '0' ):
            return(  'A' , '0' )
        if(b== '1' ):
            return(  'B' , '0' )
        if(b== '2' ):
            return(  'C' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
        if(b== 'A' ):
            return(  '7' , '1' )
        if(b== 'B' ):
            return(  '8' , '1' )
        if(b== 'C' ):
            return(  '9' , '1' )
    if(a== 'B' ):
        if(b== '0' ):
            return(  'B' , '0' )
        if(b== '1' ):
            return(  'C' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
        if(b== 'A' ):
            return(  '8' , '1' )
        if(b== 'B' ):
            return(  '9' , '1' )
        if(b== 'C' ):
            return(  'A' , '1' )
    if(a== 'C' ):
        if(b== '0' ):
            return(  'C' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
        if(b== 'A' ):
            return(  '9' , '1' )
        if(b== 'B' ):
            return(  'A' , '1' )
        if(b== 'C' ):
            return(  'B' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B14 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
        if(b== 'A' ):
            return(  'A' , '0' )
        if(b== 'B' ):
            return(  'B' , '0' )
        if(b== 'C' ):
            return(  'C' , '0' )
        if(b== 'D' ):
            return(  'D' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  'A' , '0' )
        if(b== 'A' ):
            return(  'B' , '0' )
        if(b== 'B' ):
            return(  'C' , '0' )
        if(b== 'C' ):
            return(  'D' , '0' )
        if(b== 'D' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  'A' , '0' )
        if(b== '9' ):
            return(  'B' , '0' )
        if(b== 'A' ):
            return(  'C' , '0' )
        if(b== 'B' ):
            return(  'D' , '0' )
        if(b== 'C' ):
            return(  '0' , '1' )
        if(b== 'D' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  'A' , '0' )
        if(b== '8' ):
            return(  'B' , '0' )
        if(b== '9' ):
            return(  'C' , '0' )
        if(b== 'A' ):
            return(  'D' , '0' )
        if(b== 'B' ):
            return(  '0' , '1' )
        if(b== 'C' ):
            return(  '1' , '1' )
        if(b== 'D' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  'A' , '0' )
        if(b== '7' ):
            return(  'B' , '0' )
        if(b== '8' ):
            return(  'C' , '0' )
        if(b== '9' ):
            return(  'D' , '0' )
        if(b== 'A' ):
            return(  '0' , '1' )
        if(b== 'B' ):
            return(  '1' , '1' )
        if(b== 'C' ):
            return(  '2' , '1' )
        if(b== 'D' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  'A' , '0' )
        if(b== '6' ):
            return(  'B' , '0' )
        if(b== '7' ):
            return(  'C' , '0' )
        if(b== '8' ):
            return(  'D' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
        if(b== 'A' ):
            return(  '1' , '1' )
        if(b== 'B' ):
            return(  '2' , '1' )
        if(b== 'C' ):
            return(  '3' , '1' )
        if(b== 'D' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  'A' , '0' )
        if(b== '5' ):
            return(  'B' , '0' )
        if(b== '6' ):
            return(  'C' , '0' )
        if(b== '7' ):
            return(  'D' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
        if(b== 'A' ):
            return(  '2' , '1' )
        if(b== 'B' ):
            return(  '3' , '1' )
        if(b== 'C' ):
            return(  '4' , '1' )
        if(b== 'D' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  'A' , '0' )
        if(b== '4' ):
            return(  'B' , '0' )
        if(b== '5' ):
            return(  'C' , '0' )
        if(b== '6' ):
            return(  'D' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
        if(b== 'A' ):
            return(  '3' , '1' )
        if(b== 'B' ):
            return(  '4' , '1' )
        if(b== 'C' ):
            return(  '5' , '1' )
        if(b== 'D' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  'A' , '0' )
        if(b== '3' ):
            return(  'B' , '0' )
        if(b== '4' ):
            return(  'C' , '0' )
        if(b== '5' ):
            return(  'D' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
        if(b== 'A' ):
            return(  '4' , '1' )
        if(b== 'B' ):
            return(  '5' , '1' )
        if(b== 'C' ):
            return(  '6' , '1' )
        if(b== 'D' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  'A' , '0' )
        if(b== '2' ):
            return(  'B' , '0' )
        if(b== '3' ):
            return(  'C' , '0' )
        if(b== '4' ):
            return(  'D' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
        if(b== 'A' ):
            return(  '5' , '1' )
        if(b== 'B' ):
            return(  '6' , '1' )
        if(b== 'C' ):
            return(  '7' , '1' )
        if(b== 'D' ):
            return(  '8' , '1' )
    if(a== 'A' ):
        if(b== '0' ):
            return(  'A' , '0' )
        if(b== '1' ):
            return(  'B' , '0' )
        if(b== '2' ):
            return(  'C' , '0' )
        if(b== '3' ):
            return(  'D' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
        if(b== 'A' ):
            return(  '6' , '1' )
        if(b== 'B' ):
            return(  '7' , '1' )
        if(b== 'C' ):
            return(  '8' , '1' )
        if(b== 'D' ):
            return(  '9' , '1' )
    if(a== 'B' ):
        if(b== '0' ):
            return(  'B' , '0' )
        if(b== '1' ):
            return(  'C' , '0' )
        if(b== '2' ):
            return(  'D' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
        if(b== 'A' ):
            return(  '7' , '1' )
        if(b== 'B' ):
            return(  '8' , '1' )
        if(b== 'C' ):
            return(  '9' , '1' )
        if(b== 'D' ):
            return(  'A' , '1' )
    if(a== 'C' ):
        if(b== '0' ):
            return(  'C' , '0' )
        if(b== '1' ):
            return(  'D' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
        if(b== 'A' ):
            return(  '8' , '1' )
        if(b== 'B' ):
            return(  '9' , '1' )
        if(b== 'C' ):
            return(  'A' , '1' )
        if(b== 'D' ):
            return(  'B' , '1' )
    if(a== 'D' ):
        if(b== '0' ):
            return(  'D' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
        if(b== 'A' ):
            return(  '9' , '1' )
        if(b== 'B' ):
            return(  'A' , '1' )
        if(b== 'C' ):
            return(  'B' , '1' )
        if(b== 'D' ):
            return(  'C' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B15 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
        if(b== 'A' ):
            return(  'A' , '0' )
        if(b== 'B' ):
            return(  'B' , '0' )
        if(b== 'C' ):
            return(  'C' , '0' )
        if(b== 'D' ):
            return(  'D' , '0' )
        if(b== 'E' ):
            return(  'E' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  'A' , '0' )
        if(b== 'A' ):
            return(  'B' , '0' )
        if(b== 'B' ):
            return(  'C' , '0' )
        if(b== 'C' ):
            return(  'D' , '0' )
        if(b== 'D' ):
            return(  'E' , '0' )
        if(b== 'E' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  'A' , '0' )
        if(b== '9' ):
            return(  'B' , '0' )
        if(b== 'A' ):
            return(  'C' , '0' )
        if(b== 'B' ):
            return(  'D' , '0' )
        if(b== 'C' ):
            return(  'E' , '0' )
        if(b== 'D' ):
            return(  '0' , '1' )
        if(b== 'E' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  'A' , '0' )
        if(b== '8' ):
            return(  'B' , '0' )
        if(b== '9' ):
            return(  'C' , '0' )
        if(b== 'A' ):
            return(  'D' , '0' )
        if(b== 'B' ):
            return(  'E' , '0' )
        if(b== 'C' ):
            return(  '0' , '1' )
        if(b== 'D' ):
            return(  '1' , '1' )
        if(b== 'E' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  'A' , '0' )
        if(b== '7' ):
            return(  'B' , '0' )
        if(b== '8' ):
            return(  'C' , '0' )
        if(b== '9' ):
            return(  'D' , '0' )
        if(b== 'A' ):
            return(  'E' , '0' )
        if(b== 'B' ):
            return(  '0' , '1' )
        if(b== 'C' ):
            return(  '1' , '1' )
        if(b== 'D' ):
            return(  '2' , '1' )
        if(b== 'E' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  'A' , '0' )
        if(b== '6' ):
            return(  'B' , '0' )
        if(b== '7' ):
            return(  'C' , '0' )
        if(b== '8' ):
            return(  'D' , '0' )
        if(b== '9' ):
            return(  'E' , '0' )
        if(b== 'A' ):
            return(  '0' , '1' )
        if(b== 'B' ):
            return(  '1' , '1' )
        if(b== 'C' ):
            return(  '2' , '1' )
        if(b== 'D' ):
            return(  '3' , '1' )
        if(b== 'E' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  'A' , '0' )
        if(b== '5' ):
            return(  'B' , '0' )
        if(b== '6' ):
            return(  'C' , '0' )
        if(b== '7' ):
            return(  'D' , '0' )
        if(b== '8' ):
            return(  'E' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
        if(b== 'A' ):
            return(  '1' , '1' )
        if(b== 'B' ):
            return(  '2' , '1' )
        if(b== 'C' ):
            return(  '3' , '1' )
        if(b== 'D' ):
            return(  '4' , '1' )
        if(b== 'E' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  'A' , '0' )
        if(b== '4' ):
            return(  'B' , '0' )
        if(b== '5' ):
            return(  'C' , '0' )
        if(b== '6' ):
            return(  'D' , '0' )
        if(b== '7' ):
            return(  'E' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
        if(b== 'A' ):
            return(  '2' , '1' )
        if(b== 'B' ):
            return(  '3' , '1' )
        if(b== 'C' ):
            return(  '4' , '1' )
        if(b== 'D' ):
            return(  '5' , '1' )
        if(b== 'E' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  'A' , '0' )
        if(b== '3' ):
            return(  'B' , '0' )
        if(b== '4' ):
            return(  'C' , '0' )
        if(b== '5' ):
            return(  'D' , '0' )
        if(b== '6' ):
            return(  'E' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
        if(b== 'A' ):
            return(  '3' , '1' )
        if(b== 'B' ):
            return(  '4' , '1' )
        if(b== 'C' ):
            return(  '5' , '1' )
        if(b== 'D' ):
            return(  '6' , '1' )
        if(b== 'E' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  'A' , '0' )
        if(b== '2' ):
            return(  'B' , '0' )
        if(b== '3' ):
            return(  'C' , '0' )
        if(b== '4' ):
            return(  'D' , '0' )
        if(b== '5' ):
            return(  'E' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
        if(b== 'A' ):
            return(  '4' , '1' )
        if(b== 'B' ):
            return(  '5' , '1' )
        if(b== 'C' ):
            return(  '6' , '1' )
        if(b== 'D' ):
            return(  '7' , '1' )
        if(b== 'E' ):
            return(  '8' , '1' )
    if(a== 'A' ):
        if(b== '0' ):
            return(  'A' , '0' )
        if(b== '1' ):
            return(  'B' , '0' )
        if(b== '2' ):
            return(  'C' , '0' )
        if(b== '3' ):
            return(  'D' , '0' )
        if(b== '4' ):
            return(  'E' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
        if(b== 'A' ):
            return(  '5' , '1' )
        if(b== 'B' ):
            return(  '6' , '1' )
        if(b== 'C' ):
            return(  '7' , '1' )
        if(b== 'D' ):
            return(  '8' , '1' )
        if(b== 'E' ):
            return(  '9' , '1' )
    if(a== 'B' ):
        if(b== '0' ):
            return(  'B' , '0' )
        if(b== '1' ):
            return(  'C' , '0' )
        if(b== '2' ):
            return(  'D' , '0' )
        if(b== '3' ):
            return(  'E' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
        if(b== 'A' ):
            return(  '6' , '1' )
        if(b== 'B' ):
            return(  '7' , '1' )
        if(b== 'C' ):
            return(  '8' , '1' )
        if(b== 'D' ):
            return(  '9' , '1' )
        if(b== 'E' ):
            return(  'A' , '1' )
    if(a== 'C' ):
        if(b== '0' ):
            return(  'C' , '0' )
        if(b== '1' ):
            return(  'D' , '0' )
        if(b== '2' ):
            return(  'E' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
        if(b== 'A' ):
            return(  '7' , '1' )
        if(b== 'B' ):
            return(  '8' , '1' )
        if(b== 'C' ):
            return(  '9' , '1' )
        if(b== 'D' ):
            return(  'A' , '1' )
        if(b== 'E' ):
            return(  'B' , '1' )
    if(a== 'D' ):
        if(b== '0' ):
            return(  'D' , '0' )
        if(b== '1' ):
            return(  'E' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
        if(b== 'A' ):
            return(  '8' , '1' )
        if(b== 'B' ):
            return(  '9' , '1' )
        if(b== 'C' ):
            return(  'A' , '1' )
        if(b== 'D' ):
            return(  'B' , '1' )
        if(b== 'E' ):
            return(  'C' , '1' )
    if(a== 'E' ):
        if(b== '0' ):
            return(  'E' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
        if(b== 'A' ):
            return(  '9' , '1' )
        if(b== 'B' ):
            return(  'A' , '1' )
        if(b== 'C' ):
            return(  'B' , '1' )
        if(b== 'D' ):
            return(  'C' , '1' )
        if(b== 'E' ):
            return(  'D' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
def ADDS2B16 (a,b):
    if(a== '0' ):
        if(b== '0' ):
            return(  '0' , '0' )
        if(b== '1' ):
            return(  '1' , '0' )
        if(b== '2' ):
            return(  '2' , '0' )
        if(b== '3' ):
            return(  '3' , '0' )
        if(b== '4' ):
            return(  '4' , '0' )
        if(b== '5' ):
            return(  '5' , '0' )
        if(b== '6' ):
            return(  '6' , '0' )
        if(b== '7' ):
            return(  '7' , '0' )
        if(b== '8' ):
            return(  '8' , '0' )
        if(b== '9' ):
            return(  '9' , '0' )
        if(b== 'A' ):
            return(  'A' , '0' )
        if(b== 'B' ):
            return(  'B' , '0' )
        if(b== 'C' ):
            return(  'C' , '0' )
        if(b== 'D' ):
            return(  'D' , '0' )
        if(b== 'E' ):
            return(  'E' , '0' )
        if(b== 'F' ):
            return(  'F' , '0' )
    if(a== '1' ):
        if(b== '0' ):
            return(  '1' , '0' )
        if(b== '1' ):
            return(  '2' , '0' )
        if(b== '2' ):
            return(  '3' , '0' )
        if(b== '3' ):
            return(  '4' , '0' )
        if(b== '4' ):
            return(  '5' , '0' )
        if(b== '5' ):
            return(  '6' , '0' )
        if(b== '6' ):
            return(  '7' , '0' )
        if(b== '7' ):
            return(  '8' , '0' )
        if(b== '8' ):
            return(  '9' , '0' )
        if(b== '9' ):
            return(  'A' , '0' )
        if(b== 'A' ):
            return(  'B' , '0' )
        if(b== 'B' ):
            return(  'C' , '0' )
        if(b== 'C' ):
            return(  'D' , '0' )
        if(b== 'D' ):
            return(  'E' , '0' )
        if(b== 'E' ):
            return(  'F' , '0' )
        if(b== 'F' ):
            return(  '0' , '1' )
    if(a== '2' ):
        if(b== '0' ):
            return(  '2' , '0' )
        if(b== '1' ):
            return(  '3' , '0' )
        if(b== '2' ):
            return(  '4' , '0' )
        if(b== '3' ):
            return(  '5' , '0' )
        if(b== '4' ):
            return(  '6' , '0' )
        if(b== '5' ):
            return(  '7' , '0' )
        if(b== '6' ):
            return(  '8' , '0' )
        if(b== '7' ):
            return(  '9' , '0' )
        if(b== '8' ):
            return(  'A' , '0' )
        if(b== '9' ):
            return(  'B' , '0' )
        if(b== 'A' ):
            return(  'C' , '0' )
        if(b== 'B' ):
            return(  'D' , '0' )
        if(b== 'C' ):
            return(  'E' , '0' )
        if(b== 'D' ):
            return(  'F' , '0' )
        if(b== 'E' ):
            return(  '0' , '1' )
        if(b== 'F' ):
            return(  '1' , '1' )
    if(a== '3' ):
        if(b== '0' ):
            return(  '3' , '0' )
        if(b== '1' ):
            return(  '4' , '0' )
        if(b== '2' ):
            return(  '5' , '0' )
        if(b== '3' ):
            return(  '6' , '0' )
        if(b== '4' ):
            return(  '7' , '0' )
        if(b== '5' ):
            return(  '8' , '0' )
        if(b== '6' ):
            return(  '9' , '0' )
        if(b== '7' ):
            return(  'A' , '0' )
        if(b== '8' ):
            return(  'B' , '0' )
        if(b== '9' ):
            return(  'C' , '0' )
        if(b== 'A' ):
            return(  'D' , '0' )
        if(b== 'B' ):
            return(  'E' , '0' )
        if(b== 'C' ):
            return(  'F' , '0' )
        if(b== 'D' ):
            return(  '0' , '1' )
        if(b== 'E' ):
            return(  '1' , '1' )
        if(b== 'F' ):
            return(  '2' , '1' )
    if(a== '4' ):
        if(b== '0' ):
            return(  '4' , '0' )
        if(b== '1' ):
            return(  '5' , '0' )
        if(b== '2' ):
            return(  '6' , '0' )
        if(b== '3' ):
            return(  '7' , '0' )
        if(b== '4' ):
            return(  '8' , '0' )
        if(b== '5' ):
            return(  '9' , '0' )
        if(b== '6' ):
            return(  'A' , '0' )
        if(b== '7' ):
            return(  'B' , '0' )
        if(b== '8' ):
            return(  'C' , '0' )
        if(b== '9' ):
            return(  'D' , '0' )
        if(b== 'A' ):
            return(  'E' , '0' )
        if(b== 'B' ):
            return(  'F' , '0' )
        if(b== 'C' ):
            return(  '0' , '1' )
        if(b== 'D' ):
            return(  '1' , '1' )
        if(b== 'E' ):
            return(  '2' , '1' )
        if(b== 'F' ):
            return(  '3' , '1' )
    if(a== '5' ):
        if(b== '0' ):
            return(  '5' , '0' )
        if(b== '1' ):
            return(  '6' , '0' )
        if(b== '2' ):
            return(  '7' , '0' )
        if(b== '3' ):
            return(  '8' , '0' )
        if(b== '4' ):
            return(  '9' , '0' )
        if(b== '5' ):
            return(  'A' , '0' )
        if(b== '6' ):
            return(  'B' , '0' )
        if(b== '7' ):
            return(  'C' , '0' )
        if(b== '8' ):
            return(  'D' , '0' )
        if(b== '9' ):
            return(  'E' , '0' )
        if(b== 'A' ):
            return(  'F' , '0' )
        if(b== 'B' ):
            return(  '0' , '1' )
        if(b== 'C' ):
            return(  '1' , '1' )
        if(b== 'D' ):
            return(  '2' , '1' )
        if(b== 'E' ):
            return(  '3' , '1' )
        if(b== 'F' ):
            return(  '4' , '1' )
    if(a== '6' ):
        if(b== '0' ):
            return(  '6' , '0' )
        if(b== '1' ):
            return(  '7' , '0' )
        if(b== '2' ):
            return(  '8' , '0' )
        if(b== '3' ):
            return(  '9' , '0' )
        if(b== '4' ):
            return(  'A' , '0' )
        if(b== '5' ):
            return(  'B' , '0' )
        if(b== '6' ):
            return(  'C' , '0' )
        if(b== '7' ):
            return(  'D' , '0' )
        if(b== '8' ):
            return(  'E' , '0' )
        if(b== '9' ):
            return(  'F' , '0' )
        if(b== 'A' ):
            return(  '0' , '1' )
        if(b== 'B' ):
            return(  '1' , '1' )
        if(b== 'C' ):
            return(  '2' , '1' )
        if(b== 'D' ):
            return(  '3' , '1' )
        if(b== 'E' ):
            return(  '4' , '1' )
        if(b== 'F' ):
            return(  '5' , '1' )
    if(a== '7' ):
        if(b== '0' ):
            return(  '7' , '0' )
        if(b== '1' ):
            return(  '8' , '0' )
        if(b== '2' ):
            return(  '9' , '0' )
        if(b== '3' ):
            return(  'A' , '0' )
        if(b== '4' ):
            return(  'B' , '0' )
        if(b== '5' ):
            return(  'C' , '0' )
        if(b== '6' ):
            return(  'D' , '0' )
        if(b== '7' ):
            return(  'E' , '0' )
        if(b== '8' ):
            return(  'F' , '0' )
        if(b== '9' ):
            return(  '0' , '1' )
        if(b== 'A' ):
            return(  '1' , '1' )
        if(b== 'B' ):
            return(  '2' , '1' )
        if(b== 'C' ):
            return(  '3' , '1' )
        if(b== 'D' ):
            return(  '4' , '1' )
        if(b== 'E' ):
            return(  '5' , '1' )
        if(b== 'F' ):
            return(  '6' , '1' )
    if(a== '8' ):
        if(b== '0' ):
            return(  '8' , '0' )
        if(b== '1' ):
            return(  '9' , '0' )
        if(b== '2' ):
            return(  'A' , '0' )
        if(b== '3' ):
            return(  'B' , '0' )
        if(b== '4' ):
            return(  'C' , '0' )
        if(b== '5' ):
            return(  'D' , '0' )
        if(b== '6' ):
            return(  'E' , '0' )
        if(b== '7' ):
            return(  'F' , '0' )
        if(b== '8' ):
            return(  '0' , '1' )
        if(b== '9' ):
            return(  '1' , '1' )
        if(b== 'A' ):
            return(  '2' , '1' )
        if(b== 'B' ):
            return(  '3' , '1' )
        if(b== 'C' ):
            return(  '4' , '1' )
        if(b== 'D' ):
            return(  '5' , '1' )
        if(b== 'E' ):
            return(  '6' , '1' )
        if(b== 'F' ):
            return(  '7' , '1' )
    if(a== '9' ):
        if(b== '0' ):
            return(  '9' , '0' )
        if(b== '1' ):
            return(  'A' , '0' )
        if(b== '2' ):
            return(  'B' , '0' )
        if(b== '3' ):
            return(  'C' , '0' )
        if(b== '4' ):
            return(  'D' , '0' )
        if(b== '5' ):
            return(  'E' , '0' )
        if(b== '6' ):
            return(  'F' , '0' )
        if(b== '7' ):
            return(  '0' , '1' )
        if(b== '8' ):
            return(  '1' , '1' )
        if(b== '9' ):
            return(  '2' , '1' )
        if(b== 'A' ):
            return(  '3' , '1' )
        if(b== 'B' ):
            return(  '4' , '1' )
        if(b== 'C' ):
            return(  '5' , '1' )
        if(b== 'D' ):
            return(  '6' , '1' )
        if(b== 'E' ):
            return(  '7' , '1' )
        if(b== 'F' ):
            return(  '8' , '1' )
    if(a== 'A' ):
        if(b== '0' ):
            return(  'A' , '0' )
        if(b== '1' ):
            return(  'B' , '0' )
        if(b== '2' ):
            return(  'C' , '0' )
        if(b== '3' ):
            return(  'D' , '0' )
        if(b== '4' ):
            return(  'E' , '0' )
        if(b== '5' ):
            return(  'F' , '0' )
        if(b== '6' ):
            return(  '0' , '1' )
        if(b== '7' ):
            return(  '1' , '1' )
        if(b== '8' ):
            return(  '2' , '1' )
        if(b== '9' ):
            return(  '3' , '1' )
        if(b== 'A' ):
            return(  '4' , '1' )
        if(b== 'B' ):
            return(  '5' , '1' )
        if(b== 'C' ):
            return(  '6' , '1' )
        if(b== 'D' ):
            return(  '7' , '1' )
        if(b== 'E' ):
            return(  '8' , '1' )
        if(b== 'F' ):
            return(  '9' , '1' )
    if(a== 'B' ):
        if(b== '0' ):
            return(  'B' , '0' )
        if(b== '1' ):
            return(  'C' , '0' )
        if(b== '2' ):
            return(  'D' , '0' )
        if(b== '3' ):
            return(  'E' , '0' )
        if(b== '4' ):
            return(  'F' , '0' )
        if(b== '5' ):
            return(  '0' , '1' )
        if(b== '6' ):
            return(  '1' , '1' )
        if(b== '7' ):
            return(  '2' , '1' )
        if(b== '8' ):
            return(  '3' , '1' )
        if(b== '9' ):
            return(  '4' , '1' )
        if(b== 'A' ):
            return(  '5' , '1' )
        if(b== 'B' ):
            return(  '6' , '1' )
        if(b== 'C' ):
            return(  '7' , '1' )
        if(b== 'D' ):
            return(  '8' , '1' )
        if(b== 'E' ):
            return(  '9' , '1' )
        if(b== 'F' ):
            return(  'A' , '1' )
    if(a== 'C' ):
        if(b== '0' ):
            return(  'C' , '0' )
        if(b== '1' ):
            return(  'D' , '0' )
        if(b== '2' ):
            return(  'E' , '0' )
        if(b== '3' ):
            return(  'F' , '0' )
        if(b== '4' ):
            return(  '0' , '1' )
        if(b== '5' ):
            return(  '1' , '1' )
        if(b== '6' ):
            return(  '2' , '1' )
        if(b== '7' ):
            return(  '3' , '1' )
        if(b== '8' ):
            return(  '4' , '1' )
        if(b== '9' ):
            return(  '5' , '1' )
        if(b== 'A' ):
            return(  '6' , '1' )
        if(b== 'B' ):
            return(  '7' , '1' )
        if(b== 'C' ):
            return(  '8' , '1' )
        if(b== 'D' ):
            return(  '9' , '1' )
        if(b== 'E' ):
            return(  'A' , '1' )
        if(b== 'F' ):
            return(  'B' , '1' )
    if(a== 'D' ):
        if(b== '0' ):
            return(  'D' , '0' )
        if(b== '1' ):
            return(  'E' , '0' )
        if(b== '2' ):
            return(  'F' , '0' )
        if(b== '3' ):
            return(  '0' , '1' )
        if(b== '4' ):
            return(  '1' , '1' )
        if(b== '5' ):
            return(  '2' , '1' )
        if(b== '6' ):
            return(  '3' , '1' )
        if(b== '7' ):
            return(  '4' , '1' )
        if(b== '8' ):
            return(  '5' , '1' )
        if(b== '9' ):
            return(  '6' , '1' )
        if(b== 'A' ):
            return(  '7' , '1' )
        if(b== 'B' ):
            return(  '8' , '1' )
        if(b== 'C' ):
            return(  '9' , '1' )
        if(b== 'D' ):
            return(  'A' , '1' )
        if(b== 'E' ):
            return(  'B' , '1' )
        if(b== 'F' ):
            return(  'C' , '1' )
    if(a== 'E' ):
        if(b== '0' ):
            return(  'E' , '0' )
        if(b== '1' ):
            return(  'F' , '0' )
        if(b== '2' ):
            return(  '0' , '1' )
        if(b== '3' ):
            return(  '1' , '1' )
        if(b== '4' ):
            return(  '2' , '1' )
        if(b== '5' ):
            return(  '3' , '1' )
        if(b== '6' ):
            return(  '4' , '1' )
        if(b== '7' ):
            return(  '5' , '1' )
        if(b== '8' ):
            return(  '6' , '1' )
        if(b== '9' ):
            return(  '7' , '1' )
        if(b== 'A' ):
            return(  '8' , '1' )
        if(b== 'B' ):
            return(  '9' , '1' )
        if(b== 'C' ):
            return(  'A' , '1' )
        if(b== 'D' ):
            return(  'B' , '1' )
        if(b== 'E' ):
            return(  'C' , '1' )
        if(b== 'F' ):
            return(  'D' , '1' )
    if(a== 'F' ):
        if(b== '0' ):
            return(  'F' , '0' )
        if(b== '1' ):
            return(  '0' , '1' )
        if(b== '2' ):
            return(  '1' , '1' )
        if(b== '3' ):
            return(  '2' , '1' )
        if(b== '4' ):
            return(  '3' , '1' )
        if(b== '5' ):
            return(  '4' , '1' )
        if(b== '6' ):
            return(  '5' , '1' )
        if(b== '7' ):
            return(  '6' , '1' )
        if(b== '8' ):
            return(  '7' , '1' )
        if(b== '9' ):
            return(  '8' , '1' )
        if(b== 'A' ):
            return(  '9' , '1' )
        if(b== 'B' ):
            return(  'A' , '1' )
        if(b== 'C' ):
            return(  'B' , '1' )
        if(b== 'D' ):
            return(  'C' , '1' )
        if(b== 'E' ):
            return(  'D' , '1' )
        if(b== 'F' ):
            return(  'E' , '1' )
    raise ValueError('unknown digits in ADDS2')
                                               
