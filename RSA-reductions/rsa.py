import random
import fractions

# TRICHE
# http://crypto.stackexchange.com/questions/6361/is-sharing-the-modulus-for-multiple-rsa-key-pairs-secure/14713

# ex
# hash_object = hashlib.sha224(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)



# Returns a tuple (r, t) | n = r*2^t
# Complexity O(lg n)*
def remove_even(n):
    if n == 0:
        return (0, 0)
    r = n
    t = 0
    while (r & 1) == 0:
        t = t + 1
        r = r >> 1
    return (r, t)

# Returns a non-trivial sqrt(1) mod N, or None
# Arguments:
#     x: random integer 2 <= x < N
#     k: multiple of lambda(N)
#     N: modulus
# Complexity O((lg n)^3)
def get_root_one(x, k, N):
    (r, t) = remove_even(k)
    oldi = None
    i = pow(x, r, N)
    while i != 1:
        oldi = i
        i = (i*i) % N
    if oldi == N-1:
        return None #trivial
    return oldi

# Returns a tuple (p, q) that are 
# the prime factors of N, given an
# RSA key (e, d, N)
def factor_rsa(e, d, N):
    k = e*d - 1
    y = None
    while not y:
        x = random.randrange(2, N)
        y = get_root_one(x, k, N)
    p = fractions.gcd(y-1, N)
    q = N // p
    return (p, q)
