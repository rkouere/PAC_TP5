import client
import hashlib
import random
import base64
# ex
# hash_object = hashlib.sha224(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)

def str_to_int(string):
  tmp = string.encode()
  return int(base64.b16encode(tmp), base=16)

URL = "http://pac.bouillaguet.info/TP5"
KDC = "/id-based-signature/KDC/PK"
keygen = "/id-based-signature/KDC/keygen/echallier"

answer = "/id-based-signature/check/echallier"

hash_test = "/id-based-signature/hash"

serverObj = client.Server(URL)
KDC_params = serverObj.query(KDC)
e = KDC_params['e']
n = KDC_params['n']

identity = serverObj.query(keygen)
secret_key = identity['secret-key']



# for y in range(0, 0x0f):
#   hash_obj = hashlib.sha256(b'echallier' + bytes(y))
#   i += hash_obj.hexdigest()



i = pow(secret_key, e, n)
r = random.randint(1, n-1)
t = pow(r, e, n)

m = "salut"
m_byte = m.encode()
print(m_byte)


print("=======t===========")
print(t)
print("=======t_hexa=======")
t_hexa = "{0:0512x}".format(t)
print(len(t_hexa))
print(t_hexa)
t_byte = base64.b16decode(t_hexa, casefold=True)
print("======")


tmp = m_byte + t_byte
hash_obj = hashlib.sha256(tmp).hexdigest()


print(hash_obj)
print(serverObj.query(hash_test, {'m': m, 't': t}))

s = (secret_key * pow(r, int(hash_obj, base=16), n))%n
print(serverObj.query(answer, {'s': s, 't': t, 'm' : m}))
