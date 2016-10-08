def ADDS3B2(a,b):
    if( a<='0' ):
        if( b<='0' ):
            return ('0','0') #(a='0',b='0')
        else:
            return ('1','0') #(a='0',b='1')
    else:
        if( b<='0' ):
            return ('1','0') #(a='0',b='0')
        else:
            return ('0','1') #(a='1',b='1')

    raise ValueError('unknown digits in ADDS3')
        
        
def ADDS3B3(a, b):
    if( a<='1' ):
        if( a<='0' ):
            if( b<='1' ):
                if( b<='0' ):
                    return ('0','0') #(a='0',b='0')
                else:
                    return ('1','0') #(a='0',b='1')
            else:
                return ('2','0') #(a='0',b='2')
        else:
            if( b<='1' ):
                if( b<='0' ):
                    return ('1','0') #(a='1',b='0')
                else:
                    return ('2','0') #(a='1',b='1')
            else:
                return ('0','1') #(a='1',b='2')
    else:
        if( b<='1' ):
            if( b<='0' ):
                return ('2','0') #(a='2',b='0')
            else:
                return ('0','1') #(a='2',b='1')
        else:
            return ('1','1') #(a='2',b='2')
    raise ValueError('unknown digits in ADDS3')




def ADDS3B4(a, b):
    if(a<='2'):
        if( a<='1' ):
            if( a<='0' ):
                    if(b<='2'):
                        if( b<='1' ):
                            if( b<='0' ):
                                return ('0','0') #(a='0',b='0')
                            else:
                                return ('1','0') #(a='0',b='1')
                        else:
                            return ('2','0') #(a='0',b='2')
                    else:
                        return('3','0')#(a='3',b='2')
            else:
                if( b<='2' ):
                    if( b<='1' ):
                        if (b<='0'):
                            return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    else:
                        return ('3','0') #(a='1',b='2')
                else:
                    return('4','0')#(a='1',b='2')
        else:
            if( b<='2' ):
                if( b<='1' ):
                    if (b<='0'):
                        return ('2','0') #(a='2',b='0')
                    else:
                        return ('2','1') #(a='2',b='1')
                else:
                    return ('0','1') #(a='2',b='2')
            else:
                return('1','1')# (a='2',b='2')
            
    else:
        if( b<='1' ):
            if( b<='0' ):
                return ('3','0') #(a='3',b='0')
            else:
                return ('0','1') #(a='3',b='1')
        else:
            return ('2','1') #(a='3',b='3')
    raise ValueError('unknown digits in ADDS3')


def ADDS3B5(a,b):
    if(a<='2'):
        if( a<='1' ):
            if( a<='0' ):
                if(b<='2'):
                    if( b<='1' ):
                        if( b<='0' ):
                                return ('0','0') #(a='0',b='0')
                        else:
                                return ('1','0') #(a='0',b='1')
                    else:
                        return('2','0')
 
                else:
                    if( b<='3' ):
                        return ('3','0') #(a='0',b='3')
                    else:
                        return ('4','0') #(a='0',b='4')
                
            else:
                if( b<='2' ):
                    if( b<='1' ):
                        if (b<='0'):
                            return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    else:
                        return ('3','0')                       
                
                else:
                    if( b<='3' ):
                            return ('4','0') #(a='1',b='3')
                    else:
                            return ('1','0') #(a='1',b='4')
        else:
            if(b<='2'):
                if( b<='1' ):
                    if( b<='0' ):
                        return ('2','0') #(a='2',b='0')
                    else:
                        return ('3','0') #(a='2',b='1')
                else:
                    return ('4','0') #(a='2',b='2')
            else:
                if (b<='4'):
                    if(b<='3'):
                        return ('1','0') #(a='2',b='3')
                    else:
                        return('1','1')
    else:
        if(a<='3'):
            if( b<='2' ):
                if( b<='1' ):
                    if( b<='0' ):
                        return ('2','0') #(a='3',b='0')
                    else:
                        return ('3','0') #(a='3',b='1')
                else :
                    return('0','1')
            else:
                if( b<='3' ):
                    return ('1','1') #(a='3',b='3')
                else:
                    return('2','1')
            
        else:
            if (b<='2'):
                    if(b<='1'):
                            if(b<='0'):
                                return ('4','0') 
                            else:
                                return('5','0') ##(a='4',b='1')
                    else:
                        return('1','1') ##(a='4',b='2')                   
            else:
                if(b<='3'):
                    return('2','1')
                else:
                    return('3','1') 
                           
        
    raise ValueError('unknown digits in ADDS3')

