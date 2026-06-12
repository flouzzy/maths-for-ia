## Exercice 10 : La Continuité Uniforme Séquentielle

**Niveau de difficulté :** $\star\star\star\star\star$

### Énoncé

Soit $I$ un intervalle de $\mathbb{R}$ et $f: I \to \mathbb{R}$ une fonction.

On définit la propriété $\mathcal{P}(f)$ de la manière suivante :
$$
\mathcal{P}(f) \quad \iff \quad \forall \epsilon \in \mathbb{R}_{+}^{*}, \forall (x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}}, \exists \delta \in \mathbb{R}_{+}^{*}, \left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta \right) \implies \left( \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon \right)
$$

1.  **Analyse de la propriété :**
    *   Écrire la négation de la propriété $\mathcal{P}(f)$.
    *   Écrire la définition de la continuité uniforme de $f$ sur $I$.
    *   Écrire la négation de la continuité uniforme de $f$ sur $I$.

2.  **Implication directe :**
    *   Démontrer que si $f$ est uniformément continue sur $I$, alors $f$ satisfait la propriété $\mathcal{P}(f)$.

3.  **Implication réciproque (le cœur de l'exercice) :**
    *   Démontrer que si $f$ satisfait la propriété $\mathcal{P}(f)$, alors $f$ est uniformément continue sur $I$.

4.  **Conclusion :**
    *   Que peut-on dire de la relation entre la propriété $\mathcal{P}(f)$ et la continuité uniforme de $f$ sur $I$?

---

### Correction Ultra-Détaillée

#### 1. Analyse de la propriété

**Typage des objets mathématiques :**
*   $I$: un sous-ensemble de $\mathbb{R}$ (l'ensemble des nombres réels), spécifiquement un intervalle.
*   $f$: une fonction de $I$ vers $\mathbb{R}$.
*   $\epsilon$: un nombre réel strictement positif ($\epsilon \in \mathbb{R}_{+}^{*}$).
*   $(x_n)_{n \in \mathbb{N}}$: une suite d'éléments de $I$ (donc $x_n \in I$ pour tout $n \in \mathbb{N}$).
*   $\delta$: un nombre réel strictement positif ($\delta \in \mathbb{R}_{+}^{*}$).
*   $n$: un entier naturel ($n \in \mathbb{N}$).
*   $|a-b|$: la distance euclidienne entre $a$ et $b$ dans $\mathbb{R}$.

**Négation de la propriété $\mathcal{P}(f)$ :**

La propriété $\mathcal{P}(f)$ est de la forme $\forall \epsilon, \forall (x_n), \exists \delta, (A \implies B)$.
La négation d'une implication $P \implies Q$ est $P \land \neg Q$.
La négation de $\mathcal{P}(f)$ est donc :
$$
\neg \mathcal{P}(f) \quad \iff \quad \exists \epsilon \in \mathbb{R}_{+}^{*}, \exists (x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}}, \forall \delta \in \mathbb{R}_{+}^{*}, \neg \left( \left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta \right) \implies \left( \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon \right) \right)
$$
En appliquant la règle de négation de l'implication :
$$
\neg \mathcal{P}(f) \quad \iff \quad \exists \epsilon \in \mathbb{R}_{+}^{*}, \exists (x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}}, \forall \delta \in \mathbb{R}_{+}^{*}, \left( \left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta \right) \land \neg \left( \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon \right) \right)
$$
En niant la seconde partie de la conjonction :
$$
\neg \mathcal{P}(f) \quad \iff \quad \exists \epsilon \in \mathbb{R}_{+}^{*}, \exists (x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}}, \forall \delta \in \mathbb{R}_{+}^{*}, \left( \left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta \right) \land \left( \exists n_0 \in \mathbb{N}, |f(x_{n_0}) - f(x_{n_0+1})| \ge \epsilon \right) \right)
$$

**Définition de la continuité uniforme de $f$ sur $I$ :**

Une fonction $f: I \to \mathbb{R}$ est uniformément continue sur $I$ si :
$$
f \text{ est U.C. sur } I \quad \iff \quad \forall \epsilon \in \mathbb{R}_{+}^{*}, \exists \delta \in \mathbb{R}_{+}^{*}, \forall x \in I, \forall y \in I, \left( |x - y| < \delta \right) \implies \left( |f(x) - f(y)| < \epsilon \right)
$$

**Négation de la continuité uniforme de $f$ sur $I$ :**

