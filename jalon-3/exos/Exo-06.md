En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant pour le Jalon 3.

---

## Exercice 6 : Propriétés de non-convergence et quantification

**Contexte :**
Soit $(u_n)_{n \in \mathbb{N}}$ une suite de nombres réels. Nous rappelons que $\mathbb{N} = \{0, 1, 2, \dots\}$ désigne l'ensemble des entiers naturels, et $\mathbb{R}_{>0}$ l'ensemble des nombres réels strictement positifs.

**Définition :**
On considère la propriété $\mathcal{P}$ suivante pour une suite $(u_n)_{n \in \mathbb{N}}$ :
$$ \mathcal{P}: \quad \forall L \in \mathbb{R}, \exists \epsilon \in \mathbb{R}_{>0}, \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \quad (n \ge N \land |u_n - L| \ge \epsilon) $$

**Niveau de difficulté :** $\star\star\star\text{/}\star\star\star\star\star$

---

### Questions

1.  **Négation de la propriété $\mathcal{P}$**
    Écrire la négation de la propriété $\mathcal{P}$, notée $\neg \mathcal{P}$, en utilisant les quantificateurs et les opérateurs logiques appropriés. Simplifier l'expression autant que possible pour qu'elle corresponde à une définition mathématique usuelle.

2.  **Analyse de suites spécifiques**
    Pour chacune des suites suivantes, déterminer si elle satisfait la propriété $\mathcal{P}$ ou sa négation $\neg \mathcal{P}$. Justifier rigoureusement chaque réponse en explicitant le choix des quantificateurs (valeurs de $L$, $\epsilon$, $N$, $n$).

    a)  La suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = (-1)^n$.
    b)  La suite $(v_n)_{n \in \mathbb{N}^*}$ définie par $v_n = \frac{1}{n}$ (pour cette suite, on considérera $\mathbb{N}^* = \{1, 2, 3, \dots\}$).
    c)  La suite $(w_n)_{n \in \mathbb{N}}$ définie par $w_n = n$.

---
---

### Correction Détaillée

#### 1. Négation de la propriété $\mathcal{P}$

La propriété $\mathcal{P}$ est donnée par :
$$ \mathcal{P}: \quad \forall L \in \mathbb{R}, \exists \epsilon \in \mathbb{R}_{>0}, \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \quad (n \ge N \land |u_n - L| \ge \epsilon) $$

Pour obtenir la négation $\neg \mathcal{P}$, nous appliquons successivement les règles de négation des quantificateurs ($\neg \forall x, P(x) \equiv \exists x, \neg P(x)$ et $\neg \exists x, P(x) \equiv \forall x, \neg P(x)$) et la négation d'une conjonction ($\neg (A \land B) \equiv \neg A \lor \neg B$).

1.  **Négation du premier quantificateur ($\forall L \in \mathbb{R}$)** :
    $$ \neg \mathcal{P}: \quad \exists L \in \mathbb{R}, \neg \left( \exists \epsilon \in \mathbb{R}_{>0}, \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \quad (n \ge N \land |u_n - L| \ge \epsilon) \right) $$

2.  **Négation du deuxième quantificateur ($\exists \epsilon \in \mathbb{R}_{>0}$)** :
    $$ \neg \mathcal{P}: \quad \exists L \in \mathbb{R}, \forall \epsilon \in \mathbb{R}_{>0}, \neg \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \quad (n \ge N \land |u_n - L| \ge \epsilon) \right) $$

3.  **Négation du troisième quantificateur ($\forall N \in \mathbb{N}$)** :
    $$ \neg \mathcal{P}: \quad \exists L \in \mathbb{R}, \forall \epsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \neg \left( \exists n \in \mathbb{N}, \quad (n \ge N \land |u_n - L| \ge \epsilon) \right) $$

4.  **Négation du quatrième quantificateur ($\exists n \in \mathbb{N}$)** :
    $$ \neg \mathcal{P}: \quad \exists L \in \mathbb{R}, \forall \epsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \quad \neg (n \ge N \land |u_n - L| \ge \epsilon) $$

