# Exercice 2 : Intégration par rapport à une mesure de Dirac
$\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ et $a \in \mathbb{R}$. Soit $\delta_a$ la mesure de Dirac en $a$, définie pour tout borélien $A$ par $\delta_a(A) = 1$ si $a \in A$, et $0$ sinon.
Pour toute fonction $f : \mathbb{R} \to \mathbb{R}_+$ mesurable, démontrer que $\int_{\mathbb{R}} f \, d\delta_a = f(a)$.

**Correction :**
1. **Étape 1 : Preuve pour les fonctions indicatrices.**
   Soit $A \in \mathcal{B}(\mathbb{R})$ et $f = \mathbf{1}_A$.
   Par définition de l'intégrale d'une fonction étagée :
   $$\int_{\mathbb{R}} \mathbf{1}_A \, d\delta_a = 1 \cdot \delta_a(A)$$
   - Si $a \in A$, $\mathbf{1}_A(a) = 1$ et $\delta_a(A) = 1$, donc $\int \mathbf{1}_A d\delta_a = 1 = \mathbf{1}_A(a)$.
   - Si $a \notin A$, $\mathbf{1}_A(a) = 0$ et $\delta_a(A) = 0$, donc $\int \mathbf{1}_A d\delta_a = 0 = \mathbf{1}_A(a)$.
   La propriété est vraie pour les indicatrices.

2. **Étape 2 : Preuve pour les fonctions étagées.**
   Soit $s = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}$ une fonction étagée positive (forme canonique).
   Par linéarité de l'intégrale :
   $$\int_{\mathbb{R}} s \, d\delta_a = \sum_{i=1}^n \alpha_i \int_{\mathbb{R}} \mathbf{1}_{A_i} \, d\delta_a = \sum_{i=1}^n \alpha_i \mathbf{1}_{A_i}(a) = s(a)$$

3. **Étape 3 : Passage aux fonctions mesurables positives par supremum.**
   Soit $f \in \mathcal{M}^+(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.
   Par définition, $\int_{\mathbb{R}} f \, d\delta_a = \sup \left\lbrace \int_{\mathbb{R}} s \, d\delta_a \mid 0 \le s \le f, s \text{ étagée} \right\rbrace$.
   D'après l'étape 2, $\int_{\mathbb{R}} s \, d\delta_a = s(a)$.
   Donc $\int_{\mathbb{R}} f \, d\delta_a = \sup \left\lbrace s(a) \mid 0 \le s \le f, s \text{ étagée} \right\rbrace$.
   Puisque $s \le f$ pour toute fonction $s$ considérée, on a $s(a) \le f(a)$, donc le supremum est inférieur ou égal à $f(a)$ : $\int_{\mathbb{R}} f \, d\delta_a \le f(a)$.
   Inversement, pour toute valeur constante $c < f(a)$, la fonction $s = c \mathbf{1}_{\{a\}}$ est étagée et $s \le f$. Son intégrale est $c$. En prenant le supremum sur tous les $c < f(a)$, on obtient que $\int_{\mathbb{R}} f \, d\delta_a \ge f(a)$.
   Par double inégalité, $\int_{\mathbb{R}} f \, d\delta_a = f(a)$.
