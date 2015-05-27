import client
from hashlib import sha256
import base64
import sys

from decimal import Decimal, getcontext
 
def nthroot (n, A, precision):
    getcontext().prec = precision
 
    n = Decimal(n)
    x_0 = A / n #step 1: make a while guess.
    x_1 = 1     #need it to exist before step 2
    while True:
        #step 2:
        x_0, x_1 = x_1, (1 / n)*((n - 1)*x_0 + (A / (x_0 ** (n - 1))))
        if x_0 == x_1:
            return x_1

# ex
# hash_object = hashlib.sha224(b'Hello World')
# hex_dig = hash_object.hexdigest()
# print(hex_dig)


# merci http://python.jpvweb.com/mesrecettespython/doku.php?id=racine_entiere
def lrackd(n, k=2):
    """racine entière kième d'un nombre entier n de taille quelconque
       recherche par dichotomie
    """
 
    # initialisation du signe et traitement des  cas particuliers
    signe = +1
    if n < 2:
        if n < 0:
            if k % 2 == 0:
                raise ValueError("Erreur: racine paire d'un nombre négatif")
            else:
                signe, n = -1, abs(n)
        else:
            return n  # ici n = 0 ou 1
 
    # trouve rac1 et rac2 qui encadrent de plus près la valeur cherchée de la racine
    rac1, i = 1, 1
    while i <= n:
        rac1 <<= 1
        i <<= k
    rac2 = rac1
    rac1 >>= 1
 
    # calcule par dichotomie la racine r kième de n qui est entre rac1 et rac2
    while rac1 != rac2:
        r = (rac1 + rac2) >> 1
        rn = r ** k
        if rn > n:
            rac2 = r
        else:
            rac1 = r + 1
    if n - rn < 0:
        r -= 1
 
    # retour de la racine avec le bon signe
    if signe > 0:
        return r
    return -r



sha256_oid = b'\x30\x31\x30\x0d\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20'

class EMSAError(Exception):
    pass

def emsa_pkcs1_encode(message, k):
    '''Take a message M and return
       the concatenation of length k:

        0x00 || 0x01 || PS || 0x00 || hash-oid || hash

       where PS is a string of length
       k - len(message) - 3 containing 0xfffffff.........

       hash = SHA-256(message)
       hash-oid : the Object Identifier of the hash function
       k - the length of the padded byte string

       >>> m = "toto est content".encode()
       >>> block = emsa_pkcs1_encode(m, 100)
       >>> base64.b16encode(block)
       b'0001FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF003031300D06096086480165030402010500042020EED533D25E17520EC4D8C364A0486242ED49A4E42B82489565C5A6877D1C95'
    '''
    h = sha256(message)
    payload = sha256_oid + h.digest()
    m_len = len(payload)
    if m_len > k - 11:
        raise EMSAError("n is too short")
    ps_len = k - len(message) - 3
    ps = b'\xff' * ps_len
    return b'\x00\x01' + ps + b'\x00' + payload




URL = "http://pac.bouillaguet.info/TP5"
PKCS = "/broken-PKCS-signature/PK"
answer  = "/broken-PKCS-signature/transfer/echallier"

serverObj = client.Server(URL)

PK = serverObj.query(PKCS)
e = PK['e']
n = PK['n']
account_number = 10
amount = "10"
size_of_bourage = 193

def get_borne_inf_int(m):
  m_bytes = m.encode()
  m_tmp = b'00'
  
  for i in range(193):
    m_tmp += b'00'
  

  borne_inf = emsa_pkcs1_encode(m_bytes, 100)
  borne_inf_hexa = base64.b16encode(borne_inf) + m_tmp
  print("borne_inf_hexa")
  print(borne_inf_hexa)
  borne_inf_int = int(borne_inf_hexa, base= 16)
  return borne_inf_int

def get_borne_sup_int(m):
  m_bytes = m.encode()
  m_tmp = b'ff'


  for i in range(193):
    m_tmp += b'ff'

  borne_sup = emsa_pkcs1_encode(m_bytes, 100)
  borne_sup_hexa = base64.b16encode(borne_sup) + m_tmp
  print("borne_sup_hexa")
  print(borne_sup_hexa)
  borne_sup_int = int(borne_sup_hexa, base= 16)
  return borne_sup_int
  



while True:
  m = "Virement du compte " + str(account_number) + " de " + amount + " euros pour echallier"
#  print(m)
  borne_inf_int = get_borne_inf_int(m)
#  print(borne_inf_int)
  borne_sup_int = get_borne_sup_int(m)
#  print(borne_sup_int)


  # we make sure that the two bornes are ok
  while borne_inf_int > borne_sup_int:
    print("oooooooooo")
    account_number += 1
    m = "Virement du compte " + str(account_number) + " de " + amount + " euros pour echallier"
    borne_inf_int = get_borne_inf_int(m)
    borne_sup_int = get_borne_sup_int(m)
    
  
  x = lrackd(borne_sup_int, k=3)
  print(x)
  if pow(x, 3) > borne_inf_int:
    print("YYYYYYEEEEEEEEEESSSSSSSSSS")
    print(x)
    print(account_number)
    print(amount)
    print(serverObj.query(answer, {'signature': x, 'account-number': account_number, 'amount': amount}))
    sys.exit()
  
  account_number += 100
  amount = amount * 2

#print(serverObj.query(answer, {'s': s, 't': t, 'm' : m}))
