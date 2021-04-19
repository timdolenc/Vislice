#vse kar hočemo vedet o stanju igre more bit tu shranjeno
#v tem primeru je dovolj informacij če mamo sam ugibe in geslo  
#zakaj je fajn da si nekje gor definiramo st dovoljenih napak
import random 

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA, PONOVLJENA_CRKA, NAPACNA_CRKA = '+', 'o', '-'
ZMAGA = "W"
PORAZ = "X"

class Igra:
    def __init__(self, geslo, ugibane):
        self.geslo = geslo.upper()
        self.crke = ugibane.upper() #do sedaj ugibane crke, tta init je edini način kk lahk igra vstopi tkda ko tu popravimo smo zmagali
    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]
    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]
    def stevilo_napak(self):
        return len(self.napacne_crke())
    def zmaga(self):            # all([i in self.crke for i in self. geslo]) preveri če za vse to velja
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True
    def poraz(self):
        if self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK:
            return True
        return False
    def pravilni_del_gesla(self):
        niz = ""
        for crka in self.geslo:
            if crka in self.crke:
                niz += crka
            else:
                niz += "_"
        return niz
    #def nepravilni_ugibi(self):
    #    niz = " "
    #    for crka in self.crke:
    #        if crka not in self.geslo:
    #            niz = niz + crka + " "
    #    return niz.strip()
    def nepravilni_ugibi(self):
        return " ".join(self.napacne_crke())
    def ugibaj(self, crka):
        crka = crka.upper()
        if self.poraz():
            return PORAZ
        if crka in self.crke:
            return PONOVLJENA_CRKA
        self.crke += crka
        if self.zmaga():
            return ZMAGA
        if self.poraz():
            return PORAZ
        return NAPACNA_CRKA

bazen_besed = []
with open("besede.txt", encoding="UTF-8") as input_file:
    bazen_besed = input_file.readlines()

def nova_igra(bazen_besed):
    beseda = random.choice(bazen_besed)

    return Igra(beseda, "")

i = nova_igra(bazen_besed)
print(i.geslo)



# sredi igre omogoča vpis črke








igra1 = Igra("banana", "anbk")
igra2 = Igra("papir", "sbnkmlr")
print(igra1.geslo)
print(f"NAPAČNE: {igra1.napacne_crke()}")
print(f"PRAVILNE: {igra1.pravilne_crke()}")
print(igra1.stevilo_napak())
print(igra2.pravilni_del_gesla())
print(igra2.nepravilni_ugibi())






        