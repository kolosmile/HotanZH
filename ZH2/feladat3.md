## Feladat – Golyók vízzel történő hűtése

Egy gyárban **47 mm átmérőjű**, kezdetben **132 °C hőmérsékletű** **sárgaréz golyókat**  
(λ = 132 W/(m·K), ρ = 8167 kg/m³, c = 379 J/(kg·K)) hűtenek egy vízzel töltött nagy medencében.  
A(z) **55 °C-os hűtővíz** és a gömbök közötti hőátadási tényező **240 W/(m²·K)**.  
Minden golyó **2 percig** van a medencében, úgy automatizálva, hogy percenként **132 golyót** tesznek, illetve vesznek ki a medencéből.

### Megoldás

**Jelölések:**
- $d$ - golyók átmérője [m]
- $T_0$ - kezdeti hőmérséklet [°C]
- $T_∞$ - hűtővíz hőmérséklete [°C]
- $\lambda$ - sárgaréz hővezetési tényezője [W/(m·K)]
- $\rho$ - sárgaréz sűrűsége [kg/m³]
- $c$ - sárgaréz fajhője [J/(kg·K)]
- $\alpha$ - hőátadási tényező [W/(m²·K)]
- $\tau$ - hűtési idő [s]
- $n$ - percenként berakott/kivett golyók száma [db/perc]

**9. kérdés - Peremfeltétel hasonlóságát biztosító kritérium**

A Biot-szám számítása:
$Bi = \frac{\alpha \cdot L_c}{\lambda}$

Ahol $L_c$ a karakterisztikus hossz, gömb esetén:
$L_c = \frac{d}{6} = \frac{R}{3}$

**10. kérdés - Golyók átlaghőmérséklete a hűtés végén**

A kis Biot-szám miatt (amennyiben Bi < 0.1) elegendő a "lumped" modellt használni:

$\Theta^* = \frac{T(\tau) - T_∞}{T_0 - T_∞} = \exp\left(-\frac{\alpha A}{\rho c V}\tau\right)$

Ahol:
- $A = \pi d^2$ - egy golyó felülete [m²]
- $V = \frac{4}{3}\pi\left(\frac{d}{2}\right)^3$ - egy golyó térfogata [m³]

Így egyszerűsítve:
$\Theta^* = \exp\left(-\frac{6\alpha\tau}{\rho c d}\right)$

A golyók átlaghőmérséklete a hűtés végén:
$T(\tau) = T_∞ + (T_0 - T_∞) \cdot \Theta^*$

Ha részletesebb analitikus modellre van szükség (Bi ≥ 0.1), akkor a gömbre vonatkozó sajátérték-egyenlet:

$\tan\mu_1 = \frac{3\mu_1}{3-Bi\cdot\mu_1^2}$

És a megfelelő együttható:
$C_1 = \frac{6 \cdot Bi}{(\mu_1^2 - Bi) + 3 \cdot Bi}$

**11. kérdés - Szükséges hűtőteljesítmény**

Egy golyó tömege:
$m = \rho \cdot V = \rho \cdot \frac{4}{3} \cdot \pi \cdot \left(\frac{d}{2}\right)^3$

Egy golyó leadott hője:
$Q_1 = m \cdot c \cdot (T_0 - T(\tau))$

A medencében egyszerre tartózkodó golyók száma:
$N = n \cdot \tau_{perc} = n \cdot 2$

Szükséges hűtőteljesítmény:
$P = \frac{n \cdot Q_1}{60}$ [W]

Ez azért osztva 60-nal, mert az n golyó/perc dimenzióban van, és 1 perc = 60 s.

---

### 9. kérdés
**Határozza meg a peremfeltétel hasonlóságát biztosító kritérium számértékét!**  
Válasz: `_____`

---

### 10. kérdés  
**Határozza meg a golyók átlaghőmérsékletét a hűtési folyamat végén!**  
Válasz: `_____` °C

---

### 11. kérdés  
**Határozza meg, hogy mekkora hűtőteljesítményt kell biztosítanunk annak érdekében, hogy hűtővíz hőmérsékletét állandó értéken tartsuk!**  
Válasz: `_____` W
