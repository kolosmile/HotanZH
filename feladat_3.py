def get_adatok():
    """
    A Joule-Brayton körfolyamat adatai
    """
    adatok = {
        "pi": 14,               # nyomásviszony
        "T1": 294,              # K, kompresszorba belépő hőmérséklet
        "T3": 1000,             # K, turbinába belépő hőmérséklet
        "P_hasznos": 140e6,     # W, hasznos teljesítmény
        "R": 287,               # J/(kg·K), levegő gázállandója
        "k": 1.4,               # adiabatikus kitevő
        "eta_komp": 1.0,        # kompresszor hatásfoka (ideális eset)
        "eta_turb": 1.0         # turbina hatásfoka (ideális eset)
    }
    
    # Származtatott értékek
    adatok["cp"] = adatok["k"] * adatok["R"] / (adatok["k"] - 1)  # J/(kg·K)
    adatok["cv"] = adatok["R"] / (adatok["k"] - 1)  # J/(kg·K)
    
    return adatok

def szamitsd_korfolyamatot(eta_komp=1.0, eta_turb=1.0):
    """
    A Joule-Brayton körfolyamat számítása
    
    Args:
        eta_komp: kompresszor izentropikus hatásfoka (0-1 között)
        eta_turb: turbina izentropikus hatásfoka (0-1 között)
    """
    # Adatok lekérése
    adatok = get_adatok()
    pi = adatok["pi"]
    T1 = adatok["T1"]
    T3 = adatok["T3"]
    P_hasznos = adatok["P_hasznos"]
    R = adatok["R"]
    k = adatok["k"]
    cp = adatok["cp"]
    
    # Hőmérsékletek számítása
    # Izentropikus kompresszió esetén: T2s/T1 = (p2/p1)^((k-1)/k) = pi^((k-1)/k)
    T2s = T1 * pi**((k-1)/k)
    
    # Figyelembe véve a hatásfokot: (T2-T1) = (T2s-T1)/eta_komp
    T2 = T1 + (T2s - T1) / eta_komp
    
    # Izentropikus expanzió esetén: T4s/T3 = (p4/p3)^((k-1)/k) = (1/pi)^((k-1)/k)
    T4s = T3 * (1/pi)**((k-1)/k)
    
    # Figyelembe véve a hatásfokot: (T3-T4) = eta_turb * (T3-T4s)
    T4 = T3 - eta_turb * (T3 - T4s)
    
    # Fajlagos munkák számítása (fontos a helyes előjel!)
    w_komp = -cp * (T2 - T1)  # J/kg, kompresszor munkája (negatív)
    w_turb = cp * (T3 - T4)  # J/kg, turbina munkája (pozitív)
    w_hasznos = w_turb + w_komp  # J/kg, nettó hasznos munka
    
    # Tömegáram számítása a hasznos teljesítményből
    m_dot = P_hasznos / w_hasznos  # kg/s
    
    # Fajlagos hőközlések
    q_be = cp * (T3 - T2)  # J/kg, égőkamrában bevitt hő
    q_ki = cp * (T4 - T1)  # J/kg, hőcserélőben elvitt hő
    
    # Termikus hatásfok
    eta_termikus = w_hasznos / q_be
    
    # Állapotok tárolása
    allapotok = {
        "1": {"T": T1, "p": "p1"},
        "2": {"T": T2, "p": "p1*pi"},
        "3": {"T": T3, "p": "p1*pi"},
        "4": {"T": T4, "p": "p1"}
    }
    
    eredmenyek = {
        "allapotok": allapotok,
        "m_dot": m_dot,
        "eta_termikus": eta_termikus,
        "w_komp": w_komp,
        "w_turb": w_turb,
        "w_hasznos": w_hasznos,
        "q_be": q_be,
        "q_ki": q_ki
    }
    
    return eredmenyek

def feladat_a():
    """
    Határozza meg a munkaközeg tömegáramát ideális folyamat esetén!
    """
    eredmenyek = szamitsd_korfolyamatot()
    m_dot = eredmenyek["m_dot"]
    
    print(f"a) A munkaközeg tömegárama (ideális eset): {m_dot:.2f} kg/s")
    
    return m_dot

def feladat_b():
    """
    Határozza meg a körfolyamat termikus hatásfokát ideális esetben!
    """
    eredmenyek = szamitsd_korfolyamatot()
    eta_termikus = eredmenyek["eta_termikus"]
    
    print(f"b) A körfolyamat termikus hatásfoka (ideális eset): {eta_termikus:.4f} ({eta_termikus*100:.2f}%)")
    
    return eta_termikus

def feladat_c():
    """
    Határozza meg a munkaközeg tömegáramát 94% hatásfokú gépek esetén!
    """
    eredmenyek = szamitsd_korfolyamatot(eta_komp=0.94, eta_turb=0.94)
    m_dot = eredmenyek["m_dot"]
    
    print(f"c) A munkaközeg tömegárama (94% hatásfokú gépek): {m_dot:.2f} kg/s")
    
    return m_dot

def feladat_d():
    """
    Határozza meg a körfolyamat termikus hatásfokát 94% hatásfokú gépek esetén!
    """
    eredmenyek = szamitsd_korfolyamatot(eta_komp=0.94, eta_turb=0.94)
    eta_termikus = eredmenyek["eta_termikus"]
    
    print(f"d) A körfolyamat termikus hatásfoka (94% hatásfokú gépek): {eta_termikus:.4f} ({eta_termikus*100:.2f}%)")
    
    return eta_termikus

# Főprogram
if __name__ == "__main__":
    print("Joule-Brayton körfolyamat számítása:\n")
    
    m_dot_idealis = feladat_a()
    eta_idealis = feladat_b()
    m_dot_valos = feladat_c()
    eta_valos = feladat_d()