with open("owoce.txt", "r") as plik:
    owoce = [(line.strip().split()) for line in plik]

licznik = 0
porzeczki = 0
truskawki = 0
maliny = 0
dzem_tp = 0
dzem_tm = 0
dzem_mp = 0



for dzien in range(len(owoce)):
    if owoce[dzien][3] > owoce[dzien][2] and owoce[dzien][3] > owoce[dzien][1]:
        licznik=licznik+1

print(licznik)

for dzien in range(1,len(owoce)):

    maliny = maliny + int(owoce[dzien][1])
    truskawki = truskawki + int(owoce[dzien][2])
    porzeczki = porzeczki + int(owoce[dzien][3])

    if (maliny >= truskawki) and (maliny >= porzeczki):
        skladnik1 = maliny
        maliny = maliny - skladnik1
        if (truskawki >= porzeczki):
            skladnik2 = truskawki
            truskawki = truskawki - skladnik2
        else:
            skladnik2 = porzeczki
            porzeczki = porzeczki -skladnik2
    elif (truskawki >= maliny) and (truskawki >= porzeczki):
        skladnik1 = truskawki
        truskawki = truskawki - skladnik1
        if (maliny >= porzeczki):
            skladnik2 = maliny
            maliny = maliny - skladnik2
        else:
            skladnik2 = porzeczki
            porzeczki = porzeczki - skladnik2
    else:
        skladnik1 = porzeczki
        porzeczki = porzeczki - skladnik1
        if (truskawki >= porzeczki):
            skladnik2 = truskawki
            truskawki = truskawki - skladnik2
        else:
            skladnik2 = porzeczki
            porzeczki = porzeczki - skladnik2

    print(maliny,truskawki,porzeczki, skladnik1,skladnik2)



