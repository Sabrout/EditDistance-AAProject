import numpy as np
import random
import string
import time
import copy


# INITIALIZATION
def init(s1, s2):
    m = np.empty((len(s1) + 1, len(s2) + 1))
    m[:] = np.inf
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
    return m[m.shape[0] - 1][m.shape[1] - 1], m


def med_classic_gui(s1, s2):
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

    # Alignment
    zero = 0
    mm = np.c_[[zero] * len(m[:]), m]
    mmm = np.r_[[[zero] * len(mm[1, :])], mm]
    backmatrix = [[' ' for y in range(len(s2) + 2)] for x in range(len(s1) + 2)]
    backmatrix[1][1] = 0

    for i in range(2, len(s1) + 2):
        backmatrix[i][0] = s1[i - 2]
    for j in range(2, len(s2) + 2):
        backmatrix[0][j] = s2[j - 2]

    for i in range(2, len(s1) + 2):
        backmatrix[i][1] = '|'

    for j in range(2, len(s2) + 2):
        backmatrix[1][j] = '-'

    for i in range(2, len(s1) + 2):
        for j in range(2, len(s2) + 2):
            vertical = mmm[i - 1][j] + 1
            horizontal = mmm[i][j - 1] + 1
            if s1[i - 2] == s2[j - 2]:
                diagonal = mmm[i - 1][j - 1]
            else:
                diagonal = mmm[i - 1][j - 1] + 1

            mindist = min(diagonal, vertical, horizontal)
            mmm[i][j] = mindist

            if mindist == diagonal:
                backmatrix[i][j] = 'bn'
            elif mindist == vertical:
                backmatrix[i][j] = '|'
            else:
                backmatrix[i][j] = '-'

    ss1 = ""
    ss2 = ""
    op = ""

    i = len(s1) + 1
    j = len(s2) + 1
    while not (i == 1 and j == 1):
        c = backmatrix[i][j]
        if c == '|':
            ss1 += s1[i - 2] + ' '
            ss2 += '-' + ' '
            op += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            ss1 += s1[i - 2] + ' '
            ss2 += s2[j - 2] + ' '
            if s1[i - 2] == s2[j - 2]:
                op += '|' + ' '
            else:
                op += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            ss1 += '-' + ' '
            ss2 += s2[j - 2] + ' '
            op += ' ' + ' '
            j = j - 1

    print("")
    print("ALIGNMENT:")
    print("")
    print(ss1[::-1])
    print(op[::-1])
    print(ss2[::-1])

    # printing result and running time
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(m[m.shape[0] - 1][m.shape[1] - 1])))
    return m[m.shape[0] - 1][m.shape[1] - 1], ss1[::-1], op[::-1], ss2[::-1]


# K STRIP ALGORITHM
def med_k(s1, s2, k=1):
    if len(s1) > len(s2):
        temp = s1
        s1 = s2
        s2 = temp
    # K value exception
    if k > min((len(s1)), (len(s2))) or k < 1:
        raise Exception('K VALUE OUT OF BOUNDS')

    # INITIALIZATION
    m = init(s1, s2)

    # Offset counter
    offset = - (k-2)
    # Limit counter
    cap = k + 1 + abs(len(s1) - len(s2))
    # Loop for K strips around the main diagonal
    for i in range(1, m.shape[0]):
        for j in range(max(1, offset), cap):
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
            # print("con1: {} con2: {} con3: {} min: {}".format(con1, con2, con3, m[i][i]))
            # Saving Result
        offset += 1
        if cap < m.shape[1]:
            cap += 1
    return m[m.shape[0] - 1][m.shape[1] - 1], m


