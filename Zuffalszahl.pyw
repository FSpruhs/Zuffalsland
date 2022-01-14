import random, sqlite3
from tkinter import *


class ZufallsLand:
    
    def __init__(self):
        self.interface()
        
        
    def berechnen(self):
        laender = []
        for kontinent in (self.afrika, self.asien, self.europa,self.nordamerika,
                          self.ozeanien, self.suedamerika):
            if kontinent.get():
                laender += self.datei(kontinent.get())
        self.zufallsgenerator(laender)
        
                  
    def datei(self, kontinent):
        liste=[]
        try:
            verbindung = sqlite3.connect("laender.db")
            c = verbindung.cursor()
        except:
            print("Verbindung konnte nicht hergestellt werden")
        c.execute("SELECT * FROM laender WHERE kontinent = ?;",(kontinent,))
        for zeile in c:
            liste.append(zeile[0])
        c.close()
        verbindung.close()
        return(liste)
    
    def zufallsgenerator(self, laender):
        rnd = random.randint(0,len(laender)-1)
        self.l.config(text=str(laender[rnd]))
    
    
    def interface(self):
        self.fenster = Tk()
        self.fenster.title("Zuffalsland")
        self.f = Frame(self.fenster,relief=RIDGE,bd=2)
        self.l = Label(self.fenster,text = "",width=30,font=("Arial",20))
        self.b = Button(self.f,text="OK",width=10, command=self.berechnen)
        self.afrika = StringVar()
        self.asien = StringVar()
        self.europa = StringVar()
        self.nordamerika = StringVar()
        self.ozeanien = StringVar()
        self.suedamerika = StringVar()
        self.check_afrika = Checkbutton(self.f, text="Afrika", offvalue="",
                                       onvalue="Afrika", variable=self.afrika)
        self.check_asien = Checkbutton(self.f, text="Asien", offvalue="",
                                       onvalue="Asien", variable=self.asien)
        self.check_europa = Checkbutton(self.f, text="Europa", offvalue="",
                                       onvalue="Europa", variable=self.europa)
        self.check_nordamerika = Checkbutton(self.f, text="Nordamerika", offvalue="",
                                       onvalue="Nordamerika", variable=self.nordamerika)
        self.check_ozeanien = Checkbutton(self.f, text="Ozeanien", offvalue="",
                                       onvalue="Ozeanien", variable=self.ozeanien)
        self.check_suedamerika = Checkbutton(self.f, text="Südamerika", offvalue="",
                                       onvalue="Suedamerika", variable=self.suedamerika)

        self.f.pack(side=LEFT)
        self.l.pack(side=LEFT)
        self.check_afrika.pack(anchor=W)
        self.check_asien.pack(anchor=W)
        self.check_europa.pack(anchor=W)
        self.check_nordamerika.pack(anchor=W)
        self.check_ozeanien.pack(anchor=W)
        self.check_suedamerika.pack(anchor=W)
        self.b.pack(pady=10)
        self.fenster.mainloop()
    

    
z = ZufallsLand()
