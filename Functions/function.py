# Create a function fibonacci_iterative that uses an iterative approach to create and
# print fibonacci numbers. This function should take 1 argument, num, which specifies
# how many fibonacci numbers to print out.


def fibonacci_iterative(num):
    pos1 = 0
    pos2 = 0
    currentSum = 0
    fibSum = 0
    for x in range(num):

        if x == 0:
            fibSum = 1

        if x == 1:
            fibSum = 2
        else:
            pos1 = fibSum
            pos2 = x
            fibSum = pos1 + pos2

        print(fibSum)

fibonacci_iterative(7)