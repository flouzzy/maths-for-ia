En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant, conçu pour sonder votre maîtrise des concepts de quantification, de l'ordre des quantificateurs et de la négation, dans un contexte mêlant analyse réelle et logique.

---

## Exercice 8 : Stabilité Séquentielle Locale

**Contexte :** Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction réelle et $x_0 \in \mathbb{R}$ un point de l'ensemble de définition. Nous allons définir une propriété spécifique concernant le comportement de $f$ au voisinage de $x_0$ via des suites.

**Niveau de difficulté :** $\star \star \star \star \text{ sur } 5$

---

### Énoncé de l'Exercice

Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction et $x_0 \in \mathbb{R}$ un point.
Nous définissons la propriété $\mathcal{P}(f, x_0)$ comme suit :
"Pour toute suite de nombres réels $(x_n)_{n \in \mathbb{N}}$ qui converge vers $x_0$, la suite des images $(f(x_n))_{n \in \mathbb{N}}$ est bornée."

1.  **Formalisation de la propriété :** Écrire la propriété $\mathcal{P}(f, x_0)$ en utilisant uniquement des quantificateurs ($\forall, \exists$), des connecteurs logiques ($\land, \lor, \implies, \neg$) et des symboles mathématiques usuels (appartenance, égalité, inégalité, etc.). Vous devrez expliciter la convergence d'une suite et le caractère borné d'une suite.

2.  **Négation de la propriété :** Écrire la négation de la propriété $\mathcal{P}(f, x_0)$, notée $\neg \mathcal{P}(f, x_0)$, en utilisant uniquement des quantificateurs et des connecteurs logiques, de manière à ce que la négation ne porte pas sur une implication ou une équivalence si possible.

3.  **Application 1 :** Soit la fonction $f_1: \mathbb{R} \to \mathbb{R}$ définie par
    $$ f_1(x) = \begin{cases} \frac{1}{x} & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases} $$
    Déterminer si la propriété $\mathcal{P}(f_1, 0)$ est vraie ou fausse. Justifier votre réponse de manière exhaustive.

4.  **Application 2 :** Soit la fonction $f_2: \mathbb{R} \to \mathbb{R}$ définie par
    $$ f_2(x) = \begin{cases} \sin\left(\frac{1}{x}\right) & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases} $$
    Déterminer si la propriété $\mathcal{P}(f_2, 0)$ est vraie ou fausse. Justifier votre réponse de manière exhaustive.

---

### Correction Détaillée

#### Question 1 : Formalisation de la propriété $\mathcal{P}(f, x_0)$

La propriété $\mathcal{P}(f, x_0)$ est définie comme : "Pour toute suite de nombres réels $(x_n)_{n \in \mathbb{N}}$ qui converge vers $x_0$, la suite des images $(f(x_n))_{n \in \mathbb{N}}$ est bornée."

Nous devons d'abord formaliser les deux sous-expressions :
*   **Convergence d'une suite $(x_n)_{n \in \mathbb{N}}$ vers $x_0$ :**
    Une suite $(x_n)_{n \in \mathbb{N}}$ de nombres réels converge vers $x_0 \in \mathbb{R}$ si et seulement si :
    $$ \forall \varepsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, (n \ge N \implies |x_n - x_0| < \varepsilon) $$
    Nous noterons cette proposition $C( (x_n)_{n \in \mathbb{N}}, x_0 )$.

*   **Caractère borné d'une suite $(y_n)_{n \in \mathbb{N}}$ :**
    Une suite $(y_n)_{n \in \mathbb{N}}$ de nombres réels est bornée si et seulement si :
    $$ \exists M \in \mathbb{R}_{>0}, \forall n \in \mathbb{N}, |y_n| \le M $$
    Nous noterons cette proposition $B( (y_n)_{n \in \mathbb{N}} )$.

En combinant ces définitions, la propriété $\mathcal{P}(f, x_0)$ s'écrit formellement :