def ADDS3B6(a,b):
    if(a<='2'):
        if( a<='1' ):
            if( a<='0' ):
                if(b<='2'):
                    if( b<='1' ):
                        if( b<='0' ):
                                return ('0','0') #(a='0',b='0')
                        else:
                                return ('1','0') #(a='0',b='1')
                    else:
                        return('2','0')
 
                else:
                    if(b<='6'):
                        if(b<='4'):
                            if(b<='3'):
                                return ('3','0') #(a='0',b='3')
                            else:
                                return('4','0')
                        else:
                            if(b<='5'):
                                return ('5','0')
                            else:
                                return('6','0')
                                                     
            else:
                if( b<='2' ):
                    if( b<='1' ):
                        if (b<='0'):
                            return ('1','0') #(a='1',b='0')
                        else:
                            return ('2','0') #(a='1',b='1')
                    else:
                        return ('3','0')                       
                
                else:
                    if(b<='6'):
                        if( b<='4' ):
                            if( b<='3'):
                                return ('4','0')
                            else:
                                return ('5','0') #(a='1',b='4')
                        else:
                            if(b<='5'):
                                return('0','1')#(a='1',b='5')
                            else:
                                return('1','1')
                
        else:
            if(b<='2'):
                if( b<='1' ):
                    if( b<='0' ):
                        return ('2','0') #(a='2',b='0')
                    else:
                        return ('3','0') #(a='2',b='1')
                else:
                    return ('4','0') #(a='2',b='2')
            else:
                if(b<='6'):
                    if(b<='4'):
                        if(b<='3'):
                            return ('5','0') #(a='2',b='3')
                        else:
                            return('0','1')
                    else:
                        if(b<='5'):
                            return('1','1')                           
                        else:
                            return('2','1')
                        
    else:
        if(a<='6'):
            if(a<='4'):
                if(a<='3'):
                    if( b<='2' ):
                        if( b<='1' ):
                            if( b<='0' ):
                                return ('3','0') #(a='3',b='0')
                            else:
                                return ('4','0') #(a='3',b='1')
                        else:
                            return('5','0')
                    else:
                        if( b<='6' ):
                            if( b<='4'):
                                if(b<='3'):
                                    return ('0','1') #(a='3',b='3')
                                else:
                                    return('1','1')
                            else:
                                if(b<='5'):
                                    return('2','1')
                                else:
                                    return('3','1')
                else:
                    if(b<='2'):
                        if(b<='1'):
                            if(b<='0'):
                                return ('3','0') 
                            else:
                                return ('4','0') #(a='3',b='1')
                        else:
                            return('5','0')
                    else:
                        if( b<='4' ):
                           if( b<='3'):
                               return ('0','1') #(a='3',b='3')
                           else:
                               return('1','1')
                        else:
                            return('2','1')
         
        else:
            if(a<='5'):
                if (b<='2'):
                    if(b<='1'):
                        if(b<='0'):
                            return ('5','0') 
                        else:
                            return('0','1') ##(a='4',b='1')
                    else:
                        return('1','1') ##(a='4',b='2')                   
                else:
                    if(b<='4'):
                        if(b<='3'):
                            return('2','1')
                        else:
                            return('3','1')
                    else:
                        return('4','1')
            else:
                if (b<='2'):
                    if(b<='1'):
                        if(b<='0'):
                            return ('0','1') 
                        else:
                            return('1','1') 
                    else:
                        return('2','1')
                else:
                    if(b<='4'):
                        if(b<='3'):
                            return('3','1')
                        else:
                            return('4','1')
                    else:
                        return('4','1')
               
    #raise ValueError('unknown digits in ADDS3')

