import EditDistance as ed
import random
import string
import numpy as np
import matplotlib.pyplot as plt
import random

# RANDOM STRING GENERATOR
def string_generator(size=10, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))


def robust_generator(size):
    tester = ["" for x in range(size)]
    for i in range(0, size):
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
    s1 = robust_generator(100)
    s2 = robust_generator(100)

    print("_____________________________________")
    print("CLASSIC DYNAMIC PROGRAMMING ALGORITHM")
    result = iterator(10, 100, normalize, ed.med_classic, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))

    print(" ")
    print("_________________")
    print("K STRIP ALGORITHM")
    result2 = iterator(10, 100, normalize, ed.med_k, s1, s2, 10)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result2[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result2[1]))

    print(" ")
    print("_____________________________")
    print("APPROXIMATED GREEDY ALGORITHM")
    result3 = iterator(10, 100, normalize_recursion, ed.med_greedy, s1, s2, 20)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result3[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result3[1]))

    print(" ")
    print("___________________________")
    print("BRANCH AND BOUND ALGORITHM")
    result4 = iterator(10, 100, normalize_recursion, ed.med_branch, s1, s2, 0, abs(len(s1) - len(s2)) + 2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result4[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result4[1]))

    print("____________________________")
    print("DIVIDE AND CONQUER ALGORITHM")
    result5 = iterator(10, 100, normalize_recursion, ed.calcByRow, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result5[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result5[1]))

    plotter_figure1(result[1], result2[1], result3[1], result4[1], result5[1])


def experiment_k():
    s1 = robust_generator(100)
    s2 = robust_generator(100)

    print("_____________________")
    print("K STRIP ALGORITHM [5]")
    result = iterator(50, 100, normalize, ed.med_k, s1, s2, 5)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))

    print(" ")
    print("______________________")
    print("K STRIP ALGORITHM [20]")
    result2 = iterator(50, 100, normalize, ed.med_k, s1, s2, 20)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result2[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result2[1]))

    print(" ")
    print("______________________")
    print("K STRIP ALGORITHM [45]")
    result3 = iterator(50, 100, normalize, ed.med_k, s1, s2, 45)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result3[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result3[1]))

    plotter_figure2(result[1], result2[1], result3[1])


def experiment_greedy():
    s1 = robust_generator(500)
    s2 = robust_generator(500)

    print("_________________________________")
    print("APPROXIMATED GREEDY ALGORITHM [1]")
    result = iterator(1, 500, normalize_recursion, ed.med_greedy, s1, s2, 1)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))

    print(" ")
    print("__________________________________")
    print("APPROXIMATED GREEDY ALGORITHM [10]")
    result2 = iterator(1, 500, normalize_recursion, ed.med_greedy, s1, s2, 10)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result2[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result2[1]))

    print(" ")
    print("__________________________________")
    print("APPROXIMATED GREEDY ALGORITHM [20]")
    result3 = iterator(1, 500, normalize_recursion, ed.med_greedy, s1, s2, 20)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result3[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result3[1]))

    plotter_figure3(result[1], result2[1], result3[1])


def experiment_recursive():
    s1 = robust_generator(10)
    s2 = robust_generator(10)

    print("__________________________")
    print("BRANCH AND BOUND ALGORITHM")
    result = iterator(1, 10, normalize_recursion, ed.med_branch, s1, s2, 0, abs(len(s1) - len(s2)) + 1000)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result[1]))

    print(" ")
    print("________________________")
    print("PURE RECURSIVE ALGORITHM")
    result2 = iterator(1, 10, normalize_recursion, ed.med_recursive, s1, s2)
    print(" ")
    print("{} {}".format("MINIMUM EDIT DISTANCE AVERAGE:", result2[0]))
    print("RUNNING TIME :  %s seconds" % np.sum(result2[1]))

    plotter_figure4(result[1], result2[1])


# RUNTIME CALCULATOR
def iterator(head_start, end, function, function2, s1, s2, *args):
    result = np.zeros(end)
    time = np.zeros(end)
    for i in range(head_start, end):
        temp1, temp2 = ed.calc_runtime(function, function2, s1[i], s2[i], *args)
        time[i] = temp1
        result[i] = temp2[0]
    return np.average(result), np.delete(time, np.arange(0, head_start))


# AVERAGE RUNTIME NORMALIZER
def normalize(function, s1, s2, *args):
    result = 0
    time = np.zeros(50)
    for i in range(0, time.size):
        temp1, temp2 = ed.calc_runtime(function, s1, s2, *args)
        time[i] = temp1
        result = temp2[0]
    return result, np.average(time)


def normalize_recursion(function, s1, s2, *args):
    result = 0
    time = np.zeros(50)
    for i in range(0, time.size):
        temp1, temp2 = ed.calc_runtime(function, s1, s2, *args)
        time[i] = temp1
        result = temp2
    return result, np.average(time)


def plotter_figure1(time, time2, time3, time4, time5):
    line_classic, = plt.plot(np.arange(10, 100), time, label='Classic DP')
    plt.setp(line_classic, color='r', linewidth=2.0)
    line_k, = plt.plot(np.arange(10, 100), time2, label='K Strip (K=10)')
    plt.setp(line_k, color='b', linewidth=2.0)
    line_greedy, = plt.plot(np.arange(10, 100), time3, label='Aprox. Greedy')
    plt.setp(line_greedy, color='g', linewidth=2.0)
    line_branch, = plt.plot(np.arange(10, 100), time4, label='Branch and Bound')
    plt.setp(line_branch, color='k', linewidth=2.0)
    line_divide, = plt.plot(np.arange(10, 100), time5, label='Divide and Conquer')
    plt.setp(line_divide, color='c', linewidth=2.0)
    plt.legend(loc='upper left', handles=[line_classic, line_k, line_greedy, line_branch, line_divide])
    plt.xlabel('Length of Strings')
    plt.ylabel('Running Time')
    plt.title("Time Complexity Analysis")
    plt.show()


