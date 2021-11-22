f=open('text.txt', 'w')
text=input('Dati textul pentru fisier:')
f.write(text)
f.close()

f=open('text.txt', 'r')
t=f.read()
vocale=[]
nr_vocale=0
for i in t:
    if (i=='A') or (i=='a') or (i=='E') or (i=='e') or (i=='I') or (i=='i') or (i=='O') or (i=='o') or (i=='U') or (i=='u'):
        vocale+=i
        nr_vocale+=1
f.close()

f=open('vocale.txt', 'a')
f.write(str(vocale))
f.write('\n')
f.write('Numarul de vocale este:')
f.write(str(nr_vocale))
f.close()