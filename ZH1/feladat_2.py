def get_adatok():
    """
    Az állandó fajhőjű ideális gáz és a körfolyamat adatai
    """
    adatok = {
        "kappa": 1.33,           # adiabatikus kitevő
        "R": 189,                # J/(kg·K), specifikus gázállandó
        "p1": 3e5,               # Pa, kezdeti nyomás (3 bar)
        "T1": 280,               # K, kezdeti hőmérséklet
        # További adatok a táblázatból
        # T2 = T1 (izotermikus folyamat 1->2)
        # v2 = v1/8 (térfogat csökken a 8-ad részére 1->2)
        # p3 = 1.2*p2 (nyomás növekszik 20%-kal 2->3)
        # p4 = p3 (izobar folyamat 3->4)
        # wf = 0 (2->3 folyamatban nincs fizikai munka)
        # q = 0 és Δs = 0 (4->1 adiabatikus és reverzibilis, tehát izentropikus)
    }
    # Származtatott értékek kiszámítása
    adatok["cp"] = adatok["kappa"] * adatok["R"] / (adatok["kappa"] - 1)  # J/(kg·K)
    adatok["cv"] = adatok["R"] / (adatok["kappa"] - 1)  # J/(kg·K)
    
    return adatok

def szamitsd_allapotokat():
    """
    A körfolyamat egyes állapotainak kiszámítása
    """
    # Adatok lekérése
    adatok = get_adatok()
    kappa = adatok["kappa"]
    R = adatok["R"]
    p1 = adatok["p1"]
    T1 = adatok["T1"]
    cp = adatok["cp"]
    cv = adatok["cv"]
    
    # 1. állapot - adott
    # Fajlagos térfogat számítása az 1. állapotban
    v1 = R * T1 / p1  # m³/kg
    
    # 2. állapot - izotermikus kompresszió
    T2 = T1  # K, izotermikus folyamat
    v2 = v1 / 8  # m³/kg, a térfogat 1/8-ára csökken
    p2 = R * T2 / v2  # Pa, nyomás az állapotegyenletből
    
    # 3. állapot - izochor állapotváltozás (nincs fizikai munka: wf = 0)
    p3 = 1.2 * p2  # Pa, nyomás 20%-kal növekszik
    # Izochor folyamatban a térfogat nem változik
    v3 = v2
    # Hőmérséklet az állapotegyenletből
    T3 = p3 * v3 / R  # K
    
    # 4. állapot - izobar expanzió
    p4 = p3  # Pa, izobar folyamat
    # Itt még nem tudjuk a hőmérsékletet, de tudjuk, hogy a 4->1 folyamat izentropikus
    # Az izentropikus folyamatban: p * v^kappa = állandó
    # Tehát: p4 * v4^kappa = p1 * v1^kappa
    # Ebből: v4 = (p1/p4)^(1/kappa) * v1
    v4 = (p1/p4)**(1/kappa) * v1  # m³/kg
    # Hőmérséklet az állapotegyenletből
    T4 = p4 * v4 / R  # K
    
    # Eredmények tárolása
    allapotok = {
        "1": {"p": p1, "T": T1, "v": v1},
        "2": {"p": p2, "T": T2, "v": v2},
        "3": {"p": p3, "T": T3, "v": v3},
        "4": {"p": p4, "T": T4, "v": v4}
    }
    
    # Eredmények kiírása
    print("A körfolyamat állapotai:")
    for i, allapot in allapotok.items():
        print(f"Állapot {i}:")
        print(f"  Nyomás: {allapot['p']/1e5:.4f} bar")
        print(f"  Hőmérséklet: {allapot['T']:.2f} K")
        print(f"  Fajlagos térfogat: {allapot['v']:.6f} m³/kg")
    
    return allapotok

def feladat_a():
    """
    Feladat a: Határozza meg a fajtérfogatot a 4 állapotban!
    """
    # Kiszámítjuk az összes állapotot
    allapotok = szamitsd_allapotokat()
    
    # A 4-es állapot fajlagos térfogatának kiírása
    v4 = allapotok["4"]["v"]
    print(f"\na) A fajtérfogat a 4. állapotban: {v4:.6f} m³/kg")
    
    return v4

# Főprogram
if __name__ == "__main__":
    allapotok = szamitsd_allapotokat()
    v4 = feladat_a()