import random

kleuren = ["rood","geel", "groen", "blauw"]
kleur = random.choice(kleuren)

print("random kleur is " + kleur )

N1 = ['Grote ','Kleine ','Rood ','Snele ','trage ','Warme ','Koude ','Gelukkigge ','luie ','Nieuwe ']
N2 = ["meisje", "jongen", "olifant", "vogel", "heks", "kind", "dino", "man", "vrouw" ]

naam1 = random.choice(N1)
naam2 = random.choice(N2)
for i in range(10):
    naam1 = random.choice(N1)
    naam2 = random.choice(N2)

    print("random naam is " + naam1 + naam2 )
