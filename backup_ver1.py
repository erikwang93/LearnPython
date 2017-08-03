import os
import time

source = ['~/documents/backup_test1','~/documents/backup_test2']

target_dir = '/users/erikwang/documents/backup/'

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = 'zip -qr \'%s\' %s' % (target,' '.join(source))

if os.system(zip_command) == 0:
    print('back to',target)
else:
    print('FAIL')