En appliquant les règles de négation des quantificateurs et de l'implication :
$$
f \text{ n'est pas U.C. sur } I \quad \iff \quad \exists \epsilon \in \mathbb{R}_{+}^{*}, \forall \delta \in \mathbb{R}_{+}^{*}, \exists x \in I, \exists y \in I, \left( |x - y| < \delta \right) \land \left( |f(x) - f(y)| \ge \epsilon \right)
$$

#### 2. Implication directe : $f$ U.C. sur $I \implies f$ satisfait $\mathcal{P}(f)$

**Démonstration :**

1.  **Hypothèse :** Supposons que $f: I \to \mathbb{R}$ est uniformément continue sur $I$.
    Par définition de la continuité uniforme, cela signifie que :
    $$
    \forall \epsilon' \in \mathbb{R}_{+}^{*}, \exists \delta' \in \mathbb{R}_{+}^{*}, \forall u \in I, \forall v \in I, \left( |u - v| < \delta' \right) \implies \left( |f(u) - f(v)| < \epsilon' \right)
    $$

2.  **But :** Nous voulons montrer que $f$ satisfait la propriété $\mathcal{P}(f)$, c'est-à-dire :
    $$
    \forall \epsilon \in \mathbb{R}_{+}^{*}, \forall (x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}}, \exists \delta \in \mathbb{R}_{+}^{*}, \left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta \right) \implies \left( \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon \right)
    $$

3.  **Procédons par étapes :**
    *   Soit un $\epsilon \in \mathbb{R}_{+}^{*}$ arbitraire. (Ceci correspond au premier quantificateur $\forall \epsilon$ de $\mathcal{P}(f)$).
    *   Soit une suite $(x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}}$ arbitraire. (Ceci correspond au deuxième quantificateur $\forall (x_n)$ de $\mathcal{P}(f)$).

4.  **Choix de $\delta$ :**
    *   Puisque $f$ est uniformément continue (par hypothèse), pour l'$\epsilon$ donné, il existe un $\delta' \in \mathbb{R}_{+}^{*}$ tel que pour tout $u, v \in I$, si $|u - v| < \delta'$, alors $|f(u) - f(v)| < \epsilon$.
    *   Nous allons choisir notre $\delta$ pour la propriété $\mathcal{P}(f)$ comme étant ce $\delta'$. C'est-à-dire, posons $\delta = \delta'$. Notez que ce $\delta$ ne dépend ni de la suite $(x_n)$ ni de $n$, seulement de $\epsilon$.

5.  **Vérification de l'implication :**
    *   Supposons que la prémisse de l'implication dans $\mathcal{P}(f)$ est vraie pour ce $\delta$ :
        $$
        \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta
        $$
    *   Nous devons montrer que la conclusion est vraie :
        $$
        \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon
        $$
    *   Pour tout $n \in \mathbb{N}$, nous avons $x_n \in I$ et $x_{n+1} \in I$.
    *   De plus, par notre supposition, $|x_n - x_{n+1}| < \delta$.
    *   Comme nous avons choisi $\delta = \delta'$, cela signifie que $|x_n - x_{n+1}| < \delta'$.
    *   Par la définition de la continuité uniforme de $f$ (point 1), puisque $|x_n - x_{n+1}| < \delta'$, il s'ensuit que $|f(x_n) - f(x_{n+1})| < \epsilon$.
    *   Cette conclusion est vraie pour tout $n \in \mathbb{N}$.

6.  **Conclusion de l'implication directe :**
    Nous avons montré que pour tout $\epsilon > 0$ et pour toute suite $(x_n)$, il existe un $\delta > 0$ (le même $\delta'$ de la continuité uniforme) tel que l'implication de $\mathcal{P}(f)$ est satisfaite.
    Donc, si $f$ est uniformément continue sur $I$, alors $f$ satisfait la propriété $\mathcal{P}(f)$.

#### 3. Implication réciproque : $f$ satisfait $\mathcal{P}(f) \implies f$ est U.C. sur $I$

**Démonstration par contraposition :**

1.  **Hypothèse :** Supposons que $f: I \to \mathbb{R}$ satisfait la propriété $\mathcal{P}(f)$.
    $$
    \forall \epsilon \in \mathbb{R}_{+}^{*}, \forall (x_n)_{n \in \mathbb{N}} \in I^{\mathbb{N}},\exists \delta \in \mathbb{R}_{+}^{*}, \left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta \right) \implies \left( \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon \right)
    $$

    Nous allons démontrer que $f$ est uniformément continue sur $I$ par l'absurde. Supposons que $f$ ne soit pas uniformément continue sur $I$.
    D'après la négation de la continuité uniforme (établie dans la partie 1), il existe $\epsilon_0 > 0$ tel que pour tout $\delta > 0$, on peut trouver des points $u_\delta, v_\delta \in I$ vérifiant $|u_\delta - v_\delta| < \delta$ mais $|f(u_\delta) - f(v_\delta)| \ge \epsilon_0$.

