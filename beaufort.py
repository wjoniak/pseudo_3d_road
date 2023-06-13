tekst="MAPA"
szyfrogram=[]
k=1

for i in range(len(tekst)):
    szyfrogram.append(chr(((90-ord(tekst[i])+k) % 26)+65))
    k = k + i

print(szyfrogram)