def med_k_gui(s1, s2, k=1):
    k = int(k)
    # K value exception
    if k > min((len(s1)), (len(s2))) or k < 1:
        raise Exception('K VALUE OUT OF BOUNDS')

    # INITIALIZATION
    m = init(s1, s2)

    # Offset counter
    offset = - (k - 2)
    # Limit counter
    cap = k + 1 + abs(len(s1) - len(s2))
    # Loop for K strips around the main diagonal
    for i in range(1, m.shape[0]):
        for j in range(max(1, offset), cap):
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
            # print("con1: {} con2: {} con3: {} min: {}".format(con1, con2, con3, m[i][i]))
            # Saving Result
        offset += 1
        if cap < m.shape[1]:
            cap += 1

    # Alignment
    zero = 0
    mm = np.c_[[zero] * len(m[:]), m]
    mmm = np.r_[[[zero] * len(mm[1, :])], mm]

    backmatrix = [[' ' for y in range(len(s2) + 2)] for x in range(len(s1) + 2)]
    backmatrix[1][1] = 0

    for i in range(2, len(s1) + 2):
        backmatrix[i][0] = s1[i - 2]
    for j in range(2, len(s2) + 2):
        backmatrix[0][j] = s2[j - 2]

    for i in range(2, len(s1) + 2):
        backmatrix[i][1] = '|'

    for j in range(2, len(s2) + 2):
        backmatrix[1][j] = '-'

    for i in range(2, len(s1) + 2):
        for j in range(2, len(s2) + 2):
            vertical = mmm[i - 1][j] + 1  # DEL
            horizontal = mmm[i][j - 1] + 1  # INS
            if s1[i - 2] == s2[j - 2]:
                diagonal = mmm[i - 1][j - 1]
            else:
                diagonal = mmm[i - 1][j - 1] + 1  # SUB

            mindist = min(diagonal, vertical, horizontal)
            mmm[i][j] = mindist

            if mindist == diagonal:
                backmatrix[i][j] = 'bn'
            elif mindist == vertical:
                backmatrix[i][j] = '|'
            else:
                backmatrix[i][j] = '-'
    ss1 = ""
    ss2 = ""
    op = ""

    i = len(s1) + 1
    j = len(s2) + 1
    while not (i == 1 and j == 1):
        c = backmatrix[i][j]
        if c == '|':
            ss1 += s1[i - 2] + ' '
            ss2 += '-' + ' '
            op += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            ss1 += s1[i - 2] + ' '
            ss2 += s2[j - 2] + ' '
            if s1[i - 2] == s2[j - 2]:
                op += '|' + ' '
            else:
                op += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            ss1 += '-' + ' '
            ss2 += s2[j - 2] + ' '
            op += ' ' + ' '
            j = j - 1

    print(ss1[::-1])
    print(op[::-1])
    print(ss2[::-1])

    # printing result and running time
    return m[m.shape[0] - 1][m.shape[1] - 1], m, ss1[::-1], op[::-1], ss2[::-1]


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
    con1 = med_recursive(s1[:-1], s2) + 1  # Deletion
    con2 = med_recursive(s1, s2[:-1]) + 1  # Insertion
    con3 = med_recursive(s1[:-1], s2[:-1]) + (s1[-1] != s2[-1])  # Substitution

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
    temp = max(len(s1), len(s2))
    con1, con2, con3 = temp, temp, temp
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
        print("INTEGER EXCEPTION")
        raise ("INTEGER EXCEPTION")
    return min(con1, con2, con3)


# APPROXIMATED GREEDY ALGORITHM
def med_greedy(s1, s2, lookahead=3):
    n = len(s1)
    m = len(s2)
    difference = abs(m - n)
    # base cases
    if n == 0 and m == 0:
        return 0
    if n == 0:
        return m
    if m == 0:
        return n
    # Greedy Approach
    if difference > lookahead - 1 and m > lookahead - 1 and n > lookahead - 1:
        if n > m:
            return med_greedy(s1[:-lookahead], s2) + lookahead  # Deletion
        if m > n:
            return med_greedy(s1, s2[:-lookahead]) + lookahead  # Insertion
        if m == n:
            temp = 0
            for k in range(1, lookahead + 1):
                if s1[-k] != s2[-k]:
                    temp += 1
            return med_greedy(s1[:-lookahead], s2[:-lookahead]) + temp  # Substitution
    else:
        if n > m:
            return med_greedy(s1[:-1], s2) + 1  # Deletion
        if m > n:
            return med_greedy(s1, s2[:-1]) + 1  # Insertion
        if m == n:
            return med_greedy(s1[:-1], s2[:-1]) + (s1[-1] != s2[-1])  # Substitution


