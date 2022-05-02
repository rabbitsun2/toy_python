# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 11:38:25 2022

@author: user17
"""

import helloMail.MailBox
from pkBox import DataStructure as ds

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def fib(n):
    if ( n == 1 or n == 2 ):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def noRecurFib(n):
    
    f = [0 for i in range(n)]
    
    f[0] = 1
    f[1] = 1
    
    for i in range(2, n):
        #a = f[i - 1]
        #b = f[i - 2]
        #f[i] = a + b
        f[i] = f[i - 1] + f[i - 2]
        #print("Hello:%s %s a=%s, b=%s" %(i, f[i], a, b))
    
    return f[n - 1]
    
    
        

if __name__ == "__main__":
    print(add(4, 5))
    
    print("noRecurFib():%s" %noRecurFib(6))
    
    a = 2
    b = 4
    
    c = add(a, b)
    
    print(c)
    
    d = spamMail.MailBox.echo_test()
    
    e = spamMail.MailBox.MailBox()
    print(e.add(5))
    print(e.add(2))
    
    f = ds.Node()
    f.setData(8)
    
    g = ds.Node()
    g.setData(10)
    
    print("노드:%s,%s" %( f.getData(), g.getData() ) )
    
    ## 자료구조 Circular LinkedList
    h = ds.LinkedList()
    h.push(f)
    h.push(g)
    
    i = h.pop()
    
    print(i.getData() )
    
    j = h.pop()
    print(j.getData() )