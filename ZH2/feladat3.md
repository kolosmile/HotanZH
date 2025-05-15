## Feladat – Golyók vízzel történő hűtése

Egy gyárban **47 mm átmérőjű**, kezdetben **132 °C hőmérsékletű** **sárgaréz golyókat**  
(λ = 132 W/(m·K), ρ = 8167 kg/m³, c = 379 J/(kg·K)) hűtenek egy vízzel töltött nagy medencében.  
A(z) **55 °C-os hűtővíz** és a gömbök közötti hőátadási tényező **240 W/(m²·K)**.  
Minden golyó **2 percig** van a medencében, úgy automatizálva, hogy percenként **132 golyót** tesznek, illetve vesznek ki a medencéből.

### Megoldás
## Feladat – Golyók vízzel történő hűtése  **(Javított képletrendszer)**

**Adatok (szöveg szerint)**  
- Gömbátmérő: \(d = 47\ \mathrm{mm} = 0.047\ \mathrm{m}\); sugár \(r = d/2\)  
- Kezdeti hőmérséklet: \(T_0 = 132\ ^\circ\mathrm{C}\)  
- Víz hőmérséklete: \(T_\infty = 55\ ^\circ\mathrm{C}\)  
- Hőátadási tényező: \(h = 240\ \mathrm{W/(m^2\,K)}\)  
- Anyagjellemzők (sárgaréz):  
  \(\displaystyle k = 132\ \mathrm{W/(m\,K)},\; \rho = 8167\ \mathrm{kg/m^3},\; c = 379\ \mathrm{J/(kg\,K)}\)  
- Merülési idő: \(\tau = 2\ \mathrm{min} = 120\ \mathrm{s}\)  
- Átlagos darabszám-áram: \(n = 132\ \text{db / perc}\)

---

### 1.  Peremfeltétel-hasonlósági kritérium (Biot-szám)

A gömb **karakterisztikus hossza**:  
\[
L_c = \frac{V}{A} = \frac{\tfrac{4}{3}\pi r^{3}}{4\pi r^{2}}
      =\frac{r}{3}= \frac{d}{6}
\]

Biot-szám:  
\[
\boxed{\,Bi = \dfrac{h\,L_c}{k}
        = \dfrac{h\,d}{6\,k}\,}
\]

*(A konkrét adatokkal \(Bi\approx0.014<0.1\); ezért használható a csomósított tömeg- (lumped) modell.)*

---

### 2.  Golyó átlaghőmérséklete a hűtés végén

A **dimenzió nélküli hőmérséklet** a lumped modell szerint:  
\[
\Theta^{*}(\tau) = 
\frac{T(\tau)-T_\infty}{T_0-T_\infty}
   = \exp\!\left(
     -\frac{h A}{\rho c V}\,\tau
     \right)
   = \exp\!\left(
     -\frac{6\,h}{\rho\,c\,d}\,\tau
     \right)
\]

Átlaghőmérséklet a hűtési idő végén:  
\[
\boxed{\,T(\tau) = T_\infty + (T_0 - T_\infty)\,\Theta^{*}(\tau)\,}
\]

---

### 3.  Szükséges hűtőteljesítmény 

**Egy gömb tömege**  
\[
m = \rho\,V = \rho\,\frac{4}{3}\pi r^{3}
            =\rho\,\frac{\pi d^{3}}{6}
\]

**Egy gömb által leadott hő**  
\[
Q_1 = m\,c\,[\,T_0 - T(\tau)\,]
     = m\,c\,(T_0-T_\infty)\,[\,1-\Theta^{*}(\tau)\,]
\]

**Időegység alatti hőelvonás**  
A ki-/beemelés üteme \(n\) golyó / perc \((=n/60\ \text{golyó/s})\); ezért  

\[
\boxed{\,P = \frac{n}{60}\,Q_1\;} \qquad [\mathrm{W}]
\]

*(Ez a teljesítmény fedezi azt a hőmennyiséget, amellyel a víz hőmérsékletét állandó értéken tartjuk.)*

---

###  Összefoglaló (számok nélkül)

| # | Kérdés | Képletes válasz |
|---|--------|-----------------|
| **9** | Peremfeltétel-hasonlósági kritérium | \(Bi = h\,d /(6\,k)\) |
| **10** | Átlaghőmérséklet a hűtés végén | \(T(\tau)=T_\infty + (T_0-T_\infty)\,\exp[-\,6h\tau/(\rho c d)]\) |
| **11** | Szükséges hűtőteljesítmény | \(P=(n/60)\,m\,c\,(T_0-T_\infty)\,[1-\exp(-6h\tau/(\rho c d))]\) |

> **Megjegyzés:** Mivel \(Bi\ll0.1\), a fenti lumped-modell adja a legfeljebb néhány százalékos pontosságú, zárt alakú megoldást; a részletes sajátérték-sorozat nem szükséges.


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