# DIVIDE AND CONQUER APPROACH
def calcByRow(x, y):
    prev = np.arange(0, len(y) + 1)
    curr = np.zeros(len(y) + 1)
    for i in range(1,len(y)+1):
        prev[i]= prev[i-1]+1
    for i in range(1, len(x) + 1):
            curr[0] += 1
            for j in range(1, len(y) + 1):
                ins = curr[j - 1] + 1
                dele = prev[j] + 1
                if x[i - 1] == y[j - 1]:
                    sub = prev[j - 1]
                else:
                    sub = prev[j - 1] + 1
                curr[j] = min(ins, dele, sub)
            prev = copy.deepcopy(curr)
    # hirschberge(x, y)
    return curr

def calcByRow_experiment(x, y):
    prev = np.arange(0, len(y) + 1)
    curr = np.zeros(len(y) + 1)
    for i in range(1,len(y)+1):
        prev[i]= prev[i-1]+1
    for i in range(1, len(x) + 1):
            curr[0] += 1
            for j in range(1, len(y) + 1):
                ins = curr[j - 1] + 1
                dele = prev[j] + 1
                if x[i - 1] == y[j - 1]:
                    sub = prev[j - 1]
                else:
                    sub = prev[j - 1] + 1
                curr[j] = min(ins, dele, sub)
            prev = copy.deepcopy(curr)
    # hirschberge(x, y)
    return curr[-1]

def split(scoreF, scoreR):
    # scoreF front forward, scoreR Buttom up(Reversed)
    splitIndex = 0
    # to locate the best partition (part of the solution)
    minSum = np.inf
    for i, (f, r) in enumerate(zip(scoreF, scoreR[::-1])):
        # calculate the diagonal minimum index
        # iterating over the scores and their indexes
        if sum([f, r]) < minSum:
            minSum = sum([f, r])
            splitIndex = i
    return splitIndex

# Minimum Edit Distance (MED)
# Divide and Conquer DP
def hirschberge(x,y):
    firstString = ""
    secondString = ""
    operations = ""
    if len(x) <= 2 or len(y) <= 2:
        r = med_classicdq(x, y)
        return r
    else:
        xmiddle = int(len(x)/2)
        scoreL = calcByRow(x[:xmiddle], y)
        scoreR = calcByRow(x[xmiddle:][::-1], y[::-1])
        ymid = split(scoreL, scoreR)
        rowLeft, operationsLU, columnUp  = hirschberge(x[:xmiddle], y[:ymid])
        rowRight, operationsRD, columnDown  = hirschberge(x[xmiddle:], y[ymid:])
        firstString = rowLeft + rowRight
        operations = operationsLU + operationsRD
        secondString = columnUp + columnDown

    # if sys.exi
    # print(firstString)
    # print(operations)
    # print(secondString)
    #  editDistance = calcByRow(firstString,secondString)
    # print(editDistance[-1])
    return firstString, operations, secondString

