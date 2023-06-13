n = 5
books = [10,2,15,13,1,5,25]
bib = []



for k in range(n):
    polka =[]
    for l in range(2**k):
        polka.append(0)
    bib.append(polka)


def order(m):
    i = 0
    j = 0
    if bib[i][j] == 0:
        bib[i][j] = books[m]
        m = m + 1
        if m < 7:
            order(m)
    else:
        while True:
            if bib[i][j] < books[m]:
                i = i + 1
                j = 2*j
                if bib[i][j] == 0:
                    bib[i][j] = books[m]
                    m = m + 1
                    if m < 7:
                        order(m)
            else:
                i = i + 1
                j = 2*j+1
                if bib[i][j] == 0:
                    bib[i][j] = books[m]
                    m = m + 1
                    if m < 7:
                        order(m)


order(0)

print(bib)