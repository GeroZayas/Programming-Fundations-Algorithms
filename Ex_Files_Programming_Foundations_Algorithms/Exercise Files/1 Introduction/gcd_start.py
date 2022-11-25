# Find the greatest common denominator of two numbers
# using Euclid's algorithm
import time

start_time = time.time()


def gcd(x, y) -> int:
    z: int
    found: bool = False
    top_num: int = min(x, y)
    # print("this is top num", top_num)
    z = top_num
    if x % y == 0 or y % x == 0:
        return top_num
    while not found:
        z -= 1
        if x % z == 0 and y % z == 0:
            found = True
            return z


# try out the function with a few examples
print(gcd(57596581, 49039424))  # should be 959

final_time = time.time() - start_time

print(f"\nTotal Exec Time => {final_time:.2f}")