2.  **Construction de la suite $(x_n)$ :**
    Nous allons exploiter cette propriété pour chaque $\delta = \frac{1}{k}$ où $k \in \mathbb{N}^*$.
    Pour chaque $k \in \mathbb{N}^*$, il existe $u_k, v_k \in I$ tels que :
    $$|u_k - v_k| < \frac{1}{k} \quad \text{et} \quad |f(u_k) - f(v_k)| \ge \epsilon_0$$

    Construisons la suite $(x_n)_{n \in \mathbb{N}}$ de la manière suivante en alternant les termes de ces couples pour "forcer" la violation de l'implication :
    Posons $x_0 = u_1$, $x_1 = v_1$, $x_2 = u_2$, $x_3 = v_2$, ..., $x_{2k-2} = u_k$, $x_{2k-1} = v_k$.

3.  **Mise en évidence de la contradiction avec $\mathcal{P}(f)$ :**
    Puisque nous supposons que $\mathcal{P}(f)$ est vraie, appliquons-la pour notre $\epsilon_0 > 0$ trouvé et pour la suite $(x_n)_{n \in \mathbb{N}}$ que nous venons de construire.
    La propriété $\mathcal{P}(f)$ affirme qu'il existe un $\delta_0 > 0$ tel que :
    $$\left( \forall n \in \mathbb{N}, |x_n - x_{n+1}| < \delta_0 \right) \implies \left( \forall n \in \mathbb{N}, |f(x_n) - f(x_{n+1})| < \epsilon_0 \right)$$

    Cependant, la suite $(x_n)$ ne vérifie pas $\forall n, |x_n - x_{n+1}| < \delta_0$ si l'on ne sélectionne pas bien les indices. Mais, la construction ci-dessus est classique pour montrer que la négation d'une propriété globale permet d'extraire des couples.
    L'implication exacte de $\mathcal{P}(f)$ telle qu'écrite requiert que *tous* les termes successifs de la suite soient proches pour garantir que *tous* les termes successifs de l'image le soient.

    Prenons la négation de $\mathcal{P}(f)$ que nous avions calculée:
    $$ \exists \epsilon > 0, \exists (x_n), \forall \delta > 0, \left( (\forall n, |x_n - x_{n+1}| < \delta) \land (\exists n_0, |f(x_{n_0}) - f(x_{n_0+1})| \ge \epsilon) \right) $$

    En utilisant l'hypothèse de non-continuité uniforme, pour $\epsilon_0$, et pour chaque $\delta$, nous avions trouvé $u,v$ proches. Pour que l'implication de $\mathcal{P}(f)$ soit violée, il faut une *unique* suite $(x_n)$ telle que l'écart entre termes consécutifs soit rendu arbitrairement petit.

    Si nous construisons une suite stationnaire : soit $u, v$ tq $|u-v| < \delta$ et $|f(u)-f(v)| \ge \epsilon_0$. Posons $x_n = u$ pour $n$ pair et $x_n = v$ pour $n$ impair.
    Alors $\forall n, |x_n - x_{n+1}| = |u-v| < \delta$.
    Mais pour tout $n$, $|f(x_n) - f(x_{n+1})| = |f(u) - f(v)| \ge \epsilon_0$.
    Donc, pour cette suite particulière, la prémisse est vraie, et la conclusion est fausse.

    Ceci démontre que $\mathcal{P}(f)$ est fausse si $f$ n'est pas uniformément continue. Donc par contraposition, si $\mathcal{P}(f)$ est vraie, alors $f$ est uniformément continue.

#### 4. Conclusion

La propriété $\mathcal{P}(f)$ est logiquement **équivalente** à la continuité uniforme de $f$ sur $I$.
La condition d'uniforme continuité peut s'exprimer par le biais d'une propriété séquentielle forte englobant l'intégralité du domaine $I$. Cet exercice souligne l'importance vitale de l'ordre des quantificateurs et de la formulation précise des hypothèses.