def plotter_figure2(time, time2, time3):
    line1, = plt.plot(np.arange(50, 100), time, label='K Strip (K=5)')
    plt.setp(line1, color='r', linewidth=2.0)
    line2, = plt.plot(np.arange(50, 100), time2, label='K Strip (K=20)')
    plt.setp(line2, color='b', linewidth=2.0)
    line3, = plt.plot(np.arange(50, 100), time3, label='K Strip (K=45)')
    plt.setp(line3, color='g', linewidth=2.0)
    plt.legend(loc='upper left', handles=[line1, line2, line3])
    plt.xlabel('Length of Strings')
    plt.ylabel('Running Time')
    plt.title("Time Complexity Analysis")
    plt.show()


def plotter_figure3(time, time2, time3):
    line1, = plt.plot(np.arange(1, 500), time, label='Greedy (Lookahead=1)')
    plt.setp(line1, color='r', linewidth=2.0)
    line2, = plt.plot(np.arange(1, 500), time2, label='Greedy (Lookahead=10)')
    plt.setp(line2, color='b', linewidth=2.0)
    line3, = plt.plot(np.arange(1, 500), time3, label='Greedy (Lookahead=20)')
    plt.setp(line3, color='g', linewidth=2.0)
    plt.legend(loc='upper left', handles=[line1, line2, line3])
    plt.xlabel('Length of Strings')
    plt.ylabel('Running Time')
    plt.title("Time Complexity Analysis")
    plt.show()


def plotter_figure4(time, time2):
    line1, = plt.plot(np.arange(1, 10), time, label='Branch and Bound')
    plt.setp(line1, color='r', linewidth=2.0)
    line2, = plt.plot(np.arange(1, 10), time2, label='Pure Recursive')
    plt.setp(line2, color='b', linewidth=2.0)
    plt.legend(loc='upper left', handles=[line1, line2])
    plt.xlabel('Length of Strings')
    plt.ylabel('Running Time')
    plt.title("Time Complexity Analysis")
    plt.show()


####################################################
# Protein Database Processing
def protein_database_parser(counter):
    database = list()
    file = open("ProteinDatabase.txt", "r")
    temp = ""
    read_flag = False
    for line in file:
        if counter == 0:
            break
        # print(counter)
        if not line:
            # print(10)
            continue
        if line[0] == '>' and not read_flag:
            # print(20)
            read_flag = True
            continue
        if line[0] != '>' and read_flag:
            # print(30)
            # [:-2] to remove \n
            temp += line[:-2]
            continue
        if line[0] == '>' and read_flag:
            # print(40)
            database.append(temp)
            # print(temp)
            temp = ""
            counter -= 1
            continue
    file.close()
    return database


def protein_database_processor(data):
    result = np.arange(data.__len__())
    for i in range(0, data.__len__()):
        result[i] = ed.med_classic(data[0], data[i])[0]
        # print(result[i])
    return result


def experiment_protein_database(k_nearest, batch=6222):
    data = protein_database_parser(batch)
    # for line in data:
    #     print(line)
    result = protein_database_processor(data)
    index = np.arange(result.__len__())
    clusters = list()
    # Initial Cluster
    temp_list = list()
    temp_list.append((0, 0))
    clusters.append(temp_list)
    counter = -1
    for i in result:
        counter += 1
        # Temp Distance
        temp = np.zeros(clusters.__len__())
        for k in range(0, clusters.__len__()):
            # print(i, clusters[k][0])
            # print(j)
            temp[k] = abs(i - clusters[k][0][1])
        # Update Clusters
        min_index = np.argmin(temp)
        for k in range(0, clusters.__len__()):
            if k == min_index:
                # print(clusters[k][0], i, k_nearest, 111111111111)
                if abs(clusters[k][0][1] - i) <= k_nearest:
                    clusters[k].append((counter, i))
                else:
                    temp_list = list()
                    temp_list.append((counter, i))
                    clusters.append(temp_list)
        # print(temp)
    for line in clusters:
        print(line)
    plotter_figure5(clusters, batch)


def random_color():
    rgbl=[255,0,0]
    random.shuffle(rgbl)
    return tuple(rgbl)


def plotter_figure5(list, batch):
    colors = np.zeros(list.__len__())
    counter = -1
    for cluster in list:
        counter += 1
        x = np.zeros(cluster.__len__())
        y = np.zeros(cluster.__len__())
        z = np.empty(cluster.__len__())
        colors[counter] = counter
        for entry in cluster:
            x = entry[0]
            y = entry[1]
            z = counter
        area = cluster.__len__()*100*(1/(0.01*batch))
        plt.scatter(y, z, c=("#%06x" % random.randint(0, 0xFFFFFF)), s=area)

    # x = [1, 2, 3, 4, 5, 6, 7, 8]
    # y = [1, 2, 3, 4, 5, 6, 7, 8]
    # colors = [1, 2, 3, 4, 5, 6, 7, 8]

    # plt.scatter(x, y, c=colors)
    plt.show()


def main():
    experiment100()
    # experiment_k()
    # experiment_greedy()
    # experiment_recursive()
    # experiment_protein_database(25, 6222)




if __name__ == "__main__":main()