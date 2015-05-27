import client
import tools
import hashlib
import random
import base64
from prime import *

# ex
# hash_object = hashlib.sha224(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

#merci http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
def is_square(apositiveint, n):
  x = (apositiveint // 2) % n
  seen = set([x])
  while ((x * x) % n) != apositiveint:
    x = ((x + (apositiveint // x)) // 2) % n
    if x in seen: return False
    seen.add(x)
  return True



def modular_sqrt(a, p):
    """ Find a quadratic residue (mod p) of 'a'. p
        must be an odd prime.

        Solve the congruence of the form:
            x^2 = a (mod p)
        And returns x. Note that p - x is also a root.

        0 is returned is no square root exists for
        these a and p.

        The Tonelli-Shanks algorithm is used (except
        for some simple cases in which the solution
        is known from an identity). This algorithm
        runs in polynomial time (unless the
        generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
      print("!=1")
      return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) // 4, p)

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s //= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) // 2, p)
    b = pow(a, s, p)
    g = pow(n, s, p)
    r = e

    while True:
        t = b
        m = 0
        for m in xrange(r):
            if t == 1:
                break
            t = pow(t, 2, p)

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1), p)
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """ Compute the Legendre symbol a|p using
        Euler's criterion. p is a prime, a is
        relatively prime to p (if p divides
        a, then a|p = 0)

        Returns 1 if a has a square root modulo
        p, -1 otherwise.
    """
    ls = pow(a, (p - 1) // 2, p)
    return -1 if ls == p - 1 else ls


def verif_racine(a, p, m):
  if pow(a, (p-1)//2, m) == 1:
    return True
  else:
    return False









URL = "http://pac.bouillaguet.info/TP5"
link_param = "/Rabin-signature/challenge/echallier"
answer = "/Rabin-signature/check/echallier"
confirmation = "/RSA-keygen/confirmation/echallier"


e =  535890187425344683208917930322408044245

# p , q = getTwoPrime(e)



serverObj = client.Server(URL)


p = 149871785728579182396703271816299099873001060324575983421025587324900435803056211136994970988927902368053477195910956420297694135510960420725550584373924192352775664985349082909208125965761589285929622659555333145638351401655820104432344150933805923656171234502339942329190475047812809441414703978437915464723
q = 54113125071191506049104426408467902839327059545023923729910087555523014930599677689696290292472681943278315949919086032078133860483659657532440215705072806937704107173225770437960492299815202226996494687841070574295324504028731689170296453418933353089902271451409878723916220985110353309612850717211686137579
phi = (p-1)*(q-1)
d = tools.modinv(e, phi)
n = p*q



return_server = serverObj.query(link_param, {'n': n})
cpt = 1


#while cpt == 1:
while True:
  u_int = random.randint(1, n)
  u = "{0:x}".format(u_int)
  m = return_server['m'].encode()
  y = hashlib.sha256(m+str(u_int).encode())
  y = int(y.hexdigest(), base=16)
  if modular_sqrt(y, n) != 0:
    print("==========================")
    print("YIPPPPPPPPPI")
    print(y)
    break
  cpt += 1
  print(m)
  print(u_int)
  print(u)
  print(y)
  print(cpt)
#s = modular_sqrt(y, n)
#print(serverObj.query(answer, {'n': n, 's': s, 'u': u}))

# while True:
#   try:
#     u_int = random.randint(1, n)
#     u = "{0:x}".format(u_int)
#     m = return_server['m'].encode()    
#     y = hashlib.sha256(m+u.encode())
#     y = int(y.hexdigest(), base=16)
#     s = modular_sqrt(y, n)
#     print(serverObj.query(answer, {'n': n, 's': s, 'u': u}))
#   except:
#     print("try again")

