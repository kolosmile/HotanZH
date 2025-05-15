## Feladat – Bordázott hőleadó felület

Egy alkatrészt az alábbi ábra szerinti kialakítású duralumínium bordázattal látnak el. Az alkatrész felszínének hőmérséklete 86 °C.  
Az alapfelületet és a bordákat 21 °C hőmérsékletű áramló levegővel hűtik, melyet 30 W/(m²·K) hőátadási tényező jellemez.  
A bordázat mérete az alábbi ábrán látható. A bordák négyzet keresztmetszetűek és **L = 17 mm** hosszúak.

## Megoldás

**Adatok (szöveg szerint)**  
- Felszín hőmérséklete: \(T_0 = 86\ ^\circ\mathrm{C}\)  
- Levegő hőmérséklete: \(T_\infty = 21\ ^\circ\mathrm{C}\)  
- Konvektív tényező: \(h = 30\ \mathrm{W/(m^2\,K)}\)  
- Borda hossza: \(L = 17\ \mathrm{mm} = 0.017\ \mathrm{m}\)  
- Borda négyzet-keresztmetszetének oldala: \(a\)  (az ábrából vehető le)  
- Anyag hővezetése: \(k = \lambda\)  (duralumínium)  
- Borda‐sűrűség az 1 m²‐es alapfelületen: \(n\)  (a példában megadott érték)  

---

### 1.  Segédjelölések és alapképletek  

| Jelölés | Képlet / definíció |
|---------|--------------------|
| Kerület | \(P = 4\,a\) |
| Keresztmetszet | \(A_c = a^2\) |
| Teljes felület (oldalfalak + véglap) | \(A_f = P\,L + A_c\) |
| **Fin-paraméter** | \(m = \sqrt{\dfrac{hP}{kA_c}} = 2\,\sqrt{\dfrac{h}{k\,a}}\) |
| **Bordahatásfok (konvektív véglap)** | \(\displaystyle \eta = \frac{\tanh (mL) + \dfrac{h}{m\,k}}{1 + \dfrac{h}{m\,k}\,\tanh (mL)}\) |
| **Egy borda hőárama** | \(Q_{\text{borda}} = \eta\,h\,A_f\,(T_0 - T_\infty)\) |
| **Alap (bordák közti) felület** | \(A_{\text{alap}} = 1\ \text{m}^2 - n\,A_c\) |
| **Alap hőárama** | \(Q_{\text{alap}} = h\,A_{\text{alap}}\,(T_0 - T_\infty)\) |
| **Összes hőáram** | \(Q_{\text{össz}} = n\,Q_{\text{borda}} + Q_{\text{alap}}\) |
| **Borda véglap-hőmérséklet** | \(\displaystyle T_{\text{tip}} = T_\infty + (T_0 - T_\infty)\,\frac{1}{\cosh (mL) + \dfrac{h}{m\,k}\,\sinh (mL)}\) |
| **Relatív hőteljesítmény-növekedés** | \(\displaystyle \Phi = \frac{Q_{\text{össz}}}{h \cdot 1\ \text{m}^2 \,(T_0 - T_\infty)}\) |

---

### 2.  Kérdésekhez tartozó, számok nélküli válaszok  

| # | Kérdés | Szimbolikus eredmény |
|---|--------|----------------------|
| **5** | Összes hőteljesítmény | \(Q_{\text{össz}}\) a fenti táblázatból |
| **6** | Borda véglap-hőmérséklet | \(T_{\text{tip}}\) |
| **7** | Egy borda hatásfoka | \(\eta\) (szorozva 100-zal, ha %-ban kell) |
| **8** | Hányszoros hőleadás a bordázatlanhoz képest | \(\Phi\) |

> **Megjegyzés:**  
> – A feladatszövegben szereplő **\(n\)** (bordák darabszáma 1 m²-en) konkrét értékét behelyettesítve kapod a numerikus eredményeket.  
> – A fenti képletek egységesek a tankönyvi (Incropera–DeWitt) formulákkal, és kizárólag a konvektív véglappal rendelkező, állandó keresztmetszetű egyenes bordára vonatkoznak.


### 5. kérdés
**Az alkatrész 1×1 m²-es része által leadott összes hőteljesítmény (bordák + alapfelület), ha a bordák véglapjának hőleadása nem elhanyagolható!**  
Válasz: `_____` W

---

### 6. kérdés
**A borda véglapjának hőmérsékletét!**  
Válasz: `_____` °C

---

### 7. kérdés
**Egy darab borda hatásfokát!**  
Válasz: `_____` %

---

### 8. kérdés
**A bordázatlan esethez képest hányszoros hőteljesítmény leadására képes a bordázott felület?**  
Válasz: `_____` ×