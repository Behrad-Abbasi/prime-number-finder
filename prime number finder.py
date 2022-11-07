import os
from time import sleep
from time import time
from math import sqrt

primenum = None
lpnl = []
try:
    pnl = open(""+os.path.dirname(os.path.abspath(__file__))+"\\pnl.txt" , "r")
    for line in pnl:
        if line == " " or line == "" :
            break
        lpnl.append(int(line.strip()))
    pnl.close()
except:
    pnl = open(""+os.path.dirname(os.path.abspath(__file__))+"\\pnl.txt" , "w")
    pnl.write("2")
    lpnl.append(2)
    pnl.close()
mpnl = max(lpnl)
inp = int(input("1 for auto find , 2 for number select : "))

if inp == 1:
    inp2 = int(input("max number : "))
    if inp2 <= mpnl:
        print("low number . last num saved =", mpnl)
        sleep(10)
        quit()
    inp3 = int(input("print prime numbers? 1 = yes , other = no : ")) 
    t1i1 = time()   
    inp2 = inp2 - mpnl
    n = mpnl
    for nn in range(inp2):
        n = n + 1
        sn = sqrt(n)
        if sn == int(sn):
            continue
        else :
            sn = int(sn)
            for n2 in range(len(lpnl)) :
                l = lpnl[n2]
                a = n % l
                if a == 0 :
                    primenum = False
                    break
                primenum = True
                if sn < lpnl[n2]:
                    break
            if primenum == True:
                b = open(""+os.path.dirname(os.path.abspath(__file__))+"\\pnl.txt" , "w")
                for i in range(len(lpnl)):
                    b.write(str(lpnl[i]))
                    b.write("\n")
                b.write(str(n))
                b.write("\n")
                b.close()
                lpnl.append(n)
                if inp3 == 1:
                    print(n)
                    print("prime")
                primenum = False
    t2i1 = time()
    print("spent time : ",t2i1-t1i1)

if inp == 2:
    inp3 = int(input("your number : "))
    t1i2 = time()
    if inp3 == 1:
        print("it isn't a prime number : ",inp3)
        sleep(10)
        quit()
    si = sqrt(inp3)
    if si == int(si):
        print("it isn't a prime number : ",inp3)
        print("it can be divided by : ",si)
        t2i2 = time()
        print("spent time : ",t2i2-t1i2)
        sleep(10)
        quit()
    else:
        si = int(si)
    for n in range(len(lpnl)):
        if inp3 == lpnl[n]:
            print("it's a prime number : ",inp3)
            t2i2 = time()
            print("spent time : ",t2i2-t1i2)
            sleep(10)
            quit()
        r = inp3 % lpnl[n]
        if r == 0:
            print("it isn't a prime number : ",inp3)
            print("it can be divided by : ",lpnl[n])
            t2i2 = time()
            print("spent time : ",t2i2-t1i2)
            sleep(10)
            quit()
    if si > mpnl:
        for u in range(mpnl,si+1):
            r = inp3 % u
            if r == 0:
                print("it isn't a prime number : ",inp3)
                print("it can be divided by : ",u)
                t2i2 = time()
                print("spent time : ",t2i2-t1i2)
                sleep(10)
                quit()
    print("it's a prime number : ",inp3)
    t2i2 = time()
    print("spent time : ",t2i2-t1i2)
    sleep(10)
    quit()