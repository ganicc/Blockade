from itertools import *
import itertools
vr = int(input("Broj vrsti: "))
if vr<22:
    vrsta=vr
else:
    print("Uneli ste preveliki broj za velicinu tabele")
kol = int(input("Broj kolona: "))
if kol<22:
    kolona=kol
else:
    "Uneli ste preveliki broj za velicinu tabele"
brZid= int(input("Broj zidova: "))
if brZid<22:
    brojZidova=brZid
else:
    "Uneli ste preveliki broj za velicinu tabele"

a = []
b = []
c = []

# 0 pozicije gde moze da se nadje pesak
# 1 pozicije gde moze da se nadje zid
# 2 nevalidne pozicije
# 3 pozicije gde su postavljeni zidovi
for j in range(0, int(2*kolona-1)):
    if j%2 == 0:
       b.append(0)
    else:
        b.append(1)


for i in range (0, int(2*kolona-1)):
    if(i%2==0):
        c.append(1)
    else:
        c.append(2)     

for i in range(0, int(2*vrsta-1)):
    if i%2 == 0:
       a.append(b)
    else:
        a.append(c)

lista1=list(map(lambda x: ('p',x[0],x[1]),list(product(range(1,vrsta),range(1,kolona)))))
lista2=list(map(lambda x: ('z',x[0],x[1]),list(product(range(1,vrsta),range(1,kolona)))))
moguci_zidovi=lista1+lista2

ubaceni_zidovi=[]

pocetnaPozX1=(0,0)
pocetnaPozX2=(0,0)
pocetnaPozO1=(0,0)
pocetnaPozO2=(0,0)

pozicijaX1=(0,0)
pozicijaX2=(0,0)
pozicijaO1=(0,0)
pozicijaO2=(0,0)

stanje=()

xPlaviZidovi=0
xZeleniZidovi=0
oPlaviZidovi=0
oZeleniZidovi=0


def izracunajKoordinate(poz):
    poz1=(poz[0]-1)*2
    poz2=(poz[1]-1)*2
    novaPoz=(poz1,poz2)
    return novaPoz


def zameniVrednost(pozicija,i,j,vrednost1):
    #print("zamenivrednost parametri: ",pozicija,i,j,vrednost1)
    vrednost=str(vrednost1)
    lista=list(a[i])
    lista[j]=vrednost
    a[i]=lista

    if pozicija[0] != i or pozicija[1] != j:
        lista=list(a[pozicija[0]])
        lista[pozicija[1]]=0
        a[pozicija[0]]=lista

    pozicija=(i,j)
    if vrednost == 'X':
        global pozicijaX1
        pozicijaX1=pozicija
    elif vrednost == 'x':
        global pozicijaX2
        pozicijaX2=pozicija
    elif vrednost == "O":
        global pozicijaO1
        pozicijaO1=pozicija
    elif vrednost == "o":
        global pozicijaO2
        pozicijaO2=pozicija
    else: 
        print("Doslo je do greske(zameniVrednost)")


def pocetnostanje():

    global pozicijaX1
    global pozicijaX2
    global pozicijaO1
    global pozicijaO2

    listaPesaka=[]
    listaPesaka.append(pozicijaX1)
    listaPesaka.append(pozicijaX2)
    listaPesaka.append(pozicijaO1)
    listaPesaka.append(pozicijaO2)


    for i in range (0,4):
        if i<2:
            print("Unesite koordinate pesaka X igraca")
        else:
            print("Unesite koordinate pesaka O igraca")
        
        koordinata1=int(input("X koordinata pesaka : "))
        koordinata2=int(input("Y koordinata pesaka: "))
        koordinate=(koordinata1,koordinata2)
        noveKoordinate=izracunajKoordinate(koordinate)

        if i == 0:
            vrednost='X'
        elif i==1:
            vrednost='x'
        elif i==2:
            vrednost='O'
        else:
            vrednost="o"

        listaPesaka[i]=noveKoordinate    
        kor=listaPesaka[i]
        #print("Pocetno stanje, koordinate: ",koordinate,", polje u matrici: ", noveKoordinate)
        zameniVrednost(listaPesaka[i],kor[0],kor[1],vrednost)


    global pocetnaPozX1
    global pocetnaPozX2
    global pocetnaPozO1
    global pocetnaPozO2

    pocetnaPozX1=pozicijaX1
    pocetnaPozX2=pozicijaX2
    pocetnaPozO1=pozicijaO1
    pocetnaPozO2=pozicijaO2


    global xPlaviZidovi
    global xZeleniZidovi
    global oPlaviZidovi
    global oZeleniZidovi

    xPlaviZidovi=brojZidova
    xZeleniZidovi=brojZidova
    oPlaviZidovi=brojZidova
    oZeleniZidovi=brojZidova

    prikaz(a)