$$ \mathcal{P}(f, x_0) \iff \forall (x_n)_{n \in \mathbb{N}} \in \mathbb{R}^{\mathbb{N}}, \left( C( (x_n)_{n \in \mathbb{N}}, x_0 ) \implies B( (f(x_n))_{n \in \mathbb{N}} ) \right) $$

En substituant les définitions complètes de $C$ et $B$ :

$$ \mathcal{P}(f, x_0) \iff \forall (x_n)_{n \in \mathbb{N}} \in \mathbb{R}^{\mathbb{N}}, \left( \left( \forall \varepsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, (n \ge N \implies |x_n - x_0| < \varepsilon) \right) \implies \left( \exists M \in \mathbb{R}_{>0}, \forall n \in \mathbb{N}, |f(x_n)| \le M \right) \right) $$

#### Question 2 : Négation de la propriété $\mathcal{P}(f, x_0)$

Nous voulons écrire $\neg \mathcal{P}(f, x_0)$.
Partons de la forme simplifiée :
$$ \neg \mathcal{P}(f, x_0) \iff \neg \left( \forall (x_n)_{n \in \mathbb{N}} \in \mathbb{R}^{\mathbb{N}}, \left( C( (x_n)_{n \in \mathbb{N}}, x_0 ) \implies B( (f(x_n))_{n \in \mathbb{N}} ) \right) \right) $$

Appliquons la règle de négation du quantificateur universel ($\neg \forall X, P(X) \iff \exists X, \neg P(X)$) :
$$ \neg \mathcal{P}(f, x_0) \iff \exists (x_n)_{n \in \mathbb{N}} \in \mathbb{R}^{\mathbb{N}}, \neg \left( C( (x_n)_{n \in \mathbb{N}}, x_0 ) \implies B( (f(x_n))_{n \in \mathbb{N}} ) \right) $$

Appliquons la règle de négation d'une implication ($\neg (A \implies B) \iff A \land \neg B$) :
$$ \neg \mathcal{P}(f, x_0) \iff \exists (x_n)_{n \in \mathbb{N}} \in \mathbb{R}^{\mathbb{N}}, \left( C( (x_n)_{n \in \mathbb{N}}, x_0 ) \land \neg B( (f(x_n))_{n \in \mathbb{N}} ) \right) $$

Maintenant, nous devons formaliser $\neg B( (f(x_n))_{n \in \mathbb{N}} )$.
La suite $(f(x_n))_{n \in \mathbb{N}}$ n'est pas bornée si et seulement si :
$$ \neg \left( \exists M \in \mathbb{R}_{>0}, \forall n \in \mathbb{N}, |f(x_n)| \le M \right) $$
Appliquons les règles de négation des quantificateurs :
$$ \forall M \in \mathbb{R}_{>0}, \neg \left( \forall n \in \mathbb{N}, |f(x_n)| \le M \right) $$
$$ \forall M \in \mathbb{R}_{>0}, \exists n \in \mathbb{N}, \neg \left( |f(x_n)| \le M \right) $$
$$ \forall M \in \mathbb{R}_{>0}, \exists n \in \mathbb{N}, |f(x_n)| > M $$
Nous noterons cette proposition $\neg B( (f(x_n))_{n \in \mathbb{N}} )$.

En substituant cette forme dans l'expression de $\neg \mathcal{P}(f, x_0)$ :

$$ \neg \mathcal{P}(f, x_0) \iff \exists (x_n)_{n \in \mathbb{N}} \in \mathbb{R}^{\mathbb{N}}, \left( \left( \forall \varepsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, (n \ge N \implies |x_n - x_0| < \varepsilon) \right) \land \left( \forall M \in \mathbb{R}_{>0}, \exists n \in \mathbb{N}, |f(x_n)| > M \right) \right) $$

