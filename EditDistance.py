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
def med_branch(s1, s2, cost=0, bound=0):
    cost += 1
    n = len(s1)
    m = len(s2)
    # base cases
    if n == 0 and m == 0:
        return 0
    if n == 0:
        return m
    if m == 0:
        return n
    # calculate heuristic values
    # deletion node
    h_con1 = abs((n - 1) - m)
    f_con1 = h_con1 + cost
    # insertion node
    h_con2 = abs(n - (m - 1))
    f_con2 = h_con2 + cost
    # substitution node
    h_con3 = abs((n - 1) - (m - 1))
    if s1[-1] == s2[-1]:
        f_con3 = h_con3 + cost - 1
    else:
        f_con3 = h_con3 + cost
    # recursive definition
    # print(bound)
    # print("{} {} {} {} {} {}".format("f_con1 :", f_con1, "___  f_con2 :", f_con2, "___  f_con3 :", f_con3))
    # Branching
    con1, con2, con3 = np.inf, np.inf, np.inf
    if bound >= f_con1:
        # print("Branch 1")
        con1 = med_branch(s1[:-1], s2, cost, bound) + 1  # Deletion
    if bound >= f_con2:
        # print("Branch 2")
        con2 = med_branch(s1, s2[:-1], cost, bound) + 1  # Insertion
    if bound >= f_con3:
        # print("Branch 3")
        # update bound
        bound += 1
        con3 = med_branch(s1[:-1], s2[:-1], cost, bound) + (s1[-1] != s2[-1])  # Substitution
    # Raising Errors for debugging
    if type(min(con1, con2, con3)) != int:
        print(min(con1, con2, con3))
        raise ("INTEGER EXCEPTION")
    return min(con1, con2, con3)


# RUNTIME CALCULATOR
def calc_runtime(function, *args):
    start_time = time.time()
    result = function(*args)
    return time.time() - start_time, result


# RANDOM STRING GENERATOR
def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    s1 = string_generator(100)
    s2 = string_generator(100)
    # s1 = "TVQTSKNPQVDIAEDNAFFPSEYSLSQYTSPVSDLDGVDYPKPYRGKHKILVIAADERYLPTDNGKLFST\
    #     GNHPIETLLPLYHLHAAGFEFEVATISGLMTKFEYWAMPHKDEKVMPFFEQHKSLFRNPKKLADVVASLN\
    #     ADSEYAAIFVPGGHGALIGLPESQDVAAALQWAIKNDRFVISLCHGPAAFLALRHGDNPLNGYSICAFPD\
    #     AADKQTPEIGYMPGHLTWYFGEELKKMGMNIINDDITGRVHKDRKLLTGDSPFAANALGKLAAQEMLAAY\
    #     AG"
    # s2 = "MAPKKVLLALTSYNDVFYSDGAKTGVFVVEALHPFNTFRKEGFEVDFVSETGKFGWDEHSLAKDFLNGQD\
    #     ETDFKNKDSDFNKTLAKIKTPKEVNADDYQIFFASAGHGTLFDYPKAKDLQDIASEIYANGGVVAAVCHG\
    #     PAIFDGLTDKKTGRPLIEGKSITGFTDVGETILGVDSILKAKNLATVEDVAKKYGAKYLAPVGPWDDYSI\
    #     TDGRLVTGVNPASAHSTAVRSIVALKNLEHHHHHH"
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

    # PURE RECURSIVE ALGORITHM
    print("________________________")
    print("PURE RECURSIVE ALGORITHM")
    # result = calc_runtime(med_recursive, s1, s2)
    print(" ")
    # print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1])))
    # print("RUNNING TIME :  %s seconds" % result[0])

    # BRANCH AND BOUND ALGORITHM
    print("__________________________")
    print("BRANCH AND BOUND ALGORITHM")
    result = calc_runtime(med_branch, s1, s2, 0, min(len(s1), len(s2))*0.1)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1])))
    print("RUNNING TIME :  %s seconds" % result[0])


if __name__ == "__main__":main()
