def ADDS3(a,b):
    if(a<='4'):
        if(a<='2'):
            if(a<='1'):
                if(a<='0'):
                    if(b<='4'):
                        if(b<='2'):
                            if(b<='1'):
                                if(b<='0'):
                                    return('0','0')
                                else:
                                    return('1','0')
                            else:
                                return('2','0')
                        else:
                            if(b<='3'):
                                return('3','0')
                            else:
                                return('4','0')
                    else:
                        if(b<='9'):
                            if(b<='7'):
                                if(b<='6'):
                                    if(b<='5'):
                                        return('5','0')
                                    else:
                                        return('6','0')
                                else:
                                    return('7','0')
                            else:
                                if(b<='8'):
                                    return('8','0')
                                else:
                                    return('9','0')
                else:
                    if(b<='4'):
                        if(b<='2'):
                            if(b<='1'):
                                if(b<='0'):
                                    return('1','0')
                                else:
                                    return('2','0')
                            else:
                                return('3','0')
                        else:
                            if(b<='3'):
                                return('4','0')
                            else:
                                return('5','0')
                    else:
                        if(b<='9'):
                            if(b<='7'):
                                if(b<='6'):
                                    if(b<='5'):
                                        return('6','0')
                                    else:
                                        return('7','0')
                                else:
                                    return('8','0')
                            else:
                                if(b<='8'):
                                    return('9','0')
                                else:
                                    return('0','1')
            else:
                if(b<='4'):
                    if(b<='2'):
                        if(b<='1'):
                            if(b<='0'):
                                return('2','0')
                            else:
                                return('3','0')
                        else:
                            return('4','0')
                    else:
                        if(b<='3'):
                            return('5','0')
                        else:
                            return('6','0')
                else:
                    if(b<='9'):
                        if(b<='7'):
                            if(b<='6'):
                                if(b<='5'):
                                    return('7','0')
                                else:
                                    return('8','0')
                            else:
                                return('9','0')
                        else:
                            if(b<='8'):
                                return('0','1')
                            else:
                                return('1','1')
        else:
            if(a<='3'):
                if(b<='4'):
                    if(b<='2'):
                        if(b<='1'):
                            if(b<='0'):
                                return('3','0')
                            else:
                                return('4','0')
                        else:
                            return('5','0')
                    else:
                        if(b<='3'):
                            return('6','0')
                        else:
                            return('7','0')
                else:
                    if(b<='9'):
                        if(b<='7'):
                            if(b<='6'):
                                if(b<='5'):
                                    return('8','0')
                                else:
                                    return('9','0')
                            else:
                                return('0','1')
                        else:
                            if(b<='8'):
                                return('1','1')
                            else:
                                return('2','1')
            else:
                    if(b<='4'):
                        if(b<='2'):
                            if(b<='1'):
                                if(b<='0'):
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
                        if(b<='9'):
                            if(b<='7'):
                                if(b<='6'):
                                    if(b<='5'):
                                        return('9','0')
                                    else:
                                        return('0','1')
                                else:
                                    return('1','1')
                            else:
                                if(b<='8'):
                                    return('2','1')
                                else:
                                    return('3','1')
    else:
        if(a<='9'):
            if(a<='7'):
                if(a<='6'):
                    if(a<='5'):
                        if(b<='4'):
                            if(b<='2'):
                                if(b<='1'):
                                    if(b<='0'):
                                        return('5','0')
                                    else:
                                        return('6','0')
                                else:
                                    return('7','0')
                            else:
                                if(b<='3'):
                                    return('8','0')
                                else:
                                    return('9','0')
                        else:
                            if(b<='9'):
                                if(b<='7'):
                                    if(b<='6'):
                                        if(b<='5'):
                                            return('0','1')
                                        else:
                                            return('1','1')
                                    else:
                                        return('2','1')
                                else:
                                    if(b<='8'):
                                        return('3','1')
                                    else:
                                        return('4','1')
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
                                if(b<='3'):
                                    return('9','0')
                                else:
                                    return('0','1')
                        else:
                            if(b<='9'):
                                if(b<='7'):
                                    if(b<='6'):
                                        if(b<='5'):
                                            return('1','1')
                                        else:
                                            return('2','1')
                                    else:
                                        return('3','1')
                                else:
                                    if(b<='8'):
                                        return('4','1')
                                    else:
                                        return('5','1')
                else:
                    if(b<='4'):
                        if(b<='2'):
                            if(b<='1'):
                                if(b<='0'):
                                    return('7','0')
                                else:
                                    return('8','0')
                            else:
                                return('9','0')
                        else:
                            if(b<='3'):
                                return('0','1')
                            else:
                                return('1','1')
                    else:
                        if(b<='9'):
                            if(b<='7'):
                                if(b<='6'):
                                    if(b<='5'):
                                        return('2','1')
                                    else:
                                        return('3','1')
                                else:
                                    return('4','1')
                            else:
                                if(b<='8'):
                                    return('5','1')
                                else:
                                    return('6','1')
            else:
                if(a<='8'):
                    if(b<='4'):
                        if(b<='2'):
                            if(b<='1'):
                                if(b<='0'):
                                    return('8','0')
                                else:
                                    return('9','0')
                            else:
                                return('0','1')
                        else:
                            if(b<='3'):
                                return('1','1')
                            else:
                                return('2','1')
                    else:
                        if(b<='9'):
                            if(b<='7'):
                                if(b<='6'):
                                    if(b<='5'):
                                        return('3','1')
                                    else:
                                        return('4','1')
                                else:
                                    return('5','1')
                            else:
                                if(b<='8'):
                                    return('6','1')
                                else:
                                    return('7','1')
                else:
                        if(b<='4'):
                            if(b<='2'):
                                if(b<='1'):
                                    if(b<='0'):
                                        return('9','0')
                                    else:
                                        return('0','1')
                                else:
                                    return('1','1')
                            else:
                                if(b<='3'):
                                    return('2','1')
                                else:
                                    return('3','1')
                        else:
                            if(b<='9'):
                                if(b<='7'):
                                    if(b<='6'):
                                        if(b<='5'):
                                            return('4','1')
                                        else:
                                            return('5','1')
                                    else:
                                        return('6','1')
                                else:
                                    if(b<='8'):
                                        return('7','1')
                                    else:
                                        return('8','1')
    raise ValueError('unknown digits in ADDS3')