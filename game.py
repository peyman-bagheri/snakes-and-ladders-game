from turtle import *
from random import *
import os
g = Pen()
t = Pen()
pc = Pen()
f = Pen()
t.color('green')
bg = Screen()
bg.bgcolor("yellow")
num1 = 0
num2 = 10
a = -350
b = -290
m = -350
n = -300
r1 = r2 = 0
flag = 0
lista = None
listb =[[-900,-900]]
listc = None
listd =[[-900,-900]]

def tur () : #draw a table
    
    t.up()
    t.setx(-380)
    t.sety(-310)
    t.down()
    t.forward(710)
    t.left(90)
    t.forward(510)
    t.left(90)
    t.forward(710)
    t.left(90)
    t.forward(510)
    t.backward(50)
    t.left(90)
    t.forward(710)

    def left() :
        t.left(90)
        t.forward(50)
        t.left(90)
        t.forward(710)

    def right() :
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(710)

    def left2() :
        t.left(90)
        t.forward(70)
        t.left(90)
        t.forward(510)

    def right2() :
        t.right(90)
        t.forward(70)
        t.right(90)
        t.forward(510)

    for x in range(4)  :
        left()
        right()
  
    t.left(90)
    t.forward(59)
    
    for x in range(4) :
        left2()
        right2()
  
    left2()
    t.up()
    t.right(90)
    t.forward(79)
    t.right(90)
    t.forward(30)
    t.down()
def num (x , y) : # write number
    for z in range(x,y) :
        t.write(z+1)
        t.up()
        t.forward(70)
        t.down()
    t.up()
    t.backward(710)
    t.up()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.right(180)
    t.forward(10)
    t.down()
def bomb () :#creat bomb
    for x in range(5) :
        c = a + (randint(0 , 8) * 70)
        d = b +(randint(1 , 9) * 50)
        t.goto((c+10) , d)
        t.down()
        t.write("@@")
        lista = [[c,d]]
        listb.extend(lista)
        t.up()
        t.goto(390 , 310)
def ladder () :#creat ladder
    for x in range(5) :
        c = a + (randint(1 , 8) * 70)
        d = b +(randint(0 , 8) * 50)
        for x in listb : # chek ladder != bomb
            if (c == x[0]) and (d == x[1]) :
                continue

        t.goto((c+10) , d)
        t.down()
        t.write("==>")
        listc = [[c,d]]
        listd.extend(listc)
        t.up()
        t.goto(390 , 310)


# execution
t.speed(0)
f.up()
tur()
t.up()
t.right(90)
t.forward(15)
t.down()
for x in range(10) :
    num(num1,num2)
    num1 +=10
    num2 +=10

f.goto(-290 , 290)
f.write("you are red", None, "center", "30pt")
f.goto(-290 , 250)
f.write("pc is blue", None, "center", "30pt")
f.goto(250 , 290)
f.write("Bomb = @@", None, "center", "30pt")
f.goto(250 , 250)
f.write("ladder = ==>", None, "center", "30pt")
f.goto(390 , 310)
t.up()
g.up()
pc.up()
bomb()
ladder()
t.speed(1)
g.speed(1)
pc.speed(1)
g.goto(a,b)
pc.goto(m,n)
g.pencolor("red")
pc.pencolor("blue")

