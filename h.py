import os
import platform
b = platform.architecture()[0]
if b == '64bit':
    os.system('chmod 777 t64')
    os.system('./t64')
elif b == '32bit':
    os.system('chmod 777 t32')
    os.system('./t32')