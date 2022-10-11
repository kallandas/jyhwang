#!/usr/bin/env python3
# Author ID: jyhwang


'''
Student Name: Ji Yong Hwang
Student ID: 058819954 jyhwang
'''

test_strn = 'test:x:999:999:/home/test:/bin/bash'
from_passwd = \
[ \
'arthur:x:1001:1001:Arthur Smith:/home/arthur:/bin/bash',
'backup:x:34:34:backup:/var/backups:/usr/sbin/nologin',
'bin:x:2:2:bin:/bin:/usr/sbin/nologin',
'daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin',
'gdm:x:121:127:Gnome Display Manager:/var/lib/gdm3:/bin/false',
'geoclue:x:113:120::/var/lib/geoclue:/usr/sbin/nologin',
'gordon:x:1002:1002:Gordon Freeman:/home/gordon:/bin/bash',
'proxy:x:13:13:proxy:/bin:/usr/sbin/nologin',
'root:x:0:0:root:/root:/bin/bash',
'uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin',
'uuidd:x:106:112::/run/uuidd:/usr/sbin/nologin',
'www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin'
]

def bash_user(string):
    newList = string.split(':')
    if newList[6] == '/bin/bash':
        return True
    else:
        return False

if __name__ == '__main__':
    for string in from_passwd:
        if bash_user(string) == True:
            print('User is using Bash')
        else:
            print('User is not using Bash')
