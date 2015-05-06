import client
import tools
import hashlib
import random
import base64


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


URL = "http://pac.bouillaguet.info/TP5"
link_param = "/Rabin-signature/challenge/echallier"
answer = "/RSA-keygen/PK/echallier"
confirmation = "/RSA-keygen/confirmation/echallier"

serverObj = client.Server(URL)

e =  535890187425344683208917930322408044245

p = 277461027049854810288405758908172098629253435446959073090615700876807909390843667708032667263836741272893300164600643617600904696366008257486465679283070534258115902100961955522211170750181191229411454331047399566105121104637984719523302928584689237682786859691245578154493434772170438439978284764756836074199
q = 170546191165200071045408843438399129154545534123331514137997529965617229025417495160698071473291750491846942018957300308523616269031865565796522642357711473326380517067249236995772562816300987333175837191239786364745310750596411786403167126078819373310363468430133540610399083878706320397608768367315686273137
phi = (p-1)*(q-1)
d = tools.modinv(e, phi)
n = p*q

while True:
    u = random.getrandbits(16)
    m = b'4d98f61df87dfdd61bbefdaffa78de1c'    
    y = hashlib.sha256(m+bytes(u))
    y = int(y.hexdigest(), base=16)
    if is_square(y):
        break

print("===============================")
print("u = ")
print(u)



#PubK = (n, b)
#private = (p, q)





# while True:
#     k = random.getrandbits(1025)
#     if k > 2:
#         if gcd(k, q) == 1:
#             r = pow(g, k, p)
#             s = (m-(x*r)


#print(serverObj.query(confirmation, {'m':dechifre}))
