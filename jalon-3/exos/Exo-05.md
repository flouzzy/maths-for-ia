En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant pour approfondir votre maîtrise de la quantification, de l'ordre des quantificateurs et de la négation.

---

### **Exercice 5 (Jalon 3 : Quantification, ordre des quantificateurs, négation)**

**Niveau de difficulté :** $\star\star\star\text{/}\star\star\star\star\star$

Soit $(u_n)_{n \in \mathbb{N}}$ une suite de nombres réels.

On définit les deux propriétés suivantes pour la suite $(u_n)_{n \in \mathbb{N}}$ :

**Propriété $\mathcal{P}_1$ (Visite Dense Infiniment Souvent):**
"La suite $(u_n)_{n \in \mathbb{N}}$ visite chaque intervalle ouvert non vide de $\mathbb{R}$ infiniment souvent."

**Propriété $\mathcal{P}_2$ (Non-Bornitude Éventuelle):**
"La suite $(u_n)_{n \in \mathbb{N}}$ n'est pas éventuellement bornée."

---

**Questions :**

1.  **Formalisation :**
    Écrire les propriétés $\mathcal{P}_1$ et $\mathcal{P}_2$ en utilisant uniquement des quantificateurs, des connecteurs logiques et des symboles mathématiques. Préciser le type de chaque objet mathématique introduit.

2.  **Négation :**
    Écrire la négation de $\mathcal{P}_1$ (notée $\neg \mathcal{P}_1$) et la négation de $\mathcal{P}_2$ (notée $\neg \mathcal{P}_2$) en utilisant uniquement des quantificateurs, des connecteurs logiques et des symboles mathématiques. Simplifier au maximum l'expression obtenue pour que la négation ne porte pas sur une expression quantifiée. Préciser le type de chaque objet mathématique introduit.

3.  **Implications Logiques :**
    a.  La propriété $\mathcal{P}_1$ implique-t-elle la propriété $\mathcal{P}_2$? C'est-à-dire, a-t-on $\mathcal{P}_1 \implies \mathcal{P}_2$? Justifier rigoureusement votre réponse par une démonstration ou un contre-exemple.
    b.  La propriété $\mathcal{P}_2$ implique-t-elle la propriété $\mathcal{P}_1$? C'est-à-dire, a-t-on $\mathcal{P}_2 \implies \mathcal{P}_1$? Justifier rigoureusement votre réponse par une démonstration ou un contre-exemple.

4.  **Exemples :**
    a.  Donner un exemple de suite $(u_n)_{n \in \mathbb{N}}$ qui satisfait la propriété $\mathcal{P}_1$.
    b.  Donner un exemple de suite $(u_n)_{n \in \mathbb{N}}$ qui satisfait la propriété $\mathcal{P}_2$ mais pas la propriété $\mathcal{P}_1$.
    c.  Donner un exemple de suite $(u_n)_{n \in \mathbb{N}}$ qui ne satisfait ni la propriété $\mathcal{P}_1$ ni la propriété $\mathcal{P}_2$.

---

### **Correction Ultra-Détaillée de l'Exercice 5**

Nous allons aborder chaque question avec la rigueur attendue, en explicitant chaque étape et en typant strictement les objets mathématiques. Nous utiliserons $\mathbb{N} = \{0, 1, 2, \dots\}$ pour l'ensemble des entiers naturels.

---

#### **1. Formalisation :**

**Propriété $\mathcal{P}_1$ (Visite Dense Infiniment Souvent) :**
"La suite $(u_n)_{n \in \mathbb{N}}$ visite chaque intervalle ouvert non vide de $\mathbb{R}$ infiniment souvent."

