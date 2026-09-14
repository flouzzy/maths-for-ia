## Exercice 9 : Densité d'une mesure produit (cas à densité) \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Si $\mu_1$ a pour densité $f_1$ par rapport à $\lambda$ et $\mu_2$ a pour densité $f_2$ par rapport à $\lambda$, montrer que la mesure produit $\mu_1 \otimes \mu_2$ a pour densité la fonction $(x,y) \mapsto f_1(x)f_2(y)$ par rapport à $\lambda \otimes \lambda$.

**Correction :**
1. Soit un rectangle mesurable $A \times B$.
2. Par définition, $(\mu_1 \otimes \mu_2)(A \times B) = \mu_1(A) \cdot \mu_2(B)$.
3. Comme les mesures ont des densités : $\mu_1(A) = \int_A f_1(x) dx$ et $\mu_2(B) = \int_B f_2(y) dy$.
4. Donc $(\mu_1 \otimes \mu_2)(A \times B) = \left( \int_A f_1(x) dx \right) \left( \int_B f_2(y) dy \right)$.
5. Les fonctions étant positives, et les variables séparables, cela correspond exactement à l'intégrale double sur $A \times B$ :
   $\int_{A \times B} f_1(x)f_2(y) d(\lambda \otimes \lambda)(x,y)$.
6. Cette égalité étant vraie sur tous les rectangles (qui forment un $\pi$-système engendrant la tribu), elle s'étend par le théorème d'extension de Carathéodory (ou lemme de classe monotone) à tout borélien de $\mathbb{R}^2$.
7. La densité est donc bien $f(x,y) = f_1(x)f_2(y)$.
