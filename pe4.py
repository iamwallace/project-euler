# A palindromic number reads the same both ways. The largest palindrome 
# made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.




maxProduct = 0
first = 999
second = first
finalFirst = 0
finalSecond = 0


def isPalindrome(n):
    reversed = str(n)[::-1]
    return reversed == str(n)


while first > 0:
    while second > 0:
        currentProduct = first * second

        if isPalindrome(currentProduct) and currentProduct > maxProduct:
            maxProduct = currentProduct
            finalFirst = first
            finalSecond = second

        second -= 1
    
    first -= 1
    second = first


print("The max palindromic product is: {}".format(maxProduct))
print("The factors for the product are: {first} and {second}".format(first=finalFirst, second=finalSecond))




