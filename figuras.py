class kubs:

    def __init__(self, garums, krasa): #inicializē objektu

        if garums>=2 and garums<=10: #garuma parametri/robežas
            self.garums = garums #ja garums neatrodas noteiktajās robežās
        else:
            print("Malas garums neatbilst nosacījumiem")
            self.garums = 2

        self.krasa = krasa #aprēķina kuba tilpumu

    def aprekinat_tilpums(self):
        tilpums = self.garums**3
        return tilpums

    def __del__(self): #dzēš
        print("Objekts ir likvidēts! Tā krāsa bija", self.krasa)


kubg = kubs(10, "zaļa")
kubr = kubs(1, "sarkana")

print(kubg.krasa, kubg.aprekinat_tilpums()) #izvada kuba krāsu (zaļa) un tilpumu (ko aprēķina funkcija aprekinat_tilpumu)
print(kubr.garums) #izvada kuba garumu (1)

del kubr #izsauc __del__ metodi, dzēš nederīgo kubu
#var izmantot if vietā
try:
    print(kubr.garums)
except:
    print("Objekts neeksistē!")

print(kubg.garums)


class bloks(kubs): #klase bloks manto no klases kubs

    def __init__(self, garums, krasa, kubu_skaits, forma):

        super().__init__(garums, krasa)

        if kubu_skaits >= 1 and kubu_skaits <= 4:
            self.__kubu_skaits = kubu_skaits #privātas īpašības
        else:
            print("Nepareiza kubu skaita vērtība!")

        self.nosaukums = str(self.krasa)+str(kubu_skaits)

        formas_vertibas = [11, 12, 13, 14, 22]

        if forma not in formas_vertibas:
            print("Forma neatbilst nosacījumiem!")
            self.derigums = 0
        else:
            self.derigums = 1
        
    def tilpums(self):
        kuba_tilpums = self.garums**3 #lai nebūtu jāizsauc vecāka klases metode, tilpums VIENAM kubam
        bloka_tilpums = kuba_tilpums*self.__kubu_skaits #tilpums kubu skopojumam
        return bloka_tilpums
    
    def mainit_formu(self, jauna_forma):
        formas_vertibas = [11, 12, 13, 14, 22]
        if jauna_forma not in formas_vertibas:
            print("Forma neatbilst nosacījumiem!")
            self.derigums = 0
        else:
            self.derigums = 1


orange3 = bloks(5, "oranža", 3, 13)
print(orange3.nosaukums, orange3.tilpums())

blue5 =bloks(7, "zila", 5, 23)
print(blue5.nosaukums, blue5.derigums)

blue5.mainit_formu(12)
print(blue5.nosaukums, blue5.derigums)