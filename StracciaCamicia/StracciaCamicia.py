import random
import time

mazzo1, mazzo2, completo, banco=[], [], [], []
ritiro=False
girare=1

for i in range(1, 11):
    for j in range(0, 4):
        completo.append(i)
random.shuffle(completo)

while len(completo)>0:
    mazzo1.append(completo.pop(0))
    mazzo2.append(completo.pop(0))

while True:
    if mazzo1[2]==3 and mazzo1[4]==2 and mazzo1[6]==2 and mazzo1[8]==3 and mazzo1[10]==3 and mazzo1[11]==1 and mazzo1[17]==3 and mazzo1[18]==1:
        if mazzo1[2]==1 and mazzo1[5]==2 and mazzo1[10]==2 and mazzo1[18]==1:
            random.shuffle(mazzo1)
            random.shuffle(mazzo2)
        else:
            random.shuffle(mazzo1)
    else:
        if mazzo1[2]==1 and mazzo1[5]==2 and mazzo1[10]==2 and mazzo1[18]==1:
            random.shuffle(mazzo2)
        else:
            break

turno=random.randint(1, 2)
print("Parte il giocatore "+str(turno)+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\n")

while len(mazzo1)!=0 and len(mazzo2)!=0:
    if turno==1:
        if ritiro:
            c=0
            while c<girare and len(mazzo1)>0:
                banco.append(mazzo1.pop(0))
                print("Gira una carta il giocatore 1"+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\nBanco: "+str(banco)+"\n")
                if banco[len(banco)-1]>3:
                    c=c+1
                else:
                    girare=banco[len(banco)-1]
                    break
                if len(mazzo1)==0 or c==girare:
                    while len(banco)>0:
                        mazzo2.append(banco.pop(0))
                    print("Ritira il giocatore 2"+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\nBanco: "+str(banco)+"\n")
                    girare=1
                    ritiro=False
        else:
            banco.append(mazzo1.pop(0))
            girare=banco[len(banco)-1]
            if girare<4:
                ritiro=True
            print("Gira una carta il giocatore 1"+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\nBanco: "+str(banco)+"\n")
        turno=2
    else:
        if ritiro:
            c=0
            while c<girare and len(mazzo2)>0:
                banco.append(mazzo2.pop(0))
                print("Gira una carta il giocatore 2"+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\nBanco: "+str(banco)+"\n")
                if banco[len(banco)-1]>3:
                    c=c+1
                else:
                    girare=banco[len(banco)-1]
                    break
                if len(mazzo2)==0 or c==girare:
                    while len(banco)>0:
                        mazzo1.append(banco.pop(0))
                    print("Ritira il giocatore 1"+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\nBanco: "+str(banco)+"\n")
                    girare=1
                    ritiro=False
        else:
            banco.append(mazzo2.pop(0))
            girare=banco[len(banco)-1]
            if girare<4:
                ritiro=Tru
            print("Gira una carta il giocatore 2"+"\nGiocatore1: "+str(mazzo1)+"\nGiocatore2: "+str(mazzo2)+"\nBanco: "+str(banco)+"\n")
        turno=1

if len(mazzo1)==0:
    print("Ha vinto il giocatore2")
else:
    print("Ha vinto il giocatore1")
