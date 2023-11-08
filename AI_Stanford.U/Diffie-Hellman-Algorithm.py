import secrets
def prime_checker(p):
    # Checks If the number entered is a Prime Number or not
    if p < 1:
        return -1
    elif p > 1:
        if p == 2:
            return 1
        for i in range(2, p):
            if p % i == 0:
                return -1
        return 1
def primitive_check(g, p):
    # Checks If The Entered Number Is A Primitive Root Or Not
    L = []
    for i in range(1, p):
        L.append(pow(g, i) % p)
    for i in range(1, p):
        if L.count(i) > 1:
            L.clear()
            return -1
        return 1

"""Generate a secure random prime number, I Limited this to 7000(13 prime number bits) due to local cumputing power.
larger prime numbers also require more computational power to generate and use, so there is a trade-off between security and performance.
768 prime bits is good, 1024 is better, 2048 is best excluding quantum computational power maturity."""

while True:
    P = secrets.randbelow(7000)  
    if prime_checker(P) == -1:
        continue
    break

while True:
    G = secrets.randbelow(P - 1)  # Generate a secure random primitive root of the prime number
    if primitive_check(G, P) == -1:
        continue
    break

L = []  # Initialize the L list

# Generate secure and random private keys
x1 = secrets.randbelow(P - 1)  
x2 = secrets.randbelow(P - 1)

# Calculate Public Keys
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Generate Secret Keys
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\nSecret Key For Bob Is {k1}\nSecret Key For Alice Is {k2}\n")

if k1 == k2:
    print("Keys Have Been Exchanged Successfully")
else:
    print("Keys Have Not Been Exchanged Successfully")