En langage courant, $\neg \mathcal{P}(f, x_0)$ signifie : "Il existe au moins une suite de nombres réels $(x_n)_{n \in \mathbb{N}}$ telle que cette suite converge vers $x_0$, ET la suite des images $(f(x_n))_{n \in \mathbb{N}}$ n'est pas bornée."

#### Question 3 : Application 1 avec $f_1(x)$

Soit la fonction $f_1: \mathbb{R} \to \mathbb{R}$ définie par $f_1(x) = \frac{1}{x}$ si $x \neq 0$ et $f_1(0) = 0$.
Nous devons déterminer si la propriété $\mathcal{P}(f_1, 0)$ est vraie ou fausse.

Pour cela, nous allons tenter de prouver la négation $\neg \mathcal{P}(f_1, 0)$.
Selon la formalisation de $\neg \mathcal{P}(f, x_0)$, nous devons trouver une suite $(x_n)_{n \in \mathbb{N}}$ de nombres réels telle que :
1.  $(x_n)_{n \in \mathbb{N}}$ converge vers $x_0 = 0$.
2.  La suite $(f_1(x_n))_{n \in \mathbb{N}}$ n'est pas bornée.

Considérons la suite $(x_n)_{n \in \mathbb{N}}$ définie pour tout $n \in \mathbb{N}$ par $x_n = \frac{1}{n+1}$.
*   **Vérification de la convergence de $(x_n)_{n \in \mathbb{N}}$ vers $0$ :**
    Soit $\varepsilon \in \mathbb{R}_{>0}$ un nombre réel strictement positif arbitraire.
    Nous cherchons $N \in \mathbb{N}$ tel que pour tout $n \in \mathbb{N}$, si $n \ge N$, alors $|x_n - 0| < \varepsilon$.
    Nous avons $|x_n - 0| = \left| \frac{1}{n+1} \right| = \frac{1}{n+1}$ (puisque $n+1 > 0$).
    L'inégalité $\frac{1}{n+1} < \varepsilon$ est équivalente à $n+1 > \frac{1}{\varepsilon}$, ce qui est équivalent à $n > \frac{1}{\varepsilon} - 1$.
    Choisissons $N = \max(0, \lceil \frac{1}{\varepsilon} - 1 \rceil + 1)$. Par exemple, $N = \lfloor \frac{1}{\varepsilon} \rfloor + 1$ si $\varepsilon \le 1$, ou $N=1$ si $\varepsilon > 1$. Plus simplement, on peut prendre $N = \lceil 1/\varepsilon \rceil$.
    Pour tout $n \in \mathbb{N}$ tel que $n \ge N$, nous avons $n+1 > N \ge \frac{1}{\varepsilon}$.
    Donc, $\frac{1}{n+1} < \varepsilon$.
    Ainsi, $|x_n - 0| < \varepsilon$.
    La suite $(x_n)_{n \in \mathbb{N}}$ converge bien vers $0$.

*   **Vérification du caractère non borné de $(f_1(x_n))_{n \in \mathbb{N}}$ :**
    Pour tout $n \in \mathbb{N}$, $x_n = \frac{1}{n+1} \neq 0$.
    Donc, $f_1(x_n) = f_1\left(\frac{1}{n+1}\right) = \frac{1}{\frac{1}{n+1}} = n+1$.
    La suite des images est $(f_1(x_n))_{n \in \mathbb{N}} = (1, 2, 3, \dots, n+1, \dots)$.
    Nous devons montrer que cette suite n'est pas bornée, c'est-à-dire :
    $\forall M \in \mathbb{R}_{>0}, \exists n \in \mathbb{N}, |f_1(x_n)| > M$.
    Soit $M \in \mathbb{R}_{>0}$ un nombre réel strictement positif arbitraire.
    Nous cherchons $n \in \mathbb{N}$ tel que $|f_1(x_n)| > M$.
    Nous avons $|f_1(x_n)| = |n+1| = n+1$.
    L'inégalité $n+1 > M$ est équivalente à $n > M-1$.
    Choisissons $n_M = \max(0, \lfloor M \rfloor)$. Alors $n_M \in \mathbb{N}$.
    Pour ce $n_M$, nous avons $n_M+1 > M$.
    Par exemple, si $M=10$, $n_M=10$, alors $f_1(x_{10}) = 11 > 10$.
    Donc, la suite $(f_1(x_n))_{n \in \mathbb{N}}$ n'est pas bornée.