def ADDS3B7(a,b):
    if(a<='3'):
        if( a<='1' ):
            if( a<='0' ):
                if(b<='3'):
                    if( b<='1' ):
                        if( b<='0' ):
                            return ('0','0') 
                        else:
                            return ('1','0') 
                    else:
                        if(b<='2'):
                            return('2','0')
                        else:
                            return('3','0')
 
                else:
                    if(b<='6'):
                        if(b<='5'):
                            if(b<='4'):
                                return ('4','0')
                            else:
                                return ('5','0')
                        else:
                            return('6','0')                                  
                
            else:
                if( b<='3' ):
                    if( b<='1' ):
                        if (b<='0'):
                            return ('1','0') 
                        else:
                            return ('2','0') 
                    else:
                        if(b<='2'):
                            return ('3','0')
                        else:
                            return('4','0')
                else:
                    if(b<='6'):
                        if(b<='5'):
                            if(b<='4'):
                                return ('5','0')
                            else:
                                return ('6','0')
                        else:
                            return('0','1')                              
        else:
            if (a<='2'):
                if( b<='3' ):
                    if( b<='1' ):
                        if( b<='0'):
                            return ('2','0')
                        else:
                            return ('3','0') 
                    else:
                        if(b<='2'):
                            return('4','0')
                        else:
                            return('5','0')
                else:
                    if(b<='5'):
                        if(b<='4'):
                            return('6','0')
                        else:
                            return('7','0')
                    else:
                        return('1','1')
            else:
                if( b<='3' ):
                    if( b<='1' ):
                        if( b<='0'):
                            return ('3','0')
                        else:
                            return ('4','0') 
                    else:
                        if(b<='2'):
                            return('5','0')
                        else:
                            return('6','0')
                else:
                    if(b<='5'):
                        if(b<='4'):
                            return('0','1')
                        else:
                            return('1','1')
                    else:
                        return('2','1')                                   
    else:
        if(a<='6'):
            if (a<='5'):
                if(a<='4'):
                    if(b<='3'):
                        if( b<='1'):
                            if( b<='0'):
                                return ('4','0') 
                            else:
                                return ('5','0') 
                        else:
                            if(b<='2'):
                                return ('6','1')
                            else:
                                return('0','1')
                    else:
                        if(b<='6'):
                            if (b<='5'):
                               if(b<='4'):
                                   return ('1','1') 
                               else:
                                   return('2','1')
                            else:
                                return('3','1')
                           
                               
                else:
                    if(b<='3'):
                        if(b<='1'):
                            if(b<='0'):
                                return('5','0')
                            else:
                                return('6','0')
                        else:
                            return('0','1')
                        
        else:
            if(b<='3'):
                   if( b<='1' ):
                       if( b<='0' ):
                           return ('6','0') 
                       else:
                           return ('0','1') 
            
                   else:
                      if(b<='2'):
                          return ('1','1')
                      else:
                          return('2','1')
               
            else:
                if(b<='6'):
                    if( b<='5' ):
                        if( b<='4' ):
                            return ('3','1') #(a='3',b='0')
                        else:
                            return ('4','1') #(a='3',b='1)
                    else:
                        return('5','1')
                
                           
                                   
    #raise ValueError('unknown digits in ADDS3')

