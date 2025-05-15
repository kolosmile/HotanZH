## Feladat

Két rétegből álló síkfal „A" rétegében 1,6 MW/m³ hőteljesítmény szabadul fel a térfogatban egyenletesen. Az „A" réteg vastagsága 60 mm, hővezetési tényezője 70 W/(m·K). A „B" réteg 25 mm vastag, hővezetési tényezője 140 W/(m·K) és nincs benne hőfelszabadulás. Az „A" réteg belső felülete tökéletesen hőszigetelt, míg a „B" réteg külső felületét 40 °C hőmérsékletű áramló vízzel kívánjuk hűteni. Az egyes rétegek között a hővezetés tökéletes, tehát nem lép fel kontakt hőellenállás. Akkora hőátadási tényezőt kell biztosítanunk a hűtővíz és a síkfal között, hogy a kétrétegű síkfal egyik pontjának hőmérséklete sem haladja meg a 145 °C-ot.

### Megoldás

**Jelölések:**
- $q_V$ - térfogati hőfelszabadulás [W/m³]
- $s_A$ - "A" réteg vastagsága [m]
- $s_B$ - "B" réteg vastagsága [m]
- $\lambda_A$ - "A" réteg hővezetési tényezője [W/(m·K)]
- $\lambda_B$ - "B" réteg hővezetési tényezője [W/(m·K)]
- $T_{víz}$ - hűtővíz hőmérséklete [°C]
- $T_{max}$ - maximális megengedett hőmérséklet [°C]
- $q$ - hőáramsűrűség [W/m²]
- $\alpha$ - hőátadási tényező [W/(m²K)]

**1. kérdés - Hőáramsűrűség**

Mivel az "A" réteg belső felülete hőszigetelt, a teljes hőmennyiség a külső felület felé áramlik.
A térfogati hőfelszabadulásból számított hőáramsűrűség:
$q = q_V \cdot s_A$

**2. kérdés - Hőmérséklet a rétegek érintkezésénél**

Az "A" rétegben a hőmérséklet-eloszlás parabolikus, a hőszigetelt faltól (x=0) a réteghatárig (x=s_A).
A hőmérséklet-gradiens képlete (figyelembe véve, hogy x=0-nál a gradiens nulla):
$\frac{dT_A}{dx} = -\frac{q_V}{\lambda_A} \cdot x$

Integrálva a fenti egyenletet:
$T_A(x) = T_{max} - \frac{q_V \cdot x^2}{2\lambda_A}$

Ahol $T_{max}$ a maximális hőmérséklet az "A" réteg belső (x=0) felületénél.

A réteghatárnál a hőmérséklet:
$T_{kontakt} = T_A(s_A) = T_{max} - \frac{q_V \cdot s_A^2}{2\lambda_A}$

**3. kérdés - "B" réteg külső felületének hőmérséklete**

A "B" rétegben lineáris a hőmérséklet-eloszlás:
$T_B(x) = T_{kontakt} - \frac{q \cdot (x-s_A)}{\lambda_B}$

A "B" réteg külső felületén (x = s_A + s_B):
$T_{felszín} = T_{kontakt} - \frac{q \cdot s_B}{\lambda_B}$

**4. kérdés - Szükséges hőátadási tényező**

A konvektív hőátadás egyenlete:
$q = \alpha \cdot (T_{felszín} - T_{víz})$

Ebből a szükséges hőátadási tényező:
$\alpha = \frac{q}{T_{felszín} - T_{víz}}$

Az egyenletrendszer megoldásához a maximális hőmérsékletből kell kiindulni:
$T_A(0) = T_{max}$

Ebből a kontakthőmérséklet:
$T_{kontakt} = T_{max} - \frac{q_V \cdot s_A^2}{2\lambda_A} + \frac{q \cdot s_A}{\lambda_A}$

---

### 1. kérdés
**Mekkora hőáramsűrűség távozik a síkfal egységnyi felületéről az áramló hűtővíz felé?**  
Válasz: `_____` W/m² vagy `_____` kW/m²

---

### 2. kérdés
**Mekkora a hőmérséklet a két réteg érintkezésénél (kontakt hőellenállás elhanyagolható)?**  
Válasz: `_____` °C

---

### 3. kérdés
**Mekkora a hőmérséklet a „B" síkfal hűtött felszínén?**  
Válasz: `_____` °C

---

### 4. kérdés
**Mekkora hőátadási tényezőt kell biztosítanunk a hűtővíz és a síkfal között?**  
Válasz: `_____` W/m²K vagy `_____` kW/m²K
