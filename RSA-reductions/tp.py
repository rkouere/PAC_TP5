import client
import random
from fractions import gcd
import sys


# resultat largement inspiré de 
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




# r = k
# t = 0

def get_t(k):
  t = 1
  r = k
  while True:
    if (r % 2 != 0):
      break
    r = r // 2
    t = t + 1
  return (r, t)

def mainLoop(g, k, n, r):
  y = pow(g, r, n)
  
  for i in range(1, 100):
    if y == 1 or y == -1:
      return None
    else:
      for j in range(1, t-1):
        x = pow(y, y, n)
        if x == 1:
          break
        elif x == n-1:
          return None
        y = x
      x = pow(y, y, n)
      if x == 1:
        return y
    print("prime factors not found")

# Let k = de – 1. If k is odd, then go to Step 4.
k = (e*d)-1
if k%2 != 0:
  print(k)
  print("prime factors not found")
  sys.exit()

y = None
(r, t) = get_t(k)
while not y:
  print("trying new one")
  g = random.randrange(0, n-1)
  y = mainLoop(g, k, n, r)
p = gcd(y-1, n)




print(serverObj.query(answer, {'p': p}))