*   **Analyse de la phrase :**
    *   "chaque intervalle ouvert non vide de $\mathbb{R}$" : Cela signifie que pour tout couple de nombres réels $a$ et $b$ tels que $a < b$, l'intervalle $(a,b)$ est concerné.
        *   Typage : Soient $a$ un nombre réel ($a \in \mathbb{R}$) et $b$ un nombre réel ($b \in \mathbb{R}$).
        *   Condition : $a < b$.
    *   "infiniment souvent" : Cela signifie que quel que soit le rang $N$ à partir duquel on regarde la suite, il existe toujours un terme de la suite après ce rang qui appartient à l'intervalle.
        *   Typage : Soit $N$ un entier naturel ($N \in \mathbb{N}$).
        *   Existence : Il existe un entier naturel $n$ ($n \in \mathbb{N}$).
        *   Condition sur le rang : $n \ge N$.
        *   Condition sur la valeur : $u_n \in (a,b)$, ce qui est équivalent à $a < u_n < b$.

*   **Formalisation de $\mathcal{P}_1$ :**
    $$ \mathcal{P}_1 \equiv \forall a \in \mathbb{R}, \forall b \in \mathbb{R}, \left( a < b \implies \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right) $$

**Propriété $\mathcal{P}_2$ (Non-Bornitude Éventuelle) :**
"La suite $(u_n)_{n \in \mathbb{N}}$ n'est pas éventuellement bornée."

*   **Analyse de la phrase :**
    *   "n'est pas éventuellement bornée" : C'est la négation de "la suite est éventuellement bornée".
    *   Formalisons d'abord "la suite est éventuellement bornée" :
        *   "éventuellement bornée" : Cela signifie qu'il existe un rang à partir duquel tous les termes de la suite sont bornés en valeur absolue par une certaine constante.
        *   Existence d'une borne : Il existe un nombre réel $M$ ($M \in \mathbb{R}$). On peut sans perte de généralité considérer $M \ge 0$, car si $|u_n| \le M$ pour un $M<0$, alors $|u_n|$ serait négatif, ce qui est impossible. Donc $M$ peut être pris dans $\mathbb{R}_{\ge 0}$.
        *   Existence d'un rang : Il existe un entier naturel $N$ ($N \in \mathbb{N}$).
        *   Condition sur les termes : Pour tout entier naturel $n$ ($n \in \mathbb{N}$), si $n \ge N$, alors $|u_n| \le M$.

*   **Formalisation de "la suite est éventuellement bornée" :**
    $$ \exists M \in \mathbb{R}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies |u_n| \le M \right) $$

*   **Formalisation de $\mathcal{P}_2$ (qui est la négation de l'expression ci-dessus) :**
    $$ \mathcal{P}_2 \equiv \neg \left( \exists M \in \mathbb{R}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies |u_n| \le M \right) \right) $$

---

#### **2. Négation :**

Nous allons appliquer les règles de négation des quantificateurs ($\neg \forall x, P(x) \equiv \exists x, \neg P(x)$ et $\neg \exists x, P(x) \equiv \forall x, \neg P(x)$) et les lois de De Morgan ($\neg (P \land Q) \equiv \neg P \lor \neg Q$, $\neg (P \lor Q) \equiv \neg P \land \neg Q$, $\neg (P \implies Q) \equiv P \land \neg Q$).

**Négation de $\mathcal{P}_1$ ($\neg \mathcal{P}_1$) :**

Partons de la formalisation de $\mathcal{P}_1$:
$$ \mathcal{P}_1 \equiv \forall a \in \mathbb{R}, \forall b \in \mathbb{R}, \left( a < b \implies \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right) $$

