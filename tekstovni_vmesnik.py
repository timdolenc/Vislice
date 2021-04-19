import model

def izpis_igre(igra):
    return (
        f"Igraš igro vislic:\n" + 
        f"Narobe ugibane črke so: {igra.nepravilni_ugibi()}\n"+
        f"Trenutno stanje besede: {igra.pravilni_del_gesla()}\n"
    )

def izpis_poraza(igra):
    return (
        f"Izgubil si, več sreče prihodnjič\n" +
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n" +
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n" +
        f"Pravilno geslo je bilo: {igra.geslo}" 
    )

def izpis_zmage(igra):
        return (
        f"Zmagal si!\n" +
        f"Narobe si uganil: {igra.nepravilni_ugibi()}\n" +
        f"Pravilno si uganil: {igra.pravilni_del_gesla()}\n" +
        f"Pravilno geslo je bilo: {igra.geslo()}" 
    )


def pozeni_vmesnik():
    igra = model.nova_igra(model.bazen_besed)

    while True:
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
        else:
            print(izpis_igre(igra))
            vnos = input("Vnesi novo črko:")
            igra.ugibaj(vnos)

pozeni_vmesnik()



