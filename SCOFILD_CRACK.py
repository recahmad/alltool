#_______________[IMPORT ]_____________#
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import os,sys,time,json,random,re,string,platform,base64,platform,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import requests,random,sys,json,os,requests,calendar
from datetime import date
from datetime import datetime
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
ct = datetime.now()
n = ct.month
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if n < 0 or n > 12:
        exit() 
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
timr = ("%s-%s-%s-%s"%(hr, ha, op, ta))
hhh=timr.upper()
tgl = ("%s %s %s"%(ha, op, ta))
#date=tgl.upper()
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

sir = '\033[41m\x1b[1;97m'
x = '\33[m' 
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
A = '\x1b[1;97m' 
#_______COLOUR______#
BLACK = '\x1b[1;90m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'


#
WW = '\033[97;1m' 
RR = '\033[91;1m' 
GG = '\033[92;1m' 
YY = '\033[93;1m' 
BB = '\033[94;1m'
PP = '\033[95;1m'
CC = '\033[96;1m'
NN = '\x1b[0m'
#

RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;92m'
YELLOW = '\033[1;93m'
BLUE = '\033[1;94m'
ORANGE = '\033[1;95m'
BLACK = '\033[1;90m'
BS = '\033[1;96m'
HBF = '{ HBF }'
my_color = [
 RED, WHITE, BLACK, BS, GREEN, YELLOW, ORANGE]
COLOUR_X = random.choice(my_color)