Appliquons la négation étape par étape :
1.  Négation du premier quantificateur universel :
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \neg \left( \forall b \in \mathbb{R}, \left( a < b \implies \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right) \right) $$
2.  Négation du deuxième quantificateur universel :
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \neg \left( a < b \implies \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right) $$
3.  Négation de l'implication $P \implies Q$ (où $P \equiv (a < b)$ et $Q \equiv (\forall N \in \mathbb{N}, \dots)$) : $\neg (P \implies Q) \equiv P \land \neg Q$.
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \neg \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right) $$
4.  Négation du quantificateur universel $\forall N$ :
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \exists N \in \mathbb{N}, \neg \left( \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right) $$
5.  Négation du quantificateur existentiel $\exists n$ :
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \neg \left( n \ge N \land a < u_n < b \right) \right) $$
6.  Négation de la conjonction $P \land Q$ : $\neg (P \land Q) \equiv \neg P \lor \neg Q$.
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( \neg (n \ge N) \lor \neg (a < u_n < b) \right) \right) $$
7.  Simplification des négations : $\neg (n \ge N) \equiv n < N$. $\neg (a < u_n < b) \equiv (u_n \le a \lor u_n \ge b)$.
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n < N \lor u_n \le a \lor u_n \ge b \right) \right) $$
8.  Reformulation de la disjonction $(n < N \lor \dots)$ en implication : $(n < N \lor Q) \equiv (n \ge N \implies Q)$.
    $$ \neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies (u_n \le a \lor u_n \ge b) \right) \right) $$

*   **Interprétation de $\neg \mathcal{P}_1$ :**
    "Il existe un intervalle ouvert non vide $(a,b)$ tel qu'à partir d'un certain rang $N$, aucun terme de la suite $u_n$ n'appartient à cet intervalle."
*   **Typage des objets :** $a, b \in \mathbb{R}$, $N, n \in \mathbb{N}$.

**Négation de $\mathcal{P}_2$ ($\neg \mathcal{P}_2$) :**

Partons de la formalisation de $\mathcal{P}_2$:
$$ \mathcal{P}_2 \equiv \neg \left( \exists M \in \mathbb{R}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies |u_n| \le M \right) \right) $$

