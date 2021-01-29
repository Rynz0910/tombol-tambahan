import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Additional button in termux ')
print(a+'\t  UP,Down,right,Left, CTRL ')
print(b+'\t  By:  Youtube:Rynz 01')
print('\t Instagram : @riyanhadi2020')
print(a+'+'*40)
print('\nProses..')
sleep(1)
print(b+'\n[!] Mengambil File Default Termux')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[!]Success !')
sleep(1)
print(b+'\n[!] is adding additional files')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
print(a+'[!] Loading....')
sleep(1)
print(b+'\n[!] Wait a minute')
sleep(2)
os.system('termux-reload-settings')
print(a+'[!] Proses Selesai !! ^^'+c+'\n\njika terjadi masalah hubungi saya via instagram*\n\n')
