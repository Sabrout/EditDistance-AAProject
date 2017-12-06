import EditDistance as ed
import random
import string
import numpy as np
import matplotlib.pyplot as plt


# RANDOM STRING GENERATOR
def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def robust_generator():
    tester = ["" for x in range(100)]
    for i in range(0, 100):
        tester[i] = string_generator(i + 1)
    return tester


def substring_generator():
    example = string_generator(100)
    result = ["" for x in range(100)]
    for i in range(99, -1, -1):
        result[i - 1] = example
        example = example[:-1]
    return result


def experiment100():
    s1 = robust_generator()
    s2 = robust_generator()

    print("_____________________________________")
    print("CLASSIC DYNAMIC PROGRAMMING ALGORITHM")
    result = itrator100(normalize, ed.med_classic, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))

    print(" ")
    print("_________________")
    print("K STRIP ALGORITHM")
    result2 = itrator100(normalize, ed.med_k, s1, s2, 10)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result2[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result2[1]))

    print(" ")
    print("_____________________________")
    print("APPROXIMATED GREEDY ALGORITHM")
    result3 = itrator100(normalize_recursion, ed.med_greedy, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result3[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result3[1]))

    plotter(result[1], result2[1], result3[1])


# RUNTIME CALCULATOR
def itrator100(function, function2, s1, s2, *args):
    result = np.zeros(100)
    time = np.zeros(100)
    for i in range(10, 100):
        temp1, temp2 = ed.calc_runtime(function, function2, s1[i], s2[i], *args)
        time[i] = temp1
        result[i] = temp2[0]
    return np.average(result), np.delete(time, np.arange(0, 10))


# AVERAGE RUNTIME NORMALIZER
def normalize(function, s1, s2, *args):
    result = 0
    time = np.zeros(5)
    for i in range(0, time.size):
        temp1, temp2 = ed.calc_runtime(function, s1, s2, *args)
        time[i] = temp1
        result = temp2[0]
    return result, np.average(time)


def normalize_recursion(function, s1, s2, *args):
    result = 0
    time = np.zeros(100)
    for i in range(0, time.size):
        temp1, temp2 = ed.calc_runtime(function, s1, s2, *args)
        time[i] = temp1
        result = temp2
    return result, np.average(time)


def plotter(time, time2, time3):
    line_classic, = plt.plot(np.arange(10, 100), time, label='Classic DP')
    plt.setp(line_classic, color='r', linewidth=2.0)
    line_k, = plt.plot(np.arange(10, 100), time2, label='K Strip (K=10)')
    plt.setp(line_k, color='b', linewidth=2.0)
    line_greedy, = plt.plot(np.arange(10, 100), time3, label='Aprox. Greedy')
    plt.setp(line_greedy, color='g', linewidth=2.0)
    plt.legend(loc='upper left', handles=[line_classic, line_k, line_greedy])
    plt.xlabel('Length of Strings')
    plt.ylabel('Running Time')
    plt.title("Time Complexity Analysis")
    plt.show()


def main():
    experiment100()


if __name__ == "__main__":main()