Appliquons la négation :
$$ \neg \mathcal{P}_2 \equiv \exists M \in \mathbb{R}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies |u_n| \le M \right) $$
(La double négation s'annule : $\neg (\neg Q) \equiv Q$).

*   **Interprétation de $\neg \mathcal{P}_2$ :**
    "La suite $(u_n)_{n \in \mathbb{N}}$ est éventuellement bornée."
*   **Typage des objets :** $M \in \mathbb{R}$, $N, n \in \mathbb{N}$.

---

#### **3. Implications Logiques :**

**a. La propriété $\mathcal{P}_1$ implique-t-elle la propriété $\mathcal{P}_2$? ($\mathcal{P}_1 \implies \mathcal{P}_2$)**

*   **Rappel des propriétés :**
    *   $\mathcal{P}_1 \equiv \forall a \in \mathbb{R}, \forall b \in \mathbb{R}, \left( a < b \implies \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right)$
    *   $\mathcal{P}_2 \equiv \forall M \in \mathbb{R}, \forall N_0 \in \mathbb{N}, \exists n_0 \in \mathbb{N}, \left( n_0 \ge N_0 \land |u_{n_0}| > M \right)$ (forme simplifiée de $\mathcal{P}_2$ après négation de la négation)

*   **Démonstration :**
    Supposons que la propriété $\mathcal{P}_1$ est vraie. Nous voulons montrer que la propriété $\mathcal{P}_2$ est vraie.
    Pour cela, nous devons montrer que pour tout nombre réel $M$ (soit $M \in \mathbb{R}$) et pour tout entier naturel $N_0$ (soit $N_0 \in \mathbb{N}$), il existe un entier naturel $n_0$ tel que $n_0 \ge N_0$ et $|u_{n_0}| > M$.

    1.  Soit $M \in \mathbb{R}$ un nombre réel arbitraire.
    2.  Soit $N_0 \in \mathbb{N}$ un entier naturel arbitraire.
    3.  Considérons le nombre réel $M' = |M| + 1$. Par construction, $M' > |M|$, et $M' > 0$.
    4.  Considérons l'intervalle ouvert $(M', M'+1)$. Cet intervalle est non vide car $M' < M'+1$.
    5.  Puisque $\mathcal{P}_1$ est vraie, et que $(M', M'+1)$ est un intervalle ouvert non vide, il s'ensuit que pour tout rang $N_{temp} \in \mathbb{N}$, il existe un entier naturel $n_{temp} \ge N_{temp}$ tel que $u_{n_{temp}} \in (M', M'+1)$.
    6.  Appliquons cette conclusion avec $N_{temp} = N_0$. Il existe donc un entier naturel $n_0 \in \mathbb{N}$ tel que $n_0 \ge N_0$ et $u_{n_0} \in (M', M'+1)$.
    7.  La condition $u_{n_0} \in (M', M'+1)$ signifie que $M' < u_{n_0} < M'+1$.
    8.  De $M' < u_{n_0}$, nous déduisons $u_{n_0} > M'$.
    9.  Puisque $M' = |M|+1$, nous avons $u_{n_0} > |M|+1$.
    10. Comme $u_{n_0} > |M|+1$, $u_{n_0}$ est nécessairement positif. Par conséquent, $|u_{n_0}| = u_{n_0}$.
    11. Ainsi, nous avons $|u_{n_0}| > |M|+1$.
    12. Il s'ensuit que $|u_{n_0}| > |M|$.
    13. Et par transitivité, $|u_{n_0}| > M$.
    14. Nous avons donc trouvé un $n_0 \ge N_0$ tel que $|u_{n_0}| > M$.

    Puisque $M$ et $N_0$ étaient arbitraires, la propriété $\mathcal{P}_2$ est vérifiée.
    **Conclusion :** Oui, $\mathcal{P}_1 \implies \mathcal{P}_2$.

**b. La propriété $\mathcal{P}_2$ implique-t-elle la propriété $\mathcal{P}_1$? ($\mathcal{P}_2 \implies \mathcal{P}_1$)**

*   **Rappel des propriétés :**
    *   $\mathcal{P}_1 \equiv \forall a \in \mathbb{R}, \forall b \in \mathbb{R}, \left( a < b \implies \left( \forall N \in \mathbb{N}, \exists n \in \mathbb{N}, \left( n \ge N \land a < u_n < b \right) \right) \right)$
    *   $\mathcal{P}_2 \equiv \forall M \in \mathbb{R}, \forall N_0 \in \mathbb{N}, \exists n_0 \in \mathbb{N}, \left( n_0 \ge N_0 \land |u_{n_0}| > M \right)$

*   **Recherche d'un contre-exemple :**
    Pour montrer que $\mathcal{P}_2 \not\implies \mathcal{P}_1$, nous devons trouver une suite $(u_n)_{n \in \mathbb{N}}$ qui satisfait $\mathcal{P}_2$ mais ne satisfait pas $\mathcal{P}_1$.
    C'est-à-dire, une suite qui n'est pas éventuellement bornée, mais qui ne visite pas chaque intervalle ouvert non vide de $\mathbb{R}$ infiniment souvent.

    Considérons la suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = n$ pour tout $n \in \mathbb{N}$.

    1.  **Vérifions si $u_n = n$ satisfait $\mathcal{P}_2$ :**
        *   Soit $M \in \mathbb{R}$ un nombre réel arbitraire.
        *   Soit $N_0 \in \mathbb{N}$ un entier naturel arbitraire.
        *   Nous cherchons un $n_0 \in \mathbb{N}$ tel que $n_0 \ge N_0$ et $|u_{n_0}| > M$.
        *   Choisissons $n_0 = \max(N_0, \lceil |M| \rceil + 1)$. (Ici, $\lceil x \rceil$ désigne la partie entière par excès de $x$).
        *   Par construction, $n_0 \in \mathbb{N}$ et $n_0 \ge N_0$.
        *   De plus, $n_0 \ge \lceil |M| \rceil + 1 > |M|$.
        *   Puisque $u_{n_0} = n_0$, nous avons $u_{n_0} > |M|$.
        *   Comme $u_{n_0}$ est positif, $|u_{n_0}| = u_{n_0}$. Donc $|u_{n_0}| > |M|$.
        *   Il s'ensuit que $|u_{n_0}| > M$.
        *   Ainsi, la suite $u_n = n$ satisfait $\mathcal{P}_2$.

    2.  **Vérifions si $u_n = n$ satisfait $\mathcal{P}_1$ :**
        *   Pour montrer que $u_n = n$ ne satisfait pas $\mathcal{P}_1$, nous devons montrer que $\neg \mathcal{P}_1$ est vraie pour cette suite.
        *   $\neg \mathcal{P}_1 \equiv \exists a \in \mathbb{R}, \exists b \in \mathbb{R}, \left( a < b \land \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies (u_n \le a \lor u_n \ge b) \right) \right)$.
        *   Considérons l'intervalle ouvert $(a,b) = (0.1, 0.9)$. Cet intervalle est non vide car $0.1 < 0.9$.
        *   Nous devons trouver un rang $N$ tel que pour tout $n \ge N$, $u_n \notin (0.1, 0.9)$.
        *   Pour la suite $u_n = n$, les termes sont $0, 1, 2, 3, \dots$.
        *   Aucun de ces termes n'appartient à l'intervalle $(0.1, 0.9)$.
        *   Plus formellement, pour tout $n \in \mathbb{N}$, $u_n = n$. Si $n \in (0.1, 0.9)$, alors $0.1 < n < 0.9$. Or, il n'existe aucun entier naturel $n$ qui satisfait cette condition.
        *   Par conséquent, pour n'importe quel $N \in \mathbb{N}$ (par exemple $N=0$), il est vrai que pour tout $n \in \mathbb{N}$ tel que $n \ge N$, $u_n \notin (0.1, 0.9)$.
        *   Donc, $u_n = n$ ne satisfait pas $\mathcal{P}_1$.

    Puisque la suite $u_n = n$ satisfait $\mathcal{P}_2$ mais ne satisfait pas $\mathcal{P}_1$, nous avons trouvé un contre-exemple.
    **Conclusion :** Non, $\mathcal{P}_2 \not\implies \mathcal{P}_1$.

