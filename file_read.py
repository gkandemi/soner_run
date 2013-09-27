from fileclass import *

dosya = islem()

dosya.directory()

for i in dosya.filelist:
    dosya.oku(i , "Gain")
    dosya.parse()
    dosya.yaz()

