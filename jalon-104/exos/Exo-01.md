**Exercice 1 : Introduction aux Bases Hilbertiennes en dimension finie**

**Difficulté :** $\star\star\star\star\star$

Soit $H = \mathbb{R}^2$ l'espace vectoriel réel muni du produit scalaire euclidien standard défini pour tout $x = (x_1, x_2) \in \mathbb{R}^2$ et $y = (y_1, y_2) \in \mathbb{R}^2$ par $\langle x, y \rangle = x_1 y_1 + x_2 y_2$.
Considérons les vecteurs suivants dans $H$:
$e_1 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)$
$e_2 = \left( -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)$

1.  Démontrez rigoureusement que le système de vecteurs $\{e_1, e_2\}$ est un système orthonormal dans l'espace de Hilbert $H$.
2.  Démontrez rigoureusement que le système $\{e_1, e_2\}$ constitue une base Hilbertienne pour l'espace $H$.
3.  Soit le vecteur $v = (3, 7) \in H$. Déterminez, par un calcul explicite, les coefficients de la décomposition de $v$ dans la base $\{e_1, e_2\}$. C'est-à-dire, trouvez $\alpha_1, \alpha_2 \in \mathbb{R}$ tels que $v = \alpha_1 e_1 + \alpha_2 e_2$.
4.  Vérifiez l'identité de Parseval pour le vecteur $v$ et la base $\{e_1, e_2\}$. C'est-à-dire, montrez par un calcul direct que $||v||^2 = |\alpha_1|^2 + |\alpha_2|^2$.

---

**Correction de l'Exercice 1 :**

1.  **Démonstration que $\{e_1, e_2\}$ est un système orthonormal.**

    Un système de vecteurs $\{u_1, u_2, \dots, u_n\}$ est défini comme orthonormal si et seulement si pour tout $i, j \in \{1, \dots, n\}$, nous avons $\langle u_i, u_j \rangle = \delta_{ij}$, où $\delta_{ij}$ est le symbole de Kronecker ($\delta_{ij}=1$ si $i=j$ et $\delta_{ij}=0$ si $i \ne j$). Cela implique deux conditions :
    *   Chaque vecteur du système doit être de norme 1 (condition de normalisation).
    *   Tous les couples de vecteurs distincts du système doivent être orthogonaux (condition d'orthogonalité mutuelle).

    Nous allons vérifier ces conditions pour le système $\{e_1, e_2\}$.

    Calculons le produit scalaire $\langle e_1, e_1 \rangle$:
    Le vecteur $e_1$ est donné par $e_1 = \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)$.
    En utilisant la définition du produit scalaire standard :
    $\langle e_1, e_1 \rangle = \left(\frac{1}{\sqrt{2}}\right) \cdot \left(\frac{1}{\sqrt{2}}\right) + \left(\frac{1}{\sqrt{2}}\right) \cdot \left(\frac{1}{\sqrt{2}}\right)$
    $\langle e_1, e_1 \rangle = \frac{1}{2} + \frac{1}{2}$
    $\langle e_1, e_1 \rangle = 1$
    La norme du vecteur $e_1$ est $||e_1|| = \sqrt{\langle e_1, e_1 \rangle} = \sqrt{1} = 1$. Le vecteur $e_1$ est donc normalisé.

    Calculons le produit scalaire $\langle e_2, e_2 \rangle$:
    Le vecteur $e_2$ est donné par $e_2 = \left( -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right)$.
    En utilisant la définition du produit scalaire standard :
    $\langle e_2, e_2 \rangle = \left(-\frac{1}{\sqrt{2}}\right) \cdot \left(-\frac{1}{\sqrt{2}}\right) + \left(\frac{1}{\sqrt{2}}\right) \cdot \left(\frac{1}{\sqrt{2}}\right)$
    $\langle e_2, e_2 \rangle = \frac{1}{2} + \frac{1}{2}$
    $\langle e_2, e_2 \rangle = 1$
    La norme du vecteur $e_2$ est $||e_2|| = \sqrt{\langle e_2, e_2 \rangle} = \sqrt{1} = 1$. Le vecteur $e_2$ est donc normalisé.

    Calculons le produit scalaire $\langle e_1, e_2 \rangle$:
    En utilisant la définition du produit scalaire standard :
    $\langle e_1, e_2 \rangle = \left(\frac{1}{\sqrt{2}}\right) \cdot \left(-\frac{1}{\sqrt{2}}\right) + \left(\frac{1}{\sqrt{2}}\right) \cdot \left(\frac{1}{\sqrt{2}}\right)$
    $\langle e_1, e_2 \rangle = -\frac{1}{2} + \frac{1}{2}$
    $\langle e_1, e_2 \rangle = 0$
    Puisque $\langle e_1, e_2 \rangle = 0$, les vecteurs $e_1$ et $e_2$ sont orthogonaux.

    En résumé, nous avons trouvé $\langle e_1, e_1 \rangle = 1$, $\langle e_2, e_2 \rangle = 1$ et $\langle e_1, e_2 \rangle = 0$. Ces résultats confirment que le système $\{e_1, e_2\}$ satisfait toutes les conditions requises pour être un système orthonormal dans $H$.

