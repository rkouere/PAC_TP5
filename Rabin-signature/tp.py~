import client
import random
import miller_rabin
from fractions import gcd

URL="http://pac.bouillaguet.info/TP5"
link_param = "/RSA-keygen/challenge/echallier"
answer = "/RSA-keygen/PK/echallier"
confirmation = "/RSA-keygen/confirmation/echallier"

serverObj = client.Server(URL)

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


e =  535890187425344683208917930322408044245
# p , q = getTwoPrime(e)



p = 277461027049854810288405758908172098629253435446959073090615700876807909390843667708032667263836741272893300164600643617600904696366008257486465679283070534258115902100961955522211170750181191229411454331047399566105121104637984719523302928584689237682786859691245578154493434772170438439978284764756836074199
q = 170546191165200071045408843438399129154545534123331514137997529965617229025417495160698071473291750491846942018957300308523616269031865565796522642357711473326380517067249236995772562816300987333175837191239786364745310750596411786403167126078819373310363468430133540610399083878706320397608768367315686273137
phi = (p-1)*(q-1)
d = modinv(e, phi)
n = p*q

ciphertext = serverObj.query(answer, {'n': n, 'e': e})['ciphertext']
dechifre = pow(ciphertext, d, n)    
print(serverObj.query(confirmation, {'m':dechifre}))