# CLASSIC DYNAMIC PROGRAMMING ALGORITHM USED FOR DIVIDE AND CONQURE
def med_classicdq(s1,s2):
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

    # Alignment
    zero = 0
    mm = np.c_[[zero] * len(m[:]), m]
    mmm = np.r_[[[zero] * len(mm[1, :])], mm]
    backmatrix = [[' ' for y in range(len(s2) + 2)] for x in range(len(s1) + 2)]
    backmatrix[1][1] = 0

    for i in range(2, len(s1) + 2):
        backmatrix[i][0] = s1[i - 2]
    for j in range(2, len(s2) + 2):
        backmatrix[0][j] = s2[j - 2]

    for i in range(2, len(s1) + 2):
        backmatrix[i][1] = '|'

    for j in range(2, len(s2) + 2):
        backmatrix[1][j] = '-'

    for i in range(2, len(s1) + 2):
        for j in range(2, len(s2) + 2):
            vertical = mmm[i - 1][j] + 1
            horizontal = mmm[i][j - 1] + 1
            if s1[i - 2] == s2[j - 2]:
                diagonal = mmm[i - 1][j - 1]
            else:
                diagonal = mmm[i - 1][j - 1] + 1

            mindist = min(diagonal, vertical, horizontal)
            mmm[i][j] = mindist

            if mindist == diagonal:
                backmatrix[i][j] = 'bn'
            elif mindist == vertical:
                backmatrix[i][j] = '|'
            else:
                backmatrix[i][j] = '-'

    ss1 = ""
    ss2 = ""
    op = ""

    i = len(s1) + 1
    j = len(s2) + 1
    while not (i == 1 and j == 1):
        c = backmatrix[i][j]
        if c == '|':
            ss1 += s1[i - 2] + ' '
            ss2 += '-' + ' '
            op += ' ' + ' '
            i = i - 1
        elif c == 'bn':
            ss1 += s1[i - 2] + ' '
            ss2 += s2[j - 2] + ' '
            if s1[i - 2] == s2[j - 2]:
                op += '|' + ' '
            else:
                op += ' ' + ' '
            i = i - 1
            j = j - 1
        else:
            ss1 += '-' + ' '
            ss2 += s2[j - 2] + ' '
            op += ' ' + ' '
            j = j - 1
    return ss1[::-1],op[::-1], ss2[::-1]


# RUNTIME CALCULATOR
def calc_runtime(function, *args):
    start_time = time.time()
    result = function(*args)
    return time.time() - start_time, result

# Runtime Calculation for GUI (Rohil)
def calc_runtime_md(function, *args):
    if function == med_classic_gui:
        start_time = time.time()
        result = function(*args)[0]
        result2 = function(*args)[1]
        result3 = function(*args)[2]
        result4 = function(*args)[3]
        return time.time() - start_time, result, result2, result3, result4
    if function == med_k_gui:
        start_time = time.time()
        result = function(*args)[0]
        result1 = function(*args)[1]
        result2 = function(*args)[2]
        result3 = function(*args)[3]
        result4 = function(*args)[4]
        return time.time() - start_time, result, result1, result2, result3, result4

    if function == calcByRow:
        start_time = time.time()
        result = function(*args)[-1]
        result1 = function(*args)[1]
        # result2= function(*args)[2]
        # result3= function(*args)[3]

        return time.time() - start_time, result

    if function == med_recursive or function == med_greedy or function == med_branch:
        # print(" Anything")
        start_time = time.time()
        result = function(*args)
        return time.time() - start_time, result


# RANDOM STRING GENERATOR
def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def main():
    # s1 = "INTENTION"
    # s2 = "EXECUTION"
    s1 = string_generator(6)
    s2 = string_generator(10)

    print('String #1 : ' + s1)
    print('String #2 : ' + s2)

    # CLASSIC DYNAMIC PROGRAMMING ALGORITHM
    print("_____________________________________")
    print("CLASSIC DYNAMIC PROGRAMMING ALGORITHM")
    result = calc_runtime(med_classic, s1, s2)

    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1][0])))
    print("RUNNING TIME :  %s seconds" % result[0])
    # Printing Matrix
    print("")
    print(result[1][1])

    # K STRIP ALGORITHM
    print("_________________")
    print("K STRIP ALGORITHM")
    k = 1
    result = calc_runtime(med_k_gui, s1, s2, k)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1][0])))
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

    # BRANCH AND BOUND ALGORITHM
    print("__________________________")
    print("BRANCH AND BOUND ALGORITHM")
    result = calc_runtime(med_branch, s1, s2, 0, abs(len(s1) - len(s2)) + 1)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1])))
    print("RUNNING TIME :  %s seconds" % result[0])

    # APPROXIMATED GREEDY ALGORITHM
    print("_____________________________")
    print("APPROXIMATED GREEDY ALGORITHM")
    result = calc_runtime(med_greedy, s1, s2, 50)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1])))
    print("RUNNING TIME :  %s seconds" % result[0])

    # DIVIDE AND CONQUER ALGORITHM
    print("____________________________")
    print("DIVIDE AND CONQUER ALGORITHM")
    result = calc_runtime(calcByRow, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE :", int(result[1][-1])))
    print("RUNNING TIME :  %s seconds" % result[0])


if __name__ == "__main__": main()