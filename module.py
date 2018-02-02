import math

    
def perform(a,b,oper):
    switcher = {
        '+' :  a+b,
        '-' :  a-b,
        '*':  a*b,
        '/':  a/b,
        '%':  a%b,
        '^':  pow(a,b)
    }
    a = switcher.get(oper)
    return a