import random
import miller_rabin
from fractions import gcd


def generateBigPrime():
    print("=======================")
    print("Get prime")
    while True:
        prime = random.getrandbits(1025)
        if miller_rabin.is_probable_prime(prime):
            return prime

#param = serverObj.query(link_param)
def getTwoPrime(e):
    while True:
        p = generateBigPrime()


        q = generateBigPrime()

        if gcd(e, (p-1)*(q-1)) == 1:
            print("YEEEEEEEEEEEES")
            print("p = ")
            print(p)
            print("q = ")
            print(q)
            return p, q
            break
        else:
            print("NOOOOOOOONNNNNNNN")
            print("p = ")
            print(p)
            print("q = ")
            print(q)





# merci http://python.jpvweb.com/mesrecettespython/doku.php?id=pgcd_ppcm
def pgcd(a,b):
    """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    while b!=0:
        r=a%b
        a,b=b,r
    return a

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
 
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


