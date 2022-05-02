import time
from datetime import timedelta

print("Hello World~!!!")
print("안녕 반가워~!")


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

def non_fact(n):
    start = time.process_time()
    tmp = 1
    for i in range(2, n + 1):
        tmp = i * tmp;
    
    end = time.process_time()
    time_result = start - end

    print("수행시간1:{} / {} = {}".format(start, end, time_result))

    return tmp

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__ == "__main__":
        
    #print("noRecurFib():%s" %noRecurFib(6))
    print("nonFact({})".format(non_fact(4) ))

    start = time.process_time()
    print("Fact({})".format(fact(4) ))
    end = time.process_time()
    time_result = end - start
    print("수행시간2:{} / {} = {}".format(start, end, time_result))