---

#### **4. Exemples :**

**a. Exemple de suite $(u_n)_{n \in \mathbb{N}}$ qui satisfait $\mathcal{P}_1$ :**

Une suite qui satisfait $\mathcal{P}_1$ doit avoir ses termes "densément répartis" dans $\mathbb{R}$ et les visiter infiniment souvent. Un exemple canonique est une énumération des nombres rationnels.

*   **Exemple :** Soit $(q_k)_{k \in \mathbb{N}}$ une énumération des nombres rationnels $\mathbb{Q}$. On peut définir $u_n = q_n$.
    *   **Justification :**
        1.  **$\mathcal{P}_1$ est satisfaite :**
            *   Soient $a, b \in \mathbb{R}$ tels que $a < b$. L'intervalle $(a,b)$ est un intervalle ouvert non vide.
            *   Par la propriété de densité de $\mathbb{Q}$ dans $\mathbb{R}$, l'intervalle $(a,b)$ contient une infinité de nombres rationnels.
            *   Soit $N \in \mathbb{N}$ un rang arbitraire. Puisque $(a,b)$ contient une infinité de rationnels, il existe nécessairement un nombre rationnel $q_k \in (a,b)$ dont l'indice $k$ dans l'énumération est supérieur ou égal à $N$.
            *   Donc, il existe $n \in \mathbb{N}$ (qui est $k$) tel que $n \ge N$ et $u_n = q_k \in (a,b)$.
            *   Ceci est vrai pour tout $a,b$ avec $a<b$ et tout $N$. Donc $\mathcal{P}_1$ est satisfaite.