5.  **Négation de la proposition $(n \ge N \land |u_n - L| \ge \epsilon)$** :
    La négation d'une conjonction $A \land B$ est $\neg A \lor \neg B$.
    Ici, $A$ est la proposition $n \ge N$ et $B$ est la proposition $|u_n - L| \ge \epsilon$.
    Donc, $\neg (n \ge N \land |u_n - L| \ge \epsilon)$ est équivalent à $\neg (n \ge N) \lor \neg (|u_n - L| \ge \epsilon)$.
    $\neg (n \ge N)$ est la proposition $n < N$.
    $\neg (|u_n - L| \ge \epsilon)$ est la proposition $|u_n - L| < \epsilon$.
    Ainsi, la proposition devient $(n < N \lor |u_n - L| < \epsilon)$.

    Cette proposition $(n < N \lor |u_n - L| < \epsilon)$ est logiquement équivalente à l'implication $(n \ge N \implies |u_n - L| < \epsilon)$, car $A \implies B$ est équivalent à $\neg A \lor B$.

En substituant cette forme simplifiée, nous obtenons la négation finale :
$$ \neg \mathcal{P}: \quad \exists L \in \mathbb{R}, \forall \epsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \quad (n \ge N \implies |u_n - L| < \epsilon) $$
Cette expression est la définition rigoureuse de la **convergence de la suite $(u_n)$ vers la limite $L$**.
Par conséquent, la propriété $\mathcal{P}$ signifie que "la suite $(u_n)$ ne converge pas".

---

#### 2. Analyse de suites spécifiques

**a) La suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = (-1)^n$.**

Nous devons déterminer si $(u_n)$ satisfait $\mathcal{P}$ (ne converge pas) ou $\neg \mathcal{P}$ (converge).
La suite $(u_n)$ prend alternativement les valeurs $1$ et $-1$. Il est bien connu qu'une telle suite ne converge pas. Nous allons donc démontrer qu'elle satisfait la propriété $\mathcal{P}$.

Pour montrer que $(u_n)$ satisfait $\mathcal{P}$, nous devons démontrer que :
$$ \forall L \in \mathbb{R}, \exists \epsilon \in \mathbb{R}_{>0}, \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \quad (n \ge N \land |u_n - L| \ge \epsilon) $$

1.  **Choix de $L$ :** Soit $L \in \mathbb{R}$ un nombre réel arbitraire.

2.  **Choix de $\epsilon$ :** Nous devons trouver un $\epsilon \in \mathbb{R}_{>0}$ qui fonctionne pour ce $L$.
    Les valeurs de la suite sont $1$ et $-1$. Considérons les distances de $L$ à ces deux valeurs : $|1-L|$ et $|-1-L|$.
    Par l'inégalité triangulaire, nous savons que $2 = |1 - (-1)| = |(1-L) - (-1-L)| \le |1-L| + |-1-L|$.
    Ceci implique qu'au moins une des deux distances $|1-L|$ ou $|-1-L|$ doit être supérieure ou égale à $1$.
    En effet, si $|1-L| < 1$ et $|-1-L| < 1$, alors $|1-L| + |-1-L| < 1+1=2$, ce qui contredit $2 \le |1-L| + |-1-L|$.
    Nous pouvons donc choisir $\epsilon = 1$. Ce $\epsilon$ est bien un réel strictement positif.

3.  **Choix de $N$ :** Soit $N \in \mathbb{N}$ un entier naturel arbitraire.