2.  **Démonstration que $\{e_1, e_2\}$ est une base Hilbertienne pour $H$.**

    Dans un espace de Hilbert de dimension finie $H$, un système orthonormal $\{u_1, \dots, u_n\}$ est une base Hilbertienne si et seulement si le nombre de vecteurs dans le système est égal à la dimension de l'espace $H$. Une base Hilbertienne est également appelée base orthonormée dans le contexte des espaces euclidiens de dimension finie.

    L'espace $H$ est $\mathbb{R}^2$, dont la dimension est $\text{dim}(H) = 2$.
    Le système $\{e_1, e_2\}$ contient 2 vecteurs.
    Puisque nous avons déjà démontré à la question 1 que $\{e_1, e_2\}$ est un système orthonormal, et que le nombre de ses vecteurs (2) est égal à la dimension de l'espace $H$ (2), il en découle directement que $\{e_1, e_2\}$ est une base Hilbertienne pour $H$.

    Alternativement, tout système orthonormal est linéairement indépendant. Puisque $\{e_1, e_2\}$ est un système orthonormal de 2 vecteurs dans l'espace $\mathbb{R}^2$ de dimension 2, il est un système libre maximal, et par conséquent, il forme une base de $\mathbb{R}^2$. Étant une base orthonormale, elle est une base Hilbertienne.

3.  **Détermination des coefficients de la décomposition de $v$ dans la base $\{e_1, e_2\}$.**

    Pour un vecteur $v$ dans un espace de Hilbert de dimension finie, muni d'une base Hilbertienne $\{e_1, e_2, \dots, e_n\}$, les coefficients $\alpha_i$ de la décomposition $v = \sum_{i=1}^n \alpha_i e_i$ sont donnés par la formule $\alpha_i = \langle v, e_i \rangle$.

    Nous avons le vecteur $v = (3, 7)$.

    Calculons le coefficient $\alpha_1$:
    $\alpha_1 = \langle v, e_1 \rangle$
    $\alpha_1 = \left\langle (3, 7), \left( \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right) \right\rangle$
    En utilisant la définition du produit scalaire standard :
    $\alpha_1 = (3) \cdot \left(\frac{1}{\sqrt{2}}\right) + (7) \cdot \left(\frac{1}{\sqrt{2}}\right)$
    $\alpha_1 = \frac{3}{\sqrt{2}} + \frac{7}{\sqrt{2}}$
    $\alpha_1 = \frac{3+7}{\sqrt{2}}$
    $\alpha_1 = \frac{10}{\sqrt{2}}$
    Pour rationaliser le dénominateur, multiplions le numérateur et le dénominateur par $\sqrt{2}$:
    $\alpha_1 = \frac{10\sqrt{2}}{\sqrt{2} \cdot \sqrt{2}}$
    $\alpha_1 = \frac{10\sqrt{2}}{2}$
    $\alpha_1 = 5\sqrt{2}$

    Calculons le coefficient $\alpha_2$:
    $\alpha_2 = \langle v, e_2 \rangle$
    $\alpha_2 = \left\langle (3, 7), \left( -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}} \right) \right\rangle$
    En utilisant la définition du produit scalaire standard :
    $\alpha_2 = (3) \cdot \left(-\frac{1}{\sqrt{2}}\right) + (7) \cdot \left(\frac{1}{\sqrt{2}}\right)$
    $\alpha_2 = -\frac{3}{\sqrt{2}} + \frac{7}{\sqrt{2}}$
    $\alpha_2 = \frac{-3+7}{\sqrt{2}}$
    $\alpha_2 = \frac{4}{\sqrt{2}}$
    Pour rationaliser le dénominateur, multiplions le numérateur et le dénominateur par $\sqrt{2}$:
    $\alpha_2 = \frac{4\sqrt{2}}{\sqrt{2} \cdot \sqrt{2}}$
    $\alpha_2 = \frac{4\sqrt{2}}{2}$
    $\alpha_2 = 2\sqrt{2}$

    Les coefficients de la décomposition de $v$ dans la base $\{e_1, e_2\}$ sont donc $\alpha_1 = 5\sqrt{2}$ et $\alpha_2 = 2\sqrt{2}$.
    Ceci signifie que $v = 5\sqrt{2} e_1 + 2\sqrt{2} e_2$.

4.  **Vérification de l'identité de Parseval pour le vecteur $v$.**

    L'identité de Parseval pour un vecteur $v$ et une base Hilbertienne $\{e_i\}_{i=1}^n$ énonce que la norme au carré du vecteur $v$ est égale à la somme des carrés des modules de ses coefficients de Fourier : $||v||^2 = \sum_{i=1}^n |\langle v, e_i \rangle|^2$. Dans notre cas spécifique de dimension 2, cela se traduit par $||v||^2 = |\alpha_1|^2 + |\alpha_2|^2$.

    Premièrement, calculons $||v||^2$ directement à partir de la définition de la norme euclidienne pour $v = (3, 7)$:
    $||v||^2 = \langle v, v \rangle$
    $||v||^2 = (3)^2 + (7)^2$
    $||v||^2 = 9 + 49$
    $||v||^2 = 58$

    Deuxièmement, calculons la somme des carrés des coefficients que nous avons déterminés à la question précédente :
    Nous avons $\alpha_1 = 5\sqrt{2}$ et $\alpha_2 = 2\sqrt{2}$.
    $|\alpha_1|^2 + |\alpha_2|^2 = (5\sqrt{2})^2 + (2\sqrt{2})^2$
    Calculons chaque terme séparément :
    $(5\sqrt{2})^2 = 5^2 \cdot (\sqrt{2})^2 = 25 \cdot 2 = 50$
    $(2\sqrt{2})^2 = 2^2 \cdot (\sqrt{2})^2 = 4 \cdot 2 = 8$
    Additionnons ces valeurs :
    $|\alpha_1|^2 + |\alpha_2|^2 = 50 + 8$
    $|\alpha_1|^2 + |\alpha_2|^2 = 58$

    Nous avons obtenu $||v||^2 = 58$ et $|\alpha_1|^2 + |\alpha_2|^2 = 58$.
    Puisque ces deux valeurs sont égales, l'identité de Parseval est rigoureusement vérifiée pour le vecteur $v = (3, 7)$ et la base Hilbertienne $\{e_1, e_2\}$.