import time

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

def mat_mul(m1, m2):
    result = [[0,0],
              [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += m1[i][k] * m2[k][j]
    return result

def mat_fib(n):
    f = [[1,1],[1,0]]
    new_f = f
    for i in range(n-1):
        new_f = mat_mul(new_f, f)

    return new_f[0][0]*0 + new_f[1][0]*1

print ("Fibonacci Test:")

n_lower = 50
n_upper = 51

rec_outputs = {}
fib = []
for i in range(n_lower,n_upper):
    b = time.time()
    f = rec_fib(i)
    rec_outputs[i] = (time.time() - b)*1000 
    fib.append(f)

it_outputs = {}
for i in range(n_lower,n_upper):
    b = time.time()
    f = it_fib(i)
    it_outputs[i] = (time.time() - b)*1000

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
