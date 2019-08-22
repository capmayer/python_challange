import time

import multiprocessing as mp

# use a tupla of min and max to define the ranges
# CAN BE OTIMIZED
ranges = [(1, 50000), (50000, 60000), (60000, 80000), (80000, 90000), (90000, 100000)]

# this func check if number is a perfect natural
# can also be done using a form 2^(n-1)-(2^n -1)
def is_perfect_natural(number):
    sum = 0
    for x in range(1, number):
        if(number%x == 0):
            sum += x
    if (number == sum):
        print(number, " is perfect")

    return 0

# this function is used to split the execution of is_perfect_natural()
def mult_check(min, max):
    for x in range(min, max):
        is_perfect_natural(x)


if __name__ == '__main__':
    op = 0
    while(op != 3):
        # user info and input
        print("Options to execute this program: ")
        print("1 - Using multiprocessing (5 processes)")
        print("2 - Not using multiprocessing")
        print("3 - Exit")
        op = input()

        if op == "1":
            t = time.time()
            jobs = []
            for min, max in ranges:
                p = mp.Process(target=mult_check, args=(min,max))
                jobs.append(p)
                p.start()

            for j in jobs:
                j.join()

            print("Done with multi, time: ", time.time()-t)
        else:
            t = time.time()
            for x in range(1, 100000):
                is_perfect_natural(x)

            print("Done, time: ", time.time()-t)