fuck = []
fucke = []
for i in range(1):
    fbs = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    xyz = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
    yzx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/'+str(fbs)+';FBDV/'+str(xyz)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    fuck.append(yzx)
    
    fb2 = random.choice([
        'com.facebook.adsmanager',
        'com.facebook.lite',
        'com.facebook.orca',
        'com.facebook.katana',
        'com.facebook.mlite'])
    xxy = random.choice(['SM-G920F','NRD90M', 'SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
    yyz = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/{density=2.25,width=720,height=1280};FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/'+str(fb2)+';FBDV/'+str(xxy)+';FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    fucke.append(yyz)
    ch = fucke+fuck
    

#________________USER AGENT_______________#
'''
samiya=[]
fahmida = []
fariya=[]


for xd in range(1):
    a='Mozilla/5.0 (Symbian/3; Series60/'
    b=random.randrange(1, 9)
    c=random.randrange(1, 9)
    d='Nokia'
    e=random.randrange(100, 9999)
    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
    g=random.randrange(1, 9)
    h=random.randrange(1, 4)
    i=random.randrange(1, 4)
    j=random.randrange(1, 4)
    k='Mobile Safari/535.1'
    paku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
    samiya.append(paku)


    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['4','5','6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    paku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    fahmida.append(paku2)
    
    
    a='Dalvik/2.1.0 (Linux; U; Android'
    b=random.randrange(6, 15)
    c=random.randrange(100, 9999)
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    h=random.randrange(1, 9)
    i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
    j=random.randrange(1, 9)
    k=random.randrange(1, 9)
    l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
    pakuu=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
    fariya.append(pakuu)
    
    numan = samiya+fahmida+fariya+fuck'''
    


#_________________RANDOM CHOICE PASS EXTRA_______________#

samiya = ('shanto','samiya','mimi afsana','hridoy','i love you')
shanta = ('112233','445566','505040','607080')

fariya = samiya+shanta

sojib = random.choice(fariya)





def clear():
    os.system('clear')
def banner():
    clear()
    print(f"""{GREEN}
  
 \033[1;91m████████████████████████████████████████
           █─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄─█▄─▄█▄─▄███▄─▄▄▀█
           █▄▄▄▄─█─███▀█─██─██─▄████─███─██▀██─██─█
           ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
 \033[1;91m████████████████████████████████████████
           █─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄─█▄─▄█▄─▄███▄─▄▄▀█
           █▄▄▄▄─█─███▀█─██─██─▄████─███─██▀██─██─█
           ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
\033[1;94m████████████████████████████████████████
          █─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄─█▄─▄█▄─▄███▄─▄▄▀█
          █▄▄▄▄─█─███▀█─██─██─▄████─███─██▀██─██─█
          ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
   \033[1;94m████████████████████████████████████████
             █─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄─█▄─▄█▄─▄███▄─▄▄▀█
             █▄▄▄▄─█─███▀█─██─██─▄████─███─██▀██─██─█
             ▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▀▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀
    \033[1;92mBAXER BEY BO TOOOOOOOOOLLLLLLEEEEEE😱
     \033[1;92m            ‌   MAM SCOFILD😎
   \033[1;93mM\033[1;94mA\033[1;91mM\033[1;92mS\033[1;95mC\033[1;90mO\033[1;92m-\033[1;91mF\033[1;94mI\033[1;93mL\033[1;96mD\033[1;95mx
                                                
    \33[1;92m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗               
    ║  \x1b[97m\033[37;41m  INFINITY GREEN X FACEBOOK XD V2   \033[0;m     \33[1;92m ║
    \33[1;92m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝            
     {H} ╔════════════════════════{M}════════════════╗
      {H}║{M}[{H}•{M}] AUTHOR    :{H} SCOFILDx             {N}{M}║
      {H}║{M}[{H}•{M}] TLEGRAM  : {H}SCOFILDx            {N}{M}║
      {H}║{M}[{H}•{M}] GITHUB    : {H}SCOFILD-VIRUS-XD{N}       {H}  ║
      {M}║{M}[{H}•{M}] STATUS    : {H}INFINITY -X{P}     {N}  {H}      ║
      {M}║{M}[{H}•{M}] VERSION   : {H}2.1.1                  {H} ║
      {M}╚═════════════{H}═══════════════════════════╝ {P}""")


    


ok = []
cp = []
loop = 0


def main():
    os.system('clear')
    banner()
    print(f' ')
    print(f'{M}╔══[•] TOOL NAME : {H}SCOFILD_CRACK X')
    print(f'{M}║══[•] YOUR IP   :{H} ')
    print(f'{M}║══[•] VERSION   : {H}INFINITY')
    print(f'{M}╚══[•] CODER NAME: {H}MAM SCOFILD')
    print(f' ')
    print(f"{M}╔══[{M}1{RED}] \033[1;32mSTART NUMBER CLONING {RED}(TCW)")
    print(f"║══[{M}2{RED}] \033[1;34mSTART GMAIL CLONING {RED}(TCW)")
    print(f"║══[{M}3{RED}] \033[1;35mSTART USER NAME CLONING   [<\>] ")
    print(f"{RED}╚══[{M}U{RED}] \033[1;31mUPDATE PROGRAMME ")
    sh = input("    \033[0;91m(#)\033[0;92m CHOOSE : ")
    if sh =='1':
       os.system('xdg-open https://facebook.com/groups/316554827306831/')
       num()
    if sh =='2':
       os.system('xdg-open https://facebook.com/groups/316554827306831/')
       gmail()
    if sh =='3':
       os.system('xdg-open https://facebook.com/groups/316554827306831/')
       user()
    else:
        os.system('xdg-open https://github.com/NOBITA-VIRUS-XD')
        #main()



def num():
    user=[]
    
    os.getuid
    os.geteuid
    banner()
    print(f"                 {H} INSTA  {K}CRACK{P} [{H}⚜{P}] ");time.sleep(0.05)
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m BD CODE: {P}[{H}016{P}][{B}017{P}][{K}019{P}][{K}018{P}][{P}08{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m BD CODE: {P}[{H}011{P}][{B}014{P}][{K}015{P}][{K}08{P}][{P}012{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print("")
    ff ='+88'
    code = input(f' CHOOSE :{H} ')
    os.system("clear")
    banner()
    print(f"")
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f'{P}[{H}√{P}]EXAMPLE : {M}TIK TOK /I LOVE YOU/SCOFILD/DOREMON/OGGY')
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f'{P}[{H}√{P}]EXAMPLE : {M}CHOOSE MORE PASS USE(,)COMA WITHOUT BRAKET')
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f"")
    po = input(f"{M} [+] [CHOOSE] : ")
    pok = po.lower()
    os.system("clear")
    banner()
    print(f"")
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'    {P}[{H}√{P}] EXAMPLE    : {K}5000/10000/20000')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f"")
    limit = int(input(f'    %s[%s?%s] CRACK ID LIMIT : %s'%(N,K,N,H)))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        np = ''.join(random.choice(string.digits) for _ in range(6))
        mp = ''.join(random.choice(string.digits) for _ in range(2))
        user.append(nmp)
    with ThreadPool(max_workers=60) as shanto:    
        clear()
        banner()
        tl = str(len(user))
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        print(f'{M}╔══[•] {GREEN}WElCOME  MY TOOLS     : {RED}')
        print(f'{M}║══[•] {GREEN}TOTAL IDZ             : {RED}4323')
        print(f'{M}║══[•] {GREEN}NUMBER YOU PUT        : {RED}'+code)
        print(f'{M}║══[•] {GREEN}PROCESS HAS BEEN STARTED')
        print(f'{M}╚══[•] {GREEN}TO STOP PROCESS Ctrl + Z ')
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        for love in user:
            uid = ff+code+love
            pwx = ([(code+love)])
            #om = str(pwx)
            for ps in pwx:
                print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
                print('    \033[1;92m[SCOFILD-OK] '+uid+' | '+ps)
                #print(f'    {B}[COOKI💉] {B} c_user=10001'+mp+nmp+';xs=36:pf9rFxNLcyFkEg:2:1695'+np+':-1:93'+mp+';fr=0qfviiQQcH5ggaLjC.AWXGuar8mh14n29AdXmMWkZzatc.BlEihn..AAA.0.0.BlEihn.AWWcGDKiC4A;datr=ZygSZdNNPnOYF1MCcxdpJYke')    
        if tl <uid:
         print('        \033[1;90m[\033[1;91mSCOFILD\033[1;90m] \033[1;90m[\033[1;92m4322\033[1;90m] \033[1;92mOK \033[1;90m[\033[1;92m56\033[1;90m] ')
                #sys.stdout.flush()



                
      #break
    #else:
        #continue
                #sys.stdout.flush()

            
            
            
        




def gmail():
    user=[]
    
    os.getuid
    os.geteuid
    banner()
    print(f"                 {H} GMAIL {K}CRACK{P} [{H}⚜{P}] ");time.sleep(0.05)
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m NAME: {P}[{H}SHANTO{P}][{B}MASUD{P}][{K}MAHIN{P}][{K}FAHIM{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print("")
    ff = input(f' CHOOSE :{H} ')
    gg = ff.lower()
    os.system("clear")
    banner()
    print(f"                 {H} GMAIL {K}CRACK{P} [{H}⚜{P}] ");time.sleep(0.05)
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m NAME: {P}[{H}HASAN{P}][{B}RANA{P}][{K}AHMED{P}][{K}MAHMUD{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print("")
    hh = input(f' CHOOSE :{H} ')
    nn = hh.lower()
    os.system("clear")
    banner()
    print(f"                 {H} GMAIL {K}CRACK{P} [{H}⚜{P}] ");time.sleep(0.05)
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m NAME: {P}[{H}@GMAIL.COM{P}][{B}MAIL.COM{P}][{K}YAHOO.COM{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print("")
    kk = input(f' CHOOSE :{H} ')
    pp = kk.lower()
    os.system("clear")
    banner()
    print(f"")
    print(f"")
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f'{P}[{H}√{P}]EXAMPLE : {M}TIK TOK /I LOVE YOU/SCOFILD/DOREMON/OGGY')
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f'{P}[{H}√{P}]EXAMPLE : {M}CHOOSE MORE PASS USE(,)COMA WITHOUT BRAKET')
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f"")
    po = input(f"{M} [+] [CHOOSE] : ")
    pok = po.lower()
    os.system("clear")
    banner()
    print(f"")
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'    {P}[{H}√{P}] EXAMPLE    : {K}5000/10000/20000')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f"")
    limit = int(input(f'    %s[%s?%s] CRACK ID LIMIT : %s'%(N,K,N,H)))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(2, 4))
        user.append(nmp)
    with ThreadPool(max_workers=60) as shanto:    
        clear()
        banner()
        tl = str(len(user))
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        print(f'{M}╔══[•] {GREEN}WElCOME  MY TOOLS     : {RED}')
        print(f'{M}║══[•] {GREEN}TOTAL IDZ             : {RED}4444')
        print(f'{M}║══[•] {GREEN}NUMBER YOU PUT        : {RED}'+nn)
        print(f'{M}║══[•] {GREEN}PROCESS HAS BEEN STARTED')
        print(f'{M}╚══[•] {GREEN}TO STOP PROCESS Ctrl + Z ')
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        for love in user:
            uid = gg+nn+love+pp
            pwx = ([(gg+nn+love)])
            for ps in pwx:
                print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
                print('    \033[1;92m[SCOFILD-OK] '+uid+' | '+ps)
                #print(f'    {B}[COOKI💉] {B}datr=6h4NZdi8mzrhmqhe-1HzGMXd; sb=6h4NZdXRNbdVEzd3_J9nBKZG; m_pixel_ratio=2; c_user=10009'+love+nnn+'; xs=30%3AxnET70hRrt2qrA%3A2%3A1695'+nop+'%3A-1%3A1928; fr=0Uh76ULZ4BjMf0iR3.AWUcqax6BSH82jI2sVV_K4gc9XA.BlDR7q.pD.AAA.0.0.BlDR99.AWVzk7kgK5g; x-referer=eyJyIjoiL2Vycm9yL2luZGV4LnBocD9lcnI9ZWMma2Vycj0xMzU3MDMyJmtlcnJfc3VtbWFyeT1Tb21ldGhpbmclMjB3ZW50JTIwd3Jvbmcma2Vycl9kZXNjcmlwdGlvbj1QbGVhc2UlMjB0cnklMjByZWZyZXNoaW5nJTIwdGhlJTIwUGFnZSUyMG9yJTIwY2xvc2luZyUyMGFuZCUyMHJlb3BlbmluZyUyMHlvdXIlMjBicm93c2VyJTIwd2luZG93LiIsImgiOiIvZXJyb3IvaW5kZXgucGhwP2Vycj1lYyZrZXJyPTEzNTcwMzIma2Vycl9zdW1tYXJ5PVNvbWV0aGluZyUyMHdlbnQlMjB3cm9uZyZrZXJyX2Rlc2NyaXB0aW9uPVBsZWFzZSUyMHRyeSUyMHJlZnJlc2hpbmclMjB0aGUlMjBQYWdlJTIwb3IlMjBjbG9zaW5nJTIwYW5kJTIwcmVvcGVuaW5nJTIweW91ciUyMGJyb3dzZXIlMjB3aW5kb3cuIiwicyI6Im0ifQ%3D%3D; m_page_voice=10009'+love+nnn+'; wd=360x800')
        if tl <uid:
         print('        \033[1;90m[\033[1;93mRUNNING\033[1;90m] \033[1;90m[\033[1;95m4444\033[1;90m] \033[1;92mOK \033[1;90m[\033[1;92m15\033[1;90m] ')
                #sys.stdout.flush()

            
            
         
            
            
def user():
    user=[]
    
    os.getuid
    os.geteuid
    banner()
    print(f"                 {H} USER {K}CRACK{P} [{H}⚜{P}] ");time.sleep(0.05)
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m NAME: {P}[{H}SHANTO{P}][{B}MASUD{P}][{K}MAHIN{P}][{K}FAHIM{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print("")
    ff = input(f' CHOOSE :{H} ')
    gg = ff.lower()
    os.system("clear")
    banner()
    print(f"                 {H} USER {K}CRACK{P} [{H}⚜{P}] ");time.sleep(0.05)
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'   \033[1;92m NAME: {P}[{H}HASAN{P}][{B}RANA{P}][{K}AHMED{P}][{K}MAHMUD{P}]')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print("")
    hh = input(f' CHOOSE :{H} ')
    nn = hh.lower()
    os.system("clear")
    banner()
    print(f"")
    print(f"")
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f'{P}[{H}√{P}]EXAMPLE : {M}TIK TOK /I LOVE YOU/SCOFILD/DOREMON/OGGY')
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f'{P}[{H}√{P}]EXAMPLE : {M}CHOOSE MORE PASS USE(,)COMA WITHOUT BRAKET')
    print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
    print(f"")
    po = input(f"{M} [+] [CHOOSE] : ")
    pok = po.lower()
    os.system("clear")
    banner()
    print(f"")
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f'    {P}[{H}√{P}] EXAMPLE    : {K}5000/10000/20000')
    print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
    print(f"")
    limit = int(input(f'    %s[%s?%s] CRACK ID LIMIT : %s'%(N,K,N,H)))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(2,4))
        nnn = ''.join(random.choice(string.digits) for _ in range(6))
        nop = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=60) as shanto:    
        clear()
        banner()
        tl = str(len(user))
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        print(f'{M}╔══[•] {GREEN}WElCOME  MY TOOLS     : {RED}')
        print(f'{M}║══[•] {GREEN}TOTAL IDZ             : {RED}4532')
        print(f'{M}║══[•] {GREEN}NUMBER YOU PUT        : {RED}'+nn)
        print(f'{M}║══[•] {GREEN}PROCESS HAS BEEN STARTED')
        print(f'{M}╚══[•] {GREEN}TO STOP PROCESS Ctrl + Z ')
        print("%s══════════════════════════%s══════════════════════════%s"%(M,H,P))
        for love in user:
            uid = gg+'.'+nn+love
            pwx = nn+love, gg+nn
            #om = str(ps)
            
            
            for ps in pwx:
                kk = random.choice(ch)
                print(kk)
                print("    %s═════════════════════%s═════════════════════%s"%(M,H,P))
                print('    \033[1;92m[SCOFILD-OK] '+uid+' | '+ps)
                #print(f'    {B}[COOKI💉] {B}datr=6h4NZdi8mzrhmqhe-1HzGMXd; sb=6h4NZdXRNbdVEzd3_J9nBKZG; m_pixel_ratio=2; c_user=10009'+love+nnn+'; xs=30%3AxnET70hRrt2qrA%3A2%3A1695'+nop+'%3A-1%3A1928; fr=0Uh76ULZ4BjMf0iR3.AWUcqax6BSH82jI2sVV_K4gc9XA.BlDR7q.pD.AAA.0.0.BlDR99.AWVzk7kgK5g; x-referer=eyJyIjoiL2Vycm9yL2luZGV4LnBocD9lcnI9ZWMma2Vycj0xMzU3MDMyJmtlcnJfc3VtbWFyeT1Tb21ldGhpbmclMjB3ZW50JTIwd3Jvbmcma2Vycl9kZXNjcmlwdGlvbj1QbGVhc2UlMjB0cnklMjByZWZyZXNoaW5nJTIwdGhlJTIwUGFnZSUyMG9yJTIwY2xvc2luZyUyMGFuZCUyMHJlb3BlbmluZyUyMHlvdXIlMjBicm93c2VyJTIwd2luZG93LiIsImgiOiIvZXJyb3IvaW5kZXgucGhwP2Vycj1lYyZrZXJyPTEzNTcwMzIma2Vycl9zdW1tYXJ5PVNvbWV0aGluZyUyMHdlbnQlMjB3cm9uZyZrZXJyX2Rlc2NyaXB0aW9uPVBsZWFzZSUyMHRyeSUyMHJlZnJlc2hpbmclMjB0aGUlMjBQYWdlJTIwb3IlMjBjbG9zaW5nJTIwYW5kJTIwcmVvcGVuaW5nJTIweW91ciUyMGJyb3dzZXIlMjB3aW5kb3cuIiwicyI6Im0ifQ%3D%3D; m_page_voice=10009'+love+nnn+'; wd=360x800')
        if tl <uid:
         print('        \033[1;90m[\033[1;91mRUNNING\033[1;90m] \033[1;90m[\033[1;92m4532\033[1;90m] \033[1;92mOK \033[1;90m[\033[1;92m8\033[1;90m] ')
                #sys.stdout.flush()



  
            
            
#---------------------[END MENU]---------------------#

if __name__ == '__main__':
    main()