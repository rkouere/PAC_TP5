import client


# ex
# hash_object = hashlib.sha224(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

#merci http://stackoverflow.com/questions/2489435/how-could-i-check-if-a-number-is-a-perfect-square
def is_square(apositiveint):
  x = apositiveint// 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

def isqrt(n):
  """ renvoie le plus grand entier k tel que k^2 <= n. Méthode de Newton."""
  x = n
  y = (x + 1) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x


URL = "http://pac.bouillaguet.info/TP5"
link_param = "/RSA-reductions/phi/challenge/echallier"
answer = "/RSA-reductions/phi/check/echallier"

serverObj = client.Server(URL)

reply = serverObj.query(link_param)

a = 1
n = reply['n']
c = n
phi = reply['phi']
e = reply['e']

b = (n - phi + 1)

racine_carre = isqrt((b*b)-(4*a*c))

p_1 = (-b + racine_carre)//(2*a)
p_2 = (-b - racine_carre)//(2*a)

print(abs(p_1))
print(abs(p_2))
print('==========')
print(n)
print(p_1*p_2)
print(serverObj.query(answer, {'p': abs(p_1)}))

#PubK = (n, b)
#private = (p, q)





# while True:
#     k = random.getrandbits(1025)
#     if k > 2:
#         if gcd(k, q) == 1:
#             r = pow(g, k, p)
#             s = (m-(x*r)


#print(serverObj.query(confirmation, {'m':dechifre}))
