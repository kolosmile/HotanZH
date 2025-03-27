# Közös adatok definíciója
def get_adatok():
    """
    A szivattyús energiatároló rendszer közös adatai
    """
    adatok = {
        "h": 40,                # m, magasságkülönbség
        "Q": 1.7,               # m³/s, térfogatáram
        "rho": 1000,            # kg/m³, víz sűrűsége
        "g": 9.81,              # m/s², gravitációs gyorsulás
        "eta": 0.73,            # hatásfok
        "ar_ejszakai": 20,      # Ft/kWh, éjszakai áram ára
        "ar_nappali": 40,       # Ft/kWh, nappali áram ára
        "uzemora_napi": 11,     # óra/nap
        "napok_evente": 365     # nap/év
    }
    return adatok

# Módosítás az feladat_a() függvényben, hogy opcionálisan kiírja a kimenetet
def feladat_a(verbose=True):
    """
    Szivattyús energiatároló rendszer elméleti teljesítményének számítása
    mind szivattyú, mind turbina üzemmódban
    """
    # Adatok lekérése
    adatok = get_adatok()
    h = adatok["h"]
    Q = adatok["Q"]
    rho = adatok["rho"]
    g = adatok["g"]
    eta = adatok["eta"]

    # Elméleti hidrosztatikai teljesítmény (veszteségek nélkül)
    P_elm = rho * g * h * Q  # W = kg·m²/s³
    
    # Turbina üzemmód (generátor teljesítménye)
    P_turb = P_elm * eta  # W
    
    # Szivattyú üzemmód (motor teljesítménye)
    P_pump = P_elm / eta  # W
    
    # Átváltás kW-ba
    P_elm_kW = P_elm / 1000
    P_turb_kW = P_turb / 1000
    P_pump_kW = P_pump / 1000
    
    if verbose:
        print(f"a) Elméleti teljesítmény: {P_elm_kW:.2f} kW")
        print(f"   Turbina-generátor tényleges teljesítménye: {P_turb_kW:.2f} kW")
        print(f"   Szivattyú-motor tényleges teljesítménye: {P_pump_kW:.2f} kW")
    
    return P_elm_kW, P_turb_kW, P_pump_kW

def feladat_b():
    """
    Szivattyús energiatároló rendszer szivattyú-villanymotor 
    teljesítményigényének számítása
    """
    # Használjuk az a) feladat által már kiszámított értéket
    _, _, P_pump_kW = feladat_a()
    
    print(f"b) Szivattyú-villanymotor teljesítményigénye: {P_pump_kW:.2f} kW")
    
    return P_pump_kW

def feladat_c():
    """
    Szivattyúzás éves energiaköltségének számítása
    """
    # Adatok lekérése
    adatok = get_adatok()
    ar_ejszakai = adatok["ar_ejszakai"]
    uzemora_napi = adatok["uzemora_napi"]
    napok_evente = adatok["napok_evente"]
    
    # Használjuk a b) feladat által már kiszámított értéket
    P_pump_kW = feladat_b()
    
    # Éves energiafogyasztás
    E_eves = P_pump_kW * uzemora_napi * napok_evente  # kWh/év
    
    # Éves költség
    koltseg_eves = E_eves * ar_ejszakai  # Ft/év
    
    print(f"c) Szivattyúzás éves energiaköltsége: {koltseg_eves:.0f} Ft/év")
    
    return koltseg_eves

def feladat_d():
    """
    A turbina üzem éves bevételének számítása
    """
    # Adatok lekérése
    adatok = get_adatok()
    ar_nappali = adatok["ar_nappali"]
    uzemora_napi = adatok["uzemora_napi"]
    napok_evente = adatok["napok_evente"]
    
    # A turbina teljesítményének használata az a) feladatból
    _, P_turb_kW, _ = feladat_a()
    
    # Éves energiatermelés
    E_eves_termelt = P_turb_kW * uzemora_napi * napok_evente  # kWh/év
    
    # Éves bevétel
    bevetel_eves = E_eves_termelt * ar_nappali  # Ft/év
    
    print(f"d) Turbina üzem éves bevétele: {bevetel_eves:.0f} Ft/év")
    
    return bevetel_eves

def feladat_e():
    """
    Az éves nyereség számítása
    """
    # Használjuk a c) és d) feladat által már kiszámított értékeket
    # A feladat_c() és feladat_d() függvényekből csak az értékekre van szükségünk,
    # a kiírást szeretnénk elkerülni
    
    # Adatok lekérése az alapadatokból - közvetlenül használjuk ezeket
    adatok = get_adatok()
    ar_ejszakai = adatok["ar_ejszakai"]
    ar_nappali = adatok["ar_nappali"]
    uzemora_napi = adatok["uzemora_napi"]
    napok_evente = adatok["napok_evente"]
    
    # A teljesítmények lekérése redundancia nélkül
    _, P_turb_kW, P_pump_kW = feladat_a(verbose=False)
    
    # Éves energiatermelés és -fogyasztás
    E_eves_termelt = P_turb_kW * uzemora_napi * napok_evente  # kWh/év
    E_eves_fogyasztott = P_pump_kW * uzemora_napi * napok_evente  # kWh/év
    
    # Éves bevétel és költség
    bevetel_eves = E_eves_termelt * ar_nappali  # Ft/év
    koltseg_eves = E_eves_fogyasztott * ar_ejszakai  # Ft/év
    
    # Éves nyereség
    nyereseg_eves = bevetel_eves - koltseg_eves  # Ft/év
    
    print(f"e) Turbina üzem éves bevétele: {bevetel_eves:.0f} Ft/év")
    print(f"   Szivattyúzás éves energiaköltsége: {koltseg_eves:.0f} Ft/év")
    print(f"   Éves nyereség: {nyereseg_eves:.0f} Ft/év")
    
    return nyereseg_eves

# Főprogram
if __name__ == "__main__":
    print("Szivattyús energiatároló rendszer számításai:\n")
    telj_elm, telj_turb, telj_szivattyu = feladat_a()
    teljesitmeny_szivattyu = feladat_b()
    koltseg_eves = feladat_c()
    bevetel_eves = feladat_d()
    nyereseg_eves = feladat_e()