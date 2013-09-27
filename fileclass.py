import os
class islem:
    def __init__(self):
        self.liste = []
        self.keyword = ""
        self.output = []
        self.file_name = ""
        self.folder = []
        self.filelist = []

        
    def oku(self,dosyaadi,anahtar):
        self.liste = []
        dosya = open(dosyaadi , "r")
        self.keyword = anahtar
        self.file_name = dosyaadi
        self.liste = dosya.readlines()
        dosya.close()
        return self.liste

    def parse(self):
        self.output = []
        for i in self.liste:
            if self.keyword in i:
                self.output.append(i)

    def yaz(self):
        cdosyaadi = "ex_" + self.file_name
        cdosya = open(cdosyaadi , "w")
        for i in self.output:
            cdosya.write(i)
        cdosya.close()

    def directory(self):
        self.folder = os.listdir(".")
        for i in self.folder:
            if (i[-3:len(i)]) == "txt":
                self.filelist.append(i)
        return self.folder


        
