# Find the greatest common denominator of two numbers
# using Euclid's algorithm
from et_xmlfile import xmlfile


def gcd(a, b) -> int:
    x: int
    found: bool = False
    top_num: int = min(a, b)
    # print("this is top num", top_num)
    x = top_num
    if a % b or b % a
    while not found:
        x -= 1
        if a % x == 0 and b % x == 0:
            found = True
            return x


# try out the function with a few examples
print(gcd(60, 12))  # should be 12

