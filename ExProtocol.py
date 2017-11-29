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
    for i in range(1, 100):
        tester[i] = string_generator(i)
    return tester


def substring_generator():
    example = string_generator(100)
    result = ["" for x in range(100)]
    for i in range(99, 0, -1):
        result[i-1] = example
        example = example[:-1]
    return result


def experiment100():
    s1 = substring_generator()
    s2 = substring_generator()

    print("_____________________________________")
    print("CLASSIC DYNAMIC PROGRAMMING ALGORITHM")
    result = itrator100(ed.med_classic, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))
    plotter(result[1])

    print(" ")
    print("_________________")
    print("K STRIP ALGORITHM")
    result = itrator100(ed.med_k, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))
    plotter(result[1])


# RUNTIME CALCULATOR
def itrator100(function, s1, s2, *args):
    result = np.zeros(100)
    time = np.zeros(100)
    for i in range(1, 100):
        temp1, temp2 = ed.calc_runtime(function, s1, s2, *args)
        time[i] = temp1
        result[i] = temp2[0]
    return np.average(result), time


def plotter(time):
    plt.plot(np.arange(1, 101), time)
    plt.xlabel('Length of Strings')
    plt.ylabel('Running Time')
    plt.show()


def main():
    experiment100()


if __name__ == "__main__":main()