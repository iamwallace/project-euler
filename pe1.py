# If we list all the natural numbers below 10 that are multiples 
# of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.



sum = 0


print("Please enter an upper bound for the sum of natural numbers. (e.g. 1000)")
input = int(input()) + 1


for x in range(1, input):
    if x % 3 == 0 or x % 5 == 0:
        sum += x

print("The sum of the natural numbers is: " + str(sum))








