import client
import rsa
import random
from fractions import gcd




# voir http://stackoverflow.com/questions/2921406/calculate-primes-p-and-q-from-private-exponent-d-public-exponent-e-and-the
# reponse 3

URL = "http://pac.bouillaguet.info/TP5"
link_param = "/RSA-reductions/d/challenge/echallier"
answer = "/RSA-reductions/d/check/echallier"

serverObj = client.Server(URL)

reply = serverObj.query(link_param)
a = 1
d = reply['d']
n = reply['n']
e = reply['e']

p = None
q = None

k = (e*d)-1
r = k
t = 0

def get_t(r):
  while True:
    if (r % 2 != 0) and k == pow(2, t) * r:
      break
    r = r // 2
    t = t + 1
    return (r, t)

x = random.randrange(2, n)

expo = 2
old = None

while True:
  if expo > pow(2, t):
  s = pow(x, (k // expo), n) 
  if s != 1 and old == 1:
    p = gcd(s-1, n)
    q = n // p
  oldi = s
  expo = expo * 2



factors = rsa.factor_rsa(e, d, n)

print(serverObj.query(answer, {'p': p}))