def ADDS3B8(a,b):
    if(a<='3'):
        if( a<='1' ):
            if( a<='0' ):
                if(b<='3'):
                    if( b<='1' ):
                        if( b<='0' ):
                            return ('0','0') 
                        else:
                            return ('1','0') 
                    else:
                        if(b<='2'):
                            return('2','0')
                        else:
                            return('3','0')
 
                else:
                    if(b<'7'):
                        if(b<='6'):
                            if(b<='5'):
                                if(b<='4'):
                                    return ('4','0')
                                else:
                                    return ('5','0')
                            else:
                                return('6','0')
                        else:
                            return('7','0')
                
            else:
                if( b<='3' ):
                    if( b<='1' ):
                        if (b<='0'):
                            return ('1','0') 
                        else:
                            return ('2','0') 
                    else:
                        if(b<='3'):
                            return ('3','0')
                        else:
                            return('4','0')
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if(b<='5'):
                                if(b<='4'):
                                    return ('5','0')
                                else:
                                    return ('6','0')
                            else:
                                return('7','0')
                        else:
                            return('0','1')
                            
        else:
            if (a<='2'):
                if( b<='3' ):
                    if( b<='1' ):
                        if( b<='0'):
                            return ('2','0')
                        else:
                            return ('3','0') 
                    else:
                        if(b<='2'):
                            return('4','0')
                        else:
                            return('5','0')
                else:
                    if(b<='5'):
                        if(b<='4'):
                            return('6','0')
                        else:
                            return('7','0')
                    else:
                        return('1','1')
            else:
                if( b<='3' ):
                    if( b<='1' ):
                        if( b<='0'):
                            return ('3','0')
                        else:
                            return ('4','0') 
                    else:
                        if(b<='2'):
                            return('5','0')
                        else:
                            return('6','0')
                else:
                    if(b<='5'):
                        if(b<='4'):
                            return('0','1')
                        else:
                            return('1','1')
                    else:
                        return('2','1')                                   
    else:
        if(a<='6'):
                if (a<='5'):
                    if(a<='4'):
                        if(b<='3'):
                            if( b<='1'):
                                if( b<='0'):
                                    return ('4','0') 
                                else:
                                    return ('5','0') 
                            else:
                                if(b<='2'):
                                    return ('6','0')
                                else:
                                    return('7','0')
                        else:
                            if(b<='7'):
                                if(b<='6'):
                                    if (b<='5'):
                                        if(b<='4'):
                                            return ('0','1') 
                                        else:
                                            return('1','1')
                                    else:
                                        return('2','1')                              
                    else:
                        if(b<='3'):
                            if(b<='1'):
                                if(b<='0'):
                                    return('5','0')
                                else:
                                    return('6','0')
                            else:
                                if(b<='2'):
                                    return('7','0')
                                else:
                                    return('0','1')
                                    
                        else:
                            if(b<='7'):
                                if( b<='5' ):
                                    if(b<='4'):
                                        return('1','1')
                                    else:
                                        return ('2','1')
                                else:
                                    if(b<='6'):
                                        return('3','1')
                                    else:
                                        return('4','1')
                else:
                    if(b<='3'):
                        if( b<='1' ):
                            if( b<='0' ):
                                return ('7','0') 
                            else:
                                return ('0','1') 
                        else:
                            if(b<='2'):
                                return('1','1')
                            else:
                                return('2','1')
                            
                    else:
                        if(b<='6'):
                            if(b<='5'):
                                if(b<='4'):
                                    return ('3','1')
                                else:
                                    return('4','1')
                            else:
                                  return('5','1')
                        else:
                             return('6','1')
                 
                     
