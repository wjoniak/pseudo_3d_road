n = 5
books = [10,2,15,13,1,5,25]
bib = []



for k in range(n):
    polka =[]
    for l in range(2**k):
        polka.append(0)
    bib.append(polka)

i=0
j=1
for p in range(len(books)):
    print(p,i+1,2*j)
    if bib[i][j-1] == 0:
        bib[i][j-1] = books[p]
    else:
        insert = True
        while insert:
            if bib[i][j-1] < books[p]:
                i = i + 1
                j = 2*(j-1)-1
                if bib[i][j] == 0:
                    bib[i][j] = books[p]
                    insert = False
            else:
                i = i + 1
                j = 2*(j-1)
                if bib[i][j] == 0:
                    bib[i][j] = books[p]
                    insert = False
            # i=i+1
            # j=j+1
print(bib)
