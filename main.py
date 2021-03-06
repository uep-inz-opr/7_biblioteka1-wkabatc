import re

class Biblioteka():
    def __init__(self,lista_ksiazek = []):
        self.lista_ksiazek = lista_ksiazek

    def dodaj_egzemplarz_ksiazki(self,ksiazka):
        self.lista_ksiazek.append(ksiazka)

    def dostepne_egz(self):
        tytuly = []
        ilosci = []
        wynik = []
        i = 0
        for ks in self.lista_ksiazek:
            tytuly.append(ks.tytul)
        for t in tytuly:
            ilosci.append(tytuly.count(t))
        for ks in self.lista_ksiazek:
            w = "('"+ks.tytul+"', '"+ks.autor+"', "+str(ilosci[i])+")"
            i += 1
            wynik.append(w)
        wynik = set(wynik)
        wynik = sorted(wynik)
        for wyn in wynik:
            print(wyn)

class Ksiazka():
    def __init__(self,tytul,autor):
        self.tytul = tytul
        self.autor = autor
        
class Egzemplarz(Ksiazka):
    def __init__(self,tytul,autor,rok_wydania):
        Ksiazka.__init__(self,tytul,autor)
        self.rok_wydania = rok_wydania

biblioteka = Biblioteka()
n = int(input())

for num in range(n):
    inp = input()
    ks = inp.split('"')[1::2]
    rok = int(re.search(r'\d+', inp).group())
    biblioteka.dodaj_egzemplarz_ksiazki(Egzemplarz(ks[0].strip(), ks[1].strip(), rok))

biblioteka.dostepne_egz()