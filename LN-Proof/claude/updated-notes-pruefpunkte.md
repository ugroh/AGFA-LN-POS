# Updated Notes: offene Prüfpunkte

*One-parameter Semigroups of Positive Operators*, 2. Aufl. (Springer LNM 1184), Stand: 17.10.2026.

Die folgenden drei Stellen in den Updated Notes sind **nicht geändert**. Sie sollten am jeweiligen Originalartikel geprüft werden.

---

## 1. Edeko–Gerlach–Kühner: „compact Borel probability space“

**Datei:** `part-e/un-part-c.tex`, Updated Notes Part III, Chapter 2 (Absatz zu Koopman-Halbgruppen auf $L^p$)

**Literatur:** `zbmath07036266`: N. Edeko, M. Gerlach, V. Kühner, *Measure-preserving semiflows and one-parameter Koopman semigroups*, Semigroup Forum 98 (2019).

**Aktueller Text:**

> As a consequence, every measure preserving flow on a standard probability space is isomorphic to a continuous flow on a compact Borel probability space.

**Problem:** Einen „compact Borel probability space“ gibt es so nicht. Kompakt ist der topologische Raum, das Wahrscheinlichkeitsmaß ist ein Borelmaß darauf.

**Vorschlag** (bitte am Artikel prüfen, ob „metric“ zutrifft):

> As a consequence, every measure-preserving flow on a standard probability space is isomorphic to a continuous flow on a compact metric space equipped with a Borel probability measure.

---

## 2. Beschränktheit des dominierenden Generators

**Datei:** `part-e/un-part-c.tex`, Updated Notes Part III, Chapter 2 (Absatz zu Domination)

**Literatur:** `zbmath00417080`

**Aktueller Text:**

> A uniformly continuous semigroup is dominated by some positive semigroup if and only if its generator is regular. More precisely, [zbmath00417080] show the following. Let $B$ be a bounded operator on a real or complex Banach lattice $E$ such that the following holds: $|(\exp tB)f| \le T(t)|f|$ for all $t \ge 0$, $f \in E$ where $(T(t))_{t\ge0}$ is a semigroup with generator $A$. Then the operator $B$ is regular and $A$ is bounded.

**Problem:** Der Schluss „$B$ is regular“ ist plausibel. Die Umkehrung, also dass aus $B$ regulär die Domination durch $\exp(t|B|)$ folgt, ist klar. Die Zusatzaussage „**and $A$ is bounded**“, also dass auch der *dominierende* Generator beschränkt sein muss, ist dagegen eine starke Aussage. Sie ist nicht abwegig: Aus $|\exp(tB)f| \le T(t)|f|$ und $\exp(tB) \to \mathrm{Id}$ in der Norm folgt, dass $T(t)$ für kleine $t$ „fast oberhalb der Identität“ liegt. Im Text wird sie aber ohne Begründung genannt.

**Zu prüfen:**
- Steht „$A$ is bounded“ wirklich so im Artikel?
- Gibt es dort Zusatzvoraussetzungen, etwa an den Raum oder an $T$?
- Falls nicht im Artikel: „and $A$ is bounded“ streichen; sonst ggf. die Voraussetzungen präzisieren.

---

## 3. Lumer–Phillips-Variante mit „surjective“

**Datei:** `part-e/un-part-a.tex`, Updated Notes Part I, Chapter 2 (erster Punkt)

**Literatur:** `zbmath07950102`, Theorem 1.2

**Aktueller Text:**

> Here we mention the following version of the Lumer-Phillips Theorem (Part-I, Theorem 2.2.13): *A densely defined operator $A$ is invertible and generates a contractive semigroup on a Banach space if and only if it is dissipative and surjective.*

**Problem:** In der klassischen Fassung wird die Surjektivität von $\lambda - A$ für ein $\lambda > 0$ verlangt, nicht die von $A$ selbst. Die hier zitierte Variante ($A$ selbst surjektiv, dafür „invertible“ in der Folgerung) ist eine echte Verschärfung. Sie kann richtig sein, die genaue Formulierung muss aber stimmen.

**Zu prüfen:**
- Bezieht sich „surjective“ in Theorem 1.2 des Artikels auf $A$ oder auf $\lambda - A$?
- Ist „densely defined“ Voraussetzung oder Folgerung?
- Ist „invertible“ im Sinne von $0 \in \rho(A)$ gemeint?