**b. Exemple de suite $(u_n)_{n \in \mathbb{N}}$ qui satisfait $\mathcal{P}_2$ mais pas $\mathcal{P}_1$ :**

Nous avons déjà utilisé un tel exemple dans la question 3.b.

*   **Exemple :** La suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = n$.
    *   **Justification :**
        1.  **$\mathcal{P}_2$ est satisfaite :**
            *   Soient $M \in \mathbb{R}$ et $N_0 \in \mathbb{N}$. Choisissons $n_0 = \max(N_0, \lceil |M| \rceil + 1)$.
            *   Alors $n_0 \ge N_0$ et $u_{n_0} = n_0 > |M|$, donc $|u_{n_0}| > M$.
            *   Ainsi, $\mathcal{P}_2$ est satisfaite.
        2.  **$\mathcal{P}_1$ n'est pas satisfaite :**
            *   Considérons l'intervalle $(a,b) = (0.1, 0.9)$.
            *   Pour tout $n \in \mathbb{N}$, $u_n = n$. Aucun entier naturel $n$ ne vérifie $0.1 < n < 0.9$.
            *   Par conséquent, pour tout $N \in \mathbb{N}$, il n'existe aucun $n \ge N$ tel que $u_n \in (0.1, 0.9)$.
            *   Ceci correspond à la négation de $\mathcal{P}_1$.
            *   Ainsi, $\mathcal{P}_1$ n'est pas satisfaite.

**c. Exemple de suite $(u_n)_{n \in \mathbb{N}}$ qui ne satisfait ni $\mathcal{P}_1$ ni $\mathcal{P}_2$ :**

Nous cherchons une suite qui satisfait $\neg \mathcal{P}_1$ et $\neg \mathcal{P}_2$.
*   $\neg \mathcal{P}_1$: Il existe un intervalle $(a,b)$ tel qu'à partir d'un certain rang, $u_n \notin (a,b)$.
*   $\neg \mathcal{P}_2$: La suite est éventuellement bornée.

Une suite convergente, ou même une suite constante, satisfera ces deux conditions.

*   **Exemple :** La suite $(u_n)_{n \in \mathbb{N}}$ définie par $u_n = 0$ pour tout $n \in \mathbb{N}$.
    *   **Justification :**
        1.  **$\mathcal{P}_1$ n'est pas satisfaite :**
            *   Considérons l'intervalle $(a,b) = (1, 2)$. Cet intervalle est non vide.
            *   Pour tout $n \in \mathbb{N}$, $u_n = 0$. Clairement, $0 \notin (1, 2)$.
            *   Donc, pour tout $N \in \mathbb{N}$ (par exemple $N=0$), il n'existe aucun $n \ge N$ tel que $u_n \in (1, 2)$.
            *   Ceci correspond à la négation de $\mathcal{P}_1$.
            *   Ainsi, $\mathcal{P}_1$ n'est pas satisfaite.
        2.  **$\mathcal{P}_2$ n'est pas satisfaite :**
            *   Nous devons montrer que $\neg \mathcal{P}_2$ est vraie, c'est-à-dire que la suite est éventuellement bornée.
            *   $\neg \mathcal{P}_2 \equiv \exists M \in \mathbb{R}, \exists N \in \mathbb{N}, \forall n \in \mathbb{N}, \left( n \ge N \implies |u_n| \le M \right)$.
            *   Choisissons $M=1$ (un nombre réel) et $N=0$ (un entier naturel).
            *   Pour tout $n \in \mathbb{N}$ tel que $n \ge 0$, nous avons $|u_n| = |0| = 0$.
            *   Et $0 \le 1$. Donc $|u_n| \le M$.
            *   Ainsi, la suite $u_n = 0$ est éventuellement bornée, ce qui signifie que $\neg \mathcal{P}_2$ est satisfaite.
            *   Par conséquent, $\mathcal{P}_2$ n'est pas satisfaite.

---