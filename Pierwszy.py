#!/usr/bin/env python3
# -*- coding: utf-8 -*-
marker=["s","v","o","d","D"]
from matplotlib import pyplot as plt
import numpy as np
import re
class danazcsv:
    def __init__(self):
        #inicjalizacja klasy
        self.naglowek=[]
        self.dane=[]
    #filter(None,...) zostal uzyty do wywalenia pustych słów z listy jakie generowała funkcja re.split("[,\n]",line)
    def add_naglowek(self,line):
        #dodawanie nagłówka z nazwami
        self.naglowek=list(filter(None, re.split("[,\n]", line)))
    def dodaj_dane(self,line):
        #dodawanie dodany z konwersją z tekstu do liczby
        self.dane+=[list(map(float,list(filter(None, re.split("[,\n]", line)))))]
    def konwersja_danych(self):
        #przekształcenie dotychczasowej listy w tablicę numpy
        self.dane=np.array(self.dane)
        #skrócenie 32 badań do średniej arytmetycznej przy użyciu np.mean i przekształceń z macierzami transponowanymi- łączenie dwóch macierzy
        self.dane=np.array(list(self.dane[:,:2].T)+[list(np.mean(self.dane[:,2:],axis=1))]).T
        self.naglowek=self.naglowek[:2]+["srednia"]
legenda=[]
zm1,(plocik,kocik)=plt.subplots(1,2)
ploty=[]
for k,jana in enumerate(["1coev.csv","1coevrs.csv","1evolrs.csv","2coev.csv","2coevrs.csv"]):
    ila=danazcsv()
    f=open(jana,"r")
    legenda+=[(lambda a: a[0]+'-'+a[1].upper()+a[2:a.find("rs")]+("-RS" if a.find("rs")!=-1 else a[-1]))(jana.split('.')[0])]
    plik=f.readlines()
    ila.add_naglowek(plik[0])
    for i in range(1,len(plik)):
        ila.dodaj_dane(plik[i])
    ila.konwersja_danych()
    plocik.plot(ila.dane[:,1:2].T[0]/1000,ila.dane[:,2:3].T[0],marker[k],ls='-',markevery=25)
    ploty+=[ila.dane[:,2:3].T[0]]
plocik.set_ylabel("Odsetek wygranych gier")
plocik.set_xlabel("Ilość rozegranych gier"+ r'$\times$'+ "1000")
plocik.legend(legenda)
plocik.set_title("Charakterystyka zależności odsetku wygranych gier\n do rozegranych w zależności od strategii")
plocik.grid()
kocik.boxplot(ploty)
plt.xticks([1,2,3,4,5],legenda)
plt.show()
plt.close()

