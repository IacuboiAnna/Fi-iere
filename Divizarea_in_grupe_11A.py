f=open('Lista Clasei 11A.txt', 'r')
linii=list(f)
f.close()
n=0
media=0
print('Nume', 'Prenume', 'Nota', sep='\t')
a=open('Lista Clasei 11A Engleza.txt', 'w')
b=open('Lista Clasei 11A Germana.txt', 'w')
for linie in linii:
    print(linie.rstrip())
    campuri=linie.split()
    nota=int(campuri[2])
    n+=1
    media+=nota
    if campuri[3]=='E':
        a.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        a.write('\n')
    if campuri[3]=='G':
        b.write(campuri[0]+' '+campuri[1]+' '+campuri[2])
        b.write('\n')
print('Media celor', n, 'studenti este', media/float(n))
a.close()
b.close()