4.  **Choix de $n$ :** Nous devons trouver un entier $n \in \mathbb{N}$ tel que $n \ge N$ et $|u_n - L| \ge \epsilon$.
    Nous savons que $\max(|1-L|, |-1-L|) \ge 1$.
    *   **Cas 1 :** Si $|1-L| \ge 1$.
        Nous devons trouver un $n \ge N$ tel que $u_n = 1$. Puisque $u_n = (-1)^n$, $u_n=1$ si $n$ est pair. Il existe une infinité d'entiers pairs. Nous pouvons donc toujours trouver un entier pair $n_0 \in \mathbb{N}$ tel que $n_0 \ge N$. Pour cet $n_0$, $u_{n_0} = 1$, et donc $|u_{n_0} - L| = |1 - L| \ge 1 = \epsilon$.
    *   **Cas 2 :** Si $|-1-L| \ge 1$.
        Nous devons trouver un $n \ge N$ tel que $u_n = -1$. Puisque $u_n = (-1)^n$, $u_n=-1$ si $n$ est impair. Il existe une infinité d'entiers impairs. Nous pouvons donc toujours trouver un entier impair $n_0 \in \mathbb{N}$ tel que $n_0 \ge N$. Pour cet $n_0$, $u_{n_0} = -1$, et donc $|u_{n_0} - L| = |-1 - L| \ge 1 = \epsilon$.

Puisque l'un de ces deux cas est toujours vrai pour tout $L \in \mathbb{R}$, nous avons montré que pour tout $L \in \mathbb{R}$, il existe un $\epsilon=1$ tel que pour tout $N \in \mathbb{N}$, il existe un $n \ge N$ (soit pair, soit impair) pour lequel $|u_n - L| \ge \epsilon$.

**Conclusion :** La suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = (-1)^n$ satisfait la propriété $\mathcal{P}$.

---

**b) La suite $(v_n)_{n \in \mathbb{N}^*}$ définie par $v_n = \frac{1}{n}$.**

Nous devons déterminer si $(v_n)$ satisfait $\mathcal{P}$ ou $\neg \mathcal{P}$.
La suite $(v_n)$ est la suite $(1, 1/2, 1/3, \dots)$. Il est bien connu que cette suite converge vers $0$. Nous allons donc démontrer qu'elle satisfait la propriété $\neg \mathcal{P}$.

Pour montrer que $(v_n)$ satisfait $\neg \mathcal{P}$, nous devons démontrer que :
$$ \exists L \in \mathbb{R}, \forall \epsilon \in \mathbb{R}_{>0}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \quad (n \ge N \implies |v_n - L| < \epsilon) $$

1.  **Choix de $L$ :** Nous affirmons que la limite est $L=0$. Nous choisissons donc $L=0 \in \mathbb{R}$.

2.  **Choix de $\epsilon$ :** Soit $\epsilon \in \mathbb{R}_{>0}$ un nombre réel strictement positif arbitraire.

3.  **Choix de $N$ :** Nous devons trouver un entier naturel $N \in \mathbb{N}$ (qui dépendra de $\epsilon$) tel que pour tout $n \ge N$, la condition $|v_n - L| < \epsilon$ soit satisfaite.
    La condition est $|1/n - 0| < \epsilon$, ce qui est équivalent à $1/n < \epsilon$ (car $n \in \mathbb{N}^*$, donc $1/n > 0$).
    L'inégalité $1/n < \epsilon$ est équivalente à $n > 1/\epsilon$.
    Puisque $\epsilon > 0$, $1/\epsilon$ est un nombre réel positif. Par la propriété d'Archimède, il existe un entier naturel $N_0 \in \mathbb{N}$ tel que $N_0 > 1/\epsilon$.
    Pour s'assurer que $N$ est un indice valide pour la suite $(v_n)$ (qui commence à $n=1$), nous choisissons $N = \max(1, N_0)$. Ce $N$ est un entier naturel et $N \ge 1$.

4.  **Choix de $n$ :** Soit $n \in \mathbb{N}^*$ un entier tel que $n \ge N$.
    Puisque $n \ge N$ et $N > 1/\epsilon$, il s'ensuit que $n > 1/\epsilon$.
    En prenant l'inverse des deux côtés de l'inégalité (qui sont tous deux positifs), nous obtenons $1/n < \epsilon$.
    Puisque $v_n = 1/n$, nous avons $|v_n - 0| = |1/n| = 1/n < \epsilon$.
    La condition $(n \ge N \implies |v_n - L| < \epsilon)$ est donc satisfaite.