while (True) : #start game by user
    for x in range(300000) :
        x +=1
    os.system('cls')
    w = input("press A or B \n")
    rand = randint(1,6)
    rand2 = randint(1,6)
    if w.upper() !="A" and w.upper() != "B" :
        print("ERORR")
        continue

    if w.upper() == "B" :
        x = rand
        rand = rand2
        rand2 = x
    print("Your choice" , rand)
    print(" another number is" , rand2)
    
    if rand == 6 : #check prize
        print("you have a prize ")
        rand += randint(1,6)
        print("your number is" , rand)
    r3 = (rand * 70 )
    a = a + r3

    if a > 280 and b == 160 : # if out fo range
        print("dont move!")
        a = a - r3

    if a > 280 : # if enter new column
        g.goto(280 , b)
        if a-r3 == 280 :
            b +=50
            a = -350 + (r3-70)
        else :
            b +=50
            z = (a - 280) /70
            a = -350 +((z-1) *70)
     
    if a == 280 and b == 160 : # if game end
        g.goto(a , b)
        print("you winer !!!!!!!!!!!")
        t.clear()
        g.clear()
        pc.clear()
        bg.clear()
        f.pencolor("red")
        f.goto(0 , 0)
        f.write("you winer :)", None, "center", "50pt")
        break
  
    if a == m and b == (n+10) : #check hit
        print("you hit :)")
        g.goto(a,b)
        m = -350
        n = -300
        pc.goto(m , n)
   
    for x in listb : # chek bomb
        if (a == x[0]) and (b == x[1]) :
            print("***!!!bomb!!!***")
            g.goto(a,b)
            a = -350
            b = -290
            g.goto(a,b)
            continue

    for x in listd : # chek ladder
        if (a == x[0]) and (b == x[1]) :
            print("***!!! ladder !!!***")
            g.goto(a,b)

            while( True ) :
                flag = 0
                a = a-r1
                b = b-r2
                r1 = (randint(0 , 8) * 70)
                r2 = (randint(0 , 8) * 50)
                a = a+r1
                b = b+r2

                for x in listb : # chek bomb != Destination
                    if (a == x[0]) and (b == x[1]) :
                        flag =1
                        break

                for x in listd : # chek Destination not another ladder
                    if (a == x[0]) and (b == x[1]) :
                        flag =1
                        break

                if a <= 280 and b < 160 and flag == 0  :
                    break
                    r1 = r2 = 0
    
    g.goto(a , b)
###############################################################################################

 #start game by pc
    rand = randint(1,6)
 
    if rand == 6 : #check prize
        rand += randint(1,6)
    r3 = (rand * 70 )
    m = m + r3
    
    if m > 280 and (n+10) == 160 : # if out fo range
        m = m - r3
        continue

    if m > 280 : # if enter new column
        pc.goto(280 , n)

        if m-r3 == 280 :
            n +=50
            m = -350 + (r3-70)
        else :
            n +=50
            z = (m - 280) /70
            m = -350 +((z-1) *70)

    if m == 280 and (n+10) == 160 : # if game end
        pc.goto(m , n)
        print("you loser !!!!!!!!!!!")
        t.clear()
        g.clear()
        pc.clear()
        bg.clear()
        f.pencolor("red")
        f.goto(0 , 0)
        f.write("you loser :(", None, "center", "50pt")
        break
   
    if a == m and b == (n+10) : #check hit
        print("you hit :(")
        pc.goto(m,n)
        a = -350
        b = -290
        g.goto(a , b)

    for x in listb : # chek bomb
        if (m == x[0]) and ((n+10) == x[1]) :
            pc.goto(m,n)
            m = -350
            n = -300
            pc.goto(m,n)
            continue

    for x in listd : # chek ladder
        if (m == x[0]) and ((n+10) == x[1]) :
            pc.goto(m,n)

            while( True ) :
                flag = 0
                m = m-r1
                n = n-r2
                r1 = (randint(0 , 8) * 70)
                r2 = (randint(0 , 8) * 50)
                m = m+r1
                n = n+r2

                for x in listb : # chek bomb != Destination
                    if (m == x[0]) and ((n+10) == x[1]) :
                        flag =1
                        break

                for x in listd : # chek Destination not another ladder
                    if (m == x[0]) and ((n+10) == x[1]) :
                        flag =1
                        break
                        
                if m <= 280 and n+10 < 160 and flag == 0  :
                    break
                    r1 = r2 = 0

    pc.goto(m , n)

 



























