import client
import random
import hashlib

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


# RSA
e =  535890187425344683208917930322408044245
p = 277461027049854810288405758908172098629253435446959073090615700876807909390843667708032667263836741272893300164600643617600904696366008257486465679283070534258115902100961955522211170750181191229411454331047399566105121104637984719523302928584689237682786859691245578154493434772170438439978284764756836074199
q = 170546191165200071045408843438399129154545534123331514137997529965617229025417495160698071473291750491846942018957300308523616269031865565796522642357711473326380517067249236995772562816300987333175837191239786364745310750596411786403167126078819373310363468430133540610399083878706320397608768367315686273137
phi = (p-1)*(q-1)
d = modinv(e, phi)
n = p*q

# FIN RSA



URL = "http://pac.bouillaguet.info/TP5"
sub_receipt = "/PAC-evaluation/PK"

answer  = "/broken-PKCS-signature/transfer/echallier"
token =  "/PAC-evaluation/publication-token/echallier"


serverObj = client.Server(URL)
serv_return_1 = serverObj.query(sub_receipt)

receipt = serv_return_1['receipt']
submission = serv_return_1['submission']

my_results = {}
my_results['COURS'] = {}
my_results['TD'] = {}
my_results['TP'] = {}
my_results['SAV'] = {}
my_results['SUPPORT'] = {}
my_results['PORTAIL'] = {}
my_results['DS'] = {}
my_results['DIFFICILE'] = {}
my_results['UTILE'] = {}
my_results['GENERAL'] = {}

print(my_results)




s = 269688693964389136999465584511072737497026454652634433838072633557430205657920718749080088013779347806077080604012517064873148860174505977018332203887181764314280929953054416898661526509338252284294441621014938056559950361779722276694376736499087093074781656247710197993741072774666980123049974977636205426769

m_hexa = hashlib.sha256(str(s).encode()).hexdigest()
m = int(m_hexa, base=16)


for key, value in submission.items():
    r = random.randint(2, n-1)
    blinded = (pow(r, value['e'], value['n']) * m) % value['n']
    print("=========")
    print(key)
    print(serverObj.query(token, {'category': key, 'blinded': blinded, 'signature': pow(blinded, d, n)}))
    



# s = random.getrandbits(1025)