def krajIgre()->int:
    global pozicijaX1
    global pozicijaX2
    global pozicijaO1
    global pozicijaO2

    if pozicijaX1 == pocetnaPozO1 or pozicijaX1 == pocetnaPozO2 or pozicijaX2 == pocetnaPozO1 or pozicijaX2 == pocetnaPozO2:
        print("X je pobedio!")
        return 1
    elif pozicijaO1 == pocetnaPozX1 or pozicijaO1 == pocetnaPozX2 or pozicijaO2 == pocetnaPozX1 or pozicijaO2 == pocetnaPozX2:
        print("O je pobedio!")
        return 1
    else:
        return 0
    
def prikaziHeader(a):
    red="  "
    for j in range(1,kolona+1):
        if(j<10): red+=str(j)+" "
        else: red+=chr(j+55)+" "
    print(red)
    red="  "
    for j in range(0,kolona):red += "= " 
    print(red)

def prikaziFooter(a):
    red="  "
    for j in range(0,kolona):red += "= " 
    print(red)
    red="  "
    for j in range(1,kolona+1):
        if(j<10): red+=str(j)+" "
        else: red+=chr(j+55)+" "
    print(red)


def prikaz(a):
    prikaziHeader(a)
    red=""
    for i in range(0,int(2*vrsta-1)):
        for j in range(0,int(2*kolona-1)):
            if i%2 == 0:
                if j==0:
                    if(i<9*2): red+=str(i//2+1)+"ǁ" 
                    else: red+=chr(i//2+1+55)+"ǁ"
                if j==2*kolona-2:
                    if(i<9*2): red+=" ǁ"+str(i//2+1) 
                    else: red+=" ǁ"+chr(i//2+1+55)
                if(a[i][j] == 0 or a[i][j] == 2): red+=" "
                elif(a[i][j] == 1): red+="|"
                elif(a[i][j] == 3): red+="ǁ"
                else: red+=str(a[i][j])
            else:
                if j==0: red+="  "
                if (a[i][j] == 2) : red+=" "
                elif(a[i][j] == 3): red+="="
                else: red+="—"
        print(str(red))
        red=""
    prikaziFooter(a)


def validacijaZelenogZida(noveKoordinate):
    if(noveKoordinate[0]<(vrsta*2)-2 and noveKoordinate[1]<(kolona*2)-2 and noveKoordinate[0]>-1 and noveKoordinate[1]>-1)== 1:
        if(a[noveKoordinate[0]][noveKoordinate[1]+1]==1 and a[noveKoordinate[0]+2][noveKoordinate[1]+1]==1 and a[noveKoordinate[0]+1][noveKoordinate[1]]==1 and a[noveKoordinate[0]+1][noveKoordinate[1]+2]==1): 
            return 1
        else: 
            return 0  
    else:
        return 0


def validacijaPlavogZida(noveKoordinate):
    if(noveKoordinate[0]<(vrsta*2)-2 and noveKoordinate[1]<(kolona*2)-2 and noveKoordinate[0]>-1 and noveKoordinate[1]>-1)== 1:
        if(a[noveKoordinate[0]+1][noveKoordinate[1]]==1 and a[noveKoordinate[0]+1][noveKoordinate[1]+2]==1 and a[noveKoordinate[0]][noveKoordinate[1]+1]==1 and a[noveKoordinate[0]+2][noveKoordinate[1]+1]==1): 
            return 1
        else: 
            return 0 
    else:
        return 0       


def izbaci_zid(boja,v,k):
    kor=(boja,v,k)
    filtered=[]
    global moguci_zidovi
    
    for zid in moguci_zidovi:
        if zid != kor:
            filtered.append(zid)
    moguci_zidovi=filtered


def postavljanjeZelenogZida(v,k):
    koor=(v,k)
    noveKoordinate=izracunajKoordinate(koor)

    if(validacijaZelenogZida(noveKoordinate)==1):
        novoV=noveKoordinate[0]
        novoK=noveKoordinate[1]

        lista=list(a[novoV])
        lista[novoK+1]=3
        a[novoV]=lista

        lista=list(a[novoV+2])
        lista[novoK+1]=3
        a[novoV+2]=lista

        global ubaceni_zidovi
        zid=('z',koor)
        ubaceni_zidovi.append(zid)
        print("Ubaceni zidovi: ")
        print(ubaceni_zidovi)

        izbaci_zid('p',v,k)
        izbaci_zid('z',v,k)
        izbaci_zid('z',v+1,k)

        #print("Moguci zidovi: ")
        #print(moguci_zidovi)

        global igrac
        if(igrac == "O"):
            global xZeleniZidovi
            xZeleniZidovi=xZeleniZidovi-1
        else:
            global oZeleniZidovi
            oZeleniZidovi=oZeleniZidovi-1
    else:
        print("Nevalidne koordinate za zeleni zid, unesite nove!")
        X=int(input("Unesite X koordinatu zida"))
        Y=int(input("Unesite X koordinatu zida"))
        postavljanjeZelenogZida(X,Y)


def postavljanjePlavogZida(v,k):
    koor=(v,k)
    noveKoordinate=izracunajKoordinate(koor)

    if(validacijaPlavogZida(noveKoordinate)==1):
        novoV=noveKoordinate[0]
        novoK=noveKoordinate[1]

        lista=list(a[novoV+1])
        lista[novoK]=3
        lista[novoK+2]=3
        a[novoV+1]=lista

        global ubaceni_zidovi
        zid=('p',koor)
        ubaceni_zidovi.append(zid)

        print("Ubaceni zidovi: ")
        print(ubaceni_zidovi)

        izbaci_zid('p',v,k)
        izbaci_zid('p',v,k+1)
        izbaci_zid('z',v,k)

        global igrac
        if(igrac == "O"):
            global xPlaviZidovi
            xPlaviZidovi=xPlaviZidovi-1
        else:
            global oPlaviZidovi
            oPlaviZidovi=oPlaviZidovi-1
    else: 
        print("Nevalidne koordinate za plavi zid, unesite nove!")
        X=int(input("Unesite X koordinatu zida: "))
        Y=int(input("Unesite X koordinatu zida: "))
        postavljanjePlavogZida(X,Y)


def promeniIgraca():
    global igrac
    if(igrac=="X"):
        igrac="O"
    else:
        igrac="X"


def validnoPoljeZaPesaka(pesak,novapoz)->int: 
    if novapoz[0]>-1 and novapoz[0]<int(vrsta*2) and novapoz[1]>-1 and novapoz[1]<int(kolona*2) and a[novapoz[0]][novapoz[1]]==0:
        if pesak[0]==novapoz[0]:           
            if novapoz[1]>pesak[1]:
                if (a[pesak[0]][pesak[1]+1] == 3) ==1:
                    return 0
                elif(a[pesak[0]][pesak[1]+3] == 3)==1:
                    return 2  
                else:
                    return 1
            else:
                if (a[pesak[0]][pesak[1]-1] == 3)==1:
                    return 0
                elif(a[pesak[0]][pesak[1]-3] == 3)==1:
                    return 2
                else:
                    return 1
        elif pesak[1]==novapoz[1]:
            if novapoz[0]>pesak[0]:
                if (a[pesak[0]+1][pesak[1]] == 3)==1:
                    return 0
                elif(a[pesak[0]+3][pesak[1]] == 3)==1:
                    return 2    
                else:
                    return 1
            else:
                if (a[pesak[0]-1][pesak[1]] == 3)==1:
                    return 0
                elif(a[pesak[0]-3][pesak[1]] == 3)==1:
                    return 2     
                else:
                    return 1
        else: 
            if (a[pesak[0]][pesak[1]-1]== 3 and a[novapoz[0]][novapoz[1]+1]== 3) or (a[pesak[0]-1][pesak[1]-2]== 3 and a[pesak[0]-1][pesak[1]]== 3) or (a[pesak[0]-2][pesak[1]-1]== 3 and a[pesak[0]-1][pesak[1]-2]== 3) or (a[pesak[0]][pesak[1]-1]== 3 and a[pesak[0]-1][pesak[1]]== 3) : 
                return 0
            elif (a[novapoz[0]][pesak[1]+1]== 3 and a[pesak[0]][novapoz[1]-1]== 3) or (a[pesak[0]-1][pesak[1]]== 3 and a[pesak[0]-1][pesak[1]+2]== 3) or (a[pesak[0]-2][pesak[1]-1]== 3 and a[pesak[0]-1][pesak[1]+2]== 3) or (a[pesak[0]-1][pesak[1]]== 3 and a[pesak[0]][pesak[1]+1]== 3): 
                return 0
            elif (a[novapoz[0]][pesak[1]-1]== 3 and a[pesak[0]+2][novapoz[1]-1]== 3) or (a[pesak[0]+1][pesak[1]-2]== 3 and a[pesak[0]+1][pesak[1]]== 3) or (a[pesak[0]][pesak[1]-1]== 3 and a[pesak[0]+2][pesak[1]-1]== 3) or (a[pesak[0]+1][pesak[1]-2]== 3 and a[pesak[0]+1][pesak[1]]== 3):  
                return 0
            elif (a[novapoz[0]][pesak[1]+1]== 3 and a[pesak[0]+2][novapoz[1]+1]== 3) or (a[pesak[0]+1][pesak[1]]== 3 and a[pesak[0]+1][pesak[1]+2]== 3) or (a[pesak[0]+1][pesak[1]]== 3 and a[pesak[0]][pesak[1]+1]== 3) or (a[pesak[0]+2][pesak[1]+1]== 3 and a[pesak[0]+1][pesak[1]+2]== 3): 
                return 0
            else:
                return 1
    else:
        return 0


def potezfunc(pozicija,potez,vred):
    vr=str(vred)
    global igrac
    global stanje
    if(vr=="X" or vr=="x"):
        igrac="X"
    else:
        igrac="O"
    match potez:
        case "Q":
            pozicijaI=int(pozicija[0]-2)
            pozicijaJ=int(pozicija[1]-2)
            novaPozicija=(pozicijaI,pozicijaJ)
            if validnoPoljeZaPesaka(pozicija,novaPozicija) == 1:
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            else:
                print("Nije moguce odigrati taj potez, molimo unesite novi potez")
                Potez(igrac)
                return 0
        case "W":
            pozicijaI=int(pozicija[0]-4)
            pozicijaJ=int(pozicija[1])
            novaPozicija=(pozicijaI,pozicijaJ)
            validnoPolje=validnoPoljeZaPesaka(pozicija,novaPozicija)
            if validnoPolje==1:
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            elif validnoPolje==2:
                novaPozicija=(pozicijaI+2,pozicijaJ)
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1    
            else:
                print("Nije moguce odigrati taj potez, molimo unesite novi potez")
                Potez(igrac)
                return 0 
        case "E":
            pozicijaI=int(pozicija[0]-2)
            pozicijaJ=int(pozicija[1]+2)
            novaPozicija=(pozicijaI,pozicijaJ)
            if validnoPoljeZaPesaka(pozicija,novaPozicija):
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1    
            else:
                print("Nije moguce odigrati taj potez")
                Potez(igrac)
                return 0 
        case "A":
            pozicijaI=int(pozicija[0])
            pozicijaJ=int(pozicija[1]-4)
            novaPozicija=(pozicijaI,pozicijaJ)
            validnoPolje=validnoPoljeZaPesaka(pozicija,novaPozicija)
            if validnoPolje==1:
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            elif validnoPolje==2:
                novaPozicija=(pozicijaI,pozicijaJ+2)
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            else:
                print("Nije moguce odigrati taj potez")
                Potez(igrac)
                return 0
        case "D":
            pozicijaI=int(pozicija[0])
            pozicijaJ=int(pozicija[1]+4)
            novaPozicija=(pozicijaI,pozicijaJ)
            validnoPolje=validnoPoljeZaPesaka(pozicija,novaPozicija)
            if validnoPolje ==1:
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            elif validnoPolje == 2:
                novaPozicija=(pozicijaI,pozicijaJ-2)
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1    
            else:
                print("Nije moguce odigrati taj potez")
                Potez(igrac)
                return 0 
        case "Z":
            pozicijaI=int(pozicija[0]+2)
            pozicijaJ=int(pozicija[1]-2)
            novaPozicija=(pozicijaI,pozicijaJ)
            if validnoPoljeZaPesaka(pozicija,novaPozicija):
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            else:
                print("Nije moguce odigrati taj potez") 
                Potez(igrac)
                return 0
        case "X":
            pozicijaI=int(pozicija[0]+4)
            pozicijaJ=int(pozicija[1])
            novaPozicija=(pozicijaI,pozicijaJ)
            validnoPolje=validnoPoljeZaPesaka(pozicija,novaPozicija)
            if validnoPolje==1:
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            elif validnoPolje==2:
                novaPozicija=(pozicijaI-2,pozicijaJ)
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1     
            else:
                print("Nije moguce odigrati taj potez")
                Potez(igrac)
                return 0 
        case "C":
            pozicijaI=int(pozicija[0]+2)
            pozicijaJ=int(pozicija[1]+2)
            novaPozicija=(pozicijaI,pozicijaJ)
            if validnoPoljeZaPesaka(pozicija,novaPozicija):
                zameniVrednost(pozicija,novaPozicija[0],novaPozicija[1],vr)
                print("Uspesan potez")
                promeniIgraca()
                stanje=(novaPozicija[0],novaPozicija[1])
                return 1
            else:
                print("Nije moguce odigrati taj potez") 
                Potez(igrac)
                return 0
        case _:
            print("Greska: potezfunc")


def Potez(igrac):
    print("Na potezu je igrac:",igrac)
    brojPesaka=int(input("Broj pesaka: "))
    validanBrojPesaka=0
    while validanBrojPesaka == 0:
        if brojPesaka == 1 or brojPesaka == 2:
            validanBrojPesaka=1
            if str(igrac)=="X":
                print("Broj preostalih zidova: plavi:",xPlaviZidovi," zeleni:", xZeleniZidovi)
                if brojPesaka==1:
                    igracNaPotezu="X1"
                else:
                    igracNaPotezu="X2"
            else:
                print("Broj preostalih zidova: plavi:",oPlaviZidovi," zeleni:", oZeleniZidovi)
                if brojPesaka==1:
                    igracNaPotezu="O1"
                else:
                    igracNaPotezu="O2"
        else:
            brojPesaka=int(input("Nepostojeci pesak, izaberite opet: "))           
        
    Potez=str(input("Unesite koji potez zelite da odigrate pritiskom na jedan od ovih tastera: Q W E A D Z X C: "))
    Potezi=["Q","W","E","A","D","Z","X","C"]
    
    validanTaster=0
    while validanTaster == 0:
        if Potez not in Potezi:
            Potez=str(input("Pogresan taster, unesite opet: "))
        else:
            validanTaster=1
        

    #print("Pozicije:",pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2)
    dobarPotez=0

    match igracNaPotezu:
        case "X1":
            dobarPotez=potezfunc(pozicijaX1,Potez,"X")
        case "X2":
            dobarPotez=potezfunc(pozicijaX2,Potez,"x")
        case "O1":
            dobarPotez=potezfunc(pozicijaO1,Potez,"O")
        case "O2":
            dobarPotez=potezfunc(pozicijaO2,Potez,"o")
        case _:
            print("Greska: igrac na potezu")

    ukupanBrZidova=xPlaviZidovi+xZeleniZidovi+oPlaviZidovi+oZeleniZidovi

    if dobarPotez == 1 and ukupanBrZidova>0:
        prikaz(a)
        bojaZida=str(input("Unesite boju zida: (plavi ili zeleni): "))
        if igrac=="X":
            if bojaZida == "plavi":
                if xPlaviZidovi > 0:
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('p',ZidX,ZidY)
                    postavljanjePlavogZida(ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                elif xZeleniZidovi>0:
                    print("Nemate vise plavih zidova")
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('z',ZidX,ZidY)
                    postavljanjeZelenogZida(ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                else:
                    print("Nemate vise zidova!")               
            elif bojaZida == "zeleni":
                if xZeleniZidovi > 0:
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('z',ZidX,ZidY)
                    postavljanjeZelenogZida(ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                elif xPlaviZidovi>0:
                    print("Nemate vise zelenih zidova")
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('p',ZidX,ZidY)                    
                    postavljanjePlavogZida(ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                else:
                    print("Nemate vise zidova!")
        else:
            if bojaZida == "plavi":
                if oPlaviZidovi > 0:
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('p',ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                    postavljanjePlavogZida(ZidX,ZidY)
                elif oZeleniZidovi>0:
                    print("Nemate vise plavih zidova")
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('z',ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                    postavljanjeZelenogZida(ZidX,ZidY)
                else:
                    print("Nemate vise zidova!")               
            elif bojaZida == "zeleni":
                if oZeleniZidovi > 0:
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('z',ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                    postavljanjeZelenogZida(ZidX,ZidY)
                elif oPlaviZidovi>0:
                    print("Nemate vise zelenih zidova")
                    ZidX=int(input("Unesite X koordinatu zida: "))
                    ZidY=int(input("Unesite Y koordinatu zida: "))
                    zid=('p',ZidX,ZidY)
                    stanjeIgre=(pozicijaX1,pozicijaX2,pozicijaO1,pozicijaO2,zid)
                    postavljanjePlavogZida(ZidX,ZidY)
                else:
                    print("Nemate vise zidova!")
    """
    minimaxStanjeO1=minimax(pozicijaO1,1,False)
    minimaxStanjeO2=minimax(pozicijaO2,1,False)

    if minimaxStanjeO1[1]>minimaxStanjeO2[1]:
        stanje=(pozicijaO1,minimaxStanjeO1[0])
        zid=moguci_zidovi[0]
        novoStanje=(stanje,zid)
        odigrajstanje(novoStanje,"O")
    else:
        stanje=(pozicijaO2,minimaxStanjeO2[0])
        zid=moguci_zidovi[0]
        novoStanje=(stanje,zid)
        odigrajstanje(novoStanje,"o")
    """
    

def odigrajstanje(stanje,vrednost):

    potez=stanje[0]
    trenutnaPoz=potez[0]
    novaPoz=potez[1]
    zameniVrednost(trenutnaPoz,novaPoz[0],novaPoz[1],vrednost)
    
    zid=stanje[1]
    bojaZida=zid[0]
    zidX=zid[1]
    zidY=zid[2]

    if bojaZida== 'p':
        postavljanjePlavogZida(zidX,zidY)
    else:
        postavljanjeZelenogZida(zidX,zidY)

    promeniIgraca()   
    

def novaStanja(stanje):
    Potezi=["Q","W","E","A","D","Z","X","C"]
    svaNovaStanja=[]
    
    for potez in Potezi:
        novaPoz=pokretPesaka(stanje,potez)
        if novaPoz != (0,0):
            svaNovaStanja.append(novaPoz)    

    return svaNovaStanja


def pokretPesaka(pesak,potez)->tuple:
    match potez:
            case "Q":
                pozicijaI=int(pesak[0]-2)
                pozicijaJ=int(pesak[1]-2)
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "W":
                pozicijaI=int(pesak[0]-4)
                pozicijaJ=int(pesak[1])
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "E":
                pozicijaI=int(pesak[0]-2)
                pozicijaJ=int(pesak[1]+2)
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "A":
                pozicijaI=int(pesak[0])
                pozicijaJ=int(pesak[1]-4)
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "D":
                pozicijaI=int(pesak[0])
                pozicijaJ=int(pesak[1]+4)
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "Z":
                pozicijaI=int(pesak[0]+2)
                pozicijaJ=int(pesak[1]-2)
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "X":
                pozicijaI=int(pesak[0]+4)
                pozicijaJ=int(pesak[1])
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case "C":
                pozicijaI=int(pesak[0]+2)
                pozicijaJ=int(pesak[1]+2)
                novaPozicija=(pozicijaI,pozicijaJ)
                dobarPotez=validnoPoljeZaPesaka(pesak,novaPozicija)
            case _:
                print("Greska")   
    if(dobarPotez>0):
        return novaPozicija
    else:
        return (0,0)

def procenistanje(stanje)->int:
    
    if igrac=="O":
        tx1=(pocetnaPozX1[0]-stanje[0])/2
        if(tx1<0):
            tx1=tx1*(-1)
        tx2=(pocetnaPozX2[0]-stanje[0])/2
        if(tx2<0):
            tx2=tx2*(-1)
        ty1=(pocetnaPozX1[1]-stanje[1])/2
        if(ty1<0):
            ty1=ty1*(-1)
        ty2=(pocetnaPozX2[1]-stanje[1])/2
        if(ty2<0):
            ty2=ty2*(-1)

        t1=tx1+ty1
        t2=tx2+ty2
        if(t1>t2): return t2
        else: return t1
        
def max_stanje(lsv):
    return max(lsv, key=lambda x : x[1])

def min_stanje(lsv):
    return min(lsv, key=lambda x : x[1])

def minimax(stanje, dubina, moj_potez):  
    lp = novaStanja(stanje)
    #print("Stanje je: ",stanje, " Lista novih stanja: ",lp)

    fja = max_stanje if moj_potez else min_stanje

    if dubina == 0 or lp is None:
       return (stanje, procenistanje(stanje))
    
    return fja([minimax(x, dubina - 1, not moj_potez) for x in lp])

     

global igrac
igrac="X"
pocetnostanje()
kraj=0
while(kraj != 1):  
    Potez(igrac) 
    prikaz(a)
    kraj=krajIgre()

