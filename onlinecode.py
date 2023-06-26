import math

x = 227
is_prime = True

for i in range(2, math.isqrt(x) + 1):
    if x % i == 0:
        is_prime = False
        break

if is_prime:
    print("227 is a prime number.")
else:
    print("227 is not a prime number.")