def ADDS3B9(a,b):
    if(a<='4'):
        if( a<='2' ):
            if( a<='1' ):
                if( a<='0' ):
                    if(b<='4'):
                      if( b<='2' ):
                        if( b<='1' ):
                            if( b<='0' ):
                                return ('0','0') 
                            else:
                                return ('1','0') 
                      else:
                          if(b<='3'):
                                return('3','0')
                          else:
                                return('4','0')
 
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if(b<='5'):
                                return ('5','0')
                            else:
                                return ('6','0')
                        else:
                            return('7','0')
                    else:
                        return('8','0')
                
            else:
                if( b<='4' ):
                    if( b<='2' ):
                        if (b<='1'):
                            if( b<='0'):
                                return ('1','0') 
                            else:
                                return ('2','0') 
                        else:
                            if(b<='3'):
                                return ('3','0')
                            else:
                                return('4','0')
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if(b<='5'):
                                return ('5','0')
                            else:
                                return ('6','0')
                        else:
                            return('7','0')
                    else:
                        return('8','0')
                            
        else:
            if(b<='4'):
                if( b<='2' ):
                    if( b<='1' ):
                        if( b<='0'):
                            return ('2','0')
                        else:
                            return ('3','0') 
                    else:
                        if(b<='3'):
                            return('4','0')
                        else:
                            return('5','0')
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if(b<='5'):
                                return('6','0')
                            else:
                                return('7','0')
                    else:
                        return('8','0')
            else:
                if(a<='3'):
                    if( b<='4' ):
                        if( b<='2' ):
                            if( b<='1' ):
                                if( b<='0'):
                                    return ('3','0')
                                else:
                                    return ('4','0') 
                    else:
                        if(b<='3'):
                            return('5','0')
                        else:
                            return('6','0')
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if( b<='5' ):
                                return('7','0')
                            else:
                                return('8','0')
                        else:
                            return('0','1')
                    else:
                        return('1','1')
        
        
            if( b<='4' ):
                if( b<='2' ):
                    if( b<='1' ):
                        if( b<='0'):
                            return('4','0')
                        else:
                            return('5','0')
                    else:
                        return('6','0')
                else:
                    if(b<='3'):
                        return('7','0')
                    else:
                        return('8','0')
                        
                                
                                
            else:
                if( b<='7' ):
                    if( b<='6' ):
                        if( b<='5'):
                            return('0','1')
                        else:
                            return('1','1')
                    else:
                        return('1','2')
                
                        
            
                
                
    else:
        if(a<='7'):
            if (a<='6'):
                if(a<='5'):
                    if(b<='4'):
                        if( b<='2'):
                            if( b<='1'):
                                if( b<='0'):
                                    return('5','0')
                                else:
                                    return ('6','0') 
                            else:                               
                                return ('7','0')
                        else:
                            if(b<='3'):
                                return('8','0')
                    else:
                        if(b<='7'):
                            if(b<='6'):
                                if (b<='5'):
                                    if(b<='4'):
                                        return ('9','0') 
                                    else:
                                        return('0','1')
                                else:
                                    return('1','1')                              
                else:
                    if(b<='4'):
                        if(b<='2'):
                            if(b<='1'):
                                if(b<='0'):
                                    return('6','0')
                                else:
                                    return('7','0')
                            else:
                                return('8','0')
                        else:
                            return('9','0')
                                    
                    else:
                        if(b<='7'):
                            if( b<='5' ):
                                if(b<='4'):
                                    return('1','1')
                                else:
                                    return ('2','1')
                            else:
                                if(b<='6'):
                                    return('3','1')
                                else:
                                    return('4','1')
                                    
               
            else:
                if(b<='4'):
                    if(b<='2'):
                        if( b<='1' ):
                            if( b<='0' ):
                                return ('7','0') 
                            else:
                                return ('8','0') 
                    else:
                        if(b<='3'):
                            return('0','1')
                        else:
                            return('1','1')
                            
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if(b<='5'):
                                if(b<='4'):
                                    return ('2','1')
                                else:
                                    return('3','1')
                            else:
                                return('4','1')
                        else:
                            return('5','1')
        else:
            if(a<='8'):
                if(b<='4'):
                    if(b<='2'):
                        if( b<='1' ):
                            if( b<='0' ):
                                return ('8','0') 
                            else:
                                return ('0','1')
                        else:
                            return('1','1')
                    else:
                        if(b<='3'):
                            return('2','1')
                        else:
                            return('3','1')                           
                else:
                    if(b<='7'):
                        if(b<='6'):
                            if(b<='5'):
                                if(b<='4'):
                                    return ('4','1')
                                else:
                                    return('5','1')
                            else:
                                return('6','1')
                        else:
                            return('7','1')
            
                 

                        
                                    
                                
                    
                
                           
                                   
    #raise ValueError('unknown digits in ADDS3')

    

