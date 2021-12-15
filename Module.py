def Kolmnurga_pindala(külg:float,kõrgus:float):
    """Leiab kolmnurga pindalat. On andtud kõrgus ja küljepikkus. Tagastab S float formaadis
    :param float külg: Kolmnurga külje pikkus
    :param float kõrgus: Kõrgus vastav küljele
    :rtype: var
    """
    if külg<0 or kõrgus<0:
        S="valed andmed!"
    else:
        S=0.5*külg*kõrgus

    return S

def arithmetic(chislo1:float,chislo2:float,znak:str):
    """Valib esimene ja teine number ja teeb tegevus seda numbriga (+,-,*,/)
    :param float chilso1: esimene number
    :param float chilso2: teine number
    :param float znak: tegevus
    """
    
    if znak in ["+","-","*","/"]:
        if znak=="/":
            if chislo2==0:
                vastus="Div/0"
            else:
                vastus=chislo1/chislo2
        elif znak=="*":
            vastus=chislo1*chislo2
        elif znak=="+":
            vastus=chislo1+chislo2
        elif znak=="-":
            vastus=chislo1-chislo2
        else:
            print("Неизвестная операция")

    return vastus

def liigaasta(aasta:int,):
    """Sisestame aasta number ja tagastame True, kui aasta on liigaasta ja False kui ei ole.
    :arg1: Aasta jr number
    :rtype:bool
    """
    if aasta%4==0:
        tulemus=True
    else:
        tulemus=False
    return tulemus