Nous avons donc trouvé un $L=0$ tel que pour tout $\epsilon > 0$, il existe un $N$ (dépendant de $\epsilon$) tel que pour tout $n \ge N$, $|v_n - L| < \epsilon$.

**Conclusion :** La suite $(v_n)_{n \in \mathbb{N}^*}$ définie par $v_n = \frac{1}{n}$ satisfait la propriété $\neg \mathcal{P}$.

---

**c) La suite $(w_n)_{n \in \mathbb{N}}$ définie par $w_n = n$.**

Nous devons déterminer si $(w_n)$ satisfait $\mathcal{P}$ ou $\neg \mathcal{P}$.
La suite $(w_n)$ est la suite $(0, 1, 2, 3, \dots)$. Cette suite diverge vers $+\infty$. Elle ne converge donc pas vers un nombre réel $L$. Nous allons démontrer qu'elle satisfait la propriété $\mathcal{P}$.

Pour montrer que $(w_n)$ satisfait $\mathcal{P}$, nous devons démontrer que :
$$ \forall L \in \mathbb{R}, \exists \epsilon \in \mathbb{R}_{>0}, \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \quad (n \ge N \land |w_n - L| \ge \epsilon) $$

1.  **Choix de $L$ :** Soit $L \in \mathbb{R}$ un nombre réel arbitraire.

2.  **Choix de $\epsilon$ :** Nous devons trouver un $\epsilon \in \mathbb{R}_{>0}$ qui fonctionne pour ce $L$.
    Puisque $w_n = n$ peut devenir arbitrairement grand, nous pouvons toujours trouver des termes $w_n$ qui sont "loin" de n'importe quel $L$.
    Nous choisissons $\epsilon = 1$. Ce $\epsilon$ est bien un réel strictement positif.

3.  **Choix de $N$ :** Soit $N \in \mathbb{N}$ un entier naturel arbitraire.

4.  **Choix de $n$ :** Nous devons trouver un entier $n \in \mathbb{N}$ tel que $n \ge N$ et $|w_n - L| \ge \epsilon$.
    La condition est $|n - L| \ge 1$. Ceci est équivalent à $n - L \ge 1$ ou $n - L \le -1$.
    Ces inégalités sont équivalentes à $n \ge L+1$ ou $n \le L-1$.
    Puisque $n$ peut prendre des valeurs arbitrairement grandes, nous pouvons toujours trouver un $n$ qui satisfait $n \ge L+1$.
    Pour cela, nous choisissons $n_0 = \max(N, \lfloor L \rfloor + 2)$.
    *   $n_0$ est un entier naturel car $N \in \mathbb{N}$ et $\lfloor L \rfloor + 2$ est un entier.
    *   Par construction, $n_0 \ge N$.
    *   Par construction, $n_0 \ge \lfloor L \rfloor + 2$. Ceci implique $n_0 > L+1$ (car $\lfloor L \rfloor \le L < \lfloor L \rfloor + 1$, donc $\lfloor L \rfloor + 2 > L+1$).
    Puisque $n_0 > L+1$, il s'ensuit que $n_0 - L > 1$, et donc $|n_0 - L| > 1$.
    Comme $\epsilon = 1$, nous avons $|n_0 - L| > \epsilon$, ce qui implique $|n_0 - L| \ge \epsilon$.
    La condition $(n \ge N \land |w_n - L| \ge \epsilon)$ est donc satisfaite pour $n=n_0$.

Nous avons donc montré que pour tout $L \in \mathbb{R}$, il existe un $\epsilon=1$ tel que pour tout $N \in \mathbb{N}$, il existe un $n \ge N$ pour lequel $|w_n - L| \ge \epsilon$.

**Conclusion :** La suite $(w_n)_{n \in \mathbb{N}}$ définie par $w_n = n$ satisfait la propriété $\mathcal{P}$.

---