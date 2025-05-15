## Feladat – Bordázott hőleadó felület

Egy alkatrészt az alábbi ábra szerinti kialakítású duralumínium bordázattal látnak el. Az alkatrész felszínének hőmérséklete 86 °C.  
Az alapfelületet és a bordákat 21 °C hőmérsékletű áramló levegővel hűtik, melyet 30 W/(m²·K) hőátadási tényező jellemez.  
A bordázat mérete az alábbi ábrán látható. A bordák négyzet keresztmetszetűek és **L = 17 mm** hosszúak.

### Megoldás

**Jelölések:**
- $T_0$ - alkatrész felszínének hőmérséklete [°C]
- $T_∞$ - környezeti levegő hőmérséklete [°C]
- $\alpha$ - hőátadási tényező [W/(m²·K)]
- $L$ - borda hossza [m]
- $a$ - borda keresztmetszetének oldalhossza [m]
- $\lambda$ - duralumínium hővezetési tényezője [W/(m·K)]
- $n$ - bordák száma 1 m²-en

**5. kérdés - Összes hőteljesítmény**

A borda karakterisztikus tényezője:
$m = \sqrt{\frac{\alpha \cdot P}{\lambda \cdot A_k}}$

Ahol:
- $P = 4a$ - a borda kerülete [m]
- $A_k = a^2$ - a borda keresztmetszete [m²]

Tehát: $m = \sqrt{\frac{4a \cdot \alpha}{a^2 \cdot \lambda}} = 2 \cdot \sqrt{\frac{\alpha}{a \cdot \lambda}}$

A konvektív véglappal rendelkező borda hőárama:
$Q_{borda} = \sqrt{\alpha \cdot P \cdot \lambda \cdot A_k} \cdot (T_0 - T_∞) \cdot \frac{\sinh(mL) + \frac{\alpha}{m\lambda}\cosh(mL)}{\cosh(mL) + \frac{\alpha}{m\lambda}\sinh(mL)}$

Egy borda teljes felülete:
$A_{borda} = 4aL + a^2$ (oldalfelületek + véglap)

A borda hatásfoka:
$\eta = \frac{Q_{borda}}{\alpha \cdot A_{borda} \cdot (T_0 - T_∞)}$

Az alapfelületről leadott hő (bordázat nélküli rész):
$A_{alap} = 1 - n \cdot a^2$ [m²]
$Q_{alap} = \alpha \cdot A_{alap} \cdot (T_0 - T_∞)$

Összes hőleadás:
$Q_{össz} = n \cdot Q_{borda} + Q_{alap}$

**6. kérdés - Borda véglapjának hőmérséklete**

A borda hőmérséklet-eloszlása:
$\frac{T(x) - T_∞}{T_0 - T_∞} = \frac{\cosh(m(L-x)) + \frac{\alpha}{m\lambda}\sinh(m(L-x))}{\cosh(mL) + \frac{\alpha}{m\lambda}\sinh(mL)}$

A véglap hőmérséklete (x = L):
$T_{véglap} = T_∞ + (T_0 - T_∞) \cdot \frac{1 + \frac{\alpha}{m\lambda} \cdot 0}{\cosh(mL) + \frac{\alpha}{m\lambda}\sinh(mL)} = T_∞ + (T_0 - T_∞) \cdot \frac{1}{\cosh(mL) + \frac{\alpha}{m\lambda}\sinh(mL)}$

**7. kérdés - Borda hatásfoka**

A borda hatásfoka százalékban:
$\eta[\%] = \eta \cdot 100\%$

**8. kérdés - Relatív hőteljesítmény-növekedés**

Bordázatlan felület hőleadása:
$Q_{bordázatlan} = \alpha \cdot 1 \text{ m}^2 \cdot (T_0 - T_∞)$

Hőleadás-növekedés:
$\frac{Q_{össz}}{Q_{bordázatlan}} = \frac{n \cdot Q_{borda} + Q_{alap}}{\alpha \cdot 1 \text{ m}^2 \cdot (T_0 - T_∞)}$

---

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