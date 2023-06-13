

def zamiana(liczba,podstawa):
    bin = "";
    while(liczba):
        bin=str(liczba%podstawa)+bin
        liczba=liczba//podstawa
    return  bin


def ile_blokow(liczba):
    bin = zamiana(liczba,2)
    print(bin)
    bloki = 1
    for i in range(1,len(bin)):
        print(bin[i],bloki)
        if bin[i-1] != bin[i]:
            bloki=bloki+1


ile_blokow(456)