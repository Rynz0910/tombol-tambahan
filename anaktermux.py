import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

def setup():
    try:
        os.mkdir('/data/data/com.termux/files/home/.termux')
    except:
        pass
    key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
    open('/data/data/com.termux/files/home/.termux/termux.properties','w').write(key)
    os.system('termux-reload-settings')