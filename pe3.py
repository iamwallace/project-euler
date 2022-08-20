# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?



# to do
# return largest prime factor for input
# start with lowest prime factor and increment until square root of input
# check if even number
# need to keep dividing input by most recent factor
# return prime factor if greater than 2


import math



def findMaxPrimeFactor(n):
    result = 0

    while n % 2 == 0:
        result = 2
        n = n / 2

    for x in range(3, int(math.sqrt(n))+1, 2):
        while n % x == 0:
            result = x
            n = n / x

    if n > 2:
        result = n


    print("Largest prime factor for inputted number is: {}".format(result))


input = int(input("Enter value to find highest prime factor for: "))

findMaxPrimeFactor(input)

