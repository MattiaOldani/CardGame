import random
import time

player1, player2, complete, table=[], [], [], []
retire=False
flip=1

for i in range(1, 11):
    for j in range(0, 4):
        complete.append(i)
random.shuffle(complete)

while len(complete)>0:
    player1.append(complete.pop(0))
    player2.append(complete.pop(0))

while True:
    if player1[2]==3 and player1[4]==2 and player1[6]==2 and player1[8]==3 and player1[10]==3 and player1[11]==1 and player1[17]==3 and player1[18]==1:
        if player1[2]==1 and player1[5]==2 and player1[10]==2 and player1[18]==1:
            random.shuffle(player1)
            random.shuffle(player2)
        else:
            random.shuffle(player1)
    else:
        if player1[2]==1 and player1[5]==2 and player1[10]==2 and player1[18]==1:
            random.shuffle(player2)
        else:
            break

turn=random.randint(1, 2)
print("Parte il giocatore "+str(turn)+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\n")

while len(player1)!=0 and len(player2)!=0:
    if turn==1:
        if retire:
            c=0
            while c<flip and len(player1)>0:
                table.append(player1.pop(0))
                print("Gira una carta il giocatore 1"+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\ntable: "+str(table)+"\n")
                if table[len(table)-1]>3:
                    c=c+1
                else:
                    flip=table[len(table)-1]
                    break
                if len(player1)==0 or c==flip:
                    while len(table)>0:
                        player2.append(table.pop(0))
                    print("Ritira il giocatore 2"+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\ntable: "+str(table)+"\n")
                    flip=1
                    retire=False
        else:
            table.append(player1.pop(0))
            flip=table[len(table)-1]
            if flip<4:
                retire=True
            print("Gira una carta il giocatore 1"+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\ntable: "+str(table)+"\n")
        turn=2
    else:
        if retire:
            c=0
            while c<flip and len(player2)>0:
                table.append(player2.pop(0))
                print("Gira una carta il giocatore 2"+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\ntable: "+str(table)+"\n")
                if table[len(table)-1]>3:
                    c=c+1
                else:
                    flip=table[len(table)-1]
                    break
                if len(player2)==0 or c==flip:
                    while len(table)>0:
                        player1.append(table.pop(0))
                    print("Ritira il giocatore 1"+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\ntable: "+str(table)+"\n")
                    flip=1
                    retire=False
        else:
            table.append(player2.pop(0))
            flip=table[len(table)-1]
            if flip<4:
                retire=True
            print("Gira una carta il giocatore 2"+"\nGiocatore1: "+str(player1)+"\nGiocatore2: "+str(player2)+"\ntable: "+str(table)+"\n")
        turn=1

if len(player1)==0:
    print("Ha vinto il giocatore2")
else:
    print("Ha vinto il giocatore1")
