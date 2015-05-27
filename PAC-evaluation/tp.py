
import client
import random
import hashlib
import json
from pprint import pprint

s = 269688693964389136999465584511072737497026454652634433838072633557430205657920718749080088013779347806077080604012517064873148860174505977018332203887181764314280929953054416898661526509338252284294441621014938056559950361779722276694376736499087093074781656247710197993741072774666980123049974977636205426769

my_results = {}
my_results['COURS'] = {'category': 'COURS', 'grade': 9, 'comment': '', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['TD'] = {'category': 'TD', 'grade': 6, 'comment': 'J\'ai trouvé que les TD n\étaient pas assez "concrets" et ne nous donnaient pas beaucoup d\'information nous permettant de nous aider pour de DS ou pour les TP.', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''} 
my_results['TP'] = {'category': 'TP', 'grade': 9, 'comment': 'Je pense qu\il aurait été très utile d\'avoir toutes les scéances de TP et pas seulement les premières de chaque challenge. Même si toutes mes questions posées par mail ont toujours eu une réponse, certaines des choses sur lesquels je me suis un peut "cassé les dents" auraient pu être résolu plus rapidement.', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['SAV'] = {'category': 'SAV', 'grade': 10, 'comment': '', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''} 
my_results['SUPPORT'] = {'category': 'SUPPORT', 'grade': 10, 'comment': '', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['PORTAIL'] = {'category': 'PORTAIL', 'grade': 8, 'comment': 'Et pas 10 car il y a eu pas mal de soucis avec le premier serveur et il aurait été utile d\'avoir des hyperliens. De plus le design est très "années 1990".', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['DS'] = {'category': 'DS', 'grade': 7, 'comment': 'Je l\ai trouvé très difficile mais adapté.', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['DIFFICILE'] = {'category': 'DIFFICILE', 'grade': 8, 'comment': 'C\'est probablement l\'UE la plus difficile que j\'ai eu à faire depuis que je suis à la fac.', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['UTILE'] = {'category': 'UTILE', 'grade': 10, 'comment': 'Même si c\'est l\'UE la plus difficile que j\ai fait depuis que je suis à la fac, c\'est aussi l\'une des plus utile. Je comprend mieux comment marche les differents systmèmes de crypto et je sais que cela me sera utile dans ma vie professionel et personnel.', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}
my_results['GENERAL'] = {'category': 'GENERAL', 'grade': 10, 'comment': 'Je pense qu\'une UE concernant la sécurité informatique devrait être obligatoire. Les cours que nous avons eu entre le début du semestre et l\interuption pédagogique seraient parfait pour la partie crypto. De plus, les cours étaient bien fait et interessant. Les TP, même si ils pouvaient être très très chronophages n\'en étaient pas moins adictif.', 'submission-token': '', 's': s, 'blinded': '', 'receipt-token': '', 'blind-signature': ''}




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


def export_json(dic, file_name):
    with open(file_name, 'w') as fp:
        json.dump(dic, fp)

def generate_blind(n, e, m, value):
    r = random.randint(2, n-1)
    inv_r = modinv(r, n)
    blinded = (pow(r, value['e'], value['n']) * m) % value['n']
    return (inv_r, blinded)

def import_json(file_name):
    with open(file_name) as fp:
        data = json.load(fp)
    return data

# RECUPERATION ET SAUVEGARDE DU TOKEN
def get_token(submission, file_name, my_results, n, e, m):
    for key, value in submission.items():
        (inv_r, blinded) = generate_blind(n, e, m, value)
        reply = serverObj.query(token, {'category': key, 'blinded': blinded, 'signature': pow(blinded, d, n)})
        reply_token = reply['blind-signature'] * inv_r
        
        my_results[key]['e'] = value['e']
        my_results[key]['n'] = value['n']
        
        my_results[key]['blind-signature'] = reply['blind-signature']
        my_results[key]['submission-token'] = reply_token
        
    export_json(my_results, file_name)




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
post = "/PAC-evaluation/post"

serverObj = client.Server(URL)
serv_return_1 = serverObj.query(sub_receipt)

receipt = serv_return_1['receipt']
submission = serv_return_1['submission']




m_hexa = hashlib.sha256(str(s).encode()).hexdigest()
m = int(m_hexa, base=16)

get_token(submission, 'token.json', my_results, n, e, m)



data = import_json('token.json')
print(data)
for key, value in data.items():
    (inv_r, blinded) = generate_blind(n, e, m, value)
    reply = serverObj.query(token, {'category': key, 'blinded': blinded, 'signature': pow(blinded, d, n)})
    blinded_prime = reply['blind-signature'] * inv_r
    data[key]['blinded'] = blinded_prime
    print(serverObj.query(post, {'category': key, 'grade': data[key]['grade'], 'comment': data[key]['comment'], 'submission-token': data[key]['submission-token'],'S': str(data[key]['s']),  'blinded': data[key]['blinded']}))


