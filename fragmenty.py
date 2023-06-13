fragmenty=[]
cyfry=[]
max = 0
min = 9999
plik=open("pi.txt","r")
for cyfra in plik:
    cyfry.append(cyfra.strip())
plik.close()
for i in range(10):
    for j in range(10):
        fragmenty.append(str(i)+str(j))
for f in fragmenty:
    licznik = 0
    cyfra1 = f[0]
    cyfra2 = f[1]
    for n in range(9999):
        if cyfry[n] == cyfra1 and cyfry[n+1] == cyfra2:
            licznik = licznik+1
    if licznik > max:
        max = licznik
        f_max = f
    if licznik < min:
        min = licznik
        f_min = f
print("max:",f_max,max)
print("min:", f_min, min)