Puisque nous avons trouvé une suite $(x_n)_{n \in \mathbb{N}}$ qui converge vers $0$ et dont la suite des images $(f_1(x_n))_{n \in \mathbb{N}}$ n'est pas bornée, la propriété $\neg \mathcal{P}(f_1, 0)$ est vraie.

**Conclusion :** La propriété $\mathcal{P}(f_1, 0)$ est **fausse**.

#### Question 4 : Application 2 avec $f_2(x)$

Soit la fonction $f_2: \mathbb{R} \to \mathbb{R}$ définie par $f_2(x) = \sin\left(\frac{1}{x}\right)$ si $x \neq 0$ et $f_2(0) = 0$.
Nous devons déterminer si la propriété $\mathcal{P}(f_2, 0)$ est vraie ou fausse.

Pour cela, nous allons tenter de prouver la propriété $\mathcal{P}(f_2, 0)$ elle-même.
Selon la formalisation de $\mathcal{P}(f, x_0)$, nous devons montrer que pour toute suite $(x_n)_{n \in \mathbb{N}}$ de nombres réels qui converge vers $x_0 = 0$, la suite des images $(f_2(x_n))_{n \in \mathbb{N}}$ est bornée.

Soit $(x_n)_{n \in \mathbb{N}}$ une suite de nombres réels arbitraire telle que $(x_n)_{n \in \mathbb{N}}$ converge vers $0$.
Nous devons montrer que la suite $(f_2(x_n))_{n \in \mathbb{N}}$ est bornée, c'est-à-dire :
$\exists M \in \mathbb{R}_{>0}, \forall n \in \mathbb{N}, |f_2(x_n)| \le M$.

Considérons un terme général $f_2(x_n)$ de la suite des images.
Deux cas se présentent pour chaque $x_n$:
1.  **Cas où $x_n \neq 0$ :**
    Dans ce cas, $f_2(x_n) = \sin\left(\frac{1}{x_n}\right)$.
    Nous savons que pour tout nombre réel $y \in \mathbb{R}$, la fonction sinus est bornée, et plus précisément, $|\sin(y)| \le 1$.
    Par conséquent, pour tout $n \in \mathbb{N}$ tel que $x_n \neq 0$, nous avons $\left|f_2(x_n)\right| = \left|\sin\left(\frac{1}{x_n}\right)\right| \le 1$.

2.  **Cas où $x_n = 0$ :**
    Dans ce cas, par définition de la fonction $f_2$, nous avons $f_2(x_n) = f_2(0) = 0$.
    Par conséquent, $\left|f_2(x_n)\right| = |0| = 0$.
    L'inégalité $0 \le 1$ est toujours vérifiée dans $\mathbb{R}$, donc la borne est respectée.

En combinant ces deux cas, nous constatons que pour tout $n \in \mathbb{N}$, que $x_n$ soit nul ou non nul, nous avons toujours $|f_2(x_n)| \le 1$.
Nous pouvons donc choisir $M=1$.
Pour ce choix de $M=1 \in \mathbb{R}_{>0}$, nous avons bien $\forall n \in \mathbb{N}, |f_2(x_n)| \le M$.
Ceci démontre que la suite $(f_2(x_n))_{n \in \mathbb{N}}$ est bornée.

Puisque cette démonstration est valable pour toute suite $(x_n)_{n \in \mathbb{N}}$ convergeant vers $0$, la propriété $\mathcal{P}(f_2, 0)$ est vraie.

**Conclusion :** La propriété $\mathcal{P}(f_2, 0)$ est **vraie**.

---