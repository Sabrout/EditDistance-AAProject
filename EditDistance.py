import numpy as np
import random
import string
import time
import math


# INITIALIZATION
def init(s1, s2):
    m = np.empty((len(s1) + 1, len(s2) + 1))
    m[:] = np.NAN
    # initializing the first row
    m[0] = np.arange(m.shape[1])
    # initializing the first column
    counter = 0
    for i in m:
        i[0] = counter
        counter += 1
    return m


# Minimum Edit Distance (MED)
# CLASSIC DYNAMIC PROGRAMMING ALGORITHM
def med_classic(s1, s2):
    # INITIALIZATION
    m = init(s1, s2)
    for i in range(1, m.shape[0]):
        for j in range(1, m.shape[1]):

            # first condition : i is an insertion
            con1 = m[i - 1, j] + 1

            # second condition : j is a deletion
            con2 = m[i, j - 1] + 1

            # third condition : i and j are a substitution
            if s1[i - 1] == s2[j - 1]:
                # if same letters, we add nothing
                con3 = m[i - 1, j - 1]
            else:
                # if different letters, we add one
                con3 = m[i - 1, j - 1] + 1

            # assign minimum value
            m[i][j] = min(con1, con2, con3)
    # printing result and running time
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(m[m.shape[0] - 1][m.shape[1] - 1])))
    return m[m.shape[0] - 1][m.shape[1] - 1], m


# K STRIP ALGORITHM
def med_k(s1, s2, k=0):

    # K value exception
    if k > (len(s1)-1) + (len(s2)-1) or k < 0:
        raise Exception('K VALUE OUT OF BOUNDS')

    # INITIALIZATION
    m = init(s1, s2)
    # Preparing K diagonals
    ki = int(k / 2)
    if k%2 != 0:
        ki += 1
    kj = int(k / 2)
    # Result variable initiation
    result = None

    # Flag for calculating which side of the strip
    upper = True

    # Loop for K strips around the main diagonal
    k = ki
    while k > -1:
        # Switching to calculate the other side of the diagonal
        if k == 0 and upper:
            k =kj
            upper = False
        # Deciding which side
        if upper:
            k_up = k
            k_down = 0
        else:
            k_up = 0
            k_down = k
        for i in range(1, m.shape[0]):
            for j in range(1, m.shape[1]):
                if i+k_up == j+k_down:
                    # first condition : i is an insertion
                    if not np.isnan(m[i - 1, j]):
                        con1 = m[i - 1, j] + 1
                    else:
                        con1 = math.inf

                    # second condition : j is a deletion
                    if not np.isnan(m[i, j - 1]):
                        con2 = m[i, j - 1] + 1
                    else:
                        con2 = math.inf

                    # third condition : i and j are a substitution
                    if s1[i - 1] == s2[j - 1]:
                        # if same letters, we add nothing
                        con3 = m[i - 1, j - 1]
                    else:
                        # if different letters, we add one
                        con3 = m[i - 1, j - 1] + 1

                    # assign minimum value
                    m[i][j] = min(con1, con2, con3)
                    # print("con1: {} con2: {} con3: {} min: {}".format(con1, con2, con3, m[i][i]))
                    result = m[i][j]
        k -= 1
    # printing result and running time
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result)))
    return result, m


# PURE RECURSIVE ALGORITHM
def med_recursive(s1, s2):
    n = len(s1)
    m = len(s2)
    # base cases
    if n == 0 and m == 0:
        return 0
    if n == 0:
        return m
    if m == 0:
        return n
    # recursive definition
    con1 = med_recursive(s1[:-1], s2) + 1   # Deletion
    con2 = med_recursive(s1, s2[:-1]) + 1   # Insertion
    con3 = med_recursive(s1[:-1], s2[:-1]) + (s1[-1] != s2[-1])   # Substitution

    return min(con1, con2, con3)


# BRANCH AND BOUND ALGORITHM
def med_branch():
    return 

# RUNTIME CALCULATOR
def calc_runtime(function, *args):
    startTime = time.time()
    result = function(*args)
    return time.time() - startTime, result


# RANDOM STRING GENERATOR
def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    # s1 = string_generator()
    # s2 = string_generator()
    s1 = "INTENTION"
    s2 = "EXECUTION"
    print('String #1 : ' + s1)
    print('String #2 : ' + s2)

    # CLASSIC DYNAMIC PROGRAMMING ALGORITHM
    print("_____________________________________")
    print("CLASSIC DYNAMIC PROGRAMMING ALGORITHM")
    result = calc_runtime(med_classic, s1, s2)
    print("RUNNING TIME :  %s seconds" % result[0])
    # Printing Matrix
    # print("")
    # print(result[1][1])

    # K STRIP ALGORITHM
    print("_________________")
    print("K STRIP ALGORITHM")
    k = 0
    result = calc_runtime(med_k, s1, s2, k)
    print("RUNNING TIME :  %s seconds" % result[0])
    print("K :  %s" % k)
    # Printing Matrix
    # print("")
    # print(result[1][1])

    # PURE RECURSIVE ALGORITHM
    print("________________________")
    print("PURE RECURSIVE ALGORITHM")
    result = calc_runtime(med_recursive, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1])))
    print("RUNNING TIME :  %s seconds" % result[0])


if __name__ == "__main__":main()
