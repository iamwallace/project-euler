# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting 
# numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.



global count
count = 1
maxChainLength = 1
startValue = 999999
bestStartValue = 0



def sequence(n):

    if n > 1:
        global count
        count += 1

        if n % 2 == 0:
            n = n / 2
            
        else:
            n = (3 * n) + 1

        sequence(n)

    

while startValue > 1:

    sequence(startValue)

    if count > maxChainLength:
        maxChainLength = count
        bestStartValue = startValue

    startValue -= 1
    count = 1


print("Starting value for longest chain length is: {}".format(bestStartValue))
print("Longest chain length is: {}".format(maxChainLength))



# Best start value is 837799
# Chain length for best start value is 525

