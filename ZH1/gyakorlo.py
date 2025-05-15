def feladat_1():
    """
    N2 gázzal nyitott rendszerben végbemenő reverzibilis állapotváltozás során a fajlagos fizikai munka 517 kJ/kg.
    A gáz hőmérséklete belépéskor 562 °C, míg kilépéskor 280 °C.
    Mennyi az állapotváltozás fajlagos technikai munkája?
    """
    # Adatok
    w_fizikai = 517  # kJ/kg, fajlagos fizikai munka
    T1 = 562 + 273.15  # K, belépési hőmérséklet
    T2 = 280 + 273.15  # K, kilépési hőmérséklet
    R_N2 = 0.297  # kJ/(kg·K), N2 gázállandója
    
    # Fajlagos technikai munka számítása a helyes képlettel
    # w_tech = R * (T2 - T1) - w_fizikai
    w_tech = R_N2 * (T2 - T1) - w_fizikai
    
    # Részletes kiírás
    print("1. Feladat - Fajlagos technikai munka számítása:")
    print("Adatok:")
    print(f"  Fajlagos fizikai munka: {w_fizikai} kJ/kg")
    print(f"  Belépési hőmérséklet: {T1-273.15} °C ({T1} K)")
    print(f"  Kilépési hőmérséklet: {T2-273.15} °C ({T2} K)")
    print(f"  N2 gázállandója: {R_N2} kJ/(kg·K)")
    print("\nSzámítás:")
    print(f"  w_tech = R_N2 * (T2 - T1) - w_fizikai")
    print(f"  w_tech = {R_N2} * ({T2} - {T1}) - {w_fizikai}")
    print(f"  w_tech = {R_N2} * ({T2-T1}) - {w_fizikai}")
    print(f"  w_tech = {R_N2*(T2-T1):.4f} - {w_fizikai}")
    print(f"  w_tech = {R_N2*(T2-T1)-w_fizikai:.4f} kJ/kg")
    print("\nEredmény:")
    print(f"  Fajlagos technikai munka: {w_tech:.2f} kJ/kg")
    
    return w_tech

def feladat_2():
    """
    Egy turbinában 17 kg/s tömegáramú tökéletes gáz [specifikus gázállandó: 287 J/(kg·K), 
    adiabatikus kitevő: 1,33] expandál izentropikusan. A gáz hőmérséklete belépéskor 998 K, 
    kilépéskor 602 K. Az állapotváltozás fajlagos fizikai munkájának abszolútértéke 491 kJ/kg. 
    Mennyi a turbina teljesítményének abszolútértéke?
    """
    # Adatok
    m_dot = 17  # kg/s, tömegáram
    R = 287  # J/(kg·K), specifikus gázállandó
    k = 1.33  # adiabatikus kitevő
    T1 = 998  # K, belépési hőmérséklet
    T2 = 602  # K, kilépési hőmérséklet
    w_fizikai_abs = 491  # kJ/kg, fajlagos fizikai munka abszolútértéke
    
    # A turbinában a fizikai munka előjele negatív (a gáz munkát ad le)
    w_fizikai = -w_fizikai_abs  # kJ/kg
    
    # Teljesítmény számítása (abszolútértékben)
    P_turbina = m_dot * abs(w_fizikai) * 1000  # W (J/s)
    P_turbina_MW = P_turbina / 1e6  # MW
    
    # Részletes kiírás
    print("\n2. Feladat - Turbina teljesítmény számítása:")
    print("Adatok:")
    print(f"  Tömegáram: {m_dot} kg/s")
    print(f"  Specifikus gázállandó: {R} J/(kg·K)")
    print(f"  Adiabatikus kitevő: {k}")
    print(f"  Belépési hőmérséklet: {T1} K")
    print(f"  Kilépési hőmérséklet: {T2} K")
    print(f"  Fajlagos fizikai munka abszolútértéke: {w_fizikai_abs} kJ/kg")
    
    print("\nSzámítás:")
    print(f"  P_turbina = m_dot * |w_fizikai| * 1000")
    print(f"  P_turbina = {m_dot} kg/s * {w_fizikai_abs} kJ/kg * 1000 W/(kJ/s)")
    print(f"  P_turbina = {P_turbina} W")
    print(f"  P_turbina = {P_turbina_MW} MW")
    
    # Ellenőrzés: Elméleti fizikai munka számítása a hőmérsékletkülönbségből
    cp = k * R / (k - 1)  # J/(kg·K)
    w_elmelet = cp * (T2 - T1) / 1000  # kJ/kg
    
    print("\nEllenőrzés:")
    print(f"  cp = k * R / (k - 1) = {k} * {R} / ({k} - 1) = {cp:.2f} J/(kg·K)")
    print(f"  w_elmelet = cp * (T2 - T1) / 1000 = {cp:.2f} * ({T2} - {T1}) / 1000 = {w_elmelet:.2f} kJ/kg")
    print(f"  |w_elmelet| = {abs(w_elmelet):.2f} kJ/kg (ellenőrzésként)")
    
    print("\nEredmény:")
    print(f"  A turbina teljesítményének abszolútértéke: {P_turbina_MW:.2f} MW")
    
    return P_turbina_MW

if __name__ == "__main__":
    w_tech = feladat_1()
    P_turbina = feladat_2()