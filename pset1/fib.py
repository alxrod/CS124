import time
import numpy as np
from numpy.linalg import matrix_power

import sys

# NORMAL: 
###########################################################################
def rec_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return rec_fib(n-1) + rec_fib(n-2)

def it_fib(n):
    A = [0,1]
    for i in range(2,n+1):
        A.append(A[i-1] + A[i-2])
    return A[n]

def mat_fib(n):
    i = np.array([[1,1],[1,0]])
    initial = np.array([1,0])
    new_i = matrix_power(i,n)
    return np.matmul(new_i, initial)[1]

# 2 ** 31 TEST: 
###########################################################################
def test_first_term():
    val = 2 ** 31
    A = [0,1]
    i = 2
    while A[-1] < val:
        A.append(A[i-1] + A[i-2])
        i+=1
    return {len(A): A[-1]}

# LARGEST K IN MINUTE: 
###########################################################################
TIMER = 5 
def rec_fib_mod(f_zero, f_one, start_time, k):
    if time.time() - start_time > 5:
        return {k: f_zero + f_one}
    if k < 20:
        print (f_zero+f_one)
    return ( rec_fib_mod(f_one, (f_zero+f_one), start_time, k+1) ) 




# TESTS: 
###########################################################################

def output_comp():

    n_lower = 40
    n_upper = 41

    rec_outputs = {}

    for i in range(n_lower,n_upper):
        b = time.time()
        f = rec_fib(i)
        rec_outputs[i] = (time.time() - b)*1000 
        fib.append(f)

    fib = []
    it_outputs = {}
    for i in range(n_lower,n_upper):
        b = time.time()
        f = it_fib(i)
        it_outputs[i] = (time.time() - b)*1000
        fib.append(f)

    mat_outputs = {}
    for i in range(n_lower,n_upper):
        b = time.time()
        f = mat_fib(i)
        mat_outputs[i] = (time.time() - b)*1000

    header = "Type |"
    lens = []
    for f in fib:
        added = "|    " + str(f) + "    "
        lens.append(len(added))
        header += added

    rec_print = "Rec  |"
    counter = 0
    for t in rec_outputs.values():
        added = "| " + str(round(t, 4)) + " "
        correct_len = lens[counter]
        for i in range(correct_len-len(added)):
            added += " "
        rec_print += added
        counter += 1

    it_print = "It   |"
    counter = 0
    for t in it_outputs.values():
        added = "| " + str(round(t, 4)) + " "
        correct_len = lens[counter]
        for i in range(correct_len-len(added)):
            added += " "
        it_print += added
        counter += 1

    mat_print = "Mat  |"
    counter = 0
    for t in mat_outputs.values():
        added = "| " + str(round(t, 4)) + " "
        correct_len = lens[counter]
        for i in range(correct_len-len(added)):
            added += " "
        mat_print += added
        counter += 1

    breaker = "------"
    for i in lens:
        for j in range(i):
            breaker += "-"
    print(header)
    print(breaker)
    print(rec_print)
    print(it_print)
    print(mat_print)

def oveflow_test():
    print("First term of Fib greater than 2 ** 31")
    print(test_first_term())

def mod_test():
    print(rec_fib_mod(0,1,time.time(),1))

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    mod_test()