import sqlite3

verbindung = sqlite3.connect("laender.db")
c = verbindung.cursor()

#c.execute("""CREATE TABLE laender (land VARCHAR(50),kontinent VARCHAR(50));""")
#try:
#    datei = open("Suedamerika.txt","r")
#    text = datei.read()
#    datei.close()
#except:
#    print("Datei konnte nicht geöffnet werden")
#liste=text.split("\n")

#for land in liste:
#    c.execute("""INSERT INTO laender VALUES (?,?);""",(land,"Suedamerika"))
    

#c.execute("SELECT * from laender")

#for zeile in c:
#    print(zeile)

verbindung.commit()

c.close()

verbindung.close()
