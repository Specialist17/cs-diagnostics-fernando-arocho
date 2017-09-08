# Write an algorithm (in English) that takes two inputs,
# start and end that prints every number from start to end (inclusive).
# However, if a number is evenly divisible by 3, print the word “fizz” instead of the number.
# If a number is evenly divisible by 5, print “buzz” instead of the number.
# If a number is evenly divisible by both 3 and 5, print “fizzbuzz” instead of the number.


# def func(start, end):
#     for x in range(start, end):
#         if (x modulus 3 == 0)
#             print("fizz")
#         elif (x modulus 5 == 0):
#             print("buzz")
#         elif (x mod 5 == 0 && x mod 3 == 0):
#             print("fizzbuzz")
#         else:
#             print(x)


def func(start, end):
    for x in range(start, end):

        if x%5 == 0 and x%3 == 0:
            print("fizzbuzz")
        elif x%3 == 0:
            print("fizz")
        elif x%5 == 0:
            print("buzz")

        else:
            print(x)



func(1, 31)