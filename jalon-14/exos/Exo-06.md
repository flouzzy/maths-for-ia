---
uuid: "jalon-14-exo-06"
title: "Exercice 6 : Convergence Rigoureuse de Suites Complexes et Réelles : Définitions et Contre-exemples"
tags: ["math/analyse", "suites", "exercice"]
---
# Exercice 6 : Convergence Rigoureuse de Suites Complexes et Réelles : Définitions et Contre-exemples

## Énoncé

Cet exercice explore la définition rigoureuse de la limite pour les suites réelles et complexes, ainsi que les critères de convergence.

**Partie A : Convergence d'une suite complexe**
Soit la suite de nombres complexes $(z_n)_{n \in \mathbb{N}^*}$ définie par $z_n = \frac{n + i \sin(n)}{n^2+1}$.
En utilisant la définition rigoureuse de la limite ($\epsilon, N$), démontrez que la suite $(z_n)$ converge vers 0.

**Partie B : Propriétés des limites pour les parties réelle et imaginaire**
Soit $(z_n)_{n \in \mathbb{N}}$ une suite de nombres complexes. On suppose que $(z_n)$ converge vers un nombre complexe $L$.
En utilisant la définition rigoureuse de la limite ($\epsilon, N$), démontrez que la suite des parties réelles $(\text{Re}(z_n))_{n \in \mathbb{N}}$ converge vers $\text{Re}(L)$ et que la suite des parties imaginaires $(\text{Im}(z_n))_{n \in \mathbb{N}}$ converge vers $\text{Im}(L)$.

**Partie C : Non-convergence d'une suite complexe**
Soit la suite de nombres complexes $(w_n)_{n \in \mathbb{N}}$ définie par $w_n = e^{i n \pi / 2}$.
En utilisant la négation de la définition rigoureuse de la limite ($\epsilon, N$), démontrez que la suite $(w_n)$ ne converge pas.

## Correction Détaillée

### Partie A : Convergence d'une suite complexe

1.  **Rappel de la définition de la convergence pour une suite complexe**:
    Une suite de nombres complexes $(z_n)$ converge vers un nombre complexe $L \in \mathbb{C}$ si et seulement si pour tout nombre réel $\epsilon > 0$, il existe un entier naturel $N \in \mathbb{N}$ tel que pour tout entier $n$ vérifiant $n > N$, on a $|z_n - L| < \epsilon$.

2.  **Identification de la suite et de la limite proposée**:
    La suite donnée est $z_n = \frac{n + i \sin(n)}{n^2+1}$. La limite que nous devons démontrer est $L=0$.

3.  **Calcul de la distance $|z_n - L|$**:
    Nous devons évaluer l'expression $|z_n - 0|$.
    $|z_n - 0| = \left| \frac{n + i \sin(n)}{n^2+1} \right|$.
    En utilisant la propriété du module d'un quotient, qui stipule que pour des nombres complexes $a$ et $b$ avec $b \ne 0$, $|a/b| = |a|/|b|$ :
    $|z_n - 0| = \frac{|n + i \sin(n)|}{|n^2+1|}$.
    Puisque $n \in \mathbb{N}^*$, $n^2+1$ est un nombre réel strictement positif. Par conséquent, $|n^2+1| = n^2+1$.
    Le numérateur est le module d'un nombre complexe de la forme $a+ib$, qui est $\sqrt{a^2+b^2}$. Ici, $a=n$ et $b=\sin(n)$.
    Donc, $|n + i \sin(n)| = \sqrt{n^2 + (\sin(n))^2}$.
    En substituant ces expressions, nous obtenons :
    $|z_n - 0| = \frac{\sqrt{n^2 + \sin^2(n)}}{n^2+1}$.

4.  **Majoration de l'expression pour faciliter la recherche de $N$**:
    Nous cherchons à majorer cette expression par une quantité qui tend vers 0 lorsque $n$ tend vers l'infini et qui est plus simple à manipuler.
    Nous savons que pour tout $n \in \mathbb{N}^*$, la fonction sinus est bornée entre -1 et 1, donc $0 \le \sin^2(n) \le 1$.
    En ajoutant $n^2$ à chaque partie de l'inégalité :
    $n^2 \le n^2 + \sin^2(n) \le n^2+1$.
    La fonction racine carrée est croissante sur $[0, +\infty)$, donc en prenant la racine carrée de chaque partie :
    $\sqrt{n^2} \le \sqrt{n^2 + \sin^2(n)} \le \sqrt{n^2+1}$.
    Puisque $n \in \mathbb{N}^*$, $\sqrt{n^2} = n$. Donc :
    $n \le \sqrt{n^2 + \sin^2(n)} \le \sqrt{n^2+1}$.
    Nous utilisons la majoration $\sqrt{n^2 + \sin^2(n)} \le \sqrt{n^2+1}$.
    Alors, l'expression de la distance devient :
    $|z_n - 0| \le \frac{\sqrt{n^2+1}}{n^2+1}$.
    Nous pouvons simplifier cette fraction en utilisant la propriété $\frac{\sqrt{X}}{X} = \frac{1}{\sqrt{X}}$ pour tout $X > 0$. Ici, $X=n^2+1$.
    Donc, $|z_n - 0| \le \frac{1}{\sqrt{n^2+1}}$.

5.  **Recherche d'un entier $N$ en fonction de $\epsilon$**:
    Nous voulons trouver un $N$ tel que pour tout $n > N$, l'inégalité $\frac{1}{\sqrt{n^2+1}} < \epsilon$ soit satisfaite.
    Puisque $\epsilon > 0$, nous pouvons prendre l'inverse des deux côtés de l'inégalité (ce qui inverse le sens de l'inégalité car les termes sont positifs) :
    $\sqrt{n^2+1} > \frac{1}{\epsilon}$.
    Élevons les deux côtés au carré (les deux côtés sont positifs) :
    $n^2+1 > \frac{1}{\epsilon^2}$.
    Soustrayons 1 des deux côtés :
    $n^2 > \frac{1}{\epsilon^2} - 1$.
    Puisque $n \in \mathbb{N}^*$, $n$ est positif, donc nous pouvons prendre la racine carrée des deux côtés :
    $n > \sqrt{\frac{1}{\epsilon^2} - 1}$.
    Pour garantir que $n$ satisfait cette condition, nous pouvons choisir $N$ comme le plus grand entier inférieur ou égal à $\sqrt{\frac{1}{\epsilon^2} - 1}$. Une manière standard et toujours valide est de prendre $N = \max(0, \lceil \sqrt{\frac{1}{\epsilon^2} - 1} \rceil)$.
    Pour simplifier la détermination de $N$, nous pouvons utiliser une majoration plus lâche mais suffisante. Pour $n \ge 1$, nous avons $n^2+1 \ge n^2$, ce qui implique $\sqrt{n^2+1} \ge \sqrt{n^2} = n$.
    Par conséquent, $\frac{1}{\sqrt{n^2+1}} \le \frac{1}{n}$.
    Si nous voulons que $\frac{1}{n} < \epsilon$, cela implique $n > \frac{1}{\epsilon}$.
    Nous pouvons donc choisir $N = \lceil \frac{1}{\epsilon} \rceil$.

6.  **Conclusion formelle**:
    Soit $\epsilon > 0$ un nombre réel arbitrairement petit.
    Choisissons l'entier $N = \lceil \frac{1}{\epsilon} \rceil$. (Si $\epsilon \ge 1$, alors $N=1$ est suffisant, car $1/n < 1 \le \epsilon$ pour $n>1$. Si $\epsilon < 1$, alors $N \ge 1$).
    Alors, pour tout entier $n$ tel que $n > N$, nous avons par définition de $N$:
    $n > \frac{1}{\epsilon}$.
    En prenant l'inverse des deux côtés (puisque $n$ et $\epsilon$ sont positifs), l'inégalité change de sens :
    $\frac{1}{n} < \epsilon$.
    Nous avons établi précédemment que $|z_n - 0| \le \frac{1}{\sqrt{n^2+1}}$.
    Nous avons également montré que pour $n \ge 1$, $n^2+1 \ge n^2$, ce qui implique $\sqrt{n^2+1} \ge n$.
    Par conséquent, $\frac{1}{\sqrt{n^2+1}} \le \frac{1}{n}$.
    En combinant ces inégalités, pour tout $n > N$, nous avons :
    $|z_n - 0| \le \frac{1}{\sqrt{n^2+1}} \le \frac{1}{n} < \epsilon$.
    Ceci démontre, par la définition rigoureuse de la limite, que la suite $(z_n)$ converge vers 0.

### Partie B : Propriétés des limites pour les parties réelle et imaginaire

1.  **Rappel de la définition de la convergence pour $(z_n)$**:
    La suite $(z_n)$ converge vers $L \in \mathbb{C}$ signifie que pour tout $\epsilon' > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $n > N$, on a $|z_n - L| < \epsilon'$.

2.  **Objectif pour la convergence des parties réelles**:
    Nous voulons montrer que la suite des parties réelles $(\text{Re}(z_n))$ converge vers $\text{Re}(L)$. Cela signifie que pour tout $\epsilon > 0$, il existe un entier $N_R \in \mathbb{N}$ tel que pour tout $n > N_R$, on a $|\text{Re}(z_n) - \text{Re}(L)| < \epsilon$.

3.  **Lien entre le module d'une différence de complexes et la différence de leurs parties réelles/imaginaires**:
    Soit $z_n = x_n + i y_n$, où $x_n = \text{Re}(z_n)$ et $y_n = \text{Im}(z_n)$.
    Soit $L = x_L + i y_L$, où $x_L = \text{Re}(L)$ et $y_L = \text{Im}(L)$.
    Alors la différence $z_n - L$ peut s'écrire :
    $z_n - L = (x_n + i y_n) - (x_L + i y_L) = (x_n - x_L) + i (y_n - y_L)$.
    Le module de cette différence est $|z_n - L| = \sqrt{(x_n - x_L)^2 + (y_n - y_L)^2}$.
    Nous savons que pour tout nombre complexe $Z = A+iB$, la partie réelle $A$ et la partie imaginaire $B$ sont liées au module $|Z|$ par les inégalités :
    $|A| \le \sqrt{A^2+B^2} = |Z|$
    $|B| \le \sqrt{A^2+B^2} = |Z|$
    Appliquons ces inégalités au nombre complexe $Z = z_n - L$, avec $A = x_n - x_L$ et $B = y_n - y_L$.
    Nous obtenons :
    $|\text{Re}(z_n) - \text{Re}(L)| = |x_n - x_L| \le \sqrt{(x_n - x_L)^2 + (y_n - y_L)^2} = |z_n - L|$.
    De même :
    $|\text{Im}(z_n) - \text{Im}(L)| = |y_n - y_L| \le \sqrt{(x_n - x_L)^2 + (y_n - y_L)^2} = |z_n - L|$.

4.  **Démonstration de la convergence de $(\text{Re}(z_n))$**:
    Soit $\epsilon > 0$ un nombre réel arbitrairement petit.
    Puisque la suite $(z_n)$ converge vers $L$, par la définition de la convergence (avec $\epsilon' = \epsilon$), il existe un entier $N \in \mathbb{N}$ tel que pour tout $n > N$, on a $|z_n - L| < \epsilon$.
    En utilisant l'inégalité établie au point 3, pour tout $n > N$, nous avons :
    $|\text{Re}(z_n) - \text{Re}(L)| \le |z_n - L|$.
    Puisque nous savons que $|z_n - L| < \epsilon$ pour $n > N$, il s'ensuit que :
    $|\text{Re}(z_n) - \text{Re}(L)| < \epsilon$.
    Nous avons donc trouvé un entier $N_R = N$ tel que pour tout $n > N_R$, l'inégalité $|\text{Re}(z_n) - \text{Re}(L)| < \epsilon$ est satisfaite.
    Ceci démontre que la suite des parties réelles $(\text{Re}(z_n))$ converge vers $\text{Re}(L)$.

5.  **Démonstration de la convergence de $(\text{Im}(z_n))$**:
    Soit $\epsilon > 0$ un nombre réel arbitrairement petit.
    Puisque la suite $(z_n)$ converge vers $L$, par la définition de la convergence (avec $\epsilon' = \epsilon$), il existe un entier $N \in \mathbb{N}$ tel que pour tout $n > N$, on a $|z_n - L| < \epsilon$.
    En utilisant l'inégalité établie au point 3, pour tout $n > N$, nous avons :
    $|\text{Im}(z_n) - \text{Im}(L)| \le |z_n - L|$.
    Puisque nous savons que $|z_n - L| < \epsilon$ pour $n > N$, il s'ensuit que :
    $|\text{Im}(z_n) - \text{Im}(L)| < \epsilon$.
    Nous avons donc trouvé un entier $N_I = N$ tel que pour tout $n > N_I$, l'inégalité $|\text{Im}(z_n) - \text{Im}(L)| < \epsilon$ est satisfaite.
    Ceci démontre que la suite des parties imaginaires $(\text{Im}(z_n))$ converge vers $\text{Im}(L)$.

### Partie C : Non-convergence d'une suite complexe

1.  **Rappel de la définition de la convergence**:
    Une suite $(w_n)$ converge vers $L \in \mathbb{C}$ si et seulement si pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tout $n > N$, on a $|w_n - L| < \epsilon$.

2.  **Stratégie pour démontrer la non-convergence**:
    Pour démontrer qu'une suite ne converge pas, nous pouvons utiliser la négation de la définition de la convergence. Cependant, une approche souvent plus efficace pour les suites dans un espace complet (comme $\mathbb{C}$) est de montrer qu'elle n'est pas une suite de Cauchy. En effet, toute suite convergente dans un espace complet est une suite de Cauchy. Si une suite n'est pas de Cauchy, alors elle ne peut pas être convergente.

    **Rappel de la définition d'une suite de Cauchy**:
    Une suite $(w_n)$ est de Cauchy si et seulement si pour tout $\epsilon > 0$, il existe un entier $N \in \mathbb{N}$ tel que pour tous entiers $p, q$ vérifiant $p > N$ et $q > N$, on a $|w_p - w_q| < \epsilon$.

    **Négation de la définition d'une suite de Cauchy**:
    Une suite $(w_n)$ n'est *pas* de Cauchy si et seulement s'il existe un nombre réel $\epsilon_0 > 0$ tel que pour tout entier $N \in \mathbb{N}$, il existe des entiers $p, q$ vérifiant $p > N$ et $q > N$ pour lesquels $|w_p - w_q| \ge \epsilon_0$.

3.  **Analyse de la suite $(w_n)$**:
    La suite est définie par $w_n = e^{i n \pi / 2}$. Calculons les premiers termes de la suite pour comprendre son comportement :
    Pour $n=0$: $w_0 = e^{i \cdot 0 \cdot \pi / 2} = e^0 = 1$.
    Pour $n=1$: $w_1 = e^{i \pi / 2} = \cos(\pi/2) + i \sin(\pi/2) = 0 + i \cdot 1 = i$.
    Pour $n=2$: $w_2 = e^{i 2 \pi / 2} = e^{i \pi} = \cos(\pi) + i \sin(\pi) = -1 + i \cdot 0 = -1$.
    Pour $n=3$: $w_3 = e^{i 3 \pi / 2} = \cos(3\pi/2) + i \sin(3\pi/2) = 0 + i \cdot (-1) = -i$.
    Pour $n=4$: $w_4 = e^{i 4 \pi / 2} = e^{i 2 \pi} = \cos(2\pi) + i \sin(2\pi) = 1 + i \cdot 0 = 1$.
    Nous observons que la suite est périodique de période 4, prenant successivement les valeurs $1, i, -1, -i$, puis répétant ce cycle.

4.  **Démonstration par la négation de la définition de Cauchy**:
    Nous allons montrer que la suite $(w_n)$ n'est pas une suite de Cauchy.
    Choisissons un $\epsilon_0 > 0$. Par exemple, prenons $\epsilon_0 = 1$.
    Nous devons montrer que pour tout entier $N \in \mathbb{N}$, il existe des entiers $p, q$ tels que $p > N$, $q > N$, et $|w_p - w_q| \ge \epsilon_0$.

    Soit $N$ un entier naturel quelconque.
    Nous devons trouver $p, q > N$ tels que la distance entre $w_p$ et $w_q$ soit au moins $\epsilon_0$.
    Considérons les termes de la suite qui sont $1$ et $-1$. La distance entre eux est $|1 - (-1)| = |2| = 2$.
    Nous pouvons toujours trouver des indices $p$ et $q$ supérieurs à $N$ tels que $w_p = 1$ et $w_q = -1$.
    Choisissons un entier $k$ tel que $4k > N$. Par exemple, $k = \lfloor N/4 \rfloor + 1$.
    Posons $p = 4k$. Alors $p$ est un multiple de 4, donc $p > N$.
    Le terme $w_p$ est $w_{4k} = e^{i 4k \pi / 2} = e^{i 2k \pi}$. Puisque $e^{i 2k \pi} = \cos(2k\pi) + i \sin(2k\pi) = 1 + i \cdot 0 = 1$.
    Posons $q = 4k+2$. Alors $q = p+2$, donc $q > N$.
    Le terme $w_q$ est $w_{4k+2} = e^{i (4k+2) \pi / 2} = e^{i (2k \pi + \pi)}$.
    En utilisant la propriété $e^{A+B} = e^A e^B$, nous avons $e^{i (2k \pi + \pi)} = e^{i 2k \pi} e^{i \pi}$.
    Nous savons que $e^{i 2k \pi} = 1$ et $e^{i \pi} = \cos(\pi) + i \sin(\pi) = -1 + i \cdot 0 = -1$.
    Donc, $w_q = 1 \cdot (-1) = -1$.

    Maintenant, calculons la distance entre $w_p$ et $w_q$ pour ces choix de $p$ et $q$:
    $|w_p - w_q| = |1 - (-1)| = |1+1| = |2| = 2$.
    Puisque $2 \ge \epsilon_0 = 1$, nous avons trouvé, pour tout $N$ (en choisissant $p=4(\lfloor N/4 \rfloor + 1)$ et $q=p+2$), des indices $p, q > N$ tels que $|w_p - w_q| \ge \epsilon_0$.
    Ceci démontre que la suite $(w_n)$ n'est pas une suite de Cauchy.

5.  **Conclusion finale**:
    L'espace des nombres complexes $\mathbb{C}$ est un espace métrique complet. Dans un espace complet, toute suite convergente est nécessairement une suite de Cauchy. Puisque nous avons démontré que la suite $(w_n)$ n'est pas une suite de Cauchy, il s'ensuit qu'elle ne peut pas être